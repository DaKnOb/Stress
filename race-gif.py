import thread, time, sys, Tkinter, math, hashlib

if(len(sys.argv)!=4):
    print("This is a PRNG that uses race conditions for entropy.\nIt generates a binary number in the end and a GIF file. You can use this number to test it in a Man vs Machine test or check the final image for patterns.\n\nUsage:\npython race.py <pairs> <state> <size>\n<pairs> :: Pairs of setter / resetter threads\n<state> :: The initial variable value (0/1 or even 2)\n<size> :: Amount of bits to generate\n")
    exit(5)

threadPairs = int(sys.argv[1]) # Amount of threads setting it to 1 and 0
randomn = int(sys.argv[2]) # Start with 0, 1 or a super state 2?
amount = int(sys.argv[3]) # How many bits do you like?

side = int(math.sqrt(amount)) #Calculate the best square dimensions
print(str(side) + "x" + str(side))

t = Tkinter.Tk()
i = Tkinter.PhotoImage(width=side, height=side)

def writer(bit, pos):
    global i
    if(bit==1):
        i.put("#000", (pos%side,int(pos/side)))
    else:
        i.put("#fff", (pos%side,int(pos/side)))

def setter(boo):
    global randomn
    while(1):
        randomn = boo
    
for std in range(1, threadPairs+1):
    thread.start_new_thread(setter, (1,))
    thread.start_new_thread(setter, (0,))
 
time.sleep(1)  # Make sure all threads have started
for std in range(0,amount):
    sys.stdout.write(str(randomn)) # Write bits to stdout
    sys.stdout.flush()
    writer(randomn, std) # Write to display
    time.sleep(0.001)    # Nice interval to maintain both speed and randomness
sys.stdout.write("\n")
i.write(str(hashlib.md5(str(time.gmtime())).hexdigest()) + ".gif", format="gif") # Generate a unique filename and save as GIF










