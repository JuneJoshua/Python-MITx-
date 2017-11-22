initialBalance = balance 
monthlyInterestRate = annualInterestRate/12
lowerBound = initialBalance/12
upperBound = (initialBalance * (1 + monthlyInterestRate)**12)/12.0
epsilon = 0.03

while abs(balance) > epsilon:
    monthlyPayment = (upperBound + lowerBound)/2
    balance = initialBalance
    for k in range(12):
        balance = balance - monthlyPayment + ((balance - monthlyPayment) * monthlyInterestRate)
    if balance > epsilon:
        lowerBound = monthlyPayment
    elif balance < -epsilon:
        upperBound = monthlyPayment
    else:
        break
print('Lowest Payment: ', round(monthlyPayment), 2)
