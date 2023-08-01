def input_data():
    data = []

    print(" ")
    print("Input Your Data")

    print("Male = 0\n"
          "Female = 1 ")

    print(" ")
    data.append(input("Gender: "))

    data.append(int(input("Age: ")))

    print(" Accountant: 1 \n"
          " Doctor: 2 \n"
          " Engineer: 3 \n"
          " Lawyer: 4 \n"
          " Manager: 5 \n"
          " Nurse: 6 \n"
          " Sales Representative: 7 \n"
          " Salesperson: 8 \n"
          " Scientist: 9 \n"
          " Software Developer: 10 \n"
          " Teacher: 11 ")

    data.append(input("Occupation: "))

    data.append(float(input("Sleep Duration (Hours): ")))
    data.append(int(input("Physical Activity Level (10 - 90): ")))
    data.append(int(input("Stress Level (1 - 10): ")))

    print(" Normal: 1\n"
          " Normal Weight: 2\n"
          " Obese: 3\n"
          " Overweight: 4\n")

    data.append(int(input("BMI Category: ")))

    data.append(int(input("Blood Pressure Systolic (Integer): ")))
    data.append(int(input("Blood Pressure Diastolic (Integer): ")))
    data.append(int(input("Heart Rate (Integer): ")))
    data.append(int(input("Daily Steps (Integer): ")))

    print(" None: 1\n"
          " Insomnia: 2\n"
          " Sleep Apnea: 3\n")

    data.append(int(input("Sleep Disorder: ")))

    return data
