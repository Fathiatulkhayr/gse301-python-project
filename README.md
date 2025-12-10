# Student Academic Performance Analysis System

## Project Overview
This is a comprehensive Python application that stores, processes, and analyzes student academic data. Built as part of the GSE301 Data Science: Python Fundamentals course, this system demonstrates core Python programming concepts in a practical, real-world context.

## Features Implemented

### ✅ Part 1: Data Collection and Storage
- **Variable Declaration**: Individual student profiles with proper data types (string, int, float, boolean, list, dictionary)
- **Multiple Data Structures**:
  - Lists for student collections
  - Dictionaries for detailed student profiles
  - Sets for unique courses
  - Tuples for fixed department information

### ✅ Part 2: Data Processing and Logic
- **Grading System**: 
  - `calculate_grade()` - Converts scores (0-100) to letter grades using IF/ELIF/ELSE
  - `grade_feedback()` - Provides feedback using MATCH/CASE statements
- **Input Validation**:
  - Type conversion (string → int/float)
  - Range validation (age: 16-40, CGPA: 0.0-5.0)
  - TRY/EXCEPT error handling

### ✅ Part 3: Analysis and Reporting
- **List Operations**:
  - Top 3 scores extraction using slicing
  - Last 5 scores using negative indexing
  - Every other score using step slicing
- **Set Operations**:
  - Intersection (students who passed AND have merit)
  - Union (all distinct students)
  - Difference (students who passed but not merit)

### ✅ Part 4: Interactive Menu System
- **Console Menu** (MATCH/CASE implementation):
  1. View all students
  2. Add new student
  3. Check eligibility for graduation
  4. Find top performer
  5. Demo features (list slicing, set operations, grading)
  6. Exit
- **Graduation Eligibility Checker**:
  - Uses logical operators (AND, OR)
  - Checks CGPA ≥ 2.5, no outstanding courses, active status
  - Returns detailed eligibility report

### ✅ Part 5: Advanced Challenges (Optional)
- **Nested Data Processing**: Analyzes student scores, calculates averages, identifies high performers
- **Pattern Matching**: Type detection using MATCH/CASE for int, float, str, list, dict, set, tuple

## How to Run

### Prerequisites
- Python 3.10 or higher (required for MATCH/CASE statements)

### Running the Program
1. Navigate to the project directory:
```bash
cd "DS Project 1"
```

2. Run the script:
```bash
python index.py
```

3. Follow the interactive menu prompts

## Sample Usage

### Viewing All Students
```
Enter your choice: 1
List of Students:
1. Rasheed Fatia
2. Yusuf Adeoye
3. Moses Oyedele
4. Timi Abidoye
5. Nimah Nina
```

### Checking Graduation Eligibility
```
Enter your choice: 3
Enter student name: Yusuf Adeoye
Checking eligibility...
Matric Number: 23/70JC093
CGPA: 3.45
Outstanding Courses: 0
Active Status: True

Eligibility Result:
Yusuf Adeoye is eligible for graduation.
```

### Finding Top Performer
```
Enter your choice: 4
Top Performer:
Name: Rasheed Fatia
Matric: 23/60AC389
CGPA: 4.81
Courses: ['ELE567', 'Data Science', 'Statistics']
```

## Project Structure
```
DS Project 1/
│
├── index.py          # Main Python application
└── README.md         # Project documentation
```

## Technologies Used
- **Language**: Python 3.10+
- **Concepts**: Variables, Data Types, Control Flow, Functions, Error Handling
- **Data Structures**: Lists, Tuples, Dictionaries, Sets

## Requirements Checklist

✅ Meaningful variable names using snake_case  
✅ Use of list, tuple, dictionary, and set  
✅ Demonstration of type casting  
✅ IF/ELIF/ELSE logic  
✅ MATCH/CASE used (menu system & grade feedback)  
✅ TRY/EXCEPT implemented  
✅ List slicing demonstrated  
✅ Set operations shown  
✅ Logical operators used (AND, OR)  
✅ Comments explaining major steps  

## Key Learning Outcomes

This project demonstrates proficiency in:
- Organizing complex data using appropriate Python data structures
- Implementing robust error handling and input validation
- Creating interactive console applications
- Applying control flow mechanisms (conditionals, pattern matching)
- Performing data analysis operations (slicing, set operations)
- Writing clean, well-documented, maintainable code

## Author Information
**Course**: GSE301 Data Science: Python Fundamentals  
**Institution**: University of Ilorin  
**Project Type**: Individual/Paired Project  
**Duration**: 4 days  

## Future Enhancements
- Database integration for persistent storage
- Export reports to CSV/PDF
- Web-based interface
- Advanced statistical analysis
- Grade prediction algorithms

---

*This project demonstrates comprehensive understanding of Python fundamentals through a practical academic performance management system.*
