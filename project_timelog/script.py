import pandas as pd
import datetime

file = "/Users/destinyrosado/cisc4900_project/project_timelog/Destiny_Rosado_Salcedo CISC 4900 Timelog Template - Timelog.csv"
options = ['Research, Training, Learning', 'Coding', 'Team Discussion', 'Testing & Debugging', 'Other', 'Supervisor Discussion', 'Design', 'Documentation']

def update(file):
   
    df = pd.read_csv(file)

    print("\nNew Week:")
    date = input("Date (MM/DD/YY or press Enter for today): ")
    if not date.strip():
        date = datetime.now().strftime("%m/%d/%y")

    duration = input("Duration (hours): ")
    print("\nSelect a Category:")
    for i, option in enumerate(options, 1):
        print(f"  {i}. {option}")
    choice = input("Enter the number: ")

    if choice.isdigit() and 1 <= int(choice) <= len(options):
        category = options[int(choice) - 1]
    else:
        category = choice 

    description = input("Description of completed task: ")
    challenges = input("Challenges and/or next steps: ")
    reflection = input("Reflection (optional): ")

    new_entry = {
        "Date": date,
        "Duration (hours)": duration,
        "Category": category,
        "Description of completed task": description,
        "Challenges and/or next steps": challenges,
        "Reflection": reflection
    }

    df = pd.concat([df, pd.DataFrame([new_entry])], ignore_index=True)


    df.to_csv(file, index=False)
    print("Saved.")

update(file)