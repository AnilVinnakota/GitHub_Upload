# coding: utf-8
import csv
from pathlib import Path

"""Part 1: Automate the Calculations.

Automate the calculations for the loan portfolio summaries.

First, let's start with some calculations on a list of prices for 5 loans.
    1. Use the `len` function to calculate the total number of loans in the list.
    2. Use the `sum` function to calculate the total of all loans in the list.
    3. Using the sum of all loans and the total number of loans, calculate the average loan price.
    4. Print all calculations with descriptive messages.
"""
loan_costs = [500, 600, 200, 1000, 450]

# How many loans are in the list?
# @TODO: Use the `len` function to calculate the total number of loans in the list.
# Print the number of loans from the list
# YOUR CODE HERE!

# Define a variable to store the number of loans.
total_number_of_loans = len(loan_costs)

# Print the number of loans on console.
print(f"The total number of loans is {total_number_of_loans}")

# What is the total of all loans?
# @TODO: Use the `sum` function to calculate the total of all loans in the list.
# Print the total value of the loans
# YOUR CODE HERE!

# Define a varaible to store the sum of all loans.
sum_of_all_loans = sum(loan_costs)

# Print the sum of all loans.
print(f"Total of all loans is {sum_of_all_loans} ")

# What is the average loan amount from the list?
# @TODO: Using the sum of all loans and the total number of loans, calculate the average loan price.
# Print the average loan amount
# YOUR CODE HERE!

# Define a variable to store the average loan proice.
average_loan_price = sum_of_all_loans / total_number_of_loans

# Print the average loan price
print(f"Average loan price is {average_loan_price}")

"""Part 2: Analyze Loan Data.

Analyze the loan to determine the investment evaluation.

Using more detailed data on one of these loans, follow these steps to calculate a Present Value, or a "fair price" for what this loan would be worth.

1. Use get() on the dictionary of additional information to extract the **Future Value** and **Remaining Months** on the loan.
    a. Save these values as variables called `future_value` and `remaining_months`.
    b. Print each variable.

    @NOTE:
    **Future Value**: The amount of money the borrower has to pay back upon maturity of the loan (a.k.a. "Face Value")
    **Remaining Months**: The remaining maturity (in months) before the loan needs to be fully repaid.

2. Use the formula for Present Value to calculate a "fair value" of the loan. Use a minimum required return of 20% as the discount rate.
3. Write a conditional statement (an if-else statement) to decide if the present value represents the loan's fair value.
    a. If the present value of the loan is greater than or equal to the cost, then print a message that says the loan is worth at least the cost to buy it.
    b. Else, the present value of the loan is less than the loan cost, then print a message that says that the loan is too expensive and not worth the price.

    @NOTE:
    If Present Value represents the loan's fair value (given the required minimum return of 20%), does it make sense to buy the loan at its current cost?
"""

# Given the following loan data, you will need to calculate the present value for the loan
loan = {
    "loan_price": 500,
    "remaining_months": 9,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

# @TODO: Use get() on the dictionary of additional information to extract the Future Value and Remaining Months on the loan.
# Print each variable.
# YOUR CODE HERE!

# Define variables to store Future value and Remaining Months
future_value = loan.get("future_value")
remaining_months = loan.get("remaining_months")

# Print the future value and remaining months on console.
print(f"The future value of the loan is {future_value} and it has {remaining_months} months remaining")

# @TODO: Use the formula for Present Value to calculate a "fair value" of the loan.
# Use a minimum required return of 20% as the discount rate.
#   You'll want to use the **monthly** version of the present value formula.
#   HINT: Present Value = Future Value / (1 + Discount_Rate/12) ** remaining_months

# YOUR CODE HERE!
# Define variables to compute present value.
discount_rate = .2
present_value = future_value / ( (1 + (discount_rate/12)) ** remaining_months)

# Print the preset value of the loan on Console.
print (f"Present Value of the loan is {present_value}")
# If Present Value represents what the loan is really worth, does it make sense to buy the loan at its cost?
# @TODO: Write a conditional statement (an if-else statement) to decide if the present value represents the loan's fair value.
#    If the present value of the loan is greater than or equal to the cost, then print a message that says the loan is worth at least the cost to buy it.
#    Else, the present value of the loan is less than the loan cost, then print a message that says that the loan is too expensive and not worth the price.
# YOUR CODE HERE!

# Define a variable to store loan cost
loan_price = loan["loan_price"]

# print message based on loan cost and present value
if (present_value >= loan_price) :
    # Loan cost is lower than its value. Print a message on console with a Buy recommendation
    print(f"Present value {present_value} is greater than loan price {loan_price}. It is worth at least the cost to buy it.")
else:
    # Loan cost is higher than its value. Print message on console that loan is expensive.
    print(f"Present value {present_value} is greater than loan price {loan_price}. The loan is too expensive and not worth the price")


"""Part 3: Perform Financial Calculations.

Perform financial calculations using functions.

1. Define a new function that will be used to calculate present value.
    a. This function should include parameters for `future_value`, `remaining_months`, and the `annual_discount_rate`
    b. The function should return the `present_value` for the loan.
2. Use the function to calculate the present value of the new loan given below.
    a. Use an `annual_discount_rate` of 0.2 for this new loan calculation.
"""

# Given the following loan data, you will need to calculate the present value for the loan
new_loan = {
    "loan_price": 800,
    "remaining_months": 12,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

# @TODO: Define a new function that will be used to calculate present value.
#    This function should include parameters for `future_value`, `remaining_months`, and the `annual_discount_rate`
#    The function should return the `present_value` for the loan.
# YOUR CODE HERE!
# 
def calculate_present_value(future_value, remaining_months, annual_discount_rate):
    """ Function returns present value given future_value, remiaining_months, annual_discount_rate.
        Formula is  present_value =  future_value / ((1 + (annual_discount_rate/12)) ** remaining_months)

        Keyword arguments:
        future_value          -- future value for which the present value is being computed
        remaining_months      --  Numer of months remaining
        annual_discount_rate  --  Discount rate for the computation

        return value:
        present_value using the formula above.
    """
    return future_value / ((1 + (annual_discount_rate/12)) ** remaining_months)

# @TODO: Use the function to calculate the present value of the new loan given below.
#    Use an `annual_discount_rate` of 0.2 for this new loan calculation.
# YOUR CODE HERE!

# Define a variable present_value. Call the new function to fill the value.
present_value = calculate_present_value(new_loan["future_value"], new_loan["remaining_months"], 0.2)

# Print the present value of the new loan on Console.
print(f"The present value of the loan is: {present_value}")



"""Part 4: Conditionally filter lists of loans.

In this section, you will use a loop to iterate through a series of loans and select only the inexpensive loans.

1. Create a new, empty list called `inexpensive_loans`.
2. Use a for loop to select each loan from a list of loans.
    a. Inside the for loop, write an if-statement to determine if the loan_price is less than 500
    b. If the loan_price is less than 500 then append that loan to the `inexpensive_loans` list.
3. Print the list of inexpensive_loans.
"""

loans = [
    {
        "loan_price": 700,
        "remaining_months": 9,
        "repayment_interval": "monthly",
        "future_value": 1000,
    },
    {
        "loan_price": 500,
        "remaining_months": 13,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 200,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 900,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
]

# @TODO: Create an empty list called `inexpensive_loans`
# YOUR CODE HERE!
# Define a new list for inexpensive loans
inexpensive_loans = []

# @TODO: Loop through all the loans and append any that cost $500 or less to the `inexpensive_loans` list
# YOUR CODE HERE!

# Loop through all the loans
for loan in loans:
    # if loan cost of 500 or less
    if (loan["loan_price"] <= 500):
        # add the loan to the inexpensive list.
        inexpensive_loans.append(loan)

# @TODO: Print the `inexpensive_loans` list
# YOUR CODE HERE!

# Print the inexpensive loans using builtin to_string
print(inexpensive_loans)


"""Part 5: Save the results.

Output this list of inexpensive loans to a csv file
    1. Use `with open` to open a new CSV file.
        a. Create a `csvwriter` using the `csv` library.
        b. Use the new csvwriter to write the header variable as the first row.
        c. Use a for loop to iterate through each loan in `inexpensive_loans`.
            i. Use the csvwriter to write the `loan.values()` to a row in the CSV file.

    Hint: Refer to the official documentation for the csv library.
    https://docs.python.org/3/library/csv.html#writer-objects

"""

# Set the output header
header = ["loan_price", "remaining_months", "repayment_interval", "future_value"]

# Set the output file path
output_path = Path("inexpensive_loans.csv")

# @TODO: Use the csv library and `csv.writer` to write the header row
# and each row of `loan.values()` from the `inexpensive_loans` list.
# YOUR CODE HERE!

# Open the file in write mode
with open(output_path, "w", newline='') as fp:
    # Create csc Writer on this file
    csvwriter = csv.writer(fp)

    # Write Header row into the file
    csvwriter.writerow(header)

    # Loop thorough inexpensive loans
    for loan in inexpensive_loans:
        # Write loan values into the csv file.
        csvwriter.writerow(loan.values())