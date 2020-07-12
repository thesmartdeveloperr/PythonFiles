string=input("Enter the string:\t")
a=string.split()
if(string.isalnum):
    print("True")
else:
    print("False")
count1=0
count2=0
count3=0
count4=0
for s in a:
    for i in s:
        if(i.isalpha()):
            print("True")
            break
        else:
            count1+=1
    for i in s:
        if(i.isdigit()):
            print("True")
            break
        else:
            count2+=1
    for i in s:
        if(i.islower()):
            print("True")
            break
        else:
            count3+=1
    for i in s:
        if(i.isupper()):
            print("True")
            break
        else:
            count4+=1
    if(count1==len(a)):
        print("False")
    if(count2==len(a)):
        print("False")
    if(count3==len(a)):
        print("False")
    if(count4==len(a)):
        print("False")