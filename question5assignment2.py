import pandas as pd

student_data = pd.read_csv("student.csv", delimiter = ",")
student_df = pd.DataFrame(student_data) # create a data frame with the existing data

grade_list = list(student_df["grade"])
grade_bands = []

for grade in grade_list:
    if grade >= 15:
        grade_bands.append("High")
    elif grade >= 10:
        grade_bands.append("Medium")
    else:
        grade_bands.append("Low")

student_df["grade_band"] = grade_bands # this adds a new column to the data frame

summary_table_df = pd.DataFrame()

number_of_students = [len(student_data)]

absences_list = list(student_df["absences"])
absences_total = 0
for absence in absences_list:
    absences_total += absence

average_absence = absences_total/len(absences_list)

absences_list = list(student_df["absences"])

internet_status = 0
list_of_internet_status = list(student_df["internet"])
for status in list_of_internet_status:
    internet_status += status

percentage_with_internet = internet_status/len(list_of_internet_status)
percentage_with_internet = f"{percentage_with_internet*100:.2f}%"
# i don't know how many decimal places are required for the percentage, so i just went with 2

summary_table_df["number_of_students"] = number_of_students
summary_table_df["average_absences"] = average_absence
summary_table_df["percentage_with_internet_access"] = percentage_with_internet

print(summary_table_df)

summary_table_df.to_csv("student_bands.csv")

