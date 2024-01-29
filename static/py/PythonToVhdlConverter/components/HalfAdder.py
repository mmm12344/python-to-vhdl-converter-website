from PythonToVhdlConverter.basic_converter import Entity, Input, Output, Signal, Architecture
from PythonToVhdlConverter.data_types import Bit, Std_logic, Std_logic_vector
from PythonToVhdlConverter.to_vhdl import save_to_file
from PythonToVhdlConverter.logic_converter import nand, xnor, nor, sra, sla, logic, process
import time

@Entity
class HalfAdder():
    is_component = True
    name = "HalfAdder"
    inputs = [Input("a", Std_logic()), Input("b", Std_logic())]
    outputs = [Output("sum", Std_logic()), Output("carry", Std_logic())]

@Architecture
class Arch():
    path = __file__  
    signals = []
    name = "behavior"
    entity = HalfAdder


@logic
def logic():
    @process
    def process(a, b):
        sum =  a ^ b
        carry = a and b 
