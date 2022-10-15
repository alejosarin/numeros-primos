n=int(input("\n\ndigite n : "))
j=n
a=1
cont=0
print("\nprimos :\n ")
for i in range(1,n+1):
    while a!=i:
        if i%a ==0:
            cont=cont+1
        a=a+1 
    if cont<=1:
        print(str(i))
    a=1
    cont=0
    j=j-1
    



    
