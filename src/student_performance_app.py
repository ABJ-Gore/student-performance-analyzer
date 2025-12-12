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

# ---------------------------------------------
# PART 2 — Written by: Bella Gerken
# Score statistics + test prep analysis
# ---------------------------------------------

def score_statistics(df):
    """
    Prints average, minimum, and maximum scores
    for Math, Reading, and Writing subjects.
    """
    print("\n===== SCORE STATISTICS =====")

    subjects = ["math_score", "reading_score", "writing_score"]

    for subject in subjects:
        avg = df[subject].mean()
        minimum = df[subject].min()
        maximum = df[subject].max()

        print(f"\n--- {subject.replace('_',' ').title()} ---")
        print(f"Average: {avg:.2f}")
        print(f"Minimum: {minimum}")
        print(f"Maximum: {maximum}")


def test_prep_effect(df):
    """
    Compares score averages between students who
    completed test preparation and those who did not.
    """
    print("\n===== TEST PREPARATION EFFECT =====")

    # Group by the 'test_preparation_course' column
    prep_groups = df.groupby("test_preparation_course")[["math_score", "reading_score", "writing_score"]].mean()

    print("\nAverage Scores Based on Test Preparation:")
    print(prep_groups)

    print("\nInterpretation:")
    print("Students who completed the test preparation course typically score higher.")


# ----- End of Part 2 (Bella Gerken) -----



def main_menu(df):
    """
    Handles user interaction.
    """
    while True:
        print("\n=== Student Exam Performance Analyzer ===")
        print("1. Show basic dataset info")
        print("2. Show score statistics")
        print("3. Test preparation effect analysis")
        print("4. Exit")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            show_basic_stats(df)
        elif choice == "2":
            score_statistics(df)
        elif choice == "3":
            test_prep_effect(df)
        elif choice == "4":
            print("Exiting program.")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    file_path = "StudentsPerformance.csv"
    df = load_data(file_path)

    if df is not None:
        main_menu(df)
