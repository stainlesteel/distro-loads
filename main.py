import requests
import progressbar
import argparse

par = argparse.ArgumentParser(prog='distro-load', description='Download system distributions from sh.')
sub_par = par.add_subparsers(dest="command", help="The command you want to use")
dis_par = sub_par.add_parser('distro', help='Download an available distro')
dis_par.add_argument('distribution', help="Distro name")
dis_par.add_argument('arch', help="The architectures you want to download for")
ls_par = sub_par.add_parser('ls', help='List available distros')
ls_par.add_argument('arch', choices=['x86-64', 'arm64'] ,help="architecture")
args = par.parse_args()

headers = {
    "User-Agent": 'Mozilla/5.0 (X11; Linux x86_64; rv:141.0) Gecko/20100101 Firefox/141.0',
    "Accept-Language": "en-US,en;q=0.5"
}

distros = {
    'x86-64': {
        'arch-linux': 'https://geo.mirror.pkgbuild.com/iso/2025.08.01/archlinux-x86_64.iso',
        'ubuntu': 'https://releases.ubuntu.com/25.04/ubuntu-25.04-desktop-amd64.iso',
        'edubuntu': 'https://cdimages.ubuntu.com/edubuntu/releases/25.04/release/edubuntu-25.04-desktop-amd64.iso',
        'kubuntu': 'https://cdimage.ubuntu.com/kubuntu/releases/25.04/release/kubuntu-25.04-desktop-amd64.iso',
        'lubuntu': 'https://cdimage.ubuntu.com/lubuntu/releases/25.04/release/lubuntu-25.04-desktop-amd64.iso',
        'ubuntu-budgie': 'https://cdimage.ubuntu.com/ubuntu-budgie/releases/25.04/release/ubuntu-budgie-25.04-desktop-amd64.iso',
        'ubuntu-cinnamon': 'https://cdimage.ubuntu.com/ubuntucinnamon/releases/plucky/release/ubuntucinnamon-25.04-desktop-amd64.iso',
        'ubuntu-kylin': 'https://cdimage.ubuntu.com/ubuntukylin/releases/25.04/release/ubuntukylin-25.04-desktop-amd64.iso',
        'ubuntu-mate': 'https://cdimage.ubuntu.com/ubuntu-mate/releases/25.04/release/ubuntu-mate-25.04-desktop-amd64.iso',
        'ubuntu-studio': 'https://cdimage.ubuntu.com/ubuntustudio/releases/plucky/release/ubuntustudio-25.04-desktop-amd64.iso',
        'ubuntu-unity': 'https://cdimage.ubuntu.com/ubuntu-unity/releases/plucky/release/ubuntu-unity-25.04-desktop-amd64.iso',
        'xubuntu': 'https://mirror.us.leaseweb.net/ubuntu-cdimage/xubuntu/releases/24.04/release/xubuntu-24.04.3-desktop-amd64.iso',
        'debian-netinst': 'https://cdimage.debian.org/debian-cd/current/amd64/iso-cd/debian-13.0.0-amd64-netinst.iso',
        'debian-full': 'https://cdimage.debian.org/debian-cd/current/amd64/iso-dvd/debian-13.0.0-amd64-DVD-1.iso',
        'fedora': 'https://download.fedoraproject.org/pub/fedora/linux/releases/42/Workstation/x86_64/iso/Fedora-Workstation-Live-42-1.1.x86_64.iso',
        'fedora-everything': 'https://download.fedoraproject.org/pub/fedora/linux/releases/42/Everything/x86_64/iso/Fedora-Everything-netinst-x86_64-42-1.1.iso',
        'linux-mint': 'https://pub.linuxmint.io/stable/22.1/linuxmint-22.1-cinnamon-64bit.iso',
        'linux-mint-xfce': 'https://pub.linuxmint.io/stable/22.1/linuxmint-22.1-xfce-64bit.iso',
        'linux-mint-mate': 'https://pub.linuxmint.io/stable/22.1/linuxmint-22.1-mate-64bit.iso'
    },
    'arm64': {
        'arch-linux': 'http://os.archlinuxarm.org/os/ArchLinuxARM-aarch64-latest.tar.gz',
        'ubuntu': 'https://cdimage.ubuntu.com/releases/25.04/release/ubuntu-25.04-desktop-arm64.iso',
        'edubuntu-rpi': 'https://cdimages.ubuntu.com/edubuntu/releases/25.04/release/edubuntu-25.04-preinstalled-desktop-arm64+raspi.img.xz',
        'debian-netinst': 'https://d-i.debian.org/daily-images/arm64/20250803-01:22/netboot/mini.iso',
        'fedora': 'https://download.fedoraproject.org/pub/fedora/linux/releases/42/Workstation/aarch64/iso/Fedora-Workstation-Live-42-1.1.aarch64.iso',

    }
}

def downs(url):
    try:
       fname = url.split('/')[-1]
       print(fname)
       with requests.get(url, stream=True, headers=headers) as req:
           req.raise_for_status()
           bytes = 0
           with open(fname, 'wb') as feq:
               bar = progressbar.ProgressBar(widgets=[
                     progressbar.FileTransferSpeed(unit="Mb"), ' ',
                     progressbar.Counter(), 'MBs',
                     progressbar.ETA(),
                     progressbar.Bar()
               ])
               for chunk in req.iter_content(chunk_size=1500000):
                   bytes += 1500000
                   mbs = bytes / 1500000
                   feq.write(chunk)
                   bar.update(mbs)
           print('Done.')
    except requests.exceptions.ConnectionError as err:
        print("Failed to download iso, error with connection")
        raise SystemExit(err)
    except requests.exceptions.HTTPError as err:
        print("Failed to download iso, HTTPError (error with url, endpoint server, .etc.")
        raise SystemExit(err)
             
try:
    if args.command == 'distro':
        try:
          distro = distros[f'{args.arch}'][f'{args.distribution}']
    
          downs(distro)
        except KeyError:
            if args.arch != 'x86-64' or 'arm64':
                print("You are using an invalid structure for the arguments.")
                print("Correct Structure: distro-load distro {distribution} {arch}")
            else:
                print("Distro not found. For specific architectures, some distros may not be available.")
    elif args.command == 'ls':
        print(f"These are the distributions available for the {args.arch} arch.")
        for distro in distros[f'{args.arch}']:
            print(distro)
except KeyboardInterrupt:
    raise SystemExit("\n Exited.")
