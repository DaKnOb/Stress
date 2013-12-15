import thread, time, sys

if(len(sys.argv)!=4):
    print("This is a PRNG that uses race conditions for entropy.\nIt generates a binary number in the end. You can use this number to test it in a Man vs Machine test.\n\nUsage:\npython race.py <pairs> <state> <size>\n<pairs> :: Pairs of setter / resetter threads\n<state> :: The initial variable value (0/1 or even 2)\n<size> :: Amount of bits to generate\n")
    exit(5)

threadPairs = int(sys.argv[1]) # Amount of threads setting it to 1 and 0
randomn = int(sys.argv[2]) # Start with 0, 1 or a super state 2?
amount = int(sys.argv[3]) # How many bits do you like?

def setter(boo):
    global randomn
    while(1):
        randomn = boo
    
for std in range(1, threadPairs+1):
    thread.start_new_thread(setter, (1,))
    thread.start_new_thread(setter, (0,))
 
time.sleep(0.5)   
for std in range(0,amount):
    sys.stdout.write(str(randomn))
    sys.stdout.flush()
    time.sleep(0.1)
sys.stdout.write("\n")