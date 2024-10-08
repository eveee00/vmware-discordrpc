
# vmware-discordrpc
[![pypresence](https://img.shields.io/badge/using-pypresence-00bb88.svg?style=for-the-badge&logo=discord&logoWidth=20)](https://github.com/qwertyquerty/pypresence)

A Discord rich presence for VMware written in python.

*Note: this is still in development. There is still some stuff missing.*
## Requirements

    pathlib, pypresence, psutil

## How to install
Clone the repo	

    git clone https://github.com/veeeeeeee00/vmware-discordrpc.git

  Change directory

     cd vmware-discordrpc

Install requirements

    pip install -r requirements.txt

Edit  `config.json` to include your app ID. You can get one [here.](https://discord.com/developers/)

    {
    "appId": "enter_discord_appid_here"
    }

Upload both .png files from the `assets` folder here

    https://discord.com/developers/applications/[your-application-id]/rich-presence/assets

Run file

    python main.py



## Autostart on logon (KDE)

Copy this basic `startrpc.sh` and customize it

    #!/bin/bash
    cd /path/to/vmware-discordrpc
    python main.py

OPTIONAL: in case you used a venv to install the dependencies, you have to activate it first. Use this sample instead

    #!/bin/bash
    cd /path/to/vmware-discordrpc
    source venv/bin/activate
    python main.py

Save it in a .sh script with the name of your choice

Put it in your autostart

    KDE Settings > Autostart > Add... > Add Login Script > find and pick the script

Enjoy!

## TODO

 - [x] Windows support
 - [x] External settings file
 - [x] Turning rich presence off when the vmware process isn't running
 ## Contributing
 PRs are welcome.
