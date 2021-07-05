import hashlib
a = str (input('Enter the Value '))
val = hashlib.md5(a.encode())

val_md5 = val.hexdigest()



print('The hash Value of %s is %s' %(a, val_md5))

