# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

n = int(input())
for i in range(n):
    num = input()
    checking16digits = re.match(r"^[456]\d{15}$", num)
    checkingformat = re.match(r"^[456]\d{3}\-\d{4}-\d{4}-\d{4}$", num)
    checkingforspecials = re.match(r"(?!.*(\d)(-?\1){3})", (num.replace("-", "")))
    if (bool(checking16digits) or bool(checkingformat)) and bool(checkingforspecials):
        print("Valid")
    else:
        print("Invalid")
        
