N = int(input())

arr=[]
for i in range(N):
    arr.append(int(input()))

arr.sort()

left = 0
right = N-1
sum  =0


# print(f"Zero position {arr[left]} ")
# print(f"Last Positions {arr[right]}")

while left < right:
    sum += arr[right]-arr[left]
    left = left+1
    right = right-1

print(sum)