import pandas as pd
import numpy as np
from sklearn.tree import export_text
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder
data = pd.DataFrame([
    ['Sunny', 'Hot', 'High', 'Weak', 'No'],
    ['Sunny', 'Hot', 'High', 'Strong', 'No'],
    ['Overcast', 'Hot', 'High', 'Weak', 'Yes'],
    ['Rain', 'Mild', 'High', 'Weak', 'Yes'],
    ['Rain', 'Cool', 'Normal', 'Weak', 'Yes'],
    ['Rain', 'Cool', 'Normal', 'Strong', 'No'],
    ['Overcast', 'Cool', 'Normal', 'Strong', 'Yes'],
    ['Sunny', 'Mild', 'High', 'Weak', 'No'],
    ['Sunny', 'Cool', 'Normal', 'Weak', 'Yes'],
    ['Rain', 'Mild', 'Normal', 'Weak', 'Yes'],
    ['Sunny', 'Mild', 'Normal', 'Strong', 'Yes'],
    ['Overcast', 'Mild', 'High', 'Strong', 'Yes'],
    ['Overcast', 'Hot', 'Normal', 'Weak', 'Yes'],
    ['Rain', 'Mild', 'High', 'Strong', 'No']
], columns=['Outlook', 'Temperature', 'Humidity', 'Wind', 'PlayTennis'])
label_encoders = {}  
for col in data.columns:
    le = LabelEncoder()
    data[col] = le.fit_transform(data[col])
    label_encoders[col] = le  
X = data.drop(columns=['PlayTennis'])
y = data['PlayTennis']
model = DecisionTreeClassifier(criterion='entropy')
model.fit(X, y)
new_sample = pd.DataFrame([['Sunny', 'Cool', 'High', 'Strong']], 
                          columns=['Outlook', 'Temperature', 'Humidity', 'Wind'])
for col in new_sample.columns:
    new_sample[col] = label_encoders[col].transform(new_sample[col])
prediction = model.predict(new_sample)
predicted_label = label_encoders['PlayTennis'].inverse_transform(prediction)
tree_rules = export_text(model, feature_names=X.columns.tolist())
print(tree_rules)
print("Predicted class for new sample:", predicted_label[0])