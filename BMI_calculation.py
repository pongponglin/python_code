# BMI_calculation
height = eval(input('Please input your height: '))
weight = input('Please input your weight: ')

bmi = int(weight)/((height/100)**2)
bmi = round(bmi,2)

if bmi <18.5:
    bmi_class = 'Underweight'
elif bmi >= 18.5 and bmi < 24:
    bmi_class = 'Normal'
else:
    bmi_class = 'Overweight'

print('Your BMI is {}, {}'.format(bmi,bmi_class))