import pandas as pd

#Load the data
spreadsheetName = "datarm.csv"
df=pd.read_csv(spreadsheetName)

#Drop columns not needed
df = df.drop(["mc_run_id", "grouping"],axis = 1)

#Make new dataframe
final_df = pd.DataFrame()

#Function to extract max and min of each group
def findworstbest(dietgroup, agegroup, sexgroup):
    #Grab the dataframe with min and max
    desc = df[df["diet_group"] == dietgroup][df["age_group"] == agegroup][df["sex"] == sexgroup].describe()
    #Add the three groups in their own column in new dataframe
    final_df.at[dietgroup + agegroup + sexgroup, "diet_group"] = dietgroup
    final_df.at[dietgroup + agegroup + sexgroup, "age_group"] = agegroup
    final_df.at[dietgroup + agegroup + sexgroup, "sex"] = sexgroup
    #Extract max and min
    for metric in metrics:
        final_df.at[dietgroup + agegroup + sexgroup, "max "+ metric] = desc.loc["max", metric]
    for metric in metrics:
        final_df.at[dietgroup + agegroup + sexgroup, "min "+ metric] = desc.loc["min", metric]
    
#Create list of each
diets = ["meat100", "meat", "meat50", "fish", "veggie", "vegan"]
ages = ["20-29", "30-39", "40-49", "50-59", "60-69", "70-79"]
sexes = ["male", "female"]

#Populate Dataframe
for diet in diets:
    for sex in sexes:
        for age in ages:
            findworstbest(diet, age, sex)

#Convert to excel for use in visualisation program
final_df.to_excel("output.xlsx")  

