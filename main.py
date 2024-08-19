from pypresence import Presence
import time
import os
import re
import pathlib
import psutil
import json

with open("config.json", "r") as f: # Loads config.json 
    config = json.load(f)


app_id = config.get("appId") # Extract AppId

if __name__ == "__main__":
    print(f"Using AppId: {app_id}")
 
RPC = Presence(client_id=app_id)

def is_process_running(process_name): # Checks if VMware is running.
    for proc in psutil.process_iter(['name']):
        if proc.info['name'] and proc.info['name'].lower() == process_name.lower():
            return True
    return False

def update_presence():
    vmInfoPre = os.popen('vmrun list').read().strip()  # Check VM status for total count.
    vmInfoMatch = re.search(r'Total running VMs: \d+', vmInfoPre)  # Get the number of VMs running.
    
    if vmInfoMatch:
        vmInfo = vmInfoMatch.group(0)
    else:
        vmInfo = "Cannot determine VM count!"
    
    vmPaths = re.findall(r'^[^\s].*\.vmx$', vmInfoPre, re.MULTILINE)  # Get VM path for name
    vmFolders = set(Path(path).parent.name for path in vmPaths)  # Extract folder names from VM paths

    if vmFolders:
        vmInfoDirs = "\n" + "\n" + ", ".join(vmFolders)
    else:
        vmInfoDirs = "Cannot determine VM name!" # fallback
    
    if vmInfo == "Total running VMs: 0":
        RPC.update(
            large_image="vmware",
            large_text="VMware Workstation Pro 17",
            details="No VMs running on host."
        )  # Set the presence for no running VMs.
    else:
        RPC.update(
            large_image="vmware",
            large_text="VMware Workstation Pro 17",
            small_image="play",
            small_text="VM(s) are running",
            state=vmInfoDirs,
            details=vmInfo
        )  # Update if VMs are running.

if __name__ == "__main__":
    connected = False
    while True:
        if is_process_running("vmware"):
            if not connected:
                print("VMware detected, connecting to discord RPC.") # connects do discord if VMware process is started
                RPC.connect()
                connected = True
            update_presence()
        else:
            if connected:
                print("VMware stopped running, dropping connection.") # Drops connection when VMware is closed.
                RPC.close()
                connected = False
            else:
                print("VMware seems to not be running. Rechecking in 15 seconds.")
        
        time.sleep(15)  # Wait for 15 seconds before checking again. This is a limitation by discord.
