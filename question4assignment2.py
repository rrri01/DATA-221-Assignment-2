
import pandas as pd

student_data = pd.read_csv("student.csv", delimiter = ",")

filtered_student_data = student_data[
    (student_data["studytime"] >= 3) &
    (student_data["internet"] == 1) &
    (student_data["absences"] <= 5)
]

# print(filtered_student_data)

filtered_student_data.to_csv("high_engagement.csv") # create our new csv
high_engagement_df = pd.read_csv("high_engagement.csv")

average_grade = sum(high_engagement_df["grade"])/len(high_engagement_df)
print(f"amount of students: {len(high_engagement_df)}")
print(f"the average grade is: {average_grade}")
