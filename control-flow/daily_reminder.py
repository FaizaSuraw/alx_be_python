# daily_reminder.py

task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").strip().lower()
time_bound = input("Is it time-bound? (yes/no): ").strip().lower()

match priority:
    case "high":
        base_message = f"Reminder: '{task}' is a high priority task"
    case "medium":
        base_message = f"Reminder: '{task}' is a medium priority task"
    case "low":
        base_message = f"Reminder: '{task}' is a low priority task"
    case _:
        base_message = f"Reminder: '{task}' has an unknown priority"

if time_bound == "yes":
    base_message += " that requires immediate attention today!"
else:
    base_message += "."

print(base_message)
