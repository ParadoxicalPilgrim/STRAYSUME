x=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

left,right=0,len(x)-1

mid=(left+right)//2

target=7

found=False

while left<=right:
    mid=(left+right)//2
    if x[mid]==target:
        print("Element has been found!")
        found=True
        break

    elif target>x[mid]:
        left=mid+1

    else:
        right=mid-1


if not found:
    print("Element not found!")

