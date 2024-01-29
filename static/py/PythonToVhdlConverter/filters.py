import re
from .lexer import parse_text
from . import components

## if condition types

if_type = "if"
elif_type = "elif"
else_type = "else"

inside_process = False # flag to determine if match-case statement is inside a process block

def style(block):
    styled = [""]
    styled[1:] = block.splitlines(True)
    return "\t".join(styled)


class Condition_token:
    def __init__(self, type, condition=None):
        self.condition = condition
        self.type = type
        self.statements = []
        
        
    def add_statement(self, statement):
        self.statements.append(statement)

class Match_Case_Token:
    def __init__(self, type, parameter=None, choice=None):
        self.parameter = parameter
        self.choice = choice
        self.type = type
        self.statements = []
        
        
    def add_statement(self, statement):
        self.statements.append(statement)
        

class For_loop_token:
    def __init__(self, parameter, from_var, to_var):
        self.parameter = parameter
        self.from_var = from_var
        self.to_var = to_var
        self.statements = []
    
    def add_statement(self, statement):
        self.statements.append(statement)

class While_loop_token:
    def __init__(self, condition):
        self.condition = condition
        self.statements = []
    
    def add_statement(self, statement):
        self.statements.append(statement)
        
        
        

class Capture:
    """
    A class to capture code blocks (if-elif-else, match-case, for, while, etc..)
 
    Attributes:
        lines (list): 
        pos(int): 
        current_line (int): 
        tokens (list): 
    """
    def __init__(self, lines):
        """
        Initializes a capture object.
 
        Parameters:
            lines (list): 
        """

        self.lines = lines
        self.pos = -1
        self.current_line = None
        self.tokens = []
        self.advance()
        self.tokenize()
        
    def tokenize(self):
        """
        Tokenizes the code block and appends the tokens to the tokens list.
    
        Args:
            ...
    
        Returns:
            ...
        """
        global inside_process

        # matches the current line to the corresponding code block,
        # calls on the corresponding capture function 
        # and appends the filtered code block to the tokens list
        while self.current_line != None:
            if If_condition_filter.is_if(self.current_line):
                self.tokens.append(If_condition_filter(self.capture_if()))
            elif Match_Case_Condition_Filter.is_match_case(self.current_line):
                self.tokens.append(Match_Case_Condition_Filter(self.capture_match_case(), inside_process))
            elif For_loop_filter.is_for(self.current_line):
                self.tokens.append(For_loop_filter(self.capture_for()))
            elif While_loop_filter.is_while(self.current_line):
                self.tokens.append(While_loop_filter(self.capture_while()))
            elif Process_filter.is_process(self.current_line):
                inside_process = True

                self.advance()
                self.tokens.append(Process_filter(self.capture_process()))
            elif PortMap_filter.is_portmap(self.current_line):
                self.tokens.append(PortMap_filter(self.capture_portmap()))
                self.advance()
            elif Wait_filter.is_wait(self.current_line):
                self.tokens.append(Wait_filter(self.capture_wait()))
                self.advance()
            else:
                self.tokens.append(Statement_filter(self.current_line))
                self.advance()
        
    def advance(self):
        self.pos += 1
        self.current_line = self.lines[self.pos] if self.pos < len(self.lines) else None
    
    def get_leading_white_sapces(self, line):
        """
        Calculates the leading whitespace for the given line.
    
        Args:
            line (str): the line to calculate the leading whitespace for.
    
        Returns:
            int: The leading whitespace count.
        """
        return len(line) - len(line.lstrip())
    
    def is_child(self, parent_line, child_line):
        """
        Determines whether a given line or statement is inside a code block. 
    
        Args:
            parent_line (str):
            child_line (str):
    
        Returns:
            bool: whether child_line is a child to parent_line
        """
        if self.get_leading_white_sapces(parent_line) < self.get_leading_white_sapces(child_line):
            return True
        return False
    
    def capture_if(self):
        """
        Captures if-elif-else block.
    
        Args:
            ...
    
        Returns:
            list (str): the if-elif-else block.
        """
        #if_regex_exp = "\s*if (.+):$"
        elif_regex_exp = "\s*elif (.+):$"
        else_regex_exp = "\s*else(.*):$"
        if_block_lines = []
        if_line = self.current_line
        if_block_lines.append(if_line) # current_line was already verified to be an if-statement
        self.advance()
        while self.current_line != None:
            if not self.is_child(if_line, self.current_line) and not re.match(elif_regex_exp, self.current_line) and not re.match(else_regex_exp, self.current_line):
                break
            if_block_lines.append(self.current_line)

            self.advance()
        return if_block_lines

    def capture_match_case(self):
        """
        Captures match-case block.
    
        Args:
            ...
    
        Returns:
            list (str): the match-case block.
        """
        match_case_block_lines = []
        match_case_block_lines.append(self.current_line)  # current_line was already verified to be a match-case statement
        match_line = self.current_line
        self.advance()

        while self.current_line != None:
            if not self.is_child(match_line, self.current_line):
                break
            match_case_block_lines.append(self.current_line)
            self.advance()

        return match_case_block_lines
    
    def capture_for(self):
        """
        Captures for-block.
    
        Args:
            ...
    
        Returns:
            list (str): the for-block.
        """
        for_block_lines = []     
        for_block_lines.append(self.current_line)
        for_line = self.current_line  # current_line was already verified to be a for-statement
        self.advance()
        
        while self.current_line != None:
            if not self.is_child(for_line, self.current_line):
                break
            for_block_lines.append(self.current_line)
            self.advance()
        
        return for_block_lines
    
    def capture_while(self):
        """
        Captures while-block.
    
        Args:
            ...
    
        Returns:
            list (str): the while-block.
        """
        while_block_lines = []     
        while_block_lines.append(self.current_line)
        while_line = self.current_line  # current_line was already verified to be an while-statement
        self.advance()
        
        while self.current_line != None:
            if not self.is_child(while_line, self.current_line):
                break
            while_block_lines.append(self.current_line)
            self.advance()
        
        return while_block_lines
    
    def capture_process(self):
        """
        Captures process-block.
    
        Args:
            ...
    
        Returns:
            list (str): the process-block.
        """
        process_block_lines = []
        process_line = self.current_line
        process_block_lines.append(process_line)  # current_line was already verified to be an process-statement
        self.advance()
        while self.current_line != None:
            if not self.is_child(process_line, self.current_line):
                break
            process_block_lines.append(self.current_line)
            self.advance()
        return process_block_lines
    
    def capture_portmap(self):
        return self.current_line
    
    def capture_wait(self):
        return self.current_line
                
    
    def get_tokens(self):
        return self.tokens
    
    def parse(self):
        """
        Calls on the token's corresponding parse method.
    
        Args:
            ...
    
        Returns:
            str: the parsed block.
        """
        parsed_block = ""
        for token in self.tokens:
            parsed_block += token.parse()
        return style(parsed_block)
                
            
    

class Statement_filter:
    def __init__(self, line):
        self.line = line
    def parse(self):
        return style(parse_text(self.line) +" ;\n")

class Process_filter:
    def __init__(self, lines):
        self.lines = lines 
        self.process_regex_exp = "\s*def .+\((.*)\):"
        self.sensitivity_list = ""
        self.tokens = []
        self.tokenize()
   
    def tokenize(self):
        process_match = re.match(self.process_regex_exp, self.lines[0])
        self.sensitivity_list = process_match.group(1)
        self.tokens = Capture(self.lines[1:]).get_tokens()
        global inside_process
        inside_process = False # important! sets inside_process to false before parsing
    
    def parse(self):
        if self.sensitivity_list.strip() == "":
            parsed_block = f"process\nbegin\n"
        else:
            parsed_block = f"process ({self.sensitivity_list})\nbegin\n"
        for token in self.tokens:
            parsed_block += token.parse() + "\n"
        parsed_block += "end process;\n"
        return style(parsed_block)
    
    def is_process(line):
        process_decorator_regex_exp = "\s*@process$"
        if re.match(process_decorator_regex_exp, line):
            return True
        return False
    
        

class If_condition_filter:
    def __init__(self, lines):
        self.lines = lines
        self.if_regex_exp = "\s*if (.+):$"
        self.elif_regex_exp = "\s*elif (.+):$"
        self.else_regex_exp = "\s*else(.*):$"
        self.tokens = []
        self.tokenize()
    
    def tokenize(self):
        inside_block = False
        parentLine = self.lines[0]
        index = 0
        
        while index < len(self.lines):
            if_match = re.match(self.if_regex_exp, self.lines[index])
            elif_match = re.match(self.elif_regex_exp, self.lines[index])
            else_match = re.match(self.else_regex_exp, self.lines[index])
            if if_match and (inside_block == False):
                inside_block = True
                parentLine = self.lines[index]
                token = Condition_token(if_type, if_match.group(1))
            elif elif_match and (inside_block == False):
                inside_block = True
                parentLine = self.lines[index]
                token = Condition_token(elif_type, elif_match.group(1))
            elif else_match and (inside_block == False):
                inside_block = True
                parentLine = self.lines[index]
                token = Condition_token(else_type)
            else:
                to_capture = []
                
               
                while ((index + 1) <= len(self.lines)) and ((len(parentLine) - len(parentLine.lstrip())) < (len(self.lines[index]) - len(self.lines[index].lstrip()))):
                    to_capture.append(self.lines[index])
                    index+=1

                self.tokens[-1].add_statement(Capture(to_capture))
                inside_block = False
                
                
                continue
            self.tokens.append(token)
            index += 1

    def parse(self):
        parsed_block = ""
        for token in self.tokens:
            if token.type == if_type:
                parsed_block += f"if {parse_text(token.condition)} then\n"
            elif token.type == elif_type:
                parsed_block += f"elsif {parse_text(token.condition)} then\n"
            elif token.type == else_type:
                parsed_block += f"else\n"
                
            for statement in token.statements:
                parsed_block += f"{statement.parse()}"
        
        parsed_block += "end if;\n"
        return style(parsed_block)
    
    def is_if(line):
        if_regex_exp = "\s*if (.+):$"
        if re.match(if_regex_exp, line):
            return True
        return False
    
class Match_Case_Condition_Filter:
    def __init__(self, lines, inside_process):
        self.lines = lines
        self.inside_process = inside_process
        self.match_case_regex_exp = "\s*match (.+):$"
        self.case_regex_exp = "\s*case (.+):$"
        self.tokens = []
        self.tokenize()
        pass

    def tokenize(self):
        index = 0
        parent_line = self.lines[0]
        found_match = False
        
        while index < len(self.lines):
            match_case_match = re.match(self.match_case_regex_exp, self.lines[index])
            case_match = re.match(self.case_regex_exp, self.lines[index])

            if match_case_match and (found_match == False):
                parent_line = self.lines[index]
                found_match = True
                token = Match_Case_Token("match", match_case_match.group(1), None)
            elif case_match:
                parent_line = self.lines[index]
                found_match = True
                token = Match_Case_Token("case", None, case_match.group(1))
            else:
                to_capture = []
                
                while ((index + 1) <= len(self.lines)) and ((len(parent_line) - len(parent_line.lstrip())) < (len(self.lines[index]) - len(self.lines[index].lstrip()))):
                    to_capture.append(self.lines[index])
                    index+=1

                self.tokens[-1].add_statement(Capture(to_capture))
                found_match = False                
                continue

            self.tokens.append(token)
            index += 1

        
    def parse(self):
        parsed_block = ''

        filtered_statement = []
        token_parameter = ''
        output_var = ''
        output_var_value = []

        index = 0

        for token in self.tokens:
            if(self.inside_process):
                if token.type == "match":
                    parsed_block += f"case {parse_text(token.parameter)} is\n"
                elif token.type == "case":
                    parsed_block += style(f"when {parse_text(token.choice)} =>\n")
                
                for statement in token.statements:
                    parsed_block += style(f"{statement.parse()}")

            else:
                for statement in token.statements:
                    filtered_statement = re.findall(r"\w+|\".*\"", statement.parse())
                    output_var_value.append(filtered_statement[1])

                if token.type == "match":
                    token_parameter = token.parameter
                elif token.type == "case":
                    if((index + 1) < (len(self.tokens) - 1)):
                        parsed_block += style(f"{parse_text(output_var_value[index])} when {parse_text(token_parameter)} = {token.choice} else\n")
                    else:
                        parsed_block += style(f"{parse_text(output_var_value[index])} when {parse_text(token_parameter)} = {token.choice};\n")
                    index += 1

        if(self.inside_process):
            parsed_block += "end case;\n"
        else:
            output_var = filtered_statement[0]
            parsed_block = f"{output_var} <=" + parsed_block 

        return style(parsed_block)

    def is_match_case(line):
        match_case_regex_exp = "\s*match (.+):$"
        if re.match(match_case_regex_exp, line):
            return True
        return False


class For_loop_filter:
    def __init__(self, lines):
        self.lines = lines
        self.for_regex_exp = "\s*for (.+) in range\((.+),(.+)\):"
        self.tokens = []
        self.tokenize()
    
    def tokenize(self):
        for index, line in enumerate(self.lines):
            for_match = re.match(self.for_regex_exp, line)
            if for_match:
                token = For_loop_token(for_match.group(1), for_match.group(2), for_match.group(3))
                self.tokens.append(token)
            else:
                self.tokens[-1].add_statement(Capture(self.lines[index:]))
                break

    def parse(self):
        parsed_block = ""
        for token in self.tokens:
            parsed_block += f"for {parse_text(token.parameter)} in {parse_text(token.from_var)} to {parse_text(token.to_var)} loop\n"
            for statement in token.statements:
                parsed_block += f"{statement.parse()}"
        
        parsed_block += "end loop;\n"
        return style(parsed_block)
                
    def is_for(line):
        for_regex_exp = "\s*for (.+) in range\((.+),(.+)\):"
        if re.match(for_regex_exp, line):
            return True
        return False
    
class While_loop_filter:
    def __init__(self, lines):
        self.lines = lines
        self.while_regex_exp = "\s*while (.+):"
        self.tokens = []
        self.tokenize()
    
    def tokenize(self):
        for index, line in enumerate(self.lines):
            while_match = re.match(self.while_regex_exp, line)
            if while_match:
                token = While_loop_token(while_match.group(1))
                self.tokens.append(token)
            else:
                self.tokens[-1].add_statement(Capture(self.lines[index:]))
                break

    def parse(self):
        parsed_block = ""
        for token in self.tokens:
            parsed_block += f"while {parse_text(token.condition)} loop\n"
            for statement in token.statements:
                parsed_block += f"{statement.parse()}"
        
        parsed_block += "end loop;\n"
        return style(parsed_block)
                
    def is_while(line):
        while_regex_exp = "\s*while (.+):"
        if re.match(while_regex_exp, line):
            return True
        return False
    
    
    
class PortMap_filter:
    def __init__(self, line):
        self.line = line
        self.map_list = ""
        self.var = ""
        self.component_name = ""
        self.tokenize()
    def portmap_regex_exp(self, component_name):
        return f"\s*(.+)\s*=\s*{component_name}.*\((.+)\)\s*$"
    def tokenize(self):
        for component in components:
            portmap_match = re.match(self.portmap_regex_exp(component.entity_class.name), self.line)
            if portmap_match:
                self.map_list = portmap_match.group(2).split(",")
                self.var = portmap_match.group(1)
                self.component_name = component.entity_class.name
                
    def parse(self):
        result = f"{self.var} : {self.component_name} port map("
        for item in self.map_list:
            result += parse_text(item) + " ,"
        result = result[:-1]
        result += ");\n"
        return style(result)
    
    def is_portmap(line):
        def portmap_regex_exp(component_name):
            return f"\s*(.+).*=.*{component_name}.*\((.+\))\s*$"
        for component in components:
            portmap_match = re.match(portmap_regex_exp(component.entity_class.name), line)
            if portmap_match:
                return True
        return False
    
    
class Wait_filter:
    def __init__(self, line):
        self.line = line
        self.wait_regex_exp = "\s*time.sleep\((.*)\)\s*$"
        self.wait_time = ""
        self.tokenize()
    def tokenize(self):
        match = re.match(self.wait_regex_exp, self.line)
        if match:
            self.wait_time = match.group(1)
    def parse(self):
        if self.wait_time.strip():
            return style(f"wait for {self.wait_time} ns;\n")
        return style(f"wait;\n")
    def is_wait(line):
        wait_regex_exp = "\s*time.sleep\((.*)\)\s*$"
        if re.match(wait_regex_exp, line):
            return True
        return False
