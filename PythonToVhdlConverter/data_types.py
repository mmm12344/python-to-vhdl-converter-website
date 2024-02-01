class Bit:
    def __init__(self):
        self.allowed_values = ['0', '1']
    def __repr__(self):
        return "bit"
    def __str__(self):
        return "bit"


class Std_logic:
    def __init__(self):
        self.allowed_values = ['U', 'X', '0', '1', 'Z', 'W', 'L', 'H', '-']
    def __repr__(self):
        return "std_logic"
    def __str__(self):
        return "std_logic"
    
class Std_logic_vector:
    def __init__(self, num_of_bits):
        self.allowed_values = ['U', 'X', '0', '1', 'Z', 'W', 'L', 'H', '-']
        self.num_of_bits = num_of_bits
    def __repr__(self):
        return f'std_logic_vector({self.num_of_bits-1} downto 0)'
    def __str__(self):
        return "std_logic_vector"
    
    
class Integer:
    def __init__(self, start_range=None, stop_range=None):
        self.start_range = start_range
        self.stop_range = stop_range
    
    def __repr__(self):
        if(self.start_range != None and self.stop_range != None):
            return f"integer range {self.start_range} to {self.stop_range}"
        return f"integer"
    def __str__(self):
        return "integer"
    
class Array:
    def __init__(self, start_range, stop_range, data_type):
        self.start_range = start_range
        self.stop_range = stop_range
        self.data_type = data_type
    def __repr__(self):
        return f"array ( {self.start_range} to {self.stop_range} ) of {self.data_type.__repr__()}"
    def __str__(self):
        return "array"
    

    
    