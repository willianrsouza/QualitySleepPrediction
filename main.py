import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import ExtraTreesClassifier
import numpy as np
import function_input as input

# Reading data

data = pd.read_csv('/Users/willian/Documents/IA-Study/datas/Sleep-health-treat.csv')

#print("FULL DATA")
#print(data.head(3))

# Predicts variables and target

target = data['Quality of Sleep']
predict = data.drop('Quality of Sleep', axis=1)

#print('TARGET VARIABLE')
#print(target)


# Size of DataSet

#print(data.shape)

# Train split

predict_train, predict_test, target_train, target_test = train_test_split(predict, target, test_size=0.3)

# Call predict model

model = ExtraTreesClassifier()
model.fit(predict_train,  target_train)

# Print result

result = model.score(predict_test, target_test)
print('Accuracy: ', round(result * 100), '%')


# Predict

# Assuming new_data_point is the 1D array you provided

# Gender
# Age
# Occupation
# Sleep Duration
# Physical Activity Level
# Stress Level
# BMI Category
# Blood Pressure Systolic
# Blood Pressure Diastolic
# Heart Rate
# Daily Steps
# Sleep Disorder


# Input Function

receive_input = input.input_data()

predict_data = np.array(receive_input).reshape(1, -1)
predict_dynamic_inputs = model.predict(predict_data)

print(predict_dynamic_inputs)