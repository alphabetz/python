import subprocess
from subprocess import call
from sys import argv

class bcolors:
    OKGREEN = '\033[92m'
    BOLD = '\033[1m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    
script, file_name, type_hash, ori_hash = argv

print "File name: ", file_name
print "Original Hash: ", ori_hash

fin = subprocess.check_output([type_hash + "sum", file_name])

if fin[:fin.find(' ')] == ori_hash:
    print bcolors.OKGREEN + bcolors.BOLD + "----HASH MATCHED----"\
    + bcolors.ENDC
    quit()

print bcolors.FAIL + bcolors.BOLD + "HASH NOT MATCHED!!! RE-CHECK YOUR",\
      "DOWNLOADED FILE" + bcolors.ENDC
