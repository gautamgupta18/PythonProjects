item = []
price = []
n = int(input("Enter Number of Items:"))
for i in range(n):
  product = input( "Enter name of product: ")
  item.append(product)
  pric =  int(input("Enter price of product: "))
  price.append(pric)
for i in range(n):
  print( item[i] , " = ", price[i] )

print("Highest priced Item = ", item[price.index(max(price))] )
print("Lowest priced Item = ", item[price.index(min(price))] )

print("Total Bill = ", sum(price))