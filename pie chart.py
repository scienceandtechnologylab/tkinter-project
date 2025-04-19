import matplotlib.pyplot as plt

# Sample Data
labels = ["Product A", "Product B", "Product C", "Product D"]
sizes = [35, 25, 25, 15]  # Percentage distribution
colors = ["#ff9999", "#66b3ff", "#99ff99", "#ffcc99"]  # Custom colors
explode = (0.1, 0, 0, 0)  # Explode the first slice

# Create the pie chart
plt.figure(figsize=(8, 6))
plt.pie(sizes, labels=labels, autopct="%1.1f%%", startangle=140, colors=colors, explode=explode, 
        shadow=True, wedgeprops={'edgecolor': 'black', 'linewidth': 1.5})

# Title with styling
plt.title("Professional Pie Chart - Sales Distribution", fontsize=14, fontweight="bold")

# Display the chart
plt.show()
