n=int(input("Enter the number of rows you want:\t"))
for i in range(n+1):
    for j in range(i):
        print(i,end=" ")
    print('')
