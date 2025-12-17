import pandas as pd
import matplotlib.pyplot as plt

# =====================================================
# PART 1 — Data Loading & Basic Exploration
# Written by: Abhijay Gore
# =====================================================

def load_data(file_path):
    """
    Loads the student performance dataset from a CSV file.
    """
    try:
        df = pd.read_csv(file_path)
    except FileNotFoundError:
        print("CSV file not found.")
        return None

    # Clean column names
    df.columns = [
        c.strip().lower().replace(" ", "_").replace("/", "_")
        for c in df.columns
    ]
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


# =====================================================
# PART 2 — Score Statistics & Correlation Analysis
# Written by: Bella Gerken (Statistics)
# Correlation added by: Abhijay Gore
# =====================================================

def score_statistics_and_correlation(df):
    """
    Prints score statistics and correlation between subjects.
    """
    print("\n===== SCORE STATISTICS =====")

    subjects = ["math_score", "reading_score", "writing_score"]

    for subject in subjects:
        print(f"\n--- {subject.replace('_',' ').title()} ---")
        print(f"Average: {df[subject].mean():.2f}")
        print(f"Minimum: {df[subject].min()}")
        print(f"Maximum: {df[subject].max()}")

    print("\n===== SCORE CORRELATION =====")
    corr = df[subjects].corr()
    print(corr)

    print("\nInterpretation:")
    print("Reading and writing scores are strongly correlated, while math shows a slightly weaker relationship.")


def test_prep_effect(df):
    """
    Compares score averages between students who
    completed test preparation and those who did not.
    """
    print("\n===== TEST PREPARATION EFFECT =====")

    prep_groups = df.groupby(
        "test_preparation_course"
    )[["math_score", "reading_score", "writing_score"]].mean()

    print("\nAverage Scores Based on Test Preparation:")
    print(prep_groups)

    print("\nInterpretation:")
    print("Students who completed the test preparation course generally score higher across all subjects.")


# =====================================================
# PART 3 — Group Score Comparison
# Written by: Eric Chisala
# =====================================================

def normalize_column_name(user_input):
    """
    Normalize user input to match cleaned dataframe column names.
    """
    return user_input.strip().lower().replace(" ", "_").replace("/", "_")


def compare_group_scores(df):
    """
    Compare average math, reading, and writing scores
    across groups of a chosen category.
    """
    print("\n===== GROUP SCORE COMPARISON =====")
    print("Available group categories:")
    print("- gender")
    print("- lunch")
    print("- race/ethnicity")
    print("- parental level of education")
    print("- test preparation course")

    raw_col = input("\nEnter category: ")
    group_col = normalize_column_name(raw_col)

    if group_col not in df.columns:
        print("Invalid category column.")
        return

    print(f"\n--- Comparing scores by {group_col.replace('_', ' ').title()} ---")

    for g in df[group_col].unique():
        subset = df[df[group_col] == g]
        print(f"\nGroup: {g}")
        print(f"  Math Avg:    {subset['math_score'].mean():.2f}")
        print(f"  Reading Avg: {subset['reading_score'].mean():.2f}")
        print(f"  Writing Avg: {subset['writing_score'].mean():.2f}")


# =====================================================
# PART 4 — Visualization
# Written by: Takudzwa Musimwa
# =====================================================

def plot_score_distribution(df):
    """
    Plots a histogram of scores for the selected subject.
    """
    print("\n===== SCORE DISTRIBUTION PLOT =====")
    print("Available subjects:")
    print("- math_score")
    print("- reading_score")
    print("- writing_score")

    subject = input("Enter subject to plot: ").strip().lower().replace(" ", "_")

    if subject not in df.columns:
        print("Invalid subject.")
        return

    plt.figure()
    plt.hist(df[subject].dropna(), bins=10)
    plt.xlabel(subject.replace("_", " ").title())
    plt.ylabel("Number of Students")
    plt.title(f"Distribution of {subject.replace('_', ' ').title()}")
    plt.show()


# =====================================================
# MAIN MENU — User Interaction
# =====================================================

def main_menu(df):
    """
    Handles user interaction.
    """
    while True:
        print("\n=== Interactive Student Exam Performance Analyzer ===")
        print("1. Show basic dataset info")
        print("2. Score statistics and correlation analysis")
        print("3. Test preparation effect analysis")
        print("4. Compare scores by group")
        print("5. Plot score distribution")
        print("6. Exit")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            show_basic_stats(df)
        elif choice == "2":
            score_statistics_and_correlation(df)
        elif choice == "3":
            test_prep_effect(df)
        elif choice == "4":
            compare_group_scores(df)
        elif choice == "5":
            plot_score_distribution(df)
        elif choice == "6":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Try again.")


# =====================================================
# PROGRAM ENTRY POINT
# =====================================================

if __name__ == "__main__":
    file_path = "StudentsPerformance.csv"
    df = load_data(file_path)

    if df is not None and not df.empty:
        main_menu(df)
    else:
        print("Failed to load dataset.")
