balance = int(input("Enter a balance: "))
annualInterestRate = int(input("Enter your interest rate: "))
monthlyPaymentRate = int(input("Enter your monthly payment: "))
for j in range(12):
      balance = balance - (balance * monthlyPaymentRate) + ((balance - (balance * monthlyPaymentRate)) * (annualInterestRate/12)
print("Remaining balance: ", round(balance, 2))