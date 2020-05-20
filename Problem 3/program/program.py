balance = float(input("Outstanding balance on the credit card: "))
annualInterestRate = float(input("Annual interest rate: "))

remaining = balance
payment = balance / 12
upper = (balance*(1+(annualInterestRate/12))**12)/12
while remaining > 0.1 or remaining < -0.1:
    if remaining > 0.1:
        lower = payment
    else:
        upper = payment
    remaining = balance
    payment = (lower + upper)/2
    for n in range(12):
        unpaid = remaining - payment
        remaining = unpaid + (annualInterestRate * unpaid)/12
print('Lowest Payment: ' + str(round(payment,2)))