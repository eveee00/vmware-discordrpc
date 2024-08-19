
# vmware-discordrpc
[![pypresence](https://img.shields.io/badge/using-pypresence-00bb88.svg?style=for-the-badge&logo=discord&logoWidth=20)](https://github.com/qwertyquerty/pypresence)

A Discord rich presence for VMware written in python.

*Note: this is still very early in development. There is still some stuff missing. (ex. Windows support)*
## Requirements

    pathlib, pypresence, psutil

## How to install
Clone the repo	

    git clone https://github.com/veeeeeeee00/vmware-discordrpc.git

  Change directory

     cd vmware-discordrpc

Install requirements

    pip install -r requirements.txt

Edit  `main.py` to include your app ID. You can get one [here.](https://discord.com/developers/)

     [...]
     client_id =  "enter_client_id"  # Enter your Application ID here.
     [...]

Upload both .png files from the `assets` folder here

    https://discord.com/developers/applications/[your-application-id]/rich-presence/assets

Run file

    python main.py

Enjoy!

## TODO

 - [ ] Windows support
 - [x] External settings file
 - [x] Turning rich presence off when the vmware process isn't running
 ## Contributing
 PRs are welcome.
