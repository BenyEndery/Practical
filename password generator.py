import random
print("welcom to password generatot ...")
alefba = ('abcdefglomnp123456789_*#$@!%ASDFGHJKLMNBVCXZQWERTYUIOP')
pass_range=(int(input("enter password range :")))
if pass_range>=8:
    for i in range(pass_range):
        i=random.choice(alefba)
        print(i,end="")
else:
    print("password range must be bigger thane 8 !!!")