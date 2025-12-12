import pandas as pd
import glob
import logging
import os

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def load_csv_files(folder_path="data"):
    files = glob.glob(os.path.join(folder_path, "*.csv"))
    if not files:
        raise FileNotFoundError("No CSV files found in the data folder.")
    logging.info(f"Found {len(files)} CSV file(s): {files}")
    return files

def clean_and_transform(df):
    df = df[df["product"] == "Pink Morsel"]
    df["Sales"] = df["quantity"] * df["price"]
    return df[["Sales", "date", "region"]]

def process_all_files(folder_path="data", output_file="formatted_sales.csv"):
    files = load_csv_files(folder_path)
    dataframes = []

    for file in files:
        logging.info(f"Processing file: {file}")
        df = pd.read_csv(file)
        df_clean = clean_and_transform(df)
        dataframes.append(df_clean)

    final_df = pd.concat(dataframes, ignore_index=True)
    final_df.to_csv(output_file, index=False)
    logging.info(f"Created {output_file}")
    return final_df

if __name__ == "__main__":
    process_all_files()
