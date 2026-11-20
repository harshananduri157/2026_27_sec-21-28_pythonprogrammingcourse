rows = int(input("Enter the number of rows: "))

symbol = input("Enter the symbol to print (e.g., * or 0): ")

for i in range(1, rows + 1):

  print((symbol + " ") * i)