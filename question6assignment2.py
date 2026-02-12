import pandas as pd

crime_data = pd.read_csv("crime.csv", delimiter = ",")

violent_crimes_per_pop = crime_data["ViolentCrimesPerPop"]
risks_list = []

for crimes in violent_crimes_per_pop:
    if crimes >= 0.50:
        risks_list.append("HighCrime")
    else:
        risks_list.append("LowCrime")

crime_data["Risk"] = risks_list # create the risk column

#grouping the data:
grouped_crime = crime_data.groupby("Risk")

# high risk calculation:
group_of_high_crime = grouped_crime.get_group("HighCrime")
# print(group_of_high_crime)

high_risk_unemployed_list = crime_data["PctUnemployed"]
high_risk_unemployed_total = 0
for unemployed in high_risk_unemployed_list:
    high_risk_unemployed_total += unemployed

high_risk_unemployment_average = high_risk_unemployed_total/len(high_risk_unemployed_list)

# low risk calculations:
group_of_low_crime = grouped_crime.get_group("LowCrime")
# print(group_of_low_crime)

low_risk_unemployed_list = crime_data["PctUnemployed"]
low_risk_unemployed_total = 0
for unemployed in low_risk_unemployed_list:
    low_risk_unemployed_total += unemployed

low_risk_unemployment_average = low_risk_unemployed_total/len(low_risk_unemployed_list)

print(f"high crime unemployment rate average: {high_risk_unemployment_average*100:.2f}%")
print(f"low crime unemployment rate average: {low_risk_unemployment_average*100:.2f}%")

