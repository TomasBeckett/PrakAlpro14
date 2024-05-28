def jumlah_deret_ganjil(n):
    if n == 1:
        return 1
    else:
        if n % 2 == 0:
            return 0 + jumlah_deret_ganjil(n - 1)
        else:
            return n + jumlah_deret_ganjil(n - 2)

n = 11
print("Jumlah deret ganjil untuk n =", n, "adalah", jumlah_deret_ganjil(n))
