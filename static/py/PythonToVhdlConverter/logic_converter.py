from .lexer import parse_text
from .filters import Capture



class Infix():
    def __init__(self):
        self
        
nand = Infix()
nor = Infix()
xnor = Infix()  

sra = Infix()
sla = Infix()


def logic(func):
    return 0
def process(func):
    return 0

def rising_edge(var):
    return 0
def falling_edge(var):
    return 0

def get_lines(file_path):
    """
    Reads file and returns lines.
 
    Args:
        file_path(str): path to the file to read from.
 
    Returns:
        list(str): lines
    """
    with open(file_path, 'r') as f1:
        lines = f1.readlines()
    return lines
            
        
def find_leading_white_space(line):
    """
    Calculates number of leading white space.
 
    Args:
        line(str): The line.
 
    Returns:
        int: The number of leading white space.
    """
    return len(line) - len(line.lstrip())


def process_lines(lines):
    processed_lines = []
    for line in lines:
        processed_lines.append(line.rstrip())
    return processed_lines

def get_logic(lines):
    logic_lines = []
    logic_index = lines.index("@logic\n")
    lines = process_lines(lines[logic_index+2:])
    for line in lines:
        if find_leading_white_space(line) < 2 and line.rstrip() != "":
            break
        if line.rstrip() != "":
            logic_lines.append(line)
    return logic_lines


def parse_file(file_path):
    lines = get_lines(file_path)
        
    lines = get_logic(lines)
    lines = process_lines(lines)
    
    parsed_text = Capture(lines).parse()
        
        
    return parsed_text
        
        
            

            

        
    

    

    
