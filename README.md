PIN Authentication and Withdrawal Script
This Python script simulates a simple PIN authentication process followed by a withdrawal operation for a digital bank. It demonstrates basic user input handling, conditional checks, and a simulated delay to represent transaction processing.

Features
PIN Authentication: The script prompts the user to enter a PIN and compares it with a predefined inbuilt PIN.
Amount Withdrawal: If the authentication is successful, the user can input an amount to withdraw, and the script simulates a withdrawal transaction.
Input Validation: The script checks if the entered PIN is numeric and matches the predefined PIN.
How it Works
The script sets a predefined inbuilt_pin as "0000".
It prompts the user to input their PIN.
It validates if the entered PIN is numeric:
If the entered PIN is numeric and matches the inbuilt_pin, it proceeds with the withdrawal process.
If the entered PIN does not match or is not numeric, it displays an error message.
Upon successful authentication, the user is prompted to enter the withdrawal amount.
The script simulates transaction processing with a 3-second delay.
Finally, it confirms the success of the transaction.
USAGE
Run the script.
When prompted, enter your PIN.
If the PIN is correct, enter the amount to withdraw and press Enter to confirm.
The script will simulate the transaction process and display a success message upon completion.
Notes
This is a basic simulation and does not include real banking functionalities.
