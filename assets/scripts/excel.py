import os
import pandas as pd
from glob import glob

# Define the folder path
folder_path = r"C:\Users\z003yh0e\Downloads\Lux Power"
output_file = r"C:\Users\z003yh0e\Downloads\Lux Power\luxpower.csv"

# Get all .xls files in the folder
xls_files = glob(os.path.join(folder_path, "*.xls")) + glob(os.path.join(folder_path, "*.xlsx"))

# Check if there are files
if not xls_files:
    print("No .xls or .xlsx files found in the folder!")
    exit()

# Initialize an empty list to store DataFrames
dataframes = []

# Loop through each file
for file in xls_files:
    try:
        # Check file extension and select the correct engine
        if file.endswith(".xls"):
            engine = "xlrd"  # Older Excel format
        else:
            engine = "openpyxl"  # Newer Excel format
        
        # Load the Excel file using the correct engine
        xls = pd.ExcelFile(file, engine=engine)

        # Loop through each sheet in the file
        for sheet_name in xls.sheet_names:
            df = pd.read_excel(file, sheet_name=sheet_name, engine=engine)

            # Remove the "Serial number" column if it exists
            df = df.drop(columns=["Serial number"], errors="ignore")

            # Remove columns where all values are null or blank
            df = df.dropna(axis=1, how="all")

            # Rename "Time" column to "Datetime" if it exists
            if "Time" in df.columns:
                df = df.rename(columns={"Time": "Datetime"})

                # Convert "Datetime" column to the format "yyyy-MM-dd HH:mm:ss"
                df["Datetime"] = pd.to_datetime(df["Datetime"], errors="coerce").dt.strftime("%Y-%m-%d %H:%M:%S")

            # Append to list
            dataframes.append(df)

    except Exception as e:
        print(f"Error processing {file}: {e}")

# Combine all DataFrames
if dataframes:
    final_df = pd.concat(dataframes, ignore_index=True)

    # Save to CSV
    final_df.to_csv(output_file, index=False)
    print(f"Successfully combined {len(xls_files)} files into {output_file}")
else:
    print("No valid data found to merge.")