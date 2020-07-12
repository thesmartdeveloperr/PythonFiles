n=int(input("Enter the number of rows you want:\t"))
for i in range(n+1):
    k=i
    for j in range(i):
        print(k,end=" ")
        k+=1
    print('')
