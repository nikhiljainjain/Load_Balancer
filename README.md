# Load_Balancer
Performance comparsion of different load balancing algorthims.

## Software Requirements
 - Linux or Windows
 - Nginx
 - Python3
 - Nodejs

## Start this project
_Step 1_: Go to server folder and install all the dependecies using command `npm install` 

_Step 2_: Install *LoadTest* package using `npm i -g loadtest`.<br>
This package is use to test the load capcity of different server (here we are test different load balancing algorithm.)

_Step 3_: Install *nginx* in your system, using command `sudo apt-get install -y nginx`.<br> 
(Only required in *Linux* system, files for windows availables in windows. Not need to install nginx in Windows OS).

_Step 4_: (Only for linux users) After nginx installation, run `sudo chown -R $USER:$USER /etc/nginx` on terminal. This command will change the owner and make project smoothly run.

_Step 5_: Start a certain number of servers present in server folder.<br>
Check the *package.json* file inside server folder to available commands to start servers.

_Step 6_: Come back to main folder and run `python3 menu.py`(For Linux) and `python3 windows/menu.py` (For Windows).
Menu will open and you ask the value base on the input. This project will test loading capcaity. Result will store in log folder.Sample output already present in the log. You can check it out anytime and load balancer use *Port 80*

## File Structure

<pre><font color="#3465A4"><b>Load_Balancer/</b></font>
├── LICENSE
├── <font color="#3465A4"><b>log (Save the result of load balancing capcaity of algo by their name.)</b></font>
│   ├── ip-hash.txt
│   ├── least-conn.txt
│   └── round-robin.txt
├── menu.py
├── <font color="#3465A4"><b>nginx (Config file present for each algo used to switch on different algo.)</b></font>
│   ├── ip-hash.conf
│   ├── least-conn.conf
│   └── round-robin.conf
├── README.md
├── <font color="#3465A4"><b>server (Basic expressjs based server code)</b></font>
│   ├── app.js
│   ├── <font color="#3465A4"><b>bin</b></font>
│   │   └── <font color="#4E9A06"><b>www</b></font>
│   ├── package.json
│   └── package-lock.json
└── <font color="#3465A4"><b>windows</b></font>
    ├── menu.py
    └── <font color="#3465A4"><b>nginx (Nginx files to run this project)</b></font>
        ├── <font color="#3465A4"><b>conf</b></font>
        │   ├── fastcgi.conf
        │   ├── fastcgi_params
        │   ├── koi-utf
        │   ├── koi-win
        │   ├── mime.types
        │   ├── nginx.conf
        │   ├── nginx - Copy.conf
        │   ├── project.mrx.com.conf
        │   ├── scgi_params
        │   ├── uwsgi_params
        │   └── win-utf
        ├── <font color="#3465A4"><b>contrib</b></font>
        │   ├── geo2nginx.pl
        │   ├── README
        │   ├── <font color="#3465A4"><b>unicode2nginx</b></font>
        │   │   ├── koi-utf
        │   │   ├── unicode-to-nginx.pl
        │   │   └── win-utf
        │   └── <font color="#3465A4"><b>vim</b></font>
        │       ├── <font color="#3465A4"><b>ftdetect</b></font>
        │       │   └── nginx.vim
        │       ├── <font color="#3465A4"><b>ftplugin</b></font>
        │       │   └── nginx.vim
        │       ├── <font color="#3465A4"><b>indent</b></font>
        │       │   └── nginx.vim
        │       └── <font color="#3465A4"><b>syntax</b></font>
        │           └── nginx.vim
        ├── <font color="#3465A4"><b>docs</b></font>
        │   ├── CHANGES
        │   ├── CHANGES.ru
        │   ├── LICENSE
        │   ├── OpenSSL.LICENSE
        │   ├── PCRE.LICENCE
        │   ├── README
        │   └── zlib.LICENSE
        ├── <font color="#3465A4"><b>html</b></font>
        │   ├── 50x.html
        │   └── index.html
        └── nginx.exe
</pre>

### Thanks
 - Jatin Grover (For Guidance)
 - Vayuj (For Idea)

