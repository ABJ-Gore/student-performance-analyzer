import pandas as pd

def load_data():
    return pd.read_csv("StudentsPerformance.csv")

def show_subject_averages(df):
    print("\n--- Overall Score Stats ---")
    for subject in ["math_score", "reading_score", "writing_score"]:
        print(f"{subject.capitalize()}:")
        print(f"  Mean: {df[subject].mean():.2f}")
        print(f"  Min:  {df[subject].min():.2f}")
        print(f"  Max:  {df[subject].max():.2f}")

def compare_group_scores(df, group_col):
    print(f"\n--- Comparing scores by {group_col} ---")
    groups = df[group_col].unique()
    for g in groups:
        subset = df[df[group_col] == g]
        print(f"\nGroup: {g}")
        print(f"  Math Avg:    {subset['math_score'].mean():.2f}")
        print(f"  Reading Avg: {subset['reading_score'].mean():.2f}")
        print(f"  Writing Avg: {subset['writing_score'].mean():.2f}")

def main():
    df = load_data()
    while True:
        print("\n=== Student Performance Analyzer ===")
        print("1. Show overall subject averages")
        print("2. Compare scores by group")
        print("0. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            show_subject_averages(df)
        elif choice == "2":
            print("\nChoose grouping factor:")
            print("Options: gender, lunch, test_preparation_course")
            group_col = input("Enter column name: ").strip()
            if group_col in df.columns:
                compare_group_scores(df, group_col)
            else:
                print("Invalid column. Try again.")
        elif choice == "0":
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
