balance = float(input("Outstanding balance on the credit card: "))
annualInterestRate = float(input("Annual interest rate: "))
monthlyPaymentRate = float(input("Minimum monthly payment rate as a decimal: "))

remaining = balance
for n in range(12):
    unpaid = remaining - monthlyPaymentRate * remaining
    remaining = round(unpaid + (annualInterestRate * unpaid)/12, 2)
print('Remaining balance: ' + str(remaining))