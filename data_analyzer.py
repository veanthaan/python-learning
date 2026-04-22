import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("student.csv")

print(df)

print("\nAverage Marks:", df["Marks"].mean())
print("Highest Marks:", df["Marks"].max())
print("Lowest Marks:", df["Marks"].min())

top_students = df[df["Marks"] > 85]

print("\nTop Students:")
print(top_students)

plt.bar(df["Name"], df["Marks"])
plt.title("Student Marks")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.show()