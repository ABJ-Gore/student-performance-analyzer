import pandas as pd

def load_data(file_path):
    """
    Loads the student performance dataset from a CSV file.
    """
    try:
        df = pd.read_csv(file_path)
    except FileNotFoundError:
        print("CSV file not found.")
        return None

    # Clean column names so they are easier to work with
    df.columns = [c.strip().lower().replace(" ", "_").replace("/", "_") for c in df.columns]
    return df

def show_basic_stats(df):
    """
    Displays basic information about the dataset.
    """
    print("\n--- Dataset Info ---")
    print(f"Rows: {len(df)}")
    print(f"Columns: {len(df.columns)}")

    print("\nColumn names:")
    for col in df.columns:
        print("-", col)

    print("\nFirst 5 rows:")
    print(df.head())

def main_menu(df):
    """
    Handles user interaction.
    """
    while True:
        print("\n=== Student Exam Performance Analyzer ===")
        print("1. Show basic dataset info")
        print("2. Exit")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            show_basic_stats(df)
        elif choice == "2":
            print("Exiting program.")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    file_path = "StudentsPerformance.csv"
    df = load_data(file_path)

    if df is not None:
        main_menu(df)
