f1 = 134
f2 = -129
f3 = 300
f4 = 172
f5 = 999
total  = f1 + f2 + f3 + f4 + f5 
average = total / 5
print("Total harvest   :",total,"KG")
print("Average per feld  :",average, "KG")
price_per_kg = 15
earnings = total * price_per_kg
print("Total earning    Rs.", earnings)
bags  = total// 25
leftover = total % 25 
last_year = 500
print("better than last year?",total > last_year)
print("same as last year?  :",total == last_year)
print("at least as good?  :",total >= last_year)
total += 30
print("After bonus crop  :",total, "kg")
total -= 15
print("after seed reserve  :", total,"kg")
bags = total // 25 
print("final bags packed  :", bags) 
      