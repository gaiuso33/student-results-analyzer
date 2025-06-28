# results_analyzer.py

import statistics
import csv
import matplotlib.pyplot as plt


def get_grade(score):
    if score >= 70:
        return 'A'
    elif score >= 60:
        return 'B'
    elif score >= 50:
        return 'C'
    elif score >= 45:
        return 'D'
    else:
        return 'F'

def main():
    print("Student Results Analyzer")
    num_students = int(input("Enter number of students: "))

    students = []

    for i in range(num_students):
        print(f"\nStudent {i + 1}")
        name = input("Name: ")
        score = float(input("Score: "))
        grade = get_grade(score)

        students.append({"Name": name, "Score": score, "Grade": grade})

    scores = [s['Score'] for s in students]
    grades = [s['Grade'] for s in students]

    # Stats
    avg = statistics.mean(scores)
    std_dev = statistics.stdev(scores) if len(scores) > 1 else 0
    high = max(scores)
    low = min(scores)

    print(f"\nAverage Score: {avg:.2f}")
    print(f"Standard Deviation: {std_dev:.2f}")
    print(f"Highest Score: {high}")
    print(f"Lowest Score: {low}")

    # Grade Distribution
    print("\nGrade Distribution:")
    for g in ['A', 'B', 'C', 'D', 'F']:
        count = grades.count(g)
        print(f"{g}: {count}")
# Plot grade distribution

    grade_labels = ['A', 'B', 'C', 'D', 'F']
    grade_counts = [grades.count(g) for g in grade_labels]

    plt.bar(grade_labels, grade_counts, color='skyblue')
    plt.xlabel('Grades')
    plt.ylabel('Number of Students')
    plt.title('Grade Distribution')
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.savefig('grade_chart.png')
    plt.close()
    print("Grade distribution chart saved as 'grade_chart.png'")

    # Save to CSV
    with open("results_summary.csv", "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["Name", "Score", "Grade"])
        writer.writeheader()
        writer.writerows(students)

    print("\nResults saved to 'results_summary.csv'.")

if __name__ == "__main__":
    main()
