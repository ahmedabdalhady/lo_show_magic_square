                                         #lo_shu magic square
square=[
    [4,9,2],
    [3,5,7],
    [8,1,10]
]

def loshow(list2d):
    if isinstance(list2d,list) and len(list2d)==3:
        list1d=sum(list2d,[])
        print(list1d)
        if max(list1d) >=10 or min(list1d) <=0:
            print("out of range")
            return False
        if len(list1d) != len(set(list1d)):
            print("check your list there are duplicate  values")
            return False
        row1sum=list2d[0][0]+list2d[0][1]+list2d[0][2]
        row2sum=list2d[1][0]+list2d[1][1]+list2d[1][2]
        row3sum=list2d[2][0]+list2d[2][1]+list2d[2][2]
        col1sum=list1d[0]+list1d[3]+list1d[6]
        col2sum=list1d[1]+list1d[4]+list1d[7]
        col3sum=list1d[2]+list1d[5]+list1d[8]
        rightdiagonalsum=list1d[2]+list1d[4]+list1d[6]
        leftdiagonalsum=list1d[0]+list1d[4]+list1d[8]
        if row1sum==row2sum==row3sum==col1sum==col2sum==col3sum==rightdiagonalsum==leftdiagonalsum:
            print("your 2d list is a lo shu magic square")
            return True
        else:
            print("your 2d list is not a lo shu magic square")
            return False
print(loshow(square))