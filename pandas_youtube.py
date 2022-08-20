import pandas as pd


titled_column = {
                "Name": ["Yolanda", "Eustaceo", "Florentino", "Filomeno", "Elbrian"],
                "Height": [1.6, 1.67, 1.74, 1.80, 1.55],
                "Weight": [54, 78, 115, 67, 85]
                }
data = pd.DataFrame(titled_column)
select_column = data["Weight"][4]
select_row = data.iloc[1]["Weight"]
print(f"\nDataframe Data original:\n{data}")

bmi = [] 
for i in range(len(data)):
    bmi_score = data["Weight"][i]/(data["Height"][i]**2)
    bmi.append(bmi_score)
    
data["BMI"] = bmi
print(f"\nDataframe Data + BMI row:\n{data}")

new_row = {"Name": "Belisario", "Height": 0.3, "Weight": 0.150}

data = data.append(new_row, ignore_index = True)
print(f"\nDataframe Data + New Row Belisario:\n{data}")

# bmi_B = data["Weight"][5]/(data["Height"][5]**2)
# data.at[5, "BMI"] = bmi_B
# print(f"\nDataframe Data + BMI of Belisario:\n{data}")