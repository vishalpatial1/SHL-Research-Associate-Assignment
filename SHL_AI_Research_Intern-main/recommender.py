"""
Recommendation Engine for SHL Assessments
Uses semantic search with embeddings and LLM-based ranking

Submission by: Jay Tiwari
Position: AI Reach Intern
Company: SHL Company
"""

import json
import os
from typing import List, Dict, Optional
import numpy as np
from sentence_transformers import SentenceTransformer
import google.generativeai as genai
from dotenv import load_dotenv
import pandas as pd

load_dotenv()

class AssessmentRecommender:
    def __init__(self, assessments_file: str = 'data/assessments.json'):
        self.assessments_file = assessments_file
        self.assessments = []
        self.embedding_model = None
        self.embeddings = None
        self.gemini_api_key = os.getenv('GEMINI_API_KEY')
        
        # Initialize Gemini
        if self.gemini_api_key:
            genai.configure(api_key=self.gemini_api_key)
            # Try gemini-1.5-pro first, fallback to gemini-pro
            try:
                self.llm = genai.GenerativeModel('gemini-1.5-pro')
            except:
                try:
                    self.llm = genai.GenerativeModel('gemini-1.5-flash')
                except:
                    self.llm = genai.GenerativeModel('gemini-pro')
        else:
            print("Warning: GEMINI_API_KEY not found. LLM features will be limited.")
            self.llm = None
        
        self.load_assessments()
        self.initialize_embeddings()
    
    def load_assessments(self):
        """Load assessment data from JSON file"""
        try:
            if os.path.exists(self.assessments_file):
                with open(self.assessments_file, 'r', encoding='utf-8') as f:
                    self.assessments = json.load(f)
            else:
                print(f"Warning: {self.assessments_file} not found. Using empty list.")
                self.assessments = []
        except Exception as e:
            print(f"Error loading assessments: {e}")
            self.assessments = []
    
    def initialize_embeddings(self):
        """Initialize embedding model and compute embeddings for all assessments"""
        try:
            # Use a lightweight but effective model
            self.embedding_model = SentenceTransformer('all-MiniLM-L6-v2')
            
            # Create text representations for each assessment
            assessment_texts = []
            for assessment in self.assessments:
                text_parts = [assessment.get('name', '')]
                if assessment.get('description'):
                    text_parts.append(assessment['description'])
                if assessment.get('test_type'):
                    text_parts.append(f"Type: {assessment['test_type']}")
                if assessment.get('skills'):
                    text_parts.append(f"Skills: {', '.join(assessment['skills'])}")
                
                assessment_texts.append(' '.join(text_parts))
            
            if assessment_texts:
                print("Computing embeddings for assessments...")
                self.embeddings = self.embedding_model.encode(assessment_texts, show_progress_bar=True)
                print(f"Computed embeddings for {len(assessment_texts)} assessments")
            else:
                print("No assessments to embed")
                self.embeddings = np.array([])
                
        except Exception as e:
            print(f"Error initializing embeddings: {e}")
            self.embeddings = np.array([])
    
    def get_query_embedding(self, query: str) -> np.ndarray:
        """Get embedding for a query"""
        if self.embedding_model is None:
            return None
        return self.embedding_model.encode([query])[0]
    
    def cosine_similarity(self, vec1: np.ndarray, vec2: np.ndarray) -> float:
        """Compute cosine similarity between two vectors"""
        dot_product = np.dot(vec1, vec2)
        norm1 = np.linalg.norm(vec1)
        norm2 = np.linalg.norm(vec2)
        if norm1 == 0 or norm2 == 0:
            return 0.0
        return dot_product / (norm1 * norm2)
    
    def semantic_search(self, query: str, top_k: int = 20) -> List[Dict]:
        """Perform semantic search to find relevant assessments"""
        if len(self.assessments) == 0 or self.embeddings is None or len(self.embeddings) == 0:
            return []
        
        query_embedding = self.get_query_embedding(query)
        if query_embedding is None:
            return []
        
        # Compute similarities
        similarities = []
        for i, assessment_embedding in enumerate(self.embeddings):
            similarity = self.cosine_similarity(query_embedding, assessment_embedding)
            similarities.append((similarity, i))
        
        # Sort by similarity
        similarities.sort(reverse=True, key=lambda x: x[0])
        
        # Get top k results
        results = []
        for similarity, idx in similarities[:top_k]:
            assessment = self.assessments[idx].copy()
            assessment['similarity_score'] = float(similarity)
            results.append(assessment)
        
        return results
    
    def llm_rerank(self, query: str, candidates: List[Dict], top_n: int = 10) -> List[Dict]:
        """Use LLM to rerank and balance recommendations"""
        if not self.llm or len(candidates) == 0:
            return candidates[:top_n]
        
        try:
            # Prepare candidate list for LLM
            candidate_text = "\n".join([
                f"{i+1}. {c['name']} - {c.get('description', '')[:100]}... (Type: {c.get('test_type', 'N/A')})"
                for i, c in enumerate(candidates[:20])  # Limit to top 20 for LLM processing
            ])
            
            prompt = f"""You are an expert in psychometric assessments and talent acquisition. 
Given a job description or hiring query, recommend the most relevant SHL assessments.

Query: {query}

Available assessments:
{candidate_text}

Please:
1. Select the top {top_n} most relevant assessments (numbered 1-{len(candidates[:20])})
2. Ensure a balanced mix if the query spans multiple domains (e.g., both technical skills and behavioral traits)
3. Consider both cognitive/technical assessments (Type: Knowledge & Skills) and personality/behavioral assessments (Type: Personality & Behavior)

Return only the numbers of the selected assessments, separated by commas, in order of relevance.
Example: 1, 5, 3, 7, 2, 9, 4, 6, 8, 10"""
            
            response = self.llm.generate_content(prompt)
            response_text = response.text.strip()
            
            # Parse LLM response
            selected_indices = []
            for part in response_text.split(','):
                try:
                    idx = int(part.strip()) - 1  # Convert to 0-based
                    if 0 <= idx < len(candidates):
                        selected_indices.append(idx)
                except ValueError:
                    continue
            
            # If LLM parsing fails, use original ranking
            if not selected_indices:
                return candidates[:top_n]
            
            # Reorder candidates based on LLM selection
            reranked = [candidates[i] for i in selected_indices if i < len(candidates)]
            
            # Ensure we have at least top_n results
            if len(reranked) < top_n:
                remaining = [c for c in candidates if c not in reranked]
                reranked.extend(remaining[:top_n - len(reranked)])
            
            return reranked[:top_n]
            
        except Exception as e:
            print(f"Error in LLM reranking: {e}")
            # Fallback to similarity-based ranking
            return self.balance_recommendations(query, candidates[:top_n])
    
    def balance_recommendations(self, query: str, candidates: List[Dict]) -> List[Dict]:
        """Balance recommendations across different test types"""
        if len(candidates) <= 5:
            return candidates
        
        # Group by test type
        type_groups = {}
        for candidate in candidates:
            test_type = candidate.get('test_type', 'Other')
            if test_type not in type_groups:
                type_groups[test_type] = []
            type_groups[test_type].append(candidate)
        
        # If we have multiple types, try to balance
        if len(type_groups) > 1:
            balanced = []
            max_per_type = max(1, len(candidates) // len(type_groups))
            
            # Round-robin through types
            type_keys = list(type_groups.keys())
            type_indices = {k: 0 for k in type_keys}
            
            while len(balanced) < len(candidates):
                for type_key in type_keys:
                    if len(balanced) >= len(candidates):
                        break
                    if type_indices[type_key] < len(type_groups[type_key]):
                        balanced.append(type_groups[type_key][type_indices[type_key]])
                        type_indices[type_key] += 1
            
            return balanced[:len(candidates)]
        
        return candidates
    
    def recommend(self, query: str, min_results: int = 5, max_results: int = 10) -> List[Dict]:
        """Main recommendation method"""
        if not query or len(query.strip()) == 0:
            return []
        
        query = query.strip()
        
        # Step 1: Semantic search to get candidates
        candidates = self.semantic_search(query, top_k=20)
        
        if len(candidates) == 0:
            return []
        
        # Step 2: LLM reranking for better relevance and balance
        if self.llm:
            recommendations = self.llm_rerank(query, candidates, top_n=max_results)
        else:
            recommendations = self.balance_recommendations(query, candidates[:max_results])
        
        # Step 3: Ensure minimum results
        if len(recommendations) < min_results:
            # Add more from candidates if available
            remaining = [c for c in candidates if c not in recommendations]
            recommendations.extend(remaining[:min_results - len(recommendations)])
        
        # Step 4: Format results
        formatted_results = []
        for rec in recommendations[:max_results]:
            formatted_results.append({
                'name': rec.get('name', 'Unknown'),
                'url': rec.get('url', ''),
                'description': rec.get('description', ''),
                'test_type': rec.get('test_type', ''),
                'similarity_score': rec.get('similarity_score', 0.0)
            })
        
        return formatted_results
    
    def process_url(self, url: str) -> str:
        """Extract text from a job description URL"""
        try:
            import requests
            from bs4 import BeautifulSoup
            
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
            }
            response = requests.get(url, headers=headers, timeout=30)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Extract main content
            # Remove script and style elements
            for script in soup(["script", "style"]):
                script.decompose()
            
            # Get text
            text = soup.get_text()
            
            # Clean up text
            lines = (line.strip() for line in text.splitlines())
            chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
            text = ' '.join(chunk for chunk in chunks if chunk)
            
            return text[:2000]  # Limit to 2000 characters
            
        except Exception as e:
            print(f"Error processing URL {url}: {e}")
            return ""

