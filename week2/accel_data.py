import pandas as pd
import matplotlib.pyplot as plt

# Load the data from CSV
df = pd.read_csv("accel_data.csv", header=None, names=["timestamp", "x", "y", "z"])

# Show first few rows
print("First 5 rows of the data:")
display(df.head())

# Basic statistics
print("\nBasic Statistics:")
display(df.describe())

# Plot acceleration data over time
plt.figure(figsize=(12,6))
plt.plot(df["timestamp"], df["x"], label="X-axis")
plt.plot(df["timestamp"], df["y"], label="Y-axis")
plt.plot(df["timestamp"], df["z"], label="Z-axis")
plt.xlabel("Timestamp")
plt.ylabel("Acceleration (g)")
plt.title("LSM6DS3 Acceleration Data Over Time")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
