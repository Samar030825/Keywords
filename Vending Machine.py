def calculate_change(paid , price):
    change = paid - price
    return change
snack_price = 25
print("++++Snack Vending Machine++++")
print(f"This snack cost {snack_price}")
print("Accepted coin : 1 ,5 ,10 ,25 \n")
total_inserted = 0
coin_inserted = 0
while True :
    coin = int(input("Enter a 1 , 5 , 10 or 25 unit coin : "))
    if coin != 1 and coin != 5 and coin != 10 and coin != 25 :
        print("Invalid coin ! Try again \n")
        continue
    total_inserted += coin
    coin_inserted += 1

    print(f"inserted {coin}. Total so far : {total_inserted}! \n")
    if total_inserted >= snack_price:
        print("Enough money inserted \n ")
        break

change_due  = calculate_change(total_inserted , snack_price)

print("Dispensing your snack ! ")

if change_due == 0:
    pass
else:
    print(f"Here is your change : {change_due} units ")

print("======PURCHASE SUMMARY======")
print("Snack Price : " , snack_price)
print("Coin Inserted : " , coin_inserted)
print("Total Paid : " , total_inserted)
print("Change Given : " , change_due)
print("============================")
print("Thank you for purchase ")