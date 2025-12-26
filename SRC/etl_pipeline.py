# File paths for ETL pipeline
Raw_Data_File_Path = "Data/Raw/diabetic_data.csv"
Processed_Data_File_Path = "Data/Processed/diabetic_data_processed.csv"


# ETL Pipeline: Load Module
import pandas as pd

def load_data(Raw_Data_File_Path):
    """Load raw data from a CSV file."""
    print(f"Loading data from {Raw_Data_File_Path}")
    return pd.read_csv(Raw_Data_File_Path)


# ETL Pipeline: Clean Module
def clean_data(df):
    """Clean the raw data."""
    print("Cleaning data...")

    # Remove duplicates
    df = df.drop_duplicates()

    # Impute missing values
    for column in df.columns:
        if df[column].isnull().any():
            if df[column].dtype == 'object':  # For categorical columns
                df[column].fillna(df[column].mode()[0])
            else:  # For numerical columns
                df[column].fillna(df[column].mean())
    
    return df


# ETL Pipeline: Save Processed Data
import os

def save_data(df, Processed_Data_File_Path):
    """Save processed data to a CSV file."""
    print(f"Saving processed data to {Processed_Data_File_Path}")
    os.makedirs(os.path.dirname(Processed_Data_File_Path), exist_ok=True)
    df.to_csv(Processed_Data_File_Path, index=False)


# ETL Pipeline: Test Load Module
if __name__ == "__main__":
    data = load_data(Raw_Data_File_Path)
    cleaned_data = clean_data(data)
    save_data(cleaned_data, Processed_Data_File_Path)
    print(cleaned_data.head())