# Define assumptions and rules
assumptions = [
    "Task duration is longer than expected, likely due to weather conditions.",
    "Task requires more resources, assuming high labor availability.",
    "Task duration is shorter than expected, assuming optimal conditions."
]

rules = [
    lambda duration, expected: duration > expected,  # Rule for longer durations
    lambda resources, threshold: resources > threshold,  # Rule for high resource usage
    lambda duration, expected: duration < expected  # Rule for shorter durations
]

# Sample construction schedule data with numerical values
construction_schedule = [
    {"task": "Excavation", "duration": 10.0, "expected_duration": 7.0, "resources": 50, "resource_threshold": 40},
    {"task": "Foundation", "duration": 5.0, "expected_duration": 6.0, "resources": 30, "resource_threshold": 40},
    {"task": "Roofing", "duration": 12.0, "expected_duration": 10.0, "resources": 60, "resource_threshold": 50},
]

# Function to identify assumptions based on numerical rules
def identify_assumptions(schedule, rules):
    identified_assumptions = []
    for task in schedule:
        task_assumptions = []
        if rules[0](task["duration"], task["expected_duration"]):
            task_assumptions.append(assumptions[0])
        if rules[1](task["resources"], task["resource_threshold"]):
            task_assumptions.append(assumptions[1])
        if rules[2](task["duration"], task["expected_duration"]):
            task_assumptions.append(assumptions[2])
        if task_assumptions:
            identified_assumptions.append({"task": task["task"], "assumptions": task_assumptions})
    return identified_assumptions

# Identify assumptions in the schedule
identified_assumptions = identify_assumptions(construction_schedule, rules)

# Output the results
print("Identified Assumptions:")
for item in identified_assumptions:
    print(f"Task: {item['task']}")
    for assumption in item['assumptions']:
        print(f"  - {assumption}")
