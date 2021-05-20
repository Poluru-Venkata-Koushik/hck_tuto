import subprocess
interface="eth0"
new_mac=input("[~]enter new mac address:")
subprocess.call('ifconfig',shell=True)
subprocess.call('ifconfig '+interface+' down',shell=True)
subprocess.call('ifconfig',shell=True)
subprocess.call('ifconfig '+interface+' hw ether '+new_mac,shell=True)
subprocess.call('ifconfig '+interface+' up',shell=True)
