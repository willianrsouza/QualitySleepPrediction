# QualitySleepPrediction
Beginning the development of a predictive model regarding sleep quality.


# Quality of Sleep Prediction


``` Overview
  
 The Sleep Health and Lifestyle Dataset comprises 400 rows and 13 columns, covering a wide range of variables related to sleep and daily habits.
 It includes details such as gender, age, occupation, sleep duration, quality of sleep, physical activity level, stress levels, BMI category, blood pressure, heart rate, daily steps, and the presence or absence of sleep disorders.

```


### Fields Visualization and Convertions


| Field                     | Variations | Convertions                           |
|:--------------------------| :--------- | :---------------------------------- |
| `Gender`                  | ` Male, Female` |  Male: 0 - Female: 1|
| `Age`                     | ` 0 - 90` | It's no necessary |
| `Occupation`              | `Accountant, Doctor, Engineer, Lawyer, Manager,Nurse, Sales Represetantive, Salesperson, Scientist, Software Developer, Teacher` | Accountant: 1 - Doctor: 2 - Engineer: 3 -  Lawyer: 4 - Manager: 5 - Nurse: 6 - Sales Representative: 7 -  Salesperson: 8 - Scientist: 9 - Software Developer: 10 - Teacher: 11 | 
| `Sleep Duration`          | `hours: 5.0 - 8.5 ` | It's no necessary |
| `Quality of Sleep`        | `scale: 1-10` | It's no necessary |
| `Physical Activity Level` | `10 - 90` | It's no necessary |
| `Stress Level`            | `1 - 10` | It's no necessary |
| `BMI Category`            | `Normal, Normal Weight, Obese, Overweight` | Normal: 1 - Normal Weight:2 - Obese: 3 - Overweight: 4  |
| `Blood Pressure - Systolic` | `115 - 142` | It's no necessary |
| `Blood Pressure - Diastolic` | `75 - 95` | It's no necessary |
| `Heart Rate` | `65 - 86` | It's no necessary |
| `Daily Steps` | `-1.000, 10.000+` | It's no necessary |
| `Sleep Disorder` | `None, Insomnia, Sleep Apnea` | None: 1 - Insomnia: 2 - Sleep Apnea: 3 |
