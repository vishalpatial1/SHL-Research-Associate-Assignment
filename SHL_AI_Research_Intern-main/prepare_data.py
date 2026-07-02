"""
Script to prepare and organize dataset files for the SHL Assessment Recommendation System
"""

import os
import pandas as pd
import json

def create_data_directory():
    """Create data directory structure"""
    os.makedirs('data', exist_ok=True)
    print("[OK] Created data/ directory")

def check_for_datasets():
    """Check for train/test CSV files and organize them"""
    print("\n" + "="*50)
    print("Checking for dataset files...")
    print("="*50)
    
    # Check root directory
    root_files = [f for f in os.listdir('.') if f.endswith(('.csv', '.xlsx', '.xls'))]
    print(f"\nFiles in root directory: {root_files}")
    
    # Expected files based on requirements:
    # - train.csv (labeled training set with 10 queries)
    # - test.csv (unlabeled test set with 9 queries)
    
    # Check if train.csv exists
    train_files = [f for f in root_files if 'train' in f.lower()]
    test_files = [f for f in root_files if 'test' in f.lower()]
    
    if train_files:
        print(f"\n[OK] Found training file(s): {train_files}")
        for train_file in train_files:
            try:
                df = pd.read_csv(train_file)
                print(f"  - {train_file}: {df.shape} (rows, columns)")
                print(f"    Columns: {df.columns.tolist()}")
                # Copy to data directory
                if not os.path.exists(f'data/{train_file}'):
                    df.to_csv(f'data/{train_file}', index=False)
                    print(f"    [OK] Copied to data/{train_file}")
            except Exception as e:
                print(f"    [ERROR] Error reading {train_file}: {e}")
    
    if test_files:
        print(f"\n[OK] Found test file(s): {test_files}")
        for test_file in test_files:
            try:
                df = pd.read_csv(test_file)
                print(f"  - {test_file}: {df.shape} (rows, columns)")
                print(f"    Columns: {df.columns.tolist()}")
                # Copy to data directory
                if not os.path.exists(f'data/{test_file}'):
                    df.to_csv(f'data/{test_file}', index=False)
                    print(f"    [OK] Copied to data/{test_file}")
            except Exception as e:
                print(f"    [ERROR] Error reading {test_file}: {e}")
    
    # Check data directory
    if os.path.exists('data'):
        data_files = [f for f in os.listdir('data') if f.endswith(('.csv', '.json'))]
        if data_files:
            print(f"\n[OK] Files in data/ directory: {data_files}")
        else:
            print(f"\n[WARNING] No CSV/JSON files found in data/ directory")
    
    # Check if assessments.json exists
    if not os.path.exists('data/assessments.json'):
        print("\n[WARNING] assessments.json not found. Run 'python create_sample_data.py' to create it.")
    else:
        with open('data/assessments.json', 'r') as f:
            assessments = json.load(f)
        print(f"\n[OK] Found assessments.json with {len(assessments)} assessments")

def validate_train_format(train_file='data/train.csv'):
    """Validate training set format"""
    if not os.path.exists(train_file):
        print(f"\n[WARNING] {train_file} not found")
        return False
    
    try:
        df = pd.read_csv(train_file)
        print(f"\n{'='*50}")
        print(f"Validating {train_file}")
        print(f"{'='*50}")
        print(f"Shape: {df.shape}")
        print(f"Columns: {df.columns.tolist()}")
        
        # Check for query column
        query_cols = [col for col in df.columns if 'query' in col.lower()]
        if query_cols:
            print(f"[OK] Found query column: {query_cols[0]}")
        else:
            print("[ERROR] No query column found")
        
        # Check for assessment/URL columns
        assessment_cols = [col for col in df.columns if any(kw in col.lower() for kw in ['assessment', 'url', 'recommendation'])]
        if assessment_cols:
            print(f"[OK] Found assessment columns: {assessment_cols}")
        else:
            print("[INFO] No assessment/URL columns found (this is OK for training set)")
        
        print(f"\nSample data:")
        print(df.head())
        return True
        
    except Exception as e:
        print(f"[ERROR] Error validating {train_file}: {e}")
        return False

def validate_test_format(test_file='data/test.csv'):
    """Validate test set format"""
    if not os.path.exists(test_file):
        print(f"\n[WARNING] {test_file} not found")
        print("  Expected format: CSV with 'query' column")
        return False
    
    try:
        df = pd.read_csv(test_file)
        print(f"\n{'='*50}")
        print(f"Validating {test_file}")
        print(f"{'='*50}")
        print(f"Shape: {df.shape}")
        print(f"Columns: {df.columns.tolist()}")
        
        # Check for query column
        query_cols = [col for col in df.columns if 'query' in col.lower()]
        if query_cols:
            print(f"[OK] Found query column: {query_cols[0]}")
            print(f"\nSample queries:")
            print(df[query_cols[0]].head())
            return True
        else:
            print("[ERROR] No query column found")
            print("  Expected column name: 'query' or 'Query'")
            return False
        
    except Exception as e:
        print(f"[ERROR] Error validating {test_file}: {e}")
        return False

def main():
    """Main function"""
    print("="*50)
    print("SHL Assessment Recommendation System")
    print("Data Preparation Script")
    print("="*50)
    
    # Create data directory
    create_data_directory()
    
    # Check for datasets
    check_for_datasets()
    
    # Validate formats
    print("\n" + "="*50)
    print("Validating Dataset Formats")
    print("="*50)
    
    train_valid = validate_train_format()
    test_valid = validate_test_format()
    
    # Summary
    print("\n" + "="*50)
    print("Summary")
    print("="*50)
    print(f"Training set: {'[OK] Ready' if train_valid else '[ERROR] Not found or invalid'}")
    print(f"Test set: {'[OK] Ready' if test_valid else '[ERROR] Not found or invalid'}")
    
    if not os.path.exists('data/assessments.json'):
        print(f"Assessments: [ERROR] Not found - run 'python create_sample_data.py'")
    else:
        print(f"Assessments: [OK] Ready")
    
    print("\nNext steps:")
    if not os.path.exists('data/assessments.json'):
        print("  1. Run: python create_sample_data.py")
    if not test_valid:
        print("  2. Add test.csv to data/ directory with 'query' column")
    if train_valid and test_valid and os.path.exists('data/assessments.json'):
        print("  [OK] All data ready! You can now:")
        print("    - Run: python run_server.py (to start API)")
        print("    - Run: python evaluation.py (to generate predictions)")

if __name__ == '__main__':
    main()

