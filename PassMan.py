
import random
import pyfiglet as pyf
import time
from time import sleep
import platform
import os
import sys
# Checks to See if System is Linux

if platform.system() == 'Linux':
		clear = lambda: os.system('clear') # 'cls' if windows
#Checks to see if System is Windows Based

if platform.system() == 'Windows':
		clear = lambda: os.system('cls') # 'clear' if linux
		
#Manually typed out keys, could have probably done this better

lower = ['a','b','c','d','e','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','1','2','3','4','5','6','7','8','9','!','@','#','$','%','^',"&","*","(",")","-","_","+","=","''","[","]"]
var1 = random.choice(lower)
var2 = random.choice(lower)
var3 = random.choice(lower)
var4 = random.choice(lower)
var5 = random.choice(lower)
var6 = random.choice(lower)
var7 = random.choice(lower)
var8 = random.choice(lower)
var9 = random.choice(lower)
var10 = random.choice(lower)
var11= random.choice(lower)
var12 = random.choice(lower)
var13 = random.choice(lower)
var14 = random.choice(lower)
var15= random.choice(lower)
var16 = random.choice(lower)
def backToStart():
	q = input('\n'  + 'Back to start [0] \n')
	if q == '0':
		main()
'''		
The PassGen Function is declared that will be called up every time '1' is pressed in the Main screen
PassGen takes an array that was declared in the begginning of the program and combines it at random to create passwords
'''

def PassGen():
		q = input('Generate a Weak password [W], a normal password [N], or a strong password [S]?\n')
		if q == 'W' or q == 'w':
			psw = var1 + var2 + var3 + var4
			print('Your password is: '+psw)
		if q == 'N' or q == 'n':
			psw = var1 + var2 + var3 + var4 + var5+var6+var7+var8
			print('Your password is: '+psw)
		if q == 'S' or q == 's': 
			psw = var1 + var2 + var3 + var4 + var5+var6+var7+var8+var9+var10+var11+var12+var13+var14+var15+var16
			print('Your password is: '+psw)
#PassSave saves typed in or Generated passwords along with Usernames onto a text file called accounts.txt

def PassSave():
	w = open('accounts.txt', 'a')
	with open('accounts.txt', 'a') as w:
			cat = input('What would you like to store it as? [Category] [Site] \n')
			clear()
			w.write('------ [' + cat + '] ' + ' ------\n')
			name = input('What is your Username\Email?\n')
			clear()
			p = input('Would you like to enter in your own password [O], or generate a new one? [G]\n')
			clear()
			if p == "O" or p == "o":
				q = input('What is your password?\n')
				w.write(name + ':' + q +'\n')
			if p == "G" or p == "g":
				q = input("Normal [N] or Strong [S]?")
			if q == 'N' or q == 'n':
				psw = var1 + var2 + var3 + var4 + var5+var6+var7+var8
				print('Your password is: '+psw)
				w.write(name + ":" + psw + '\n')
			if q == 'S' or q == 's': 
				psw = var1 + var2 + var3 + var4 + var5+var6+var7+var8+var9+var10+var11+var12+var13+var14+var15+var16
				print('Your password is: '+psw)

				w.write(name + ":"+ psw +'\n')
			def space():
				w.write('\n')
			space()
			space()
			space()
		#Add way to choose methods 
		#Ex: q = ('Which method?')
		#if q == '1':
		#method1 removed // Def couldn't take 80 lines of code in it 
ascii_banner = pyf.figlet_format('Welcome to PassMan!')
print(ascii_banner + 'By Dylan Bedi')
time.sleep(.885)
#Main is the Main screen that will be called upon after 
def main():
	if platform.system() == 'Linux':
		clear = lambda: os.system('clear') # 'cls' if windows
	if platform.system() == 'Windows':
		clear = lambda: os.system('cls') # 'clear' if linux
	clear()
	question = input(' Password Generator [1]\n Password Saver [2]\n Password Viewer [3] \n Delete Password [4] \n Exit [0]\n')
	if question == '1':
		clear()
		PassGen()
		q = input('\n'  + 'Back to start [0]\n')
		if q == '0':
			main()
	if question == '2':
		clear()
		PassSave() 
		backToStart()


#PassView allows you to read your previously made accounts through the Terminal
	def PassView():
		q = input('[1] Read all accounts \n[2] Read one account?\n')
		if q == '2':
			read = input('What is your account stored as (number, category, etc [Case Sensitive]?\n')
			with open('accounts.txt', 'r') as r:
				for line in r:
					if read in line:
						line1 = r.readline()
						print("\n" + "\n" + "Your account for "+ q +":" +"\n" + "\n" +line1+"\n")

		if q == '1':
			with open('accounts.txt','r') as r:
				for line in r:
					print(line)
	
	if question == '3':
		clear()
		PassView()
		backToStart()
main()
'''
	if question == '4':
		q = input('What is the Category/Title?\n')
		with open('accounts.txt','w') as r:
			for line in r:
				if q in line:
					line1 = r.writeline('                 '
					print('Deleted Line!')
					
'''
					
