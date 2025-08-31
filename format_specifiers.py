#format specifiers = {value:flags} format a value based on what flags are inserted

price1 = 89.3456
price2 = 789.234
price3 = 89.73
price4 = 789.34
price5 = 345.23
price6 = 12.4
price7 = 867.98
price8 = 78459.324
price9 = 34564.987
price10 = 23468.456

print(f"price1 is {price1:.2f}")
print(f"price2 is {price2:10}")
print(f"price3 is {price3:010}")
print(f"price4 is {price4:>10}")
print(f"price5 is {price5:<10}")
print(f"price6 is {price6:^10}")
print(f"price7 is {price7:+}")
print(f"price8 is {price8:,}")
print(f"price9 is {price9:+,.1f}")
print(f"price10 is {price10: }")
