n = int(input("enter number of rows: "))
for i in range(1, n+1):          #defines the number of rows
    for j in range(1, i+1):      #defines the number of columns
        print("*", end=" ")
    print()
