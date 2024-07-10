# import random
# import string

# pass_len=6
# charvalues = string.ascii_letters + string.digits + string.punctuation

# password=""
# for i in range(pass_len):
#    password += random.choice(charvalues)

# print("your random password is : ",password)


#list comprehension [function for i in range(n)]
import random
import string

pass_len=6
charvalues = string.ascii_letters + string.digits + string.punctuation

password=" ".join([random.choice(charvalues)for i in range(pass_len)])
print("random password is: ",password)