def jumlah_digit(bilangan):
    if len(bilangan) == 1:
        return int(bilangan), bilangan
    else:
        jumlah_sisa = jumlah_digit(bilangan[1:])
        return int(bilangan[0]) + jumlah_sisa[0], bilangan[0] + "+" + jumlah_sisa[1]


bilangan = "234"
jumlah, deret = jumlah_digit(bilangan)
print(f"{bilangan} maka jumlah digitnya adalah {deret} = {jumlah}")

