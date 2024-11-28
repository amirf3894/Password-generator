import random
import string
import os
# defines the variable
symbol=['@','#','$','%','&','*','(',')','-','=','+','_','/','?','{','}']
number=list(range(0,10))
upper=list(string.ascii_uppercase)
lower=list(string.ascii_lowercase)
options={'symbol':True,'number':True,'uppercase':True,'lowercase':True}
pass_elements=[symbol,number,upper,lower]
del symbol,upper,number,lower # for more perfornace, I delete these variables
length=-1
num_of_enabled=0

# a function that takes the options to generate password
def take_options():
    print("just press enter if you want an option enable, otherwise type something and press enter" )
    num_of_enabled=0
    
    for key in list(options.keys()):
        options[key]=not bool(input (f'include {key}?'))
        if options[key]:
            print('enabled')
        else:
            print('disabled')
            num_of_enabled+=1
        print('*'*50)
    return options,num_of_enabled


# a function which takes the lenght of password
def take_lenght():
    length=input('Enter the length of the password, defualt is 8 : ')
    if length.isdigit():
        length=int(length)
    else:
        length=8
    return length

#it choose a random number for quantity of each element type (for example it chooses 3 lowecase , 2 uppercase, 1 symbol and 4 number) and select a random element from each type of characters
def generate_first_pass(characters,length,index):
    password=[]
    for __ in range(1,random.randint(2,length+1)):
            password.append(random.choice(characters))
    return password,len(password)


# takes the options and checks if all options are not disabled
options,num_of_enabled=take_options()
while num_of_enabled==0:
    os.system('cls' if os.name=='nt'else "clear")
    print('All options can not be disabled')
    options,num_of_enabled=take_options()



# it takes a valid length
length=take_lenght()
while num_of_enabled>length:
    print('length can not be lower than number of enabled options so enter the length again ')
    length=take_lenght()
else: 
        print('length it : ',length,'\n','*'*50)

# now we have valid length and valid option

#now we creat a password which sorted with folowimg form : symbol, number, upper, lower
length_saver=length
password_phase1 =[]
for index in range(len(options)):
    if list(options.values())[index]:
        returned_pass,reterned_len=generate_first_pass(pass_elements[index],(length)-(num_of_enabled)+1,index)
        password_phase1+=returned_pass
        length-=reterned_len
        num_of_enabled-=1
        index_saver=index
while len(password_phase1)!=length_saver:#for some reason the length of password_phase1 might be lower than entered length so i add this loop to solve this problem
	password_phase1.append(random.choice(pass_elements[index_saver]))

#now we randomize the order of password_phase1's elements and save it in password_phase2
password_phase2=''
for ___ in range(len(password_phase1)):
    password_phase2+=str(password_phase1.pop(random.randint(0,len(password_phase1)-1)))
print(password_phase2)


#Created by Amir Foorjani on November 28, 2024
