n=(int)(input("No. of nos. : "))
print("Enter the nos. =>")
a=[(int)(input()) for i in range(n)]
x=(int)(input("Enter secret no. : "))
a=sorted(a)
l,r=0,n-1
print("Say my chosen number is "+str(x)+". What are you going to do? Do a binary search:")
while(l<=r):
    mid=(l+r)//2
    print("Guess",a[mid],"(mid of",a[l],"and",a[r],"in the list) ->",end=" ")
    if(a[mid]==x):
        print("spot on!")
        break
    elif(a[mid]<x):
        print("you're too low.")
        l=mid+1
    else:
        print("you're too high.")
        r=mid-1
        


