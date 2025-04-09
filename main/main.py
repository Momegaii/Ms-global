
from yt import *
from sc import *
from inst import *
import logging



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

def exit():
    print ("Bye ! solid ")

def main():
    
    while True:
        print("1. Upload")

        print("2. Exit")

        choice = input("Enter your choice: ")

        
        elif choice == '1':
            upload()
        
        
        elif choice == '2':
            exit()
            break
        
        else:
            print("Invalid choice, please try again.")
main()
