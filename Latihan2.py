def palindrom(kalimat):
    
    if len(kalimat) <= 1:
        return True
    
    if kalimat[0] != kalimat[-1]:
        return False
    
    return palindrom(kalimat[1:-1])


kalimat1 = "kasur rusak"
kalimat2 = "saya makan"


print(f"{kalimat1} = {palindrom(kalimat1)}")
print(f"{kalimat2} = {palindrom(kalimat2)}")

