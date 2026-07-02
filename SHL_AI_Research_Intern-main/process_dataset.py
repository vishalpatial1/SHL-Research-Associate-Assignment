"""
Process the dataset file and convert to the format needed for the recommendation system
"""

import pandas as pd
import os
import json

def process_excel_file(file_path='company_database.xlsx'):
    """Process Excel file and identify if it contains assessment data"""
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        return None
    
    print(f"Processing: {file_path}")
    
    # Read Excel file
    excel_file = pd.ExcelFile(file_path)
    print(f"Sheet names: {excel_file.sheet_names}")
    
    for sheet_name in excel_file.sheet_names:
        print(f"\nProcessing sheet: {sheet_name}")
        df = pd.read_excel(file_path, sheet_name=sheet_name, header=None)
        
        # Try to find header row
        print(f"\nFirst 10 rows:")
        print(df.head(10))
        
        # Check if this looks like assessment data
        # Look for common patterns: query, assessment, url, etc.
        text_content = ' '.join(df.astype(str).values.flatten()).lower()
        
        if any(keyword in text_content for keyword in ['query', 'assessment', 'shl', 'test', 'recommendation']):
            print(f"\n✓ This sheet might contain assessment/recommendation data!")
            # Try to find the actual header row
            for i in range(min(5, len(df))):
                row = df.iloc[i]
                if any(keyword in str(row).lower() for keyword in ['query', 'assessment', 'url']):
                    print(f"  Potential header at row {i}: {row.tolist()}")
        
        # Check if this looks like train/test data
        if 'train' in sheet_name.lower() or 'test' in sheet_name.lower():
            print(f"\n✓ This appears to be a train/test dataset!")
            # Try reading with different headers
            for header_row in range(3):
                try:
                    df_with_header = pd.read_excel(file_path, sheet_name=sheet_name, header=header_row)
                    print(f"\n  Reading with header row {header_row}:")
                    print(f"  Columns: {df_with_header.columns.tolist()}")
                    if 'query' in df_with_header.columns.str.lower() or 'Query' in df_with_header.columns:
                        print(f"  ✓ Found query column!")
                        print(f"  Sample queries:")
                        query_col = df_with_header.columns[df_with_header.columns.str.lower().str.contains('query', na=False)][0]
                        print(df_with_header[query_col].head())
                except:
                    pass

def check_for_csv_files():
    """Check for CSV files that might be train/test sets"""
    csv_files = [f for f in os.listdir('.') if f.endswith('.csv')]
    if csv_files:
        print(f"\nFound CSV files: {csv_files}")
        for csv_file in csv_files:
            print(f"\n{'='*50}")
            print(f"File: {csv_file}")
            print(f"{'='*50}")
            try:
                df = pd.read_csv(csv_file)
                print(f"Shape: {df.shape}")
                print(f"Columns: {df.columns.tolist()}")
                print(f"\nFirst few rows:")
                print(df.head())
            except Exception as e:
                print(f"Error reading {csv_file}: {e}")
    else:
        print("\nNo CSV files found in current directory")

if __name__ == '__main__':
    print("="*50)
    print("Dataset Processing Script")
    print("="*50)
    
    # Check for CSV files first
    check_for_csv_files()
    
    # Process Excel file
    if os.path.exists('company_database.xlsx'):
        process_excel_file('company_database.xlsx')
    else:
        print("\ncompany_database.xlsx not found")
    
    # Check data directory
    if os.path.exists('data'):
        print(f"\n{'='*50}")
        print("Files in data/ directory:")
        print(f"{'='*50}")
        for f in os.listdir('data'):
            print(f"  - {f}")

