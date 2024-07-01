import random
print("==============welcome to password generator==============")
alpha=["a","b","c",'d','e','f','g','h','i','j','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
num=['1','2','3','4','5','6','7','8','9','10','0']
spc=['@','$','*','&','%','#','!','.','?',]
n_alpha=int(input("how many letters u want"))
n_num=int(input("how many numbers u want"))
n_spc=int(input("how many special character  u want"))
password=[]

for i in range(1,n_alpha+1):
    char=(random.choice(alpha))
    password+=char
for i in range(1,n_num+1):
    char=(random.choice(num))
    password+=char
for i in range(1,n_spc+1):
    char=(random.choice(spc))
    password+=char


random.shuffle(password)
print("your random password is","".join(password))
