#blue start 
	BS="\033[1;34m"
#color end
	CE="\033[0m"
#red start
	RS="\033[1;31m"
#green start
	GNS="-e \033[1;32m"
#white start
        WHS="\033[0;97m"
        
if [[ -d /data/data/com.termux ]]
then
if [[ -f /data/data/com.termux/files/usr/bin/arissploit ]]
then
UPD="true"
else
UPD="false"
fi
else
if [[ -f /usr/local/bin/mouse ]]
then
UPD="true"
else
UPD="false"
fi
fi
{
ASESR="$( curl -s checkip.dyndns.org | sed -e 's/.*Current IP Address: //' -e 's/<.*$//' )"
} &> /dev/null
if [[ "$ASESR" = "" ]]
then 
sleep 1
echo -e ""$RS"[-] "$WHS"Download failed!"$CE""
sleep 1
exit
fi
if [[ $EUID -ne 0 ]]
then
sleep 1
echo -e ""$RS"[-] "$WHS"Permission denied!"$CE""
sleep 1
exit
fi
sleep 1
echo -e ""$BS"[*] "$WHS"Installing update..."$CE""
{
rm -rf ~/arissploit
rm /bin/arissploit
rm /usr/local/bin/arissploit
rm /data/data/com.termux/files/usr/bin/arissploit
cd ~
git clone https://github.com/entynetproject/arissploit.git
if [[ "$UPD" != "true" ]]
then
sleep 0
else
cd ~/arissploit
chmod +x install.sh
./install.sh
fi
} &> /dev/null
echo -e ""$BS"[+] "$WHS"Successfully updated!"$CE""
sleep 1
exit
