import os
from datetime import datetime

# Function to create or load a timetable
def create_or_load_timetable(date):
    formatted_date = date.strftime("%d-%m-%Y")
    filename = f"{formatted_date}_timetable.txt"
    
    if os.path.exists(filename):
        print(f"Loading timetable for {formatted_date}...")
        with open(filename, 'r') as file:
            timetable = file.readlines()
    else:
        timetable = []

    return timetable

# Function to display the timetable without mentioning completed tasks
def display_timetable(timetable):
    if not timetable:
        print("No tasks scheduled.")
    else:
        print("\nTimetable:")
        for i, task in enumerate(timetable, 1):
            task_info = task.strip().split(" ", 1)
            if not task_info[0].startswith("(completed)"):
                print(f"{i}. {task_info[1]}")

# Function to add a task with a time slot to the timetable
def add_task(timetable):
    time_slot = input("Enter the time slot (e.g., '09:00 AM - 10:00 AM'): ")
    task = input("Enter task description: ")
    timetable.append(f"( ) {time_slot}: {task}\n")
    print("Task added successfully!")

# Function to mark a task as completed
def mark_completed(timetable):
    display_timetable(timetable)
    task_index = int(input("Enter the task number to mark as completed (0 to cancel): "))
    
    if task_index == 0:
        return
    
    if 1 <= task_index <= len(timetable):
        timetable[task_index - 1] = "(completed)" + timetable[task_index - 1][9:]
        print("Task marked as completed!")
    else:
        print("Invalid task number.")

# Function to save the timetable to a file and exit
def save_timetable_and_exit(date, timetable):
    formatted_date = date.strftime("%d-%m-%Y")
    filename = f"{formatted_date}_timetable.txt"
    with open(filename, 'w') as file:
        file.writelines(timetable)
    print(f"Timetable saved to {filename}")
    print("Exiting...")
    exit(0)

# Main program
if __name__ == "__main__":
    date_str = input("Enter the date (DD-MM-YYYY): ")
    date = datetime.strptime(date_str, "%d-%m-%Y")
    timetable = create_or_load_timetable(date)
    
    while True:
        print("\nOptions:")
        print("1. Display timetable")
        print("2. Add task with time slot")
        print("3. Mark task as completed")
        print("4. Save timetable and exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            display_timetable(timetable)
        elif choice == '2':
            add_task(timetable)
        elif choice == '3':
            mark_completed(timetable)
        elif choice == '4':
            save_timetable_and_exit(date, timetable)
        else:
            print("Invalid choice. Please try again.")
