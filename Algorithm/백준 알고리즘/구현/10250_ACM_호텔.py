T= int(input())
#h:호텔층수 w: 층의 방수 n: 몇번째손님
for i in range(T):
    H,W,N = map(int,input().split())
    floor = 0
    ho=0
    if N %H ==0:
        floor = H*100
        ho = N//H
    else:
        floor =(N%H)*100
        ho = N//H+1
    print(floor+ho)

