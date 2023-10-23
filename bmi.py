def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))
    bmi = weight/(height*height)
    check_bmi_range(bmi)

def check_bmi_range(bmi):
    print(bmi)
    if(bmi < 18.5):
        print("Under Weight")
    elif(bmi >= 18.5 and bmi <= 25.0):
        print("Normal Weight")
    elif(bmi > 25.0):
        print("Over Weight")

print(str(calculate_bmi(weight=57, height=1.73)))

