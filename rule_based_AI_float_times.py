#    Define Assumptions.
#    Create Rules.
#    Extract Data.
#   Calculate Float Values.
#   Implement Rule-Based System.
#    Output Results.

#Step-by-Step Implementation
#Step 1: Define Assumptions and Rules

#Assumptions could be related to float times, like tasks having enough float time to handle delays. Rules can include conditions based on float values.
#Step 2: Extract Data from Construction Schedule

#We'll assume you have a list of tasks with their start and end dates, along with float values.
#Step 3: Calculate Float Values

#Calculate the float values for each task. Float is typically the amount of time a task can be delayed without affecting the overall project timeline.
#Step 4: Implement Rule-Based System

#Check tasks against rules and calculate maximum, minimum, and average float.

# Define assumptions and rules
assumptions = [
    "Tasks have sufficient float to handle delays.",
]

rules = [
    lambda task: task['float'] < 2,  # Rule for minimal float time
    lambda task: task['float'] >= 2 and task['float'] <= 5,  # Rule for moderate float time
    lambda task: task['float'] > 5,  # Rule for significant float time
]

# Sample construction schedule data
construction_schedule = [
    {"task": "Excavation", "start": "2024-07-01", "end": "2024-07-07", "float": 1},
    {"task": "Foundation", "start": "2024-07-08", "end": "2024-07-15", "float": 3},
    {"task": "Framing", "start": "2024-07-16", "end": "2024-07-25", "float": 6},
]

# Function to identify assumptions
def identify_assumptions(schedule, rules):
    identified_assumptions = []
    for task in schedule:
        for rule in rules:
            if rule(task):
                identified_assumptions.append(task)
    return identified_assumptions

# Function to calculate float statistics
def calculate_float_stats(schedule):
    floats = [task['float'] for task in schedule]
    max_float = max(floats)
    min_float = min(floats)
    avg_float = sum(floats) / len(floats)
    return max_float, min_float, avg_float

# Identify assumptions in the schedule
identified_assumptions = identify_assumptions(construction_schedule, rules)
max_float, min_float, avg_float = calculate_float_stats(construction_schedule)

# Output the results
print("Identified Assumptions:")
for assumption in identified_assumptions:
    print(f"Task: {assumption['task']}, Float: {assumption['float']}")

print("\nFloat Statistics:")
print(f"Maximum Float: {max_float}")
print(f"Minimum Float: {min_float}")
print(f"Average Float: {avg_float}")
