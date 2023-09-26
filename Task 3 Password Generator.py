import random
letter=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
        'w', 'x', 'y', 'z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
        'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X','Y','Z']
digit=['0','1','2','3','4','5','6','7','8','9','0']
symbol=['@','_','#','%','$','&','(',')','!']
print('                     *****************************')
print('                     WELCOME TO PASSWORD GENERATOR')
print('                     *****************************')
print('\n')
n_letter=int(input('            Enter the number of letter you want in password:'))
n_symbol=int(input('            Enter the number of symbol you want in password:'))
n_digit=int(input ('            Enter the number of digits you want in password:'))
password=[]
for i in range(1,n_letter+1):
    char=random.choice(letter)
    password+=char
for i in range(1,n_symbol+1):
    char=random.choice(symbol)
    password+=char
for i in range(1,n_digit+1):
    char=random.choice(digit)
    password+=char
#print(password)
random.shuffle(password)
#print(password
print('\n')
print('                            Password Generated:')
print('                     -------------------------------')
pass_generated=''
for i in range(len(password)):
    pass_generated+=password[i]
    
print('','                             ',pass_generated)


    
    

