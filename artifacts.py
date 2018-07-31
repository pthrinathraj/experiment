
import subprocess
vpn_connection = subprocess.call("ifconfig utun1 &> /dev/null", shell=True, stderr=subprocess.STDOUT)
#print(vpn_connection)

if vpn_connection == 0 :
     print( "you are connected to VPN")

idoru_version = input('please go to "http://brmopc-x4-16.us.oracle.com:8100" and find the version being deployed: ')
print ("so we are deploying ", idoru_version )

import wget
download_files = subprocess.call(['wget -A  zip, tar.gz, md5 -r -l 1 -nd '+ "http://brmopc-x4-16.us.oracle.com:8100/"+ idoru_version])
#wget -A zip, tar.gz, md5 -r -l 1 -nd http://brmopc-x4-16.us.oracle.com:8100/3.31.13/