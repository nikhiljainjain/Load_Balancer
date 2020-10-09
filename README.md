# Load_Balancer
Performance comparsion of different load balancing algorthims. Commands used in this project are based on Ubuntu OS.

## Software Requirements
 - Linux OS
 - Nginx
 - Python3
 - Nodejs

## Start this project
_Step 1_: Go to server folder and install all the dependecies using command `npm install` 

_Step 2_: Install *LoadTest* package using `npm i -g loadtest`.<br>
This package is use to test the load capcity of different server (here we are test different load balancing algorithm.)

_Step 3_: Install *nginx* in your system.

_Step 4_: (Only for linux users) After nginx installation, run `sudo chown -R $USER:$USER /etc/nginx` on terminal. This command will change the owner and make project smoothly run.

_Step 5_: Start a certain number of servers present in server folder.<br>
Check the *package.json* file inside server folder to available commands to start servers.

_Step 6_: Come back to main folder and run `python3 menu.py`(For Linux) and `python3 windows/menu.py` (For Windows).
Menu will open and you ask the value base on the input. This project will test loading capcaity. Result will store in log folder.Sample output already present in the log. You can check it out anytime and load balancer use *Port 80*

## File Structure

<pre><font color="#3465A4"><b>Load_Balancer/</b></font>
├── LICENSE
├── <font color="#3465A4"><b>log (save the result of load balancing capcaity of algo by their name.)</b></font>
│   ├── ip-hash.txt
│   ├── least-conn.txt
│   └── round-robin.txt
├── menu.py
├── <font color="#3465A4"><b>nginx (config file present for each algo used to switch on different algo.)</b></font>
│   ├── ip-hash.conf
│   ├── least-conn.conf
│   └── round-robin.conf
├── README.md
└── <font color="#3465A4"><b>server (basic expressjs based server code)</b></font>
    ├── app.js
    ├── <font color="#3465A4"><b>bin</b></font>
    │   └── <font color="#4E9A06"><b>www</b></font>
    ├── package.json
    └── package-lock.json
</pre>

### Thanks
 - Jatin Grover (For Guidance)
 - Vayuj (For Idea)

