"""
Script to examine the dataset structure
"""

import pandas as pd
import os

file_path = 'company_database.xlsx'

if os.path.exists(file_path):
    print(f"Found file: {file_path}")
    
    # Read Excel file
    try:
        # Try to read all sheets
        excel_file = pd.ExcelFile(file_path)
        print(f"\nSheet names: {excel_file.sheet_names}")
        
        for sheet_name in excel_file.sheet_names:
            print(f"\n{'='*50}")
            print(f"Sheet: {sheet_name}")
            print(f"{'='*50}")
            df = pd.read_excel(file_path, sheet_name=sheet_name)
            print(f"Shape: {df.shape} (rows, columns)")
            print(f"\nColumns: {df.columns.tolist()}")
            print(f"\nFirst 5 rows:")
            print(df.head())
            print(f"\nData types:")
            print(df.dtypes)
            
            # Check for train/test indicators
            if 'query' in df.columns or 'Query' in df.columns:
                print(f"\n✓ Found query column!")
            if 'assessment' in str(df.columns).lower() or 'url' in str(df.columns).lower():
                print(f"✓ Found assessment/URL columns!")
                
    except Exception as e:
        print(f"Error reading file: {e}")
        import traceback
        traceback.print_exc()
else:
    print(f"File not found: {file_path}")
    print(f"Current directory: {os.getcwd()}")
    print(f"Files in directory: {[f for f in os.listdir('.') if f.endswith(('.xlsx', '.csv'))]}")

