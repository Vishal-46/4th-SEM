import pandas as pd
import json
import time
from io import StringIO
csv_data = """
Breathing_Problem,Fever,Dry_Cough,Sore_Throat,Running_Nose,Asthma,Chronic_Lung_Disease,Headache,Heart_Disease,Diabetes,Hyper_Tension,Infection_Prob
1,1,1,0,0,0,0,1,0,1,1,Yes
0,1,0,1,1,1,0,0,0,0,0,No
1,1,1,1,0,0,0,1,1,1,1,Yes
0,0,0,0,0,0,0,0,0,0,0,No
1,1,0,0,0,1,1,0,1,1,1,Yes
0,1,1,1,1,0,0,0,0,0,0,No
"""

def load_data():
    time.sleep(1)
    df = pd.read_csv(StringIO(csv_data))
    return df

def train_model(df):
    time.sleep(2)
    features = df.columns[:-1]
    label_col = df.columns[-1]

    trained_data = {"totalYes": 0, "totalNo": 0}
    totalYes = len(df[df[label_col] == "Yes"])
    totalNo = len(df[df[label_col] == "No"])
    trained_data["totalYes"] = totalYes
    trained_data["totalNo"] = totalNo

    for feature in features:
        trained_data[feature] = {}
        for val in [0, 1]:
            subset = df[df[feature] == val]
            count_yes = len(subset[subset[label_col] == "Yes"])
            count_no = len(subset[subset[label_col] == "No"])
            total = len(subset)

            trained_data[feature][val] = {
                "yes": count_yes,
                "no": count_no,
                "total": total
            }
    return trained_data

def predict(test_data, trained_data, total_count):
    sum1Yes = trained_data["totalYes"] / total_count
    sum2Yes = 1
    sum1No = trained_data["totalNo"] / total_count
    sum2No = 1

    for feature, value in test_data.items():
        feature_stats = trained_data[feature][value]
        sum1Yes *= (feature_stats["yes"] / trained_data["totalYes"])
        sum2Yes *= (feature_stats["total"] / total_count)

        sum1No *= (feature_stats["no"] / trained_data["totalNo"])
        sum2No *= (feature_stats["total"] / total_count)

    prob_yes = sum1Yes / sum2Yes
    prob_no = sum1No / sum2No

    print(f"\nProbability of Infection = Yes : {format(prob_yes, '.2f')}")
    print(f"Probability of Infection = No  : {format(prob_no, '.2f')}")

    result = "Yes" if prob_yes > prob_no else "No"
    print(f"\nPredicted Result: {result}\n")
    return result

# MAIN
if __name__ == "__main__":
    df = load_data()
    trained_data = train_model(df)
    total_count = len(df)

    while True:
        print("\nEnter test data (0 or 1) for each symptom/condition:")
        test_sample = {}
        for feature in df.columns[:-1]:
            val = int(input(f"{feature} (0 or 1): "))
            test_sample[feature] = val

        predict(test_sample, trained_data, total_count)
