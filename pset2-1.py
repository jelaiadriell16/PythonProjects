print("Paying the Minimum\n")

balance = int(raw_input("Balance: "))
annualInterestRate = float(raw_input("Annual Interest Rate: "))
monthlyPaymentRate = float(raw_input("Monthly Payment Rate: "))

monIntRate = annualInterestRate/12.0
month = 1
totalPaid = 0

while month <= 12:
    
    minPayment = monthlyPaymentRate * balance
    monthBalance = balance - minPayment
    remBalance = monthBalance + (monIntRate * monthBalance)

    print("Month: %d" % month)
    print("Minimum monthly payment: "), round(minPayment, 2)
    print("Remaining balance: "), round(remBalance, 2)

    balance = remBalance
    month += 1
    totalPaid += minPayment

print "Total paid: ", round(totalPaid, 2)
print "Remaining balance: ", round(balance, 2)