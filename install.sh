#!/bin/bash

#            ---------------------------------------------------
#                           Arissploit Framework                                 
#            ---------------------------------------------------
#                Copyright (C) <2019-2020>  <Entynetproject>
#
#        This program is free software: you can redistribute it and/or modify
#        it under the terms of the GNU General Public License as published by
#        the Free Software Foundation, either version 3 of the License, or
#        any later version.
#
#        This program is distributed in the hope that it will be useful,
#        but WITHOUT ANY WARRANTY; without even the implied warranty of
#        MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#        GNU General Public License for more details.
#
#        You should have received a copy of the GNU General Public License
#        along with this program.  If not, see <http://www.gnu.org/licenses/>.

BS="\033[1;34m"
RS="\033[1;31m"
YS="\033[1;33m"
GNS="\033[1;32m"
CE="\033[0m"

printf '\033]2;install.sh\a'

if [[ $EUID -ne 0 ]]
then
   echo -e "["$RS"err"$CE"] This script must be run as root!"$CE""
   exit
fi

{
ASESR="$(ping -c 1 -q www.google.com >&/dev/null; echo $?)"
} &> /dev/null
if [[ "$ASESR" != 0 ]]
then 
   echo -e "["$RS"err"$CE"] No Internet connection!"$CE""
   exit
fi

sleep 0.5
clear
sleep 0.5
echo
cat banner/banner.txt
echo

sleep 1
echo -e "["$BS"inf"$CE"] Installing dependencies..."
sleep 1

{
pkg update
pkg -y install git
pkg -y install python
pkg -y install wget
pkg -y install perl
pkg -y install libany-uri-escape-perl
pkg -y install libhtml-html5-entities-perl
pkg -y install libhtml-entities-numbered-perl
pkg -y install libhtml-parser-perl
pkg -y install libwww-perl
pkg -y install php
pkg -y install libdnet
pkg -y install ethtool
pkg -y install aircrack-ng
pkg -y install ettercap-text-only
pkg -y install dsniff
pkg -y install xterm
pkg -y install driftnet
pkg -y install tcpdump
pkg -y install libnetfilter-queue-dev
pkg -y install hcitool
pkg -y install sslstrip
pkg -y install l2ping
apt-get update
apt-get -y install git
apt-get -y install python3
apt-get -y install python3-pip
apt-get -y install wget
apt-get -y install perl
apt-get -y install libany-uri-escape-perl
apt-get -y install libhtml-html5-entities-perl
apt-get -y install libhtml-entities-numbered-perl
apt-get -y install libhtml-parser-perl
apt-get -y install libwww-perl
apt-get -y install php
apt-get -y install libdnet
apt-get -y install ethtool
apt-get -y install aircrack-ng
apt-get -y install ettercap-text-only
apt-get -y install dsniff
apt-get -y install xterm
apt-get -y install driftnet
apt-get -y install tcpdump
apt-get -y install libnetfilter-queue-dev
apt-get -y install python3-dev
apt-get -y install hcitool
apt-get -y install sslstrip
apt-get -y install l2ping
apk update
apk add git
apk add python3
apk add py3-pip
apk add wget
apk add perl
apk add libany-uri-escape-perl
apk add libhtml-html5-entities-perl
apk add libhtml-entities-numbered-perl
apk add libhtml-parser-perl
apk add libwww-perl
apk add php
apk add install libdnet
apk add ethtool
apk add aircrack-ng
apk add ettercap-text-only
apk add dsniff
apk add xterm
apk add driftnet
apk add tcpdump
apk add libnetfilter-queue-dev
apk add python3-dev
apk add hcitool
apk add sslstrip
apk add l2ping
pacman -Sy
pacman -S --noconfirm git
pacman -S --noconfirm python3
pacman -S --noconfirm python-pip
pacman -S --noconfirm wget
pacman -S --noconfirm perl
pacman -S --noconfirm libany-uri-escape-perl
pacman -S --noconfirm libhtml-html5-entities-perl
pacman -S --noconfirm libhtml-entities-numbered-perl
pacman -S --noconfirm libhtml-parser-perl
pacman -S --noconfirm libwww-perl
pacman -S --noconfirm php
pacman -S --noconfirm libdnet
pacman -S --noconfirm ethtool
pacman -S --noconfirm aircrack-ng
pacman -S --noconfirm ettercap-text-only
pacman -S --noconfirm dsniff
pacman -S --noconfirm xterm
pacman -S --noconfirm driftnet
pacman -S --noconfirm tcpdump
pacman -S --noconfirm libnetfilter-queue-dev
pacman -S --noconfirm python3-dev
pacman -S --noconfirm hcitool
pacman -S --noconfirm sslstrip
pacman -S --noconfirm l2ping
zypper refresh
zypper install -y git
zypper install -y python3
zypper install -y python3-pip
zypper install -y wget
zypper install -y perl
zypper install -y libany-uri-escape-perl
zypper install -y libhtml-html5-entities-perl
zypper install -y libhtml-entities-numbered-perl
zypper install -y libhtml-parser-perl
zypper install -y libwww-perl
zypper install -y php
zypper install -y libdnet
zypper install -y ethtool
zypper install -y aircrack-ng
zypper install -y ettercap-text-only
zypper install -y dsniff
zypper install -y xterm
zypper install -y driftnet
zypper install -y tcpdump
zypper install -y libnetfilter-queue-dev
zypper install -y python3-dev
zypper install -y hcitool
zypper install -y sslstrip
zypper install -y l2ping
yum -y install git
yum -y install python3
yum -y install python3-pip
yum -y install wget
yum -y install perl
yum -y install libany-uri-escape-perl
yum -y install libhtml-html5-entities-perl
yum -y install libhtml-entities-numbered-perl
yum -y install libhtml-parser-perl
yum -y install libwww-perl
yum -y install php
yum -y install libdnet
yum -y install ethtool
yum -y install aircrack-ng
yum -y install ettercap-text-only
yum -y install dsniff
yum -y install xterm
yum -y install driftnet
yum -y install tcpdump
yum -y install libnetfilter-queue-dev
yum -y install python3-dev
yum -y install hcitool
yum -y install sslstrip
dnf -y install git
dnf -y install python
dnf -y install wget
dnf -y install perl
dnf -y install libany-uri-escape-perl
dnf -y install libhtml-html5-entities-perl
dnf -y install libhtml-entities-numbered-perl
dnf -y install libhtml-parser-perl
dnf -y install libwww-perl
dnf -y install php
dnf -y install libdnet
dnf -y install ethtool
dnf -y install aircrack-ng
dnf -y install ettercap-text-only
dnf -y install dsniff
dnf -y install xterm
dnf -y install driftnet
dnf -y install tcpdump
dnf -y install libnetfilter-queue-dev
dnf -y install python3-dev
dnf -y install hcitool
dnf -y install sslstrip
dnf -y install l2ping
eopkg update-repo
eopkg -y install git
eopkg -y install python3
eopkg -y install pip
eopkg -y install wget
eopkg -y install perl
eopkg -y install libany-uri-escape-perl
eopkg -y install libhtml-html5-entities-perl
eopkg -y install libhtml-entities-numbered-perl
eopkg -y install libhtml-parser-perl
eopkg -y install libwww-perl
eopkg -y install php
eopkg -y install libdnet
eopkg -y install ethtool
eopkg -y install aircrack-ng
eopkg -y install ettercap-text-only
eopkg -y install dsniff
eopkg -y install xterm
eopkg -y install driftnet
eopkg -y install tcpdump
eopkg -y install libnetfilter-queue-dev
eopkg -y install python3-dev
eopkg -y install hcitool
eopkg -y install sslstrip
eopkg -y install l2ping
xbps-install -S
xbps-install -y git
xbps-install -y python
xbps-install -y python3-pip
xbps-install -y wget
xbps-install -y perl
xbps-install -y libany-uri-escape-perl
xbps-install -y libhtml-html5-entities-perl
xbps-install -y libhtml-entities-numbered-perl
xbps-install -y libhtml-parser-perl
xbps-install -y libwww-perl
xbps-install -y php
xbps-install -y libdnet
xbps-install -y ethtool
xbps-install -y aircrack-ng
xbps-install -y ettercap-text-only
xbps-install -y dsniff
xbps-install -y xterm
xbps-install -y driftnet
xbps-install -y tcpdump
xbps-install -y libnetfilter-queue-dev
xbps-install -y python3-dev
xbps-install -y hcitool
xbps-install -y sslstrip
xbps-install -y l2ping
} &> /dev/null

if [[ -d ~/arissploit ]]
then
sleep 0
else
cd ~
{
git clone https://github.com/entynetproject/arissploit.git
} &> /dev/null
fi

{
python3 -m pip install setuptools
python3 -m pip install -r requirements.txt
} &> /dev/null

{
cd bin
cp arissploit /bin
chmod +x /bin/arissploit
cp arissploit /usr/local/bin
chmod +x /usr/local/bin/arissploit
cp arissploit /data/data/com.termux/files/usr/bin
chmod +x /data/data/com.termux/files/usr/bin/arissploit
} &> /dev/null

sleep 1
echo -e "["$GNS"suc"$CE"] Successfully installed!"
sleep 1
