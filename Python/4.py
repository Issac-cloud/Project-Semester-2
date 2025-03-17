age = int(input("Please enter your age: "))
if age <= 0:
    print("Age cannot be nagetive.")
elif age <= 19:
    print("You have the qualifity for student discounts.")
elif age <= 54:
    print("You have the qualifity for no age discounts.")
else:
    print("You have the qualifity for student discounts.")
