a = int(input("Enter your grades (in %): "))

if a > 100 or a < 0:
    print("Enter valid grades")
elif a > 80:
    print("Excellent!")
elif a > 70 or a == 80:
    print("Very Good!")
elif a > 60 or a == 70:
    print("Good")
else:
    print("Average")