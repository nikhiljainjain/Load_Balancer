# importing the module 
import os 

# sets the text colour to green 
#os.system("tput setaf 2") 

print("Launching Terminal User Interface") 

# sets the text color to red 
#os.system("tput setaf 1") 

print("\t\tWELCOME TO Terminal User Interface\t\t\t") 

# sets the text color to white 
#os.system("tput setaf 7") 

print("\t-------------------------------------------------") 
print("Entering local device\nMade by Nikhil Jain\n") 

def copy_nginx_algo_config(config_file):
	os.system(("copy ../nginx/"+config_file+".conf ./nginx/conf/nginx.conf"))
	os.system("start ./nginx/nginx.exe")
	print("Processing......")
	os.system("loadtest http://localhost:80/ -t 20 -c 100 --rps 1000 -n 200000 > ../log/"+config_file+".txt")

while True: 
	os.system("cls")
	print(""" 
		1. Start IP Hash Algorithm 
		2. Start Round Robin Algorithm
		3. Start Least Connection Algorithm
		4. Exit""") 

	ch=int(input("Enter your choice: ")) 

	if(ch == 1): 
		copy_nginx_algo_config("ip-hash")

	elif ch == 2: 
		copy_nginx_algo_config("round-robin")

	elif ch == 3: 
		copy_nginx_algo_config("least-conn") 

	elif ch == 4: 
		print("Exiting application") 
		exit() 
	else: 
		print("Invalid entry") 

	input("Press enter to continue")  
