x=int(input("enter how many numbers are their in list"))
list1=[]
for i in range (0,x+1//2):
    d=int(input("enter the number"))
    list1.append(d)
list1.sort()
print(list1)
key=int(input("enter a number to find "))
low=0
high=x
mid=low+high//2
if list1[mid]==key:
    print("the number ",key," is present in the array at the position ",mid)
elif list1[mid]<key:
    low1=mid+1
    mid1=(low1+high)//2
    if list1[mid1]==key:
        print("the number ",key," is present in the array at the position ",mid1)
    elif list1[mid1]>key:
        high=mid1-1
        mid1=(low1+high)//2
        if list1[mid1]==key:
            print("the number ",key," is present in the array at the position ",mid1)
        else:
            print("the number ",key," is not present in the array")
        
    else:
        print("the number ",key," is not present in the array")
elif list1[mid]>key:
    high1=mid-1
    mid2=(low+high1)//2
    if list1[mid2]==key:
        print("the number ",key," is present in the array at the position ",mid2)
    elif list1[mid2]<key:
        low1=mid2+1
        mid3=(low1+high1)//2
        if list1[mid3]==key:
            print("the number ",key," is present in the array at the position ",mid3)
        else:
            print("the number ",key," is not present in the array")
    else:
        print("the number ",key," is not present in the array")
