monthlyPayment = 0
initialBalance = balance
monthlyInterestRate = annualInterestRate / 12

while abs(unpaidbalance) > 0:
    for i in range(12):
        balance = balance - monthlyPayment + ((balance - monthlyPayment) * monthlyInterestRate)
    if balance > 0:
        monthlyPayment += 10
        balance = initialBalance
    elif balance <= 0:
       break
print("Lowest Payment: ", monthlyPayment)
