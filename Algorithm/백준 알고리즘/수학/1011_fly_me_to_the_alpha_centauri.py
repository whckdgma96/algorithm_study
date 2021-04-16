T= int(input())

for i in range(T):
    a,b = map(int, input().split())
    c= b-a    #b=4, a= 0 c=4
    num=1
    while True:      #4
        if num ** 2 <=c<(num + 1)**2:
            break
        num += 1
        #num = 2
    if num ** 2 ==c:
        print((2*num)-1)
    elif num ** 2 <c<= num**2 +num:
        print(2*num)
    else:
        print((2*num)+1)