age = int(input("Enter your age: "))

if age < 18:
    consent = input("Do you have parental consent? (yes/no): ").lower()

    # A person under 18 is eligible only if they are at least 13 and have consent.
    if age >= 13 and consent == "yes":
        print("Welcome to the club!")
    else:
        print("Sorry, you are not eligible yet.")

else:
    # A person aged 18 or older is eligible without parental consent.
    if age >= 18 or not (age < 18):
        print("Welcome to the club!")
    else:
        print("Sorry, you are not eligible yet.")
