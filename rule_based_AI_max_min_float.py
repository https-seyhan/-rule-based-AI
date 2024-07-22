import numpy as np

# Sample construction schedule data with durations (days), costs, and resources
construction_schedule = [
    {"task": "Excavation", "duration": 5, "cost": 10000, "resources": 10},
    {"task": "Foundation", "duration": 10, "cost": 50000, "resources": 20},
    {"task": "Framing", "duration": 15, "cost": 30000, "resources": 15},
    {"task": "Roofing", "duration": 7, "cost": 20000, "resources": 10},
]

# Rules for identifying assumptions
rules = {
    "max_duration": lambda tasks: max(task["duration"] for task in tasks),
    "min_duration": lambda tasks: min(task["duration"] for task in tasks),
    "average_cost": lambda tasks: np.mean([task["cost"] for task in tasks]),
    "total_resources": lambda tasks: sum(task["resources"] for task in tasks)
}

# Function to identify assumptions based on rules
def identify_assumptions(schedule, rules):
    identified_assumptions = {}
    for assumption, rule in rules.items():
        identified_assumptions[assumption] = rule(schedule)
    return identified_assumptions

# Identify assumptions in the schedule
identified_assumptions = identify_assumptions(construction_schedule, rules)

# Output the results
print("Identified Assumptions:")
for assumption, value in identified_assumptions.items():
    print(f"{assumption}: {value}")

# Sample output format for detailed assumptions
print("\nDetailed Assumptions:")
for task in construction_schedule:
    if task["duration"] == identified_assumptions["max_duration"]:
        print(f"Task with max duration: {task['task']} - {task['duration']} days")
    if task["duration"] == identified_assumptions["min_duration"]:
        print(f"Task with min duration: {task['task']} - {task['duration']} days")
