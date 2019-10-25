#!/bin/bash

# MIT License

# Copyright (C) 2019, Arissploit Team. All Rights Reserved.

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

NV="\033[1;37m"
RS="\033[1;31m"
YS="\033[1;33m"
CE="\033[0m"

if [[ $EUID -ne 0 ]]
then
   sleep 1
   echo -e "["$RS"*"$CE"] "$RS"This script must be run as "$YS"root"$C"" 1>&2
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
cp bin/arissploit /bin
chmod +x /bin/arissploit
cp bin/arissploit /usr/local/bin
chmod +x /usr/local/bin/arissploit
cp bin/arissploit /data/data/com.termux/files/usr/bin/
chmod +x /data/data/com.termux/files/usr/bin/arissploit
} &> /dev/null

sleep 1
echo -e "What is your architecture?("$YS"amd"$CE"/"$YS"intel"$CE"/"$YS"arm"$CE"):"
echo -e "Arissploit supports "$YS"amd"$CE", "$YS"intel"$CE" and "$YS"arm"$CE" architectures!"
echo -e "Select your architecture to install compatible dependencies!"
read -e -p $'(\033[4;93march\033[0m)> ' CONF

if [[ "$CONF" = "arm" ]]
then
sleep 1
clear
sleep 1
echo -e "Is this a single board computer?("$YS"yes"$CE"/"$YS"no"$CE"):"
echo -e "Single board computer like Raspberry PI!"
echo -e "Arissploit supports Raspberry PI!"
read -e -p $'(\033[4;93mconfirm\033[0m)> ' PI
if [[ "$PI" = "yes" ]]
then
CONF="amd"
fi
fi

if [[ "$CONF" = "amd" ]]
then
sleep 1
clear
sleep 1
if [[ -d /System/Library/CoreServices/Finder.app ]]
then
sleep 1
else
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
sleep 0.5
fi
fi

if [[ "$CONF" = "arm" ]]
then
sleep 1
clear
sleep 1
if [[ -d /System/Library/CoreServices/SpringBoard.app ]]
then
sleep 1
else
pkg update
pkg -y install git
pkg -y install python3
pkg -y install python3-pip
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
pkg -y install python3-dev
pkg -y install hcitool
pkg -y install sslstrip
sleep 0.5
fi
fi

if [[ "$CONF" = "intel" ]]
then
sleep 1
clear
sleep 1
if [[ -d /System/Library/CoreServices/Finder.app ]]
then
sleep 1
else
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
sleep 0.5
fi
fi

{
pip3 install netfilterqueue
} &> /dev/null

clear
printf '\033]2;Arissploit INSTALLER\a'
sleep 3
echo -e "Open a NEW terminal and type '"$YS"arissploit"$CE"' to launch the framework"
sleep 2
