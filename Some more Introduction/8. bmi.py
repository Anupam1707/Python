#To find the bmi from height in cm and weight is kg
#bmi.py
#25-07-2022
#By Anupam Kanoongo 

print("Welcome to the BMI calculater")
print() 
m = float(input("Enter your Height in m : "))
kg = float(input("Enter your Weight in kg : "))
cm = m*100
bmi = ((kg/cm**2)*10000)

if bmi <= 18.5 :
    stat = "Underweight"
if 24.9 >= bmi >= 18.5 :
    stat = "Normal"
if 29.9 >= bmi >= 25.0 :
    stat = "Overweight"
if bmi >= 30 :
    stat = "Obesity"
print()
print("Height : ",m,"meters \nWeight : ",kg," kilograms \nBMI : ",bmi,"kg/cm²","\nStatus : ",stat)


##Output
##Welcome to the BMI calculater
##
##Enter your Height in m : 1.7
##Enter your Weight in kg : 45
##
##Height :  1.7 meters 
##Weight :  45.0  kilograms 
##BMI :  15.570934256055363 kg/cm² 
##Status :  Underweight
