import re

password = input()

regxs = [r'[a-z]',r'[0-9]',r'[A-Z]', r'[S#@]']

def check_low(password):

    checks = []

    password = password.rstrip()
    if len(password) <= 12 and len(password) >= 6:
        for regx in regxs:
            
            if re.findall(pattern=regx,string=password):
                checks.append(True)
            else:
                checks.append(False)

        if all(checks):
            return True
        else:
            return False

    else:
        return False

print(check_low(password))


