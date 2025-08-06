height=float(input("Enter your Height in cm:"))
weight=float(input("Enter your Weight in kg:"))

height=height/100

BMI=weight/(height*height)

print("Your Body mass index is:",BMI)

if BMI>0:

    if BMI<=16:
        print("You are severely Underweight")

    elif BMI<=18.5:
        print("You are Underweight")

    elif BMI<=25:
        print("You are Healthy")

    elif BMI<=30:
        print("You are Overweight")

    else:
        printf("You are Severely Overweight")

else:
    print("You have Entered invalid Details !")