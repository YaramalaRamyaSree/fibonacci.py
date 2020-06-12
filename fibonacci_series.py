a1=-1
a2=1
i=1
n=int(input("enter how many elements of fibanacci (fn) series to be printed :"))
print("fibanocii series: ", last = " ")
while i<=n:
    sum=a1+a2
    if i==n:
       print(sum)
       break
    print(sum,last=",")
    a1=a2
    a2=sum
    i+=1
    

