import sys
import inspect

import memory

bin_files = sys.argv[1:]
if len(bin_files) < 1:
    print "No files given."
    quit()

for bin_file in bin_files:
    bin_file_name = bin_file
    bin_file = open(bin_file)
    while True:
        opcode = bin_file.read(1)
        if not opcode:
            print "Program Finished"
            break
        opcode = ord(opcode)
        opcode = memory.ADDRESS[opcode]
        
        addrs = []
        for arg in inspect.getargspec(opcode)[0]:
            addr = bin_file.read(1)
            if not addr:
                print "Invalid arguments to opcode <%s>!" % opcode
                break
            addr = ord(addr)
            addr = memory.ADDRESS[addr]
            addrs.append(addr)
        
        apply(opcode, addrs)
    bin_file.close()
