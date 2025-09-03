#concession stand program

menu={"ice cream":50,
      "popcorn":150,
      "lays":50,
      "juice":90,
      "puff":45,
      "fries":80,
      "chacolate":20}
cart=[]
total=0

print("--------MENU---------")
for keys,values in menu.items():
     print(f"{keys:10} : Rs{values:.2f}")
print("---------------------")

while True:
    food =input("which food you like to eat(q to quit):")
    if food.lower() =="q":
        break
    elif menu.get(food) is not None:
        cart.append(food)
print("-------YOUR ORDER------")
for food in cart:
    total+=menu.get(food)
    print(food,end=" ")
print()
print(f"your total: RS{total:.2f}")
