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
        'ubuntu-server': 'https://releases.ubuntu.com/25.04/ubuntu-25.04-live-server-amd64.iso',
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
        'debian': 'https://cdimage.debian.org/debian-cd/current/amd64/iso-dvd/debian-13.0.0-amd64-DVD-1.iso',
        'fedora': 'https://download.fedoraproject.org/pub/fedora/linux/releases/42/Workstation/x86_64/iso/Fedora-Workstation-Live-42-1.1.x86_64.iso',
        'fedora-everything': 'https://download.fedoraproject.org/pub/fedora/linux/releases/42/Everything/x86_64/iso/Fedora-Everything-netinst-x86_64-42-1.1.iso',
        'fedora-kde': 'https://download.fedoraproject.org/pub/fedora/linux/releases/42/KDE/x86_64/iso/Fedora-KDE-Desktop-Live-42-1.1.x86_64.iso',
        'fedora-server': 'https://download.fedoraproject.org/pub/fedora/linux/releases/42/Server/x86_64/iso/Fedora-Server-dvd-x86_64-42-1.1.iso',
        'fedora-server-netinst': 'https://download.fedoraproject.org/pub/fedora/linux/releases/42/Server/x86_64/iso/Fedora-Server-netinst-x86_64-42-1.1.iso',
        'fedora-coreos': 'https://builds.coreos.fedoraproject.org/prod/streams/stable/builds/42.20250721.3.0/x86_64/fedora-coreos-42.20250721.3.0-live-iso.x86_64.iso',
        'fedora-silverblue': 'https://builds.coreos.fedoraproject.org/prod/streams/stable/builds/42.20250721.3.0/aarch64/fedora-coreos-42.20250721.3.0-live-iso.aarch64.iso',
        'fedora-kinoite': 'https://download.fedoraproject.org/pub/fedora/linux/releases/42/Kinoite/x86_64/iso/Fedora-Kinoite-ostree-x86_64-42-1.1.iso',
        'fedora-sway-atomic': 'https://download.fedoraproject.org/pub/fedora/linux/releases/42/Sericea/x86_64/iso/Fedora-Sericea-ostree-x86_64-42-1.1.iso',
        'fedora-budgie-atomic': 'https://download.fedoraproject.org/pub/fedora/linux/releases/42/Onyx/x86_64/iso/Fedora-Onyx-ostree-x86_64-42-1.1.iso',
        'fedora-cosmic-atomic': 'https://download.fedoraproject.org/pub/fedora/linux/releases/42/COSMIC-Atomic/x86_64/iso/Fedora-COSMIC-Atomic-ostree-x86_64-42-1.1.iso',
        'fedora-iot': 'https://download.fedoraproject.org/pub/alt/iot/42/IoT/x86_64/iso/Fedora-IoT-ostree-42-20250724.1.x86_64.iso',
        'fedora-xfce': 'https://download.fedoraproject.org/pub/fedora/linux/releases/42/Spins/x86_64/iso/Fedora-Xfce-Live-42-1.1.x86_64.iso',
        'fedora-cinnamon': 'https://download.fedoraproject.org/pub/fedora/linux/releases/42/Spins/x86_64/iso/Fedora-Cinnamon-Live-x86_64-42-1.1.iso',
        'fedora-mate-compiz': 'https://download.fedoraproject.org/pub/fedora/linux/releases/42/Spins/x86_64/iso/Fedora-MATE_Compiz-Live-x86_64-42-1.1.iso',
        'fedora-i3': 'https://download.fedoraproject.org/pub/fedora/linux/releases/42/Spins/x86_64/iso/Fedora-i3-Live-x86_64-42-1.1.iso',
        'fedora-lxqt': 'https://download.fedoraproject.org/pub/fedora/linux/releases/42/Spins/x86_64/iso/Fedora-LXQt-Live-42-1.1.x86_64.iso',
        'fedora-lxde': 'https://download.fedoraproject.org/pub/fedora/linux/releases/42/Spins/x86_64/iso/Fedora-LXDE-Live-x86_64-42-1.1.iso',
        'linux-mint': 'https://pub.linuxmint.io/stable/22.1/linuxmint-22.1-cinnamon-64bit.iso',
        'linux-mint-xfce': 'https://pub.linuxmint.io/stable/22.1/linuxmint-22.1-xfce-64bit.iso',
        'linux-mint-mate': 'https://pub.linuxmint.io/stable/22.1/linuxmint-22.1-mate-64bit.iso',
        'kali': 'https://cdimage.kali.org/kali-2025.2/kali-linux-2025.2-installer-amd64.iso',
        'kali-netinst': 'https://cdimage.kali.org/kali-2025.2/kali-linux-2025.2-installer-netinst-amd64.iso',
        'manjaro-kde': 'https://download.manjaro.org/kde/25.0.7/manjaro-kde-25.0.7-250812-linux612.iso',
        'manjaro-xfce': 'https://download.manjaro.org/xfce/25.0.7/manjaro-xfce-25.0.7-250812-linux612.iso',
        'manjaro-gnome': 'https://download.manjaro.org/gnome/25.0.7/manjaro-gnome-25.0.7-250812-linux612.iso',
        'manjaro-cinnamon': 'https://download.manjaro.org/cinnamon/25.0.3/manjaro-cinnamon-25.0.3-250609-linux612.iso',
        'manjaro-i3': 'https://download.manjaro.org/i3/25.0.3/manjaro-i3-25.0.3-250609-linux612.iso',
        'manjaro-sway': 'https://manjaro-sway.download/download?file=manjaro-sway-25.0.0-250817-linux612.iso',
        'opensuse-tumbleweed-netinst': 'https://download.opensuse.org/tumbleweed/iso/openSUSE-Tumbleweed-NET-x86_64-Current.iso',
        'opensuse-tumbleweed': 'https://download.opensuse.org/tumbleweed/iso/openSUSE-Tumbleweed-DVD-x86_64-Current.iso',
        'opensuse-leaf-netinst': 'https://download.opensuse.org/distribution/leap/15.6/iso/openSUSE-Leap-15.6-NET-x86_64-Media.iso',
        'opensuse-leaf': 'https://download.opensuse.org/distribution/leap/15.6/iso/openSUSE-Leap-15.6-DVD-x86_64-Media.iso',
        'tails': 'https://download.tails.net/tails/stable/tails-amd64-6.18/tails-amd64-6.18.img',
        'mx-xfce': 'https://cytranet-dal.dl.sourceforge.net/project/mx-linux/Final/Xfce/MX-23.6_x64.iso',
        'mx-kde': 'https://pilotfiber.dl.sourceforge.net/project/mx-linux/Final/KDE/MX-23.6.1_KDE_x64.iso',
        'mx-fluxbox': 'https://netactuate.dl.sourceforge.net/project/mx-linux/Final/Fluxbox/MX-23.6_fluxbox_x64.iso',
        'centos-stream': 'https://mirror.cpsc.ucalgary.ca/mirror/centos-stream/10-stream/BaseOS/x86_64/iso/CentOS-Stream-10-latest-x86_64-dvd1.iso',
        'zorin-os': 'https://mirror.umd.edu/zorin/17/Zorin-OS-17.3-Core-64-bit-r2.iso',
    },
    'arm64': {
        'arch-linux': 'http://os.archlinuxarm.org/os/ArchLinuxARM-aarch64-latest.tar.gz',
        'ubuntu': 'https://cdimage.ubuntu.com/releases/25.04/release/ubuntu-25.04-desktop-arm64.iso',
        'edubuntu-rpi': 'https://cdimages.ubuntu.com/edubuntu/releases/25.04/release/edubuntu-25.04-preinstalled-desktop-arm64+raspi.img.xz',
        'debian-netinst': 'https://d-i.debian.org/daily-images/arm64/20250803-01:22/netboot/mini.iso',
        'fedora': 'https://download.fedoraproject.org/pub/fedora/linux/releases/42/Workstation/aarch64/iso/Fedora-Workstation-Live-42-1.1.aarch64.iso',
        'fedora-server': 'https://download.fedoraproject.org/pub/fedora/linux/releases/42/Server/aarch64/iso/Fedora-Server-dvd-aarch64-42-1.1.iso',
        'fedora-server-netinst': 'https://download.fedoraproject.org/pub/fedora/linux/releases/42/Server/aarch64/iso/Fedora-Server-netinst-aarch64-42-1.1.iso',
        'fedora-everything': 'https://download.fedoraproject.org/pub/fedora/linux/releases/42/Everything/aarch64/iso/Fedora-Everything-netinst-aarch64-42-1.1.iso',
        'fedora-minimal': 'https://download.fedoraproject.org/pub/fedora-secondary/releases/42/Spins/aarch64/images/Fedora-Minimal-42-1.1.aarch64.raw.xz',
        'fedora-kde': 'https://download.fedoraproject.org/pub/fedora/linux/releases/42/KDE/aarch64/iso/Fedora-KDE-Desktop-Live-42-1.1.aarch64.iso', 
        'fedora-coreos': 'https://builds.coreos.fedoraproject.org/prod/streams/stable/builds/42.20250721.3.0/aarch64/fedora-coreos-42.20250721.3.0-live-iso.aarch64.iso',
        'fedora-silverblue': 'https://download.fedoraproject.org/pub/fedora/linux/releases/42/Silverblue/aarch64/iso/Fedora-Silverblue-ostree-aarch64-42-1.1.iso',
        'fedora-kinoite': 'https://download.fedoraproject.org/pub/fedora/linux/releases/42/Kinoite/aarch64/iso/Fedora-Kinoite-ostree-aarch64-42-1.1.iso',
        'fedora-cosmic-atomic': 'https://download.fedoraproject.org/pub/fedora/linux/releases/42/COSMIC-Atomic/aarch64/iso/Fedora-COSMIC-Atomic-ostree-aarch64-42-1.1.iso',
        'fedora-iot': 'https://download.fedoraproject.org/pub/alt/iot/42/IoT/aarch64/iso/Fedora-IoT-ostree-42-20250724.1.aarch64.iso',
        'fedora-xfce': 'https://download.fedoraproject.org/pub/fedora/linux/releases/42/Spins/aarch64/iso/Fedora-Xfce-Live-42-1.1.aarch64.iso',
        'fedora-i3': 'https://download.fedoraproject.org/pub/fedora/linux/releases/42/Spins/aarch64/iso/Fedora-i3-Live-aarch64-42-1.1.iso',
        'fedora-lxqt': 'https://download.fedoraproject.org/pub/fedora/linux/releases/42/Spins/aarch64/iso/Fedora-LXQt-Live-42-1.1.aarch64.iso',
        'opensuse-tumbleweed-netinst': 'https://download.opensuse.org/ports/aarch64/tumbleweed/iso/openSUSE-Tumbleweed-NET-aarch64-Current.iso',
        'opensuse-tumbleweed': 'https://download.opensuse.org/ports/aarch64/tumbleweed/iso/openSUSE-Tumbleweed-DVD-aarch64-Current.iso',
        'opensuse-leaf-netinst': 'https://download.opensuse.org/distribution/leap/15.6/iso/openSUSE-Leap-15.6-NET-aarch64-Media.iso',
        'opensuse-leaf': 'https://download.opensuse.org/distribution/leap/15.6/iso/openSUSE-Leap-15.6-DVD-aarch64-Media.iso',
        'centos-stream': 'https://mirrors.centos.org/mirrorlist?path=/10-stream/BaseOS/aarch64/iso/CentOS-Stream-10-latest-aarch64-dvd1.iso',
        'kali': 'https://cdimage.kali.org/kali-2025.2/kali-linux-2025.2-installer-arm64.iso',
        'kali-netinst': 'https://cdimage.kali.org/kali-2025.2/kali-linux-2025.2-installer-netinst-arm64.iso',
        'kali-rpi-2-5': 'https://kali.download/arm-images/kali-2025.2/kali-linux-2025.2-raspberry-pi-arm64.img.xz',
        'kali-rpi-0-2': 'https://kali.download/arm-images/kali-2025.2/kali-linux-2025.2-raspberry-pi-zero-2-w-armhf.img.xz',
        'kali-pine64': 'https://kali.download/arm-images/kali-2025.2/kali-linux-2025.2-pinebook-arm64.img.xz',
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
