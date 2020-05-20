balance = float(input("Outstanding balance on the credit card: "))
annualInterestRate = float(input("Annual interest rate: "))

remaining = balance
payment = 0
while remaining > 0:
    remaining = balance
    payment += 10
    for n in range(12):
        unpaid = remaining - payment
        remaining = round(unpaid + (annualInterestRate * unpaid)/12, 2)
print('Lowest Payment: ' + str(payment))