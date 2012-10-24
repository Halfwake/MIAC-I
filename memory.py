A = 0
B = 0

ADDRESS = [0] * 256

def op_PL(addr):
    global A
    A = addr
def op_MUL(addr):
    global B
    B = A * addr
def op_SUB(addr):
    global B
    B = B - addr
def op_DIV(addr):
    global A
    A = B / addr
def op_ROA():
    print A
def op_ROB():
    print B
def op_ADD(addr):
    global B
    B = B + addr

ADDRESS[0] = 2
ADDRESS[30] = op_PL
ADDRESS[24] = op_MUL
ADDRESS[20] = op_SUB
ADDRESS[37] = op_DIV
ADDRESS[43] = op_ROA
ADDRESS[49] = op_ROB
ADDRESS[19] = op_ADD
