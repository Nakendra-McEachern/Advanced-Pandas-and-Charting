
import pandas as pd
import matplotlib.pyplot as plt

def main():
    # Display my student ID.
    print("nakmce5302")

    # Create a classroom roster with 10 students.
    students = [
        "John", "Mary", "James", "Sarah", "Michael",
        "Jessica", "David", "Ashley", "Daniel", "Emily"
    ]

    # Create the two subjects for each student.
    subjects = ["Math", "Science"]

    # Create a MultiIndex using students and subjects.
    index = pd.MultiIndex.from_product(
        [students, subjects],
        names=["Student", "Subject"]
    )

    # Store grades for each student in both subjects.
    grades = [
        85, 90, 92, 88, 78, 84, 95, 91, 87, 89,
        82, 86, 76, 80, 93, 94, 88, 85, 90, 92
    ]

    # Create a DataFrame containing the grades.
    df = pd.DataFrame({"Grade": grades}, index=index)

    # Display the complete classroom DataFrame.
    print("\nClassroom Roster and Grades:")
    print(df)

    # Group the grades by subject and calculate the mean.
    averageGrades = df.groupby(level="Subject").mean()

    # Display the average grade for each subject.
    print("\nAverage Grades by Subject:")
    print(averageGrades)

    # Create a vertical bar chart of average grades.
    averageGrades.plot(kind="bar", color="green")

    # Add my student ID and a descriptive chart title.
    plt.title("nakmce5302 Average Grades by Subject")

    # Label the horizontal axis.
    plt.xlabel("Subject")

    # Label the vertical axis.
    plt.ylabel("Average Grade")

    # Keep the subject labels horizontal.
    plt.xticks(rotation=0)

    # Adjust spacing so labels are visible.
    plt.tight_layout()

    # Display the completed graph.
    plt.show()

# Start the program by calling main.
if __name__ == "__main__":
    main()
