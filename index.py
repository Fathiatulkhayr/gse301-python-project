# ============================================
# DATA COLLECTION AND STORAGE
# ============================================

# Variable Declaration and Data Types (Individual Student Example)
student_name = "Ahmad Yusuff"
matric_number = "21/60AC389"
age = 30
cgpa = 4.95
is_active = True
courses_registered = ["ANP 517", "ANP 519","ARP 534", "STA 343"]
grades = {"ANP 517": "A", "ANP 519": "A", "ARP 534": "A", "STA 343": "A"}

# Data Structures for Multiple Students
# List of student names
student_names = [
    "Rasheed Fathia",
    "Yusuf Adeoye", 
    "Moses Oyedele",
    "Bamidele Fathia Ajoke",
    "Nimah Nina"
]

# Dictionary for each student's full profile (stored in a list)
student_list = [
    {
        "name": "Rasheed Fathia",
        "matric_number": "23/60AC389",
        "age": 21,
        "cgpa": 4.81,
        "is_active": True,
        "courses": ["ANP 517", "ANP 519","ARP 534", "STA 343"],
        "grades": {"ANP 517": "A", "ANP 519": "B", "ARP 534": "A", "STA 343": "A"},
        "outstanding_courses": 0
    },
    {
        "name": "Yusuf Adeoye",
        "matric_number": "23/70JC093",
        "age": 22,
        "cgpa": 4.45,
        "is_active": True,
        "courses": ["PYTHON", "ALGORITHMS","DATABASES", "DATA SCIENCE"],
        "grades": {"PYTHON": "B", "ALGORITHMS": "B", "DATABASES": "A", "DATA SCIENCE": "A"},
        "outstanding_courses": 0
    },
    {
        "name": "Moses Oyedele",
        "matric_number": "23/80DC045",
        "age": 18,
        "cgpa": 2.95,
        "is_active": True,
        "courses": ["Web Development", "Python", "Networking"],
        "grades": {"Web Development": "F", "Python": "B", "Networking": "C"},
        "outstanding_courses": 1
    },
    {
        "name": "Bamidele Fathia Ajoke",
        "matric_number": "22/90EC078",
        "age": 21,
        "cgpa": 4.85,
        "is_active": True,
        "courses": ["Data Science", "Machine Learning", "Python"],
        "grades": {"Data Science": "A", "Machine Learning": "A", "Python": "B"},
        "outstanding_courses": 0
    },
    {
        "name": "Nimah Nina",
        "matric_number": "23/50BC012",
        "age": 21,
        "cgpa": 3.78,
        "is_active": False,
        "courses": ["Statistics", "Python", "Data Mining"],
        "grades": {"Statistics": "B", "Python": "A", "Data Mining": "B"},
        "outstanding_courses": 0
    }
]

# Set to store unique courses offered in the dt
unique_courses = {
    "Python", "Data Science", "Statistics", "Algorithms", 
    "Databases", "Web Development", "Networking", 
    "Machine Learning", "Data Mining", "ANP 517"
}

# Tuple for fixed dt information
dt_info = ("Agriculture", "Faculty of Agric", 2025)

# Sample assignment scores for(List Operations)
assignment_scores = [55, 67, 72, 95, 68, 73, 88, 91, 89, 87]

# Sets for(Set Operations)
set_pass = {"Ahmad Yusuff", "Yusuf Adeoye", "Moses Oyedele", "Bamidele Fathia Ajoke", "Nimah Nina"}  # Students who passed Python
set_merit = {"Ahmad Yusuff","Bamidele Fathia Ajoke", "Yusuf Adeoye"}  # Students with CGPA above 4.0


# ============================================
# DATA PROCESSING AND LOGIC
# ============================================

# Conditional Statements for Grading
def calculate_grade(score):
    """
    Converts numeric score (0-90) to letter grade using IF/ELIF/ELSE
    
    Args:
        score (int/float): Numeric score between 0 and 90
        
    Returns:
        str: Letter grade (A, B, C, D, E, F)
    """
    if score >= 70:
        return "A"
    elif score >= 60:
        return "B"
    elif score >= 50:
        return "C"
    elif score >= 45:
        return "D"
    elif score >= 40:
        return "E"
    else:
        return "F"


def grade_feedback(grade):
    """
    Uses MATCH CASE to print feedback based on the grade
    
    Args:
        grade (str): Letter grade
    """
    match grade:
        case "A":
            print("Excellent! Outstanding performance!")
        case "B":
            print("Very Good! Keep up the good work!")
        case "C":
            print("Good! You passed with a fair grade.")
        case "D":
            print("Passed. Consider improving your performance.")
        case "E":
            print("Barely passed. You need significant improvement.")
        case "F":
            print("Failed. Please retake this course.")
        case _:
            print("Invalid grade.")


# Type Conversion and Validation
def validate_and_convert_input():
    """
    Asks user for age and CGPA as strings, converts them to int and float,
    and validates the input using TRY/EXCEPT
    
    Returns:
        tuple: (age, cgpa) or (None, None) if validation fails
    """
    try:
        # Get input as strings
        age_input = input("Enter age: ")
        cgpa_input = input("Enter CGPA: ")
        
        # Type conversion
        age = int(age_input)
        cgpa = float(cgpa_input)
        
        # Validation
        if age < 16 or age > 40:
            print("Error: Age must be between 16 and 40.")
            return None, None
        
        if cgpa < 0.0 or cgpa > 5.0:
            print("Error: CGPA must be between 0.0 and 5.0.")
            return None, None
        
        print("Input validated successfully!")
        return age, cgpa
        
    except ValueError:
        print("Error: Invalid input. Age must be an integer and CGPA must be a number.")
        return None, None


# ============================================
# ANALYSIS AND REPORTING
# ============================================

# List Operations and Slicing
def analyze_assignment_scores():
    """
    Demonstrates list slicing operations on assignment scores
    """
    print("\n" + "="*50)
    print("     Assignment Scores Analysis")
    print("="*50)
    print(f"All scores: {assignment_scores}")
    
    # Extract top 3 scores using slicing
    sorted_scores = sorted(assignment_scores, reverse=True)
    top_3_scores = sorted_scores[:3]
    print(f"Top 3 scores: {top_3_scores}")
    
    # Extract last 5 scores using negative indexing
    last_5_scores = assignment_scores[-5:]
    print(f"Last 5 scores: {last_5_scores}")
    
    # Extract every other score using step slicing
    every_other_score = assignment_scores[::2]
    print(f"Every other score: {every_other_score}")
    print("="*50)


# Set Operations
def analyze_student_sets():
    """
    Performs set operations to analyze student performance
    """
    print("\n" + "="*50)
    print("     Student Set Analysis")
    print("="*50)
    print(f"Students who passed Python: {set_pass}")
    print(f"Students with merit (CGPA > 4.0): {set_merit}")
    
    # Intersection: Students who passed AND have merit
    passed_and_merit = set_pass & set_merit
    print(f"\nStudents who passed Python AND have merit: {passed_and_merit}")
    
    # Union: All distinct students in both sets
    all_distinct_students = set_pass | set_merit
    print(f"All distinct students (union): {all_distinct_students}")
    
    # Difference: Students who passed but do not have merit
    passed_no_merit = set_pass - set_merit
    print(f"Students who passed but do NOT have merit: {passed_no_merit}")
    print("="*50)


# ============================================
# INTERACTIVE MENU SYSTEM
# ============================================

# Eligibility Checker
def check_eligibility(student):
    """
    Uses logical operators (and, or) to determine graduation eligibility
    
    A student is eligible if:
    - CGPA is 2.5 or above
    - No outstanding courses
    - Is_active is True
    
    Args:
        student (dict): Student profile dictionary
        
    Returns:
        tuple: (bool, str) - eligibility status and detailed message
    """
    name = student["name"]
    cgpa = student["cgpa"]
    outstanding = student["outstanding_courses"]
    active = student["is_active"]
    
    # Use logical operators (and) to check all conditions
    is_eligible = (cgpa >= 2.5) and (outstanding == 0) and active
    
    # Build detailed message
    print("\nChecking eligibility...")
    print(f"Matric Number: {student['matric_number']}")
    print(f"CGPA: {cgpa}")
    print(f"Outstanding Courses: {outstanding}")
    print(f"Active Status: {active}")
    print("\nEligibility Result:")
    
    if is_eligible:
        message = f"{name} is eligible for graduation."
        print(message)
        return True, message
    else:
        # Determine specific reason for ineligibility using or operator
        reasons = []
        if cgpa < 2.5:
            reasons.append("CGPA is below 2.5")
        if outstanding > 0:
            reasons.append("has outstanding courses")
        if not active:
            reasons.append("student is not active")
        
        message = f"{name} is NOT eligible for graduation. Reasons: {', '.join(reasons)}."
        print(message)
        return False, message


def find_top_performer(students):
    """
    Identifies the student with the highest CGPA
    
    Args:
        students (list): List of student dictionaries
        
    Returns:
        dict: Top performing student
    """
    if not students:
        return None
    
    top_student = students[0]
    for student in students:
        if student["cgpa"] > top_student["cgpa"]:
            top_student = student
    
    return top_student


def view_all_students(students):
    """
    Displays all student names
    
    Args:
        students (list): List of student dictionaries
    """
    print("\nList of Students:")
    for i, student in enumerate(students, 1):
        print(f"{i}. {student['name']}")


def add_new_student(students):
    """
    Adds a new student to the system with validation
    
    Args:
        students (list): List of student dictionaries to add the new student to
    """
    print("\nAdd New Student")
    
    try:
        name = input("Enter name: ")
        matric_number = input("Enter matric number: ")
        
        age_input = input("Enter age: ")
        age = int(age_input)
        if age < 16 or age > 40:
            print("Error: Age must be between 16 and 40.")
            return
        
        cgpa_input = input("Enter CGPA: ")
        cgpa = float(cgpa_input)
        if cgpa < 0.0 or cgpa > 5.0:
            print("Error: CGPA must be between 0.0 and 5.0.")
            return
        
        active_input = input("Is the student active (yes/no): ").lower()
        is_active = True if active_input == "yes" else False
        
        courses_input = input("Enter courses (comma separated): ")
        courses = [course.strip() for course in courses_input.split(",")]
        
        # Create new student dictionary
        new_student = {
            "name": name,
            "matric_number": matric_number,
            "age": age,
            "cgpa": cgpa,
            "is_active": is_active,
            "courses": courses,
            "grades": {},
            "outstanding_courses": 0
        }
        
        students.append(new_student)
        print("Student record added successfully.")
        
    except ValueError:
        print("Error: Invalid input. Please enter correct data types.")


# ============================================
# ADVANCED CHALLENGES (OPTIONAL)
# ============================================

# Nested Data Processing
def analyze_nested_scores(nested_data):
    """
    Analyzes nested dictionary of students and their scores
    Calculates average score and identifies high performers
    
    Args:
        nested_data (dict): Nested dictionary with student names as keys
                           and dictionaries of course:score as values
    """
    print("\n" + "="*50)
    print("     Nested Data Analysis")
    print("="*50)
    
    for student_name, scores in nested_data.items():
        # Calculate average score
        if scores:
            average = sum(scores.values()) / len(scores)
            print(f"\n{student_name}:")
            print(f"  Courses and Scores: {scores}")
            print(f"  Average Score: {average:.2f}")
            
            # Check if scored above 70 in all courses
            all_above_70 = all(score > 70 for score in scores.values())
            if all_above_70:
                print(f"  ✓ {student_name} scored above 70 in ALL courses!")
            else:
                print(f"  × {student_name} did not score above 70 in all courses.")
    
    print("="*50)


# Pattern Matching with MATCH CASE
def detect_data_type(data):
    """
    Uses MATCH CASE to identify the type of input data and return formatted summary
    
    Args:
        data: Any data type
        
    Returns:
        str: Formatted summary of the data type and its properties
    """
    match data:
        case int():
            return f"Type: Integer | Value: {data} | Is Even: {data % 2 == 0}"
        case float():
            return f"Type: Float | Value: {data} | Rounded: {round(data, 2)}"
        case str():
            return f"Type: String | Length: {len(data)} | Value: '{data}'"
        case list():
            return f"Type: List | Length: {len(data)} | Items: {data}"
        case dict():
            return f"Type: Dictionary | Keys: {len(data)} | Keys List: {list(data.keys())}"
        case set():
            return f"Type: Set | Size: {len(data)} | Items: {data}"
        case tuple():
            return f"Type: Tuple | Length: {len(data)} | Items: {data}"
        case _:
            return f"Type: Unknown | Value: {data}"


# ============================================
# MAIN MENU SYSTEM
# ============================================

def display_menu():
    """
    Displays the main menu options
    """
    print("\n" + "-"*50)
    print("Menu Options")
    print("1. View all students")
    print("2. Add new student")
    print("3. Check eligibility for graduation")
    print("4. Find top performer")
    print("5. Demo: List slicing operations")
    print("6. Demo: Set operations")
    print("7. Demo: Grade calculator")
    print("8. Demo: Data type detector")
    print("9. Exit")
    print("-"*50)


def main():
    """
    Main function that runs the interactive menu system using MATCH CASE
    """
    print("="*50)
    print("     Student Academic Performance System")
    print("="*50)
    print("Loading student records...")
    print(f"{len(student_list)} student profiles loaded successfully.")
    print(f"Dt: {dt_info[0]}")
    print(f"Faculty: {dt_info[1]}")
    print(f"Academic Year: {dt_info[2]}")
    
    # Main menu loop
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        
        # Menu using MATCH CASE
        match choice:
            case "1":
                # View all students
                view_all_students(student_list)
                
            case "2":
                # Add new student
                add_new_student(student_list)
                
            case "3":
                # Check eligibility for graduation
                student_name_input = input("\nEnter student name: ")
                
                # Find student in list
                found = False
                for student in student_list:
                    if student["name"].lower() == student_name_input.lower():
                        check_eligibility(student)
                        found = True
                        break
                
                if not found:
                    print(f"Student '{student_name_input}' not found in records.")
                    
            case "4":
                # Find top performer
                top = find_top_performer(student_list)
                if top:
                    print("\nTop Performer:")
                    print(f"Name: {top['name']}")
                    print(f"Matric: {top['matric_number']}")
                    print(f"CGPA: {top['cgpa']}")
                    print(f"Courses: {top['courses']}")
                else:
                    print("No students in the system.")
                    
            case "5":
                # Demo: List slicing operations
                analyze_assignment_scores()
                
            case "6":
                # Demo: Set operations
                analyze_student_sets()
                
            case "7":
                # Demo: Grade calculator with validation
                try:
                    score_input = input("\nEnter a score (0-100): ")
                    score = float(score_input)
                    
                    if 0 <= score <= 100:
                        grade = calculate_grade(score)
                        print(f"Score: {score} → Grade: {grade}")
                        grade_feedback(grade)
                    else:
                        print("Error: Score must be between 0 and 100.")
                except ValueError:
                    print("Error: Please enter a valid number.")
                    
            case "8":
                # Demo: Data type detector
                print("\nData Type Detector Demo")
                test_data = [
                    42,
                    3.14,
                    "Hello Python",
                    [1, 2, 3, 4, 5],
                    {"name": "John", "age": 20},
                    {1, 2, 3},
                    (10, 20, 30)
                ]
                
                for data in test_data:
                    result = detect_data_type(data)
                    print(f"  {result}")
                    
            case "9":
                # Exit
                print("\nExiting the system...")
                print("Goodbye!")
                break
                
            case _:
                # Invalid choice
                print("\nInvalid choice. Please select a valid option (1-9).")


# ============================================
# PROGRAM ENTRY POINT
# ============================================

if __name__ == "__main__":
    main()
