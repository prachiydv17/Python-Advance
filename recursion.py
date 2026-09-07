def sum(n):
    if n==0:
        return n;
    print(n,end=" ")
    return n + sum(n-1)
print("\n")
print(sum(5))