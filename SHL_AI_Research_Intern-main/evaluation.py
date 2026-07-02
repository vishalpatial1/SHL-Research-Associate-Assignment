"""
Evaluation script to generate predictions for test set
"""

import pandas as pd
import json
from recommender import AssessmentRecommender
import os

def load_test_set(test_file: str = 'data/test.csv') -> pd.DataFrame:
    """Load test set queries"""
    try:
        if os.path.exists(test_file):
            df = pd.read_csv(test_file)
            return df
        else:
            print(f"Warning: {test_file} not found. Creating sample test set.")
            # Create sample test set if file doesn't exist
            sample_queries = [
                "I am hiring for Java developers who can also collaborate effectively with my business teams.",
                "Looking to hire mid-level professionals who are proficient in Python, SQL and Java Script.",
                "Here is a JD text, can you recommend some assessment that can help me screen applications. I am hiring for an analyst and wants applications to screen using Cognitive and personality tests"
            ]
            df = pd.DataFrame({'query': sample_queries})
            return df
    except Exception as e:
        print(f"Error loading test set: {e}")
        return pd.DataFrame()

def generate_predictions(recommender: AssessmentRecommender, test_df: pd.DataFrame) -> pd.DataFrame:
    """Generate predictions for test queries"""
    results = []
    
    for idx, row in test_df.iterrows():
        query = row['query']
        print(f"Processing query {idx + 1}/{len(test_df)}: {query[:50]}...")
        
        # Get recommendations
        recommendations = recommender.recommend(query, min_results=5, max_results=10)
        
        # Format for submission (query, assessment_url pairs)
        # Note: Column names must match exactly: "Query" and "Assessment_url"
        for rec in recommendations:
            results.append({
                'Query': query,
                'Assessment_url': rec['url']
            })
    
    return pd.DataFrame(results)

def main():
    """Main evaluation function"""
    print("Starting evaluation...")
    
    # Initialize recommender
    print("Loading recommender...")
    recommender = AssessmentRecommender()
    
    # Load test set
    print("Loading test set...")
    test_df = load_test_set('data/test.csv')
    
    if test_df.empty:
        print("Error: Test set is empty. Please provide test.csv in the data/ directory.")
        return
    
    print(f"Found {len(test_df)} test queries")
    
    # Generate predictions
    print("\nGenerating predictions...")
    predictions_df = generate_predictions(recommender, test_df)
    
    # Save to CSV
    output_file = 'predictions.csv'
    predictions_df.to_csv(output_file, index=False)
    print(f"\nPredictions saved to {output_file}")
    print(f"Total predictions: {len(predictions_df)}")
    
    # Display sample
    print("\nSample predictions:")
    print(predictions_df.head(10).to_string())

if __name__ == '__main__':
    main()

