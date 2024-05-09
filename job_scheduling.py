# Define a class to represent a job with deadline and penalty
class Job:
    def __init__(self, name, deadline, penalty):
        self.name = name
        self.deadline = deadline
        self.penalty = penalty

    def __repr__(self):
        return f"Job({self.name}, Deadline: {self.deadline}, Penalty: {self.penalty})"

# Function to calculate penalties for a given job schedule
def calculate_penalties(schedule):
    current_time = 1
    total_penalty = 0
    for job in schedule:
        if current_time > job.deadline:
            total_penalty += job.penalty
        current_time += 1
    return total_penalty

# Function to generate all permutations of jobs
def permutations(jobs):
    if len(jobs) <= 1:
        return [jobs]
    else:
        result = []
        for i in range(len(jobs)):
            remaining = jobs[:i] + jobs[i+1:]
            for perm in permutations(remaining):
                result.append([jobs[i]] + perm)
        return result

# Function to find the optimal job schedule to minimize penalty
def find_optimal_schedule(jobs):
    best_schedule = None
    best_penalty = float('inf')  # Infinity
    all_permutations = permutations(jobs)
    
    for perm in all_permutations:
        penalty = calculate_penalties(perm)
        if penalty < best_penalty:
            best_penalty = penalty
            best_schedule = perm
    
    return best_schedule, best_penalty

# Main function to create a menu-driven program
def main():
    jobs = []
    
    while True:
        print("\n----------------- MENU -----------------")
        print("1. Add a job")
        print("2. Show all jobs")
        print("3. Find optimal schedule")
        print("4. Exit")
        choice = input("\nChoose an option: ")
        
        if choice == "1":
            name = input("Enter job name: ")
            deadline = int(input("Enter job deadline: "))
            penalty = int(input("Enter job penalty: "))
            jobs.append(Job(name, deadline, penalty))
            print("Job added successfully!")
        
        elif choice == "2":
            if not jobs:
                print("\nNo jobs added yet.")
            else:
                print("\nJobs:")
                for job in jobs:
                    print(f"- {job}")
        
        elif choice == "3":
            if not jobs:
                print("No jobs to schedule.")
            else:
                optimal_schedule, best_penalty = find_optimal_schedule(jobs)
                print("\nOptimal schedule to minimize penalties:")
                for job in optimal_schedule:
                    print(f"- {job.name}")
                print(f"\nTotal penalty: {best_penalty}")
        
        elif choice == "4":
            print("Exiting...")
            break
        
        else:
            print("Invalid choice. Please try again.")

# Run the main function if the script is executed
if __name__ == "__main__":
    main()
