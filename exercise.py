# Write a Python program that ask the user to enter a number and then
# determine if the number is even or odd

number = int(input("Enter Number:"))
if number % 2 == 0:
    print(f"{number} is even.")
else:
    print(f"{number} is even.")


#Write a python program that takes a person's age and then
#then  'classifies it into different life stages'
#  (e.g child, teen, Adult, Senior)

       # Lec Method
age = int(input("Enter your age:"))
if 51 < age <= 130:
    print(" Senior")
elif 20 <= age <= 50:
    print("Adult")
elif 13 <= age <= 19:
    print("Teen")
elif 0 <= age <= 12:
    print("Child")

else:
    print("Please insert a value within the lifespan")

    # Chatgpt Method
def classify_age(age):
    if age < 0:
        return "Invalid age"  # Handle negative age as invalid
    elif age <= 12:
        return "Child"
    elif age <= 19:
        return "Teenager"
    elif age <= 59:
        return "Adult"
    else:
        return "Senior"

def main():
    while True:
        try:
            age = int(input("Enter your age (or -1 to exit): "))
            if age == -1:
                break
            stage = classify_age(age)
            print(f"You are classified as a '{stage}'")
        except ValueError:
            print("Invalid input. Please enter a valid age (integer).")

if __name__ == "__main__":
    main()
