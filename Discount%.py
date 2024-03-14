qty=int(input("Enter the quantity you want to buy: "))
rate=int(input("Enter the rate of the product: "))
amt=qty*rate
print("Total Amount =",amt)

if amt>=2000:
    Disc=20
elif 2000>amt>=1000:
    Disc=10
else:
    Disc=5

DiscAmt=(Disc*amt)/100
NetAmt=amt-DiscAmt

print("Total Discount you get:",DiscAmt)
print("Afte Discount Total Amount is",NetAmt)