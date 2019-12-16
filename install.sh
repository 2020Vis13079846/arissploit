#!/bin/bash

# MIT License
#
# Copyright (C) 2019, Arissploit Team. All Rights Reserved.
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

NV="\033[1;37m"
RS="\033[1;91m"
YS="\033[1;33m"
CE="\033[0m"

if [[ $EUID -ne 0 ]]
then
   sleep 1
   echo -e "["$RS"err"$CE"] This script must be run as root!" 1>&2
   sleep 1
   exit
fi

cd ~ 
if [[ -d arissploit ]]
then
clear
cd arissploit
else
{
git clone https://github.com/entynetproject/arissploit.git
} &> /dev/null
cd arissploit 
chmod +x install.sh
fi

printf '\033]2;arissploit INSTALLER\a'
clear
cat ~/arissploit/banner/banner.txt
echo -e "\033[1;33mBy Arissploit Team\033[0m"
sleep 3
echo -e "More on our site:"
sleep 3
echo -e "==> \033[1;33mhttp://entynetproject.simplesite.com/\033[0m"
sleep 3
echo -e "Creators of Arissploit Framework (\033[4;33mArissploit Team\033[0m):"
sleep 3
echo -e "\033[4;34mEntynetproject\033[0m - Main Developer"
sleep 3
echo -e "\033[4;33mDJ Mobley\033[0m      - Ascii Designer"
sleep 3
echo -e "Press \033[1;33many key\033[0m to install arissploit"
read -n 1

clear

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
apk add git
apk add python3
apk add python3-pip
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
apk add install sslstrip
pacman -S git
pacman -S python3
pacman -S python3-pip
pacman -S wget
pacman -S perl
pacman -S libany-uri-escape-perl
pacman -S libhtml-html5-entities-perl
pacman -S libhtml-entities-numbered-perl
pacman -S libhtml-parser-perl
pacman -S libwww-perl
pacman -S php
pacman -S install libdnet
pacman -S ethtool
pacman -S aircrack-ng
pacman -S ettercap-text-only
pacman -S dsniff
pacman -S xterm
pacman -S driftnet
pacman -S tcpdump
pacman -S libnetfilter-queue-dev
pacman -S python3-dev
pacman -S hcitool
pacman -S sslstrip
} &> /dev/null

{
pip3 install setuptools
pip3 install netfilterqueue
} &> /dev/null

{
cp bin/arissploit /bin
chmod +x /bin/arissploit
cp bin/arissploit /usr/local/bin
chmod +x /usr/local/bin/arissploit
cp bin/arissploit /data/data/com.termux/files/usr/bin
chmod +x /data/data/com.termux/files/usr/bin/arissploit
} &> /dev/null

clear
printf '\033]2;Arissploit INSTALLER\a'
sleep 3
echo -e "Open a NEW terminal and type '"$YS"arissploit"$CE"' to launch the framework"
sleep 2
