all_num = set(range(1, 10001))
not_self_number = set()

for i in range(1,10001):
    for j in str(i):
        i += int(j)
    not_self_number.add(i)

self_number = sorted(all_num - not_self_number)
for i in self_number:
    print(i)
