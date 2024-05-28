def kombinasi(n, k):
    if k == 0 or k == n:
        return 1
    else:
        return kombinasi(n - 1, k - 1) + kombinasi(n - 1, k)

n = 5
k = 2
print(f"C({n}, {k}) = {kombinasi(n, k)}")

