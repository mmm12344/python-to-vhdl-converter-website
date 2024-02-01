import re

digits = "0123456789"
literals = "thequickbrownfoxjumpsoverthelazydog"
break_string_symbols = """['"]<>-+*/%^<>=!(),"""
symbols = """'"_<>-+*/%^<>=!|,"""

variable_regex_exp = "^([A-Z]|[a-z])+(_*|[0-9]|[A-Z]|[a-z])*$"


tokens = []

def register_token(token):
    tokens.append(token)
        

def register_tokens(*tokens):
    for token in tokens:
        register_token(token)
        


class Token:
    """
    A class representing a token.
 
    Attributes:
        token_name(str): The token typed.
        replace_with(str): The token to replace with.
        type(str): The type of token (arithmetic, logical, bitwise, etc..).
        in_middle(bool): ...
    """
    def __init__(self, token_name, replace_with, type=None, in_middle=True):
        """
        Initializes a Token object.
 
        Parameters:
            token_name(str): The token typed.
            replace_with(str): The token to replace with.
            type(str): The type of token (arithmetic, logical, bitwise, etc..).
            in_middle (bool): ...
        """
        self.name = token_name
        self.replace_with = replace_with
        self.type = type
        self.in_middle = in_middle
        register_token(self)
    def __repr__(self):
        return self.replace_with
    def __str__(self):
        return f"{self.token_name} => {self.replace_with} : {self.type}"


class Lexer:
    """
    A class representing a lexical analyzer which is reponsible for the conversion of a text into meaningful tokens belonging to categories.
 
    Attributes:
        text(str): The text to convert into tokens.
    """
    def __init__(self, text):
        """
        Initializes a Lexer object.
 
        Parameters:
            text(str): The text to convert into tokens.
        """
        self.text = text.lstrip()   # remove leading white space
        self.pos = -1   #position of current char
        self.current_char = None
        self.advance()
    def advance(self):
        """
        Advances to the next character in text.
 
        Args:
            self
 
        Returns:
            void
        """
        self.pos += 1
        self.current_char = self.text[self.pos] if self.pos < len(self.text) else None
        
    def make_tokens(self):
        """
        Tokenizes text by calling appropriate functions (make_number() and make_string())
 
        Args:
            self
 
        Returns:
            list(str): List of tokens.
        """
        tokens = []
        
        
        while self.current_char != None: # checks if current character is a tab, digit or else (literals or symbols).
            if self.current_char in ' \t':
                self.advance()
            elif self.current_char in digits:
                tokens.append(self.make_number())
            else :
                tokens.append(self.make_string())
           
                
        return tokens
                
    def make_number(self):
        """
        Tokenizes a number.
 
        Args:
            self
 
        Returns:
            str: The number as a string.
        """
        num_str = ""
        dot_count = 0
        
        
        while self.current_char != None and self.current_char in digits + '.': # Checks if the current character is not None and is a digit or a dot.
            if self.current_char == '.':
                if dot_count == 1:break # ensures no more than one decimal place.
                dot_count += 1
                num_str += '.'
            else:
                num_str += self.current_char
            self.advance()
            
        return num_str
        
    def make_string(self):
        string = ''
        
        if self.current_char in break_string_symbols:
            while self.current_char != None and (self.current_char in break_string_symbols):
                string += self.current_char
                self.advance()
        else:
            while self.current_char != None and (self.current_char.lower() in literals or self.current_char in symbols or self.current_char in digits):
                string += self.current_char
                self.advance()
        
        token = self.string_in_tokens(string)
        if token:
            return token
        elif re.match(variable_regex_exp, string):
            return string
        else:
            raise Exception(f"Illegal string [ {string} ] in line [ {self.text} ] position [ {self.pos} ]")
        
        
    def string_in_tokens(self, string):
        for token in tokens:
            if token.name == string:
                return token
        return False
        



def generate_tokens(text):
    lexer = Lexer(text)
    tokens = lexer.make_tokens()
    
    return tokens

def parse_text(text):
    tokens = generate_tokens(text)
    parsed_text = []
    find_qout = False
    qout_text = ''
    for item in tokens:
        if not find_qout:
            if type(item) == str:
                parsed_text.append(item)
            elif item.__repr__() == "'" or item.__repr__() == '"':
                qout_text += item.__repr__()
                find_qout = True
            else:
                parsed_text.append(item.__repr__())
        else:
            if type(item) == str:
                qout_text += item
            elif item.__repr__() == "'" or item.__repr__() == '"':
                qout_text += item.__repr__()
                find_qout = False
                parsed_text.append(qout_text)
                qout_text = ""
            else:
                qout_text += item.__repr__()
            
    return " ".join(parsed_text)


            
        
        
            