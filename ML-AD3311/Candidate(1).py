import numpy as np
import pandas as pd
data = pd.DataFrame({
    'Sky': ['Sunny', 'Sunny', 'Rainy', 'Sunny'],
    'AirTemp': ['Warm', 'Warm', 'Cold', 'Warm'],
    'Humidity': ['Normal', 'High', 'High', 'High'],
    'Wind': ['Strong', 'Strong', 'Strong', 'Strong'],
    'Water': ['Warm', 'Warm', 'Warm', 'Cool'],
    'Forecast': ['Same', 'Same', 'Change', 'Change'],
    'EnjoySport': ['Yes', 'Yes', 'No', 'Yes']
})
attributes = data.iloc[:, :-1].values 
target = data.iloc[:, -1].values      
num_attributes = attributes.shape[1]
for i in range(len(target)):
    if target[i] == "Yes":
        S = attributes[i].copy()
        break
G = [["?"] * num_attributes]
for i in range(len(target)):
    if target[i] == "Yes": 
        for j in range(num_attributes):
            if S[j] != attributes[i][j]:  
                S[j] = "?"
        G = [g for g in G if all(g[k] == "?" or g[k] == S[k] for k in range(num_attributes))]
    elif target[i] == "No":  
        new_G = []
        for g in G:
            for j in range(num_attributes):
                if g[j] == "?": 
                    new_hypothesis = g.copy()
                    new_hypothesis[j] = attributes[i][j]
                    new_G.append(new_hypothesis)   
        G = new_G 
print("Final Specific Hypothesis:", S)
print("Final General Hypothesis:", G)