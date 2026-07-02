"""
Script to help set up the dataset for SHL Assessment Recommendation System
This script will:
1. Check for train.csv and test.csv files
2. Create sample data if needed
3. Validate the format
4. Organize files into the data/ directory
"""

import os
import pandas as pd
import json

def check_for_dataset_files():
    """Check for train.csv and test.csv in current directory and data/"""
    print("="*60)
    print("Checking for Dataset Files")
    print("="*60)
    
    # Check root directory
    root_files = [f for f in os.listdir('.') if f.endswith('.csv')]
    print(f"\nCSV files in root directory: {root_files}")
    
    # Check data directory
    data_files = []
    if os.path.exists('data'):
        data_files = [f for f in os.listdir('data') if f.endswith('.csv')]
        print(f"CSV files in data/ directory: {data_files}")
    
    # Look for train/test files
    all_files = root_files + data_files
    train_files = [f for f in all_files if 'train' in f.lower()]
    test_files = [f for f in all_files if 'test' in f.lower()]
    
    return train_files, test_files, root_files

def examine_csv_file(filepath):
    """Examine a CSV file to understand its structure"""
    try:
        df = pd.read_csv(filepath)
        print(f"\n  File: {filepath}")
        print(f"  Shape: {df.shape} (rows, columns)")
        print(f"  Columns: {df.columns.tolist()}")
        
        # Check if it has query column
        query_cols = [col for col in df.columns if 'query' in col.lower()]
        if query_cols:
            print(f"  [OK] Found query column: {query_cols[0]}")
            print(f"  Sample queries:")
            for i, query in enumerate(df[query_cols[0]].head(3)):
                print(f"    {i+1}. {str(query)[:80]}...")
            return True, query_cols[0]
        else:
            print(f"  [ERROR] No query column found")
            print(f"  First few rows:")
            print(df.head(3))
            return False, None
    except Exception as e:
        print(f"  [ERROR] Error reading file: {e}")
        return False, None

def create_sample_train_test():
    """Create sample train and test CSV files if they don't exist"""
    print("\n" + "="*60)
    print("Creating Sample Train/Test Files")
    print("="*60)
    
    os.makedirs('data', exist_ok=True)
    
    # Sample training set (labeled - with recommendations)
    sample_train = pd.DataFrame({
        'query': [
            "I am hiring for Java developers who can also collaborate effectively with my business teams.",
            "Looking to hire mid-level professionals who are proficient in Python, SQL and Java Script.",
            "Need assessments for a customer service role requiring good communication and problem-solving skills.",
            "Hiring for a data analyst position requiring analytical thinking and attention to detail.",
            "Looking for assessments to evaluate leadership potential and team collaboration skills."
        ]
    })
    
    train_path = 'data/train.csv'
    if not os.path.exists(train_path):
        sample_train.to_csv(train_path, index=False)
        print(f"\n[OK] Created sample {train_path}")
        print(f"  Contains {len(sample_train)} sample queries")
    else:
        print(f"\n[OK] {train_path} already exists")
    
    # Sample test set (unlabeled - for predictions)
    sample_test = pd.DataFrame({
        'query': [
            "I am hiring for Java developers who can also collaborate effectively with my business teams.",
            "Looking to hire mid-level professionals who are proficient in Python, SQL and Java Script.",
            "Here is a JD text, can you recommend some assessment that can help me screen applications. I am hiring for an analyst and wants applications to screen using Cognitive and personality tests",
            "Need to assess candidates for a software engineering role with strong problem-solving abilities.",
            "Hiring for a project manager who needs to work with cross-functional teams and stakeholders.",
            "Looking for assessments to evaluate technical skills for a DevOps engineer position.",
            "Need personality and behavioral assessments for a sales role.",
            "Hiring for a financial analyst requiring numerical reasoning and analytical skills.",
            "Looking for comprehensive assessments for a senior developer role."
        ]
    })
    
    test_path = 'data/test.csv'
    if not os.path.exists(test_path):
        sample_test.to_csv(test_path, index=False)
        print(f"[OK] Created sample {test_path}")
        print(f"  Contains {len(sample_test)} sample queries")
    else:
        print(f"[OK] {test_path} already exists")

def process_existing_files(train_files, test_files, root_files):
    """Process existing CSV files and organize them"""
    print("\n" + "="*60)
    print("Processing Existing Files")
    print("="*60)
    
    os.makedirs('data', exist_ok=True)
    
    # Process train files
    if train_files:
        for train_file in train_files:
            print(f"\nProcessing: {train_file}")
            # Handle files in data/ directory
            filepath = train_file if os.path.exists(train_file) else f'data/{train_file}'
            is_valid, query_col = examine_csv_file(filepath)
            if is_valid:
                # Copy to data directory if not already there
                dest_path = f'data/{os.path.basename(train_file)}'
                if not os.path.exists(dest_path):
                    df = pd.read_csv(train_file)
                    df.to_csv(dest_path, index=False)
                    print(f"  ✓ Copied to {dest_path}")
                else:
                    print(f"  ✓ Already exists in data/")
    
    # Process test files
    if test_files:
        for test_file in test_files:
            print(f"\nProcessing: {test_file}")
            # Handle files in data/ directory
            filepath = test_file if os.path.exists(test_file) else f'data/{test_file}'
            is_valid, query_col = examine_csv_file(filepath)
            if is_valid:
                # Copy to data directory if not already there
                dest_path = f'data/{os.path.basename(test_file)}'
                if not os.path.exists(dest_path):
                    df = pd.read_csv(test_file)
                    df.to_csv(dest_path, index=False)
                    print(f"  ✓ Copied to {dest_path}")
                else:
                    print(f"  ✓ Already exists in data/")
    
    # Check other CSV files that might be datasets
    other_csvs = [f for f in root_files if f not in train_files + test_files]
    if other_csvs:
        print(f"\nOther CSV files found (might be datasets): {other_csvs}")
        for csv_file in other_csvs:
            print(f"\nExamining: {csv_file}")
            is_valid, query_col = examine_csv_file(csv_file)
            if is_valid:
                response = input(f"  This file has a query column. Use it as train.csv or test.csv? (train/test/skip): ")
                if response.lower() == 'train':
                    df = pd.read_csv(csv_file)
                    df.to_csv('data/train.csv', index=False)
                    print(f"  [OK] Saved as data/train.csv")
                elif response.lower() == 'test':
                    df = pd.read_csv(csv_file)
                    df.to_csv('data/test.csv', index=False)
                    print(f"  [OK] Saved as data/test.csv")

def main():
    """Main function"""
    print("="*60)
    print("SHL Assessment Recommendation System - Dataset Setup")
    print("="*60)
    
    # Check for existing files
    train_files, test_files, root_files = check_for_dataset_files()
    
    # Check if we have the required files
    has_train = os.path.exists('data/train.csv')
    has_test = os.path.exists('data/test.csv')
    
    if has_train and has_test:
        print("\n[OK] Both train.csv and test.csv found in data/ directory!")
        print("\nValidating files...")
        examine_csv_file('data/train.csv')
        examine_csv_file('data/test.csv')
    else:
        # Process existing files
        if train_files or test_files:
            process_existing_files(train_files, test_files, root_files)
        
        # Create sample files if still missing
        if not os.path.exists('data/train.csv') or not os.path.exists('data/test.csv'):
            print("\n" + "="*60)
            print("Creating Sample Files")
            print("="*60)
            print("\nNote: You should replace these with your actual train.csv and test.csv files")
            print("Expected format:")
            print("  train.csv: CSV with 'query' column (and optionally assessment URLs)")
            print("  test.csv: CSV with 'query' column (for generating predictions)")
            create_sample_train_test()
    
    # Check for assessments.json
    print("\n" + "="*60)
    print("Checking Assessment Data")
    print("="*60)
    if not os.path.exists('data/assessments.json'):
        print("\n[MISSING] assessments.json not found")
        print("  Run: python create_sample_data.py")
    else:
        with open('data/assessments.json', 'r') as f:
            assessments = json.load(f)
        print(f"\n[OK] Found assessments.json with {len(assessments)} assessments")
    
    # Final summary
    print("\n" + "="*60)
    print("Setup Summary")
    print("="*60)
    print(f"Train CSV: {'[OK]' if os.path.exists('data/train.csv') else '[MISSING]'}")
    print(f"Test CSV: {'[OK]' if os.path.exists('data/test.csv') else '[MISSING]'}")
    print(f"Assessments: {'[OK]' if os.path.exists('data/assessments.json') else '[MISSING]'}")
    
    if os.path.exists('data/train.csv') and os.path.exists('data/test.csv') and os.path.exists('data/assessments.json'):
        print("\n[OK] All required files are ready!")
        print("\nNext steps:")
        print("  1. Review and update data/train.csv with your actual training data")
        print("  2. Review and update data/test.csv with your actual test queries")
        print("  3. Run: python run_server.py (to start the API)")
        print("  4. Run: python evaluation.py (to generate predictions)")
    else:
        print("\n[WARNING] Some files are missing. Please:")
        if not os.path.exists('data/assessments.json'):
            print("  - Run: python create_sample_data.py")
        if not os.path.exists('data/train.csv') or not os.path.exists('data/test.csv'):
            print("  - Add your train.csv and test.csv files to the data/ directory")
            print("  - Format: CSV files with a 'query' column")

if __name__ == '__main__':
    main()

