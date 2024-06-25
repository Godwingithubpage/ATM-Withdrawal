import time

inbuilt_pin = "0000"
user_pin = input("Enter your pin ")
if user_pin.isdigit():
    if inbuilt_pin == user_pin:
        print("Welcome to Godwin Digital Bank")
        print("Enter amount to withdraw ")
        amount = input(">> ")
        input(f"You are about to withdraw {amount} press enter to continue ")
        print("Transaction processing... ")
        time.sleep(3)
        print("Transaction successful ")
    else:
        print("Wrong pin ")
else:
    print("Invalid value ")
