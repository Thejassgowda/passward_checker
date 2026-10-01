pas=input("enter the passward:")

is_upper=False
is_lower=False
is_num=False

for char in pas:
    if char.isupper():
        is_upper=True
    if char.islower():
        is_lower=True
    if char.isdigit():
        is_num=True
        
if len(pas) >= 8 and is_upper and is_lower and is_num:
    print("strong passward")
else:
    print("week passward")
        


        