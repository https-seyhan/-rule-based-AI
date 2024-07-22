import pandas as pd

# Define assumptions
assumptions = [
    "Maximum allowable float is 10 days.",
    "Minimum float for a task should be at least 2 days.",
    "Average float should be monitored for schedule health.",
]

# Define rules
max_float = 10
min_float = 2

def check_max_float(float_value):
    return float_value > max_float

def check_min_float(float_value):
    return float_value < min_float

# Sample construction schedule data
data = {
    "Task": ["Excavation", "Foundation", "Roofing"],
    "Duration": [5, 10, 7],
    "Start": ["2023-01-01", "2023-01-06", "2023-01-17"],
    "Finish": ["2023-01-06", "2023-01-16", "2023-01-24"],
    "Float": [1, 12, 3],
}

df = pd.DataFrame(data)

# Function to identify assumptions
def identify_assumptions(df):
    identified_assumptions = []

    for index, row in df.iterrows():
        if check_max_float(row["Float"]):
            identified_assumptions.append(f"Task '{row['Task']}' exceeds max float with {row['Float']} days.")
        if check_min_float(row["Float"]):
            identified_assumptions.append(f"Task '{row['Task']}' has less than minimum float with {row['Float']} days.")
    
    return identified_assumptions

# Identify assumptions in the schedule
identified_assumptions = identify_assumptions(df)

# Calculate float metrics
max_schedule_float = df["Float"].max()
min_schedule_float = df["Float"].min()
average_schedule_float = df["Float"].mean()

# Output the results
print("Identified Assumptions:")
for assumption in identified_assumptions:
    print(assumption)

print("\nSchedule Float Metrics:")
print(f"Maximum Float: {max_schedule_float} days")
print(f"Minimum Float: {min_schedule_float} days")
print(f"Average Float: {average_schedule_float:.2f} days")
