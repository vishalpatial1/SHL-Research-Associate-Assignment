"""
Web scraper for SHL Assessment Catalog
Crawls individual test solutions from https://www.shl.com/solutions/products/product-catalog/
"""

import requests
from bs4 import BeautifulSoup
import json
import time
import re
from typing import List, Dict

class SHLScraper:
    def __init__(self):
        self.base_url = "https://www.shl.com"
        self.catalog_url = "https://www.shl.com/solutions/products/product-catalog/"
        self.assessments = []
        
    def scrape_catalog(self) -> List[Dict]:
        """Scrape all individual test solutions from the catalog"""
        print("Starting to scrape SHL catalog...")
        
        try:
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
            }
            response = requests.get(self.catalog_url, headers=headers, timeout=30)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Find all assessment links
            # The structure may vary, so we'll look for links that contain assessment information
            assessment_links = []
            
            # Look for links in the catalog page
            # This is a simplified approach - in production, you'd need to handle pagination and dynamic loading
            for link in soup.find_all('a', href=True):
                href = link.get('href', '')
                text = link.get_text(strip=True)
                
                # Filter for individual test solutions (exclude pre-packaged solutions)
                if '/solutions/products/' in href and 'product-catalog' not in href:
                    full_url = href if href.startswith('http') else self.base_url + href
                    
                    # Skip pre-packaged job solutions
                    if 'pre-packaged' in text.lower() or 'job-solution' in href.lower():
                        continue
                    
                    if text and len(text) > 5:  # Filter out navigation links
                        assessment_links.append({
                            'name': text,
                            'url': full_url,
                            'text': text
                        })
            
            # Also try to find assessment cards/items
            # Look for common patterns in SHL's website structure
            cards = soup.find_all(['div', 'article', 'section'], class_=re.compile(r'card|product|assessment|test', re.I))
            
            for card in cards:
                link_elem = card.find('a', href=True)
                if link_elem:
                    href = link_elem.get('href', '')
                    name = link_elem.get_text(strip=True)
                    
                    if '/solutions/products/' in href and name:
                        full_url = href if href.startswith('http') else self.base_url + href
                        
                        # Get additional details if available
                        description = ""
                        desc_elem = card.find(['p', 'div'], class_=re.compile(r'desc|summary|text', re.I))
                        if desc_elem:
                            description = desc_elem.get_text(strip=True)
                        
                        # Extract test type if available
                        test_type = ""
                        type_elem = card.find(['span', 'div'], class_=re.compile(r'type|category', re.I))
                        if type_elem:
                            test_type = type_elem.get_text(strip=True)
                        
                        assessment_links.append({
                            'name': name,
                            'url': full_url,
                            'description': description,
                            'test_type': test_type
                        })
            
            # Remove duplicates
            seen_urls = set()
            unique_assessments = []
            for assessment in assessment_links:
                if assessment['url'] not in seen_urls:
                    seen_urls.add(assessment['url'])
                    unique_assessments.append(assessment)
            
            print(f"Found {len(unique_assessments)} assessments")
            
            # For a more comprehensive scrape, we might need to:
            # 1. Handle JavaScript-rendered content
            # 2. Use Selenium or Playwright for dynamic content
            # 3. Follow pagination links
            
            # For now, we'll create a more comprehensive dataset by scraping individual pages
            detailed_assessments = []
            for i, assessment in enumerate(unique_assessments[:100]):  # Limit to avoid too many requests
                print(f"Scraping details for {i+1}/{min(len(unique_assessments), 100)}: {assessment['name']}")
                detailed = self.scrape_assessment_details(assessment)
                if detailed:
                    detailed_assessments.append(detailed)
                time.sleep(1)  # Be respectful with requests
            
            self.assessments = detailed_assessments
            return detailed_assessments
            
        except Exception as e:
            print(f"Error scraping catalog: {e}")
            # Return sample data structure if scraping fails
            return self.get_sample_data()
    
    def scrape_assessment_details(self, assessment: Dict) -> Dict:
        """Scrape detailed information from individual assessment page"""
        try:
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
            }
            response = requests.get(assessment['url'], headers=headers, timeout=15)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Extract description
            description = assessment.get('description', '')
            desc_selectors = [
                soup.find('div', class_=re.compile(r'description|content|body', re.I)),
                soup.find('section', class_=re.compile(r'description|overview', re.I)),
                soup.find('p', class_=re.compile(r'lead|intro', re.I))
            ]
            for desc in desc_selectors:
                if desc:
                    description = desc.get_text(strip=True)
                    break
            
            # Extract test type/category
            test_type = assessment.get('test_type', '')
            type_selectors = [
                soup.find(['span', 'div'], class_=re.compile(r'type|category|tag', re.I)),
                soup.find('meta', {'property': 'og:type'}),
            ]
            for type_elem in type_selectors:
                if type_elem:
                    test_type = type_elem.get_text(strip=True) or type_elem.get('content', '')
                    break
            
            # Extract skills/competencies if available
            skills = []
            skill_elems = soup.find_all(['li', 'span'], class_=re.compile(r'skill|competency|ability', re.I))
            for skill in skill_elems[:10]:  # Limit to 10
                skill_text = skill.get_text(strip=True)
                if skill_text:
                    skills.append(skill_text)
            
            return {
                'name': assessment['name'],
                'url': assessment['url'],
                'description': description,
                'test_type': test_type,
                'skills': skills
            }
            
        except Exception as e:
            print(f"Error scraping {assessment['url']}: {e}")
            return {
                'name': assessment['name'],
                'url': assessment['url'],
                'description': assessment.get('description', ''),
                'test_type': assessment.get('test_type', ''),
                'skills': []
            }
    
    def get_sample_data(self) -> List[Dict]:
        """Return sample assessment data structure when scraping fails"""
        # This is a fallback - in production, you'd want comprehensive data
        return [
            {
                'name': 'OPQ32 (Occupational Personality Questionnaire)',
                'url': 'https://www.shl.com/solutions/products/opq32/',
                'description': 'Comprehensive personality assessment measuring behavioral preferences',
                'test_type': 'Personality & Behavior',
                'skills': ['Personality', 'Behavioral Preferences', 'Work Styles']
            },
            {
                'name': 'Verify G+',
                'url': 'https://www.shl.com/solutions/products/verify-g-plus/',
                'description': 'Cognitive ability test measuring numerical, verbal, and abstract reasoning',
                'test_type': 'Knowledge & Skills',
                'skills': ['Numerical Reasoning', 'Verbal Reasoning', 'Abstract Reasoning']
            }
        ]
    
    def save_to_json(self, filename: str = 'data/assessments.json'):
        """Save scraped assessments to JSON file"""
        import os
        os.makedirs('data', exist_ok=True)
        
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(self.assessments, f, indent=2, ensure_ascii=False)
        print(f"Saved {len(self.assessments)} assessments to {filename}")

if __name__ == '__main__':
    scraper = SHLScraper()
    assessments = scraper.scrape_catalog()
    scraper.save_to_json()
    print(f"\nScraping complete! Found {len(assessments)} assessments.")

