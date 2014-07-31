# Kainoa Gaddis (c) 2014
# Assembler for Dr. Harrisons johnniac

instruction_list = []

# Function to print the items
def dump_code(instruction_list):
    for code_item in instruction_list:
        print(code_item)


def read_program(instruction_list):
    # Get input
    entry = input("? ").upper()
    while (entry != "GO"):
        # Get variables
        (opcode, operand) = entry.split(" ")
        
        # Instructions for HALT
        if opcode == "HALT":
            instruction = "00000"
            
        # Instructions for HALT
        if opcode == "LOAD":
            instruction = "01" + operand
        
        # Instructions for HALT
        if opcode == "STORE":
            instruction = "02" + operand
        
        # Instructions for HALT
        if opcode == "ADD":
            instruction = "03" + operand
        
        # Instructions for HALT
        if opcode == "MULTIPLY":
            instruction = "04" + operand
        
        # Instructions for HALT
        if opcode == "DIVIDE":
            instruction = "05" + operand
        
        # Instructions for HALT
        if opcode == "SUBTRACT":
            instruction = "06" + operand
        
        # Instructions for HALT
        if opcode == "TEST":
            instruction = "07" + operand
        
        # Instructions for HALT
        if opcode == "GET":
            instruction = "08" + operand
        
        # Instructions for HALT
        if opcode == "DISPLAY":
            instruction = "09" + operand
        
        # Instructions for HALT
        if opcode == "NOOP":
            instruction = "10" + operand
        
        # Add instructions to the list
        instruction_list.append(instruction)
        
        entry = input("? ").upper()
        
read_program(instruction_list)
dump_code(instruction_list)
