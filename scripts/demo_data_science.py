import pandas as pd
import matplotlib.pyplot as plt
from surfkit import solve

# Create an AI agent for data analysis tasks
agent_name = "data_agent"
agent_type = "pbarker/DataAnalyzer"
device_name = "data_device"

# Create a new agent
solve(
    description="Create a new data analysis agent",
    agent_type=agent_type,
    agent=agent_name,
    device=device_name
)

# Load a sample dataset
data = pd.read_csv("sample_data.csv")

# Analyze the dataset using the AI agent
task = solve(
    description="Analyze the dataset for insights",
    agent=agent_name,
    device=device_name
)
task.wait_for_done()
analysis_result = task.result

# Generate insights from the analyzed data
task = solve(
    description="Generate insights from the analyzed data",
    agent=agent_name,
    device=device_name
)
task.wait_for_done()
insights = task.result

# Visualize the data
plt.figure(figsize=(10, 6))
plt.plot(data['Date'], data['Value'], label='Data')
plt.title('Data Visualization')
plt.xlabel('Date')
plt.ylabel('Value')
plt.legend()
plt.show()
