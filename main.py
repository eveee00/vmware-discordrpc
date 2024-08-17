from pypresence import Presence
import time
import os
import re
from pathlib import Path

client_id = "enter_client_id"  # Enter your Application ID here.
RPC = Presence(client_id=client_id)
RPC.connect()

while True:
    vmInfoPre = os.popen('vmrun list').read().strip()  # Check VM status fot total count.
    vmInfoMatch = re.search(r'Total running VMs: \d+', vmInfoPre) # Get the number of VMs running.
    # Check if vm count fails
    if vmInfoMatch:
        vmInfo = vmInfoMatch.group(0)
    else:
        vmInfo = "Cannot determine VM count!"
    vmPaths = re.findall(r'^[^\s].*\.vmx$', vmInfoPre, re.MULTILINE) # Get VM path for name
    # Extract folder names from VM paths
    vmFolders = set(Path(path).parent.name for path in vmPaths)

    # Prepare folder names as a single string
    if vmFolders:
        vmInfoDirs = "\n" + "\n" + ", ".join(vmFolders)
    else:
        vmInfoDirs = "No VM folders available"
    
    # Update presence based on the number of running VMs
    if vmInfo == "Total running VMs: 0":
        RPC.update(large_image="vmware_workstation_16_icon_svg", large_text="VMware Workstation Pro 17", state="*Imagine something here.*", details="No VMs running on host")  # Set the presence for no running vms.
    else:
        RPC.update(large_image="vmware_workstation_16_icon_svg", large_text="VMware Workstation Pro 17", small_image="play", small_text="VM(s) are running", state= vmInfoDirs, details= vmInfo)  # Update if VMs are running.

    time.sleep(15)  # Wait for 15 seconds before checking again, this is a limitation by discord.
