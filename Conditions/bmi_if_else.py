
print("Welcome to BMI Calculator!!!")

weight = float(input("Enter your weight(kg) - "))
height = float(input("Enter your height(m) - "))

bmi = weight/ (height ** 2)
bmi = round(bmi,1)
print(bmi)

if bmi < 18.2:
    print(f"Your BMI is {bmi}. you are Underwheight.")
elif 18.5 < bmi < 25:
    print(f"Your BMI is {bmi}. you are Normal.")
elif 25 <bmi <=30:
    print(f"Your BMI is {bmi}. you are Overwheght.")
else:
    print(f"Output: your BMI is{bmi}. you are Obese.")