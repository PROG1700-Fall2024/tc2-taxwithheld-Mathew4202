# Tax Withheld Calculator

# Write a console program that calculates the total amount of tax withheld from an employee’s weekly salary.
# The total withheld tax amount is calculated by combining the amount of provincial tax withheld and the amount of 
# federal tax withheld, minus a per-dependent deduction from the total tax withheld. The user will enter their pre-tax 
# weekly salary amount and the number of dependents they wish to claim. 
# 
# The program will calculate and output the amount of provincial tax withheld, amount of federal tax withheld, the 
# dependent tax deduction, and the user’s final take-home amount.
# Provincial withholding tax is calculated at 6.0%. Federal withholding tax is calculated at 25.0%. 
# The tax deduction for dependents is calculated at 2.0% of the employee’s salary per dependent.
"""
Student Name:    Mathew Akunyili
Program Title:   Tax Withholding Calculator
Description:    calculate total tax withheld, and total money taken
"""
def main():
    # YOUR CODE STARTS HERE, each line must be indented (one tab)

    # Declare variables
    provincialPercent = 0.06
    federalPercent = 0.25
    dependantPercent = 0.02

    # Name of program
    print("Tax Withholding Calculator")

    # Prompt uset to enter full amount of weekly salary
    salary = float(input("Please enter the full amount of your weekly salary:"))


    # Ask users for how many dependants they have
    dependants = int(input("How many dependants do you have?:"))

    #Calculations
    provincialWithheld = salary * provincialPercent
    federalWithheld =  salary * federalPercent
    dependantsDeduction =  salary * (dependants * dependantPercent)
    totalWithheld = provincialWithheld + federalWithheld - dependantsDeduction
    totalPay = salary - totalWithheld

    # Print results to user
    print(f"Provincial Tax Withheld: ${provincialWithheld:.2f}")
    print(f"Federal Tax Withheld: ${federalWithheld:.2f}")
    print("Dependant Deduction for",dependants,f"- dependants: ${dependantsDeduction:.2f}")
    print(f"Total Withheld: ${totalWithheld:.2f}")
    print(f"Total Take-Home Pay: ${totalPay:.2f}")








    # YOUR CODE ENDS HERE

main()
