from os import urandom
from sys import argv

if(len(argv)!=2):
    print("***\nThis is a tool to calculate the entropy of /dev/urandom where applicable.\nIt generates two pairs of random data and checks whether they are identical. It stops when it successfully finds 50 identical pairs.\nThe greater the iterations needed the better.\n\nUsage:\npython urandom.py <bytecount>\n<bytecount> :: Amount of each pair's bytes\n***")
    exit(2)

size = int(argv[1])
if(size<=0):
    print("***\nYou need to supply a number greater than or equal to zero to proceed.\n***")
    exit(3)
found = 0
ran = 0
while(1):
    a = urandom(size)
    b = urandom(size)
    ran = ran + 1
    if(str(a) == str(b)):
        found = found + 1
        pp = ""
        for byte in a:
            pp = pp + str(hex(ord(byte))) + "\t"
        print ("Found [" + str(found) + "/" + str(ran) + "]\t:\t" + pp)
    if(found==50):
        break