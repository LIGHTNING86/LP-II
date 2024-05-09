# Employee class with its attributes:
class Employee:
    def __init__(
        self,
        name,
        domain,
        gender,
        completed_tasks,
        avg_work_hours,
        salary,
        previous_rating,
        presentations,
        experience,
        leaves,
    ):
        self.name = name
        self.domain = domain
        self.gender = gender
        self.completed_tasks = completed_tasks
        self.avg_work_hours = avg_work_hours
        self.salary = salary
        self.previous_rating = previous_rating
        self.presentations = presentations
        self.experience = experience
        self.leaves = leaves


# Function to evaluate an employee's performance and generate a final verdict
def evaluate_employee(employee):
    # Initialize score
    score = 0
    explanation = []

    # Scoring based on number of tasks successfully completed
    if employee.completed_tasks > 100:
        score += 3
        explanation.append("High number of completed tasks (+3).")
    elif employee.completed_tasks > 50:
        score += 2
        explanation.append("Moderate number of completed tasks (+2).")
    else:
        score += 1
        explanation.append("Low number of completed tasks (+1).")

    # Scoring based on average working hours per week
    if employee.avg_work_hours > 40:
        score += 1  # Extra effort
        explanation.append("Working more than 40 hours per week (+1).")
    elif employee.avg_work_hours < 30:
        score -= 1  # Potential underperformance
        explanation.append("Working less than 30 hours per week (-1).")

    # Scoring based on salary
    if employee.salary > 70000:
        score += 2
        explanation.append("High salary, indicating greater responsibility (+2).")
    elif employee.salary > 50000:
        score += 1
        explanation.append("Moderate salary (+1).")
    else:
        score -= 1
        explanation.append("Low salary (-1).")

    # Scoring based on previous performance rating
    if employee.previous_rating >= 4:
        score += 2
        explanation.append("Previous high performance rating (+2).")
    elif employee.previous_rating >= 3:
        score += 1
        explanation.append("Previous moderate performance rating (+1).")
    else:
        score -= 1
        explanation.append("Previous low performance rating (-1).")

    # Scoring based on number of presentations given
    if employee.presentations >= 10:
        score += 2
        explanation.append("Given at least 10 presentations, indicating leadership (+2).")
    elif employee.presentations >= 5:
        score += 1
        explanation.append("Given 5 to 9 presentations (+1).")

    # Scoring based on experience in years
    if employee.experience > 10:
        score += 2
        explanation.append("More than 10 years of experience (+2).")
    elif employee.experience > 5:
        score += 1
        explanation.append("5 to 10 years of experience (+1).")
    else:
        score -= 1
        explanation.append("Less than 5 years of experience (-1).")

    # Scoring based on leaves taken in the last year
    if employee.leaves > 20:
        score -= 2
        explanation.append("More than 20 leaves in the last year (-2).")
    elif employee.leaves > 10:
        score -= 1
        explanation.append("10 to 20 leaves in the last year (-1).")

    # Determine the final performance evaluation
    if score >= 8:
        evaluation = "Excellent"
    elif score >= 5:
        evaluation = "Good"
    elif score >= 3:
        evaluation = "Satisfactory"
    else:
        evaluation = "Needs Improvement"

    # Generate a final verdict based on the evaluation
    if evaluation == "Excellent":
        verdict = (
            "The employee has demonstrated outstanding performance across several key "
            "metrics. This individual should be recognized for their efforts and considered "
            "for leadership roles or promotions."
        )
    elif evaluation == "Good":
        verdict = (
            "\nThe employee has shown solid performance with a few areas for improvement. Encouragement and development opportunities could help this individual reach even greater heights."
        )
    elif evaluation == "Satisfactory":
        verdict = (
            "\nThe employee has met the basic performance expectations, but there's room for growth. Consider providing additional training or guidance to help this individual improve."
        )
    else:
        verdict = (
            "\nThe employee's performance is below expectations. Address the areas of concern and consider closer supervision or performance improvement plans."
        )

    # Return both the evaluation, explanation, and final verdict
    return evaluation, explanation, verdict


# Function to gather employee details from user input
def get_employee_details():
    print("\nEnter the following employee details:")
    name = input("\nName: ")
    domain = input("Domain of expertise: ")
    gender = input("Gender: ")
    completed_tasks = int(input("Number of tasks successfully completed: "))
    avg_work_hours = int(input("Average working hours per week: "))
    salary = int(input("Salary: "))
    previous_rating = float(input("Previous rating by the expert system (out of 5): "))
    presentations = int(input("Number of presentations given: "))
    experience = int(input("Experience (in years): "))
    leaves = int(input("Number of leaves in the last year: "))

    return Employee(
        name=name,
        domain=domain,
        gender=gender,
        completed_tasks=completed_tasks,
        avg_work_hours=avg_work_hours,
        salary=salary,
        previous_rating=previous_rating,
        presentations=presentations,
        experience=experience,
        leaves=leaves,
    )


# Gather employee details from the user
employee = get_employee_details()

# Evaluate the employee's performance and get the final verdict
performance_rating, explanation, verdict = evaluate_employee(employee)

# Display the final rating, detailed explanation, and the final verdict
print(f"\nEmployee {employee.name} performance rating: {performance_rating}\n")
print("Explanation:")
for line in explanation:
    print(f"  - {line}")

print("\nFinal Verdict:")
print(verdict)