#run commands with admin privileges
import subprocess
subprocess.call(['runas','/user:[[RYAN]\\]user','netsh wlan start hostednetwork'])
