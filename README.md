# 🧮 Student Results Analyzer (Python)
This is a simple Python command-line application that allows you to input student names and scores, calculate statistics (mean, standard deviation, etc.), generate grade distributions, and export the results to a CSV file. It also creates a visual chart of the grade distribution using Matplotlib.
## 🔧 Features
- Input student names and scores
- Calculate:
  - Class average
  - Standard deviation
  - Highest and lowest scores
  - Grade distribution (A–F)
- Generate a bar chart (`grade_chart.png`)
- Export results to a CSV file
## 📦 Dependencies
You only need Python and `matplotlib`.
Install matplotlib if you don't already have it:
`pip install matplotlib`

## How to run
1. Clone this repo or download the Python file:
git clone `https://github.com/gaiuso33/student-results-analyzer.git`
cd student-results-analyzer
2. Run the script in your terminal or command line:
python results_analyzer.py
3. Follow the prompts to enter student names and scores.

## Sample Output
Enter number of students: 3

Student 1
Name: Alice
Score: 80

Student 2
Name: Bob
Score: 55

Student 3
Name: Clara
Score: 67

Average Score: 67.33
Standard Deviation: 12.50
Highest Score: 80
Lowest Score: 55

Grade Distribution:
A: 1
B: 1
C: 1
D: 0
F: 0

Results saved to 'results_summary.csv'.
Grade distribution chart saved as 'grade_chart.png'.

## Outputs Generated

    results_summary.csv: Contains a table of names, scores, and grades.

    grade_chart.png: Visual bar chart of grade counts.

## Concepts Practiced

    Python dictionaries and lists

    Basic statistics (mean, standard deviation)

    File handling (CSV)

    Data visualization (Matplotlib)

    Grade classification logic

🧑‍💻 Author: gaiuso33

[Oluwole Gaius]
🎓 Final-year Statistics & 300-level Computer Science student
🌍 Based in Nigeria
📫 [oluwolegaiusayokunle@gmail.com]
🔗 [(https://www.linkedin.com/in/oluwole-gaius-962342260/)]
🌐 [https://www.notion.so/hero-section-22064fc37bca80e1ae99fcb6a8cf5704?source=copy_link]
⭐️ Feel free to fork this project and try new features like:

    GUI version with Tkinter

    Support for importing student data from Excel

    Interactive charts with Plotly