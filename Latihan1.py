def ini_prima(n, pembagi=None):
    
    if pembagi is None:
        pembagi = n - 1
   
    if n < 2:
        return False
    
    if pembagi == 1:
        return True
    
    if n % pembagi == 0:
        return False
    
    return ini_prima(n, pembagi - 1)


bilangan = 29
if ini_prima(bilangan):
    print(f"{bilangan} bilangan prima")
else:
    print(f"{bilangan} bukan bilangan prima")
