from .validation import validate_data_types
from .logic_converter import parse_file
from . import files, components

def style(block):
    styled = [""]
    styled[1:] = block.splitlines(True)
    return "\t".join(styled)

class Packages:
    def __init__(self):
        pass
    def get_Packages(self):
        return "library IEEE;\nuse IEEE.STD_LOGIC_1164.ALL;\nuse IEEE.STD_LOGIC_ARITH.ALL;\nuse IEEE.STD_LOGIC_UNSIGNED.ALL;"




class Entity():
    """
    A class representing an entity.
 
    Attributes:
        ?: ?
    """

    def __init__(self, entity_class):
        """
        Initializes an Entity object.
 
        Parameters:
            ?: ?
        """
        self.entity_class = entity_class
        entity_structure = self.convert_entity()
        files.append({"entity": self})
        try:
            if self.entity_class.is_component:
                components.append(self)
                
          
        except:
            pass

    def convert_entity(self):
        """
        Converts class (entity) to VHDL code.
 
        Args:
            self
 
        Returns:
            str: VHDL code for an entity.
        """
        if len(self.entity_class.inputs) == 0 and len(self.entity_class.outputs) == 0:
            return f"{Packages().get_Packages()}\n\nentity {self.entity_class.name} is\nend {self.entity_class.name};"
        return f"{Packages().get_Packages()}\n\nentity {self.entity_class.name} is\nport(\n{self.create_port()}\n);\nend {self.entity_class.name};"
    def create_port(self):
        """
        Creates VHDL port.
 
        Args:
            self
 
        Returns:
            str: The VHDL code for a port with inputs and outputs.
        """
        port = ""
        for input in self.entity_class.inputs:
            port += input.__str__() + ";\n"
        for output in self.entity_class.outputs:
            port += "\n" + output.__str__() + ";"
        port = port[:-1] # to avoid writing ';);'
        return style(port)
        
        
class Architecture():
    """
    A class representing an architecture.
 
    Attributes:
        ?: ?
    """
    def __init__(self, architecture_class):
        """
        Initializes an Architecture object.
 
        Parameters:
            ?:?
        """
        self.file_name = architecture_class.path.split("\\")[-1].split(".")[0]
        self.architecture_class = architecture_class
        self.entity_name = architecture_class.entity.entity_class.name
        try:
            if self.architecture_class.entity.entity_class.is_component:
                self.is_component = True
            else:
                self.is_component = False
        except:
            self.is_component = False
        files[-1]["architicture"] = self
    def convert_arch(self):
        """
        Converts class (architecture) to VHDL code.
 
        Args:
            self
 
        Returns:
            str: The VHDL code for an architecture with signals.
        """
        if not self.is_component:
            components_to_add = CreateComponents().convert_component()
        else:
            components_to_add = ''
        return f"architecture {self.architecture_class.name} of {self.entity_name} is\n{style(components_to_add)}\n{self.create_signals()}\n{self.create_constants()}\n\tbegin\n{parse_file(self.architecture_class.path)}\n\tend {self.architecture_class.name};"
    def create_signals(self):
        """
        Creates VHDL signals.
 
        Args:
            self
 
        Returns:
            str: The VHDL code for signals.
        """
        signals = ""
        for signal in self.architecture_class.signals:
            signals += signal.__str__() + ";\n"
        return style(signals)
    
    def create_constants(self):
        constants = ""
        try:
            for constant in self.architecture_class.constants:
                constants += constant.__str__() + ";\n"
        except:
            return ""
        return style(constants)
        

class CreateComponents:
    def __init__(self):
        pass

    def convert_component(self):
        result = ""
      
        for component in components:
            result += f"component {component.entity_class.name} is\nport(\n{self.create_port(component)}\n);\nend component;\n"
        return result
       
    def create_port(self, component):
        """
        Creates VHDL port.
 
        Args:
            self
 
        Returns:
            str: The VHDL code for a port with inputs and outputs.
        """
        port = ""
        for input in component.entity_class.inputs:
            port += input.__str__() + ";\n"
        for output in component.entity_class.outputs:
            port += "\n" + output.__str__() + ";"
        port = port[:-1] # to avoid writing ';);'
        return style(port)
            
            

class Input():
    def __init__(self, name, type):
        self.name = name
        self.type = type
        validate_data_types(type)
        
    def __str__(self):
        return f"{self.name} : in {self.type.__repr__()}"
    
class Output():
    def __init__(self, name, type):
        self.name = name
        self.type = type
        validate_data_types(type)
    def __str__(self):
        return f"{self.name} : out {self.type.__repr__()}"

class Signal():
    def __init__(self, name, type):
        self.name = name
        self.type = type
        validate_data_types(type)
    def __str__(self):
        return f"signal {self.name} : {self.type.__repr__()}"
    
class Constant:
    def __init__(self, name, type):
        self.name = name
        self.type = type
        validate_data_types(type)
    def __str__(self):
        return f"constant {self.name} : {self.type.__repr__()}"