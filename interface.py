
HEX_BINARY = {
    '0': "0000", '1': "0001", '2': "0010", '3': "0011", '4': "0100", 
    '5': "0101", '6': "0110", '7': "0111", '8': "1000", '9': "1001", 
    'A': "1010", 'B': "1011", 'C': "1100", 'D': "1101", 'E': "1110",
    'F': "1111"
}

IR = []
TR = []
AR = []
PC = []
AR = []
DR = []
AC = []
M = []

for i in range(16):
    DR.append(0)
    AC.append(0)
    IR.append(0)
    TR.append(0)
for i in range(12):
    AR.append(0)
    PC.append(0)

for i in range(2**8):
    M.append(0)

T = 0
PC_point = 0

def operationDecode(instruction):
    I = instruction[0]
    opcode = instruction[1:4]
    memRef = instruction[4:]
    decode(I, opcode, memRef)

def decode(I, Opcode, MemRef):
    pass

def hexToBinary(hex):
    '''
    Converts hex to decimal and returns a str
    '''
    binary = ""
    for char in hex:
        binary += HEX_BINARY[char]
    
    return binary
        
def hexToDecimal(hex):
    '''
    converts hex to decimal and returns a int
    '''
    binary = hexToBinary(hex)
    decimal = 0
    index = 0
    for i in binary:
        if i == '0':
            index +=1
        if i == '1':
            decimal += 2**index

    return decimal


print("Input your instruction into the Memory in the format: TTT XYYYZZZ")
print("Where T refernces where to store the instuction in Memory in Hex, X refernces I, YYY references opcode, and ZZZ references memory location in Hex")
print("The max size of the Memory is 100")

while (True):
    print("Input your instruction into the Memory in the format: TTT 1111FFF")
    print("Input X to cancel \n")
    TBS = input()
    if TBS == "X":
        break
    location = TBS[0:4]
    instruction = TBS[5:12]
    M[hexToDecimal(location)] = instruction


while (PC_point != len(M)):
    instruction = input()
    operationDecode(instruction)



# 1 111 FFF