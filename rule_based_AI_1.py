# Define assumptions and rules
assumptions = [
    "Weather conditions are favorable.",
    "Materials will be delivered on time.",
    "Labor is available as scheduled.",
]

rules = [
    lambda task: "rain" in task.lower(),  # Rule to check for weather-related assumptions
    lambda task: "delivery" in task.lower(),  # Rule to check for material delivery assumptions
    lambda task: "labor" in task.lower(),  # Rule to check for labor availability assumptions
]

# Sample construction schedule data
construction_schedule = [
    "Excavation work assuming no rain delays",
    "Foundation concrete delivery scheduled for Monday",
    "Labor required for roofing is available as planned",
]

# Function to identify assumptions
def identify_assumptions(schedule, rules):
    identified_assumptions = []
    for task in schedule:
        for rule in rules:
            if rule(task):
                identified_assumptions.append(task)
    return identified_assumptions

# Identify assumptions in the schedule
identified_assumptions = identify_assumptions(construction_schedule, rules)

# Output the results
print("Identified Assumptions:")
for assumption in identified_assumptions:
    print(assumption)
