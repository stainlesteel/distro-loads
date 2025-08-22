# distro-loads
A command-line interface to download ISOs for x86-64 or arm64/aarch64.

## Features
- Download over 50+ distros from the command line.
- List available distros for your architecture.
- Netboot, Server, and Minimal distros available when provided by the distro site.
## Distro List
Some distros and vartiations of them, this is the total for x86-64.
- Arch Linux  
- Ubuntu (edubuntu, lubuntu, budgie, cinnamon, .etc)
- Debian   
- Fedora (KDE, Server, Core, Kinoite, Sway, XFCE, .etc)
- Linux Mint (Cinnamon, XFCE, MATE)
- Kali Linux  
- Manjaro (KDE, XFCE, GNOME)
- OpenSUSE (Tumbleweed, Leaf)
- Tails OS
- MX Linux (XFCE, KDE, Fluxbox)
- CentOS  
- ZorinOS 
- EndeavourOS 
- PopOS (Normal, Nvidia) 
- Elementary OS 
- Antix Linux
- Apline Linux
- Alma Linux
- CachyOS (Normal, Handheld)
- Puppy Linux (Bookworm, F96)
## Install  
### Python3.x
You can run this as a portable python app (not recommended).
1. Install repository contents.
2. Install package requirements via `python3 -m pip install -r requc.txt`
3. Run the .py file, Windows: `python main.py`, MacOS/Linux: `python3 main.py`
### RPM (RHEL-based distros)
An RPM is available in the Releases tab.
To install, run:
```bash
dnf install distro-loads-1.0-1.fc42.x8_64.rpm 
```
### Generic Linux (x86-64)
Another binary is available to be used portablly for any Linux distro, in the Releases tab.
## Usage
This is a command-line tool, as such you type in commands along with required arguments.

### Commands:

#### distro
lets you download a distro
```bash
distro-loads distro {DISTRO_NAME} {ARCH}  # example: distro debian x86-64
```

#### ls
list the distros for your architecture.
```bash
distro-loads ls {ARCH} # example ls arm64
```


