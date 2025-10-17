amount_of_vouchers = int(input())
vouchers = []
sum = 0
for i in range(amount_of_vouchers):
    inp = input().split(" ")
    vouchers.append((int(inp[0]), int(inp[1])))

for i in range(len(vouchers)):
    vouchers = sorted(vouchers, key=lambda o: o[0])
    print(vouchers)
    sum += vouchers[0][0]
    vouchers.pop(0)
print(sum)
    

