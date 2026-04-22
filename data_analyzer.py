import pandas as pd

df = pd.read_csv("student.csv")

print(df)

print("\nAverage Marks:", df["Marks"].mean())
print("Highest Marks:", df["Marks"].max())
print("Lowest Marks:", df["Marks"].min())

top_students = df[df["Marks"] > 85]

print("\nTop Students:")
print(top_students)