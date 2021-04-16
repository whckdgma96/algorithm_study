number = int(input())
new_number = 0
original_number = number
cnt = 0
temp = 0

#26
while True:
    temp = number // 10 + number % 10 #2+6=8
    new_number = (number % 10) * 10 + temp % 10 #6+8=14
    cnt += 1
    number = new_number
    if new_number ==original_number:
        break

print(cnt)

