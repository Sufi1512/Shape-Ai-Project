import hashlib
a = input('Enter the Vlaue ')
val = hashlib.md5(a.encode())

val_md5 = val.hexdigest()



print(val_md5)

 
