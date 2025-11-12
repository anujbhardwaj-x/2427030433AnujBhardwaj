import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

print("NumPy Example:")
arr = np.array([10, 20, 30, 40, 50])
print("Array:", arr)
print("Mean:", np.mean(arr))
print("Standard Deviation:", np.std(arr))
print("Array squared:", arr ** 2)

print("\nPandas Example:")
data = {
    'Student': ['A', 'B', 'C', 'D'],
    'Math': [85, 90, 78, 92],
    'Science': [88, 76, 95, 89]
}
df = pd.DataFrame(data)
print(df)

print("\nStudents with Math > 80:")
print(df[df['Math'] > 80])

print("\nMatplotlib Example: Generating Bar Chart...")

df.plot(x='Student', y=['Math', 'Science'], kind='bar', title='Student Marks Comparison')
plt.xlabel("Students")
plt.ylabel("Marks")
plt.show()