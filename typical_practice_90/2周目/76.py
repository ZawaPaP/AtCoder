N = int(input())
A = list(map(int, input().split()))

target = sum(A) / 10


# 周回を調べるのに2Aを 2pointerで調べればいい
A = A + A

l, r = 0, 1

size = A[0]
while r < 2 * N:
    if size == target:
        print("Yes")
        exit()
    elif size > target and r - l > 1:
        size -= A[l]
        l += 1
    else:
        size += A[r]
        r += 1

print("No")
