
from yt import *
from sc import *
from inst import *
import logging


def search():
    pass

def upload():
	
	uiu = input("1.YT | 2.SC |3.insta |1.2.3each ")
	
	if uiu == "1":
		main_yt()
	
	elif uiu == "2":
		
		main_sc()
	
	elif uiu == "3":
		main_inst()
	
	elif uiu == "1.2.3":
		main_yt()
		
		main_sc()
		
		main_inst()

def download():
    pass

def learn():
    pass

def play():
    pass

def exit():
    print ("Bye ! solid ")

def main():
    
    while True:
        print("1. Search")
        print("2. Upload")
        print("3. Download")
        print("4. Learn")
        print("5. Play")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            search()
        
        elif choice == '2':
            upload()
        
        elif choice == '3':
            download()
        
        elif choice == '4':
            learn()
        
        elif choice == '5':
            play()
        
        elif choice == '6':
            exit()
            break
        
        else:
            print("Invalid choice, please try again.")
main()
