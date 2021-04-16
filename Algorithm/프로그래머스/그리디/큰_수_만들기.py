number = "4177252841"
k= 4

def solution(number, k):
    stack = []
    for num in number:
        while len(stack)>0 and k>0 and stack[-1] < num:
            k -= 1
            stack.pop()
        stack.append(num)

    if k !=0:
        stack = stack[:-k]
    return ''.join(stack)



print(solution(number,k))