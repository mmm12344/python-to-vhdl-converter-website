from PythonToVhdlConverter.basic_converter import Entity, Input, Output, Signal, Architecture
from PythonToVhdlConverter.data_types import Bit, Std_logic, Std_logic_vector
from PythonToVhdlConverter.to_vhdl import save_to_file
from PythonToVhdlConverter.logic_converter import nand, xnor, nor, sra, sla, logic, process
import time

@Entity
class FullAdder():
    is_component = True
    name = "FullAdder"
    inputs = [Input("a", Std_logic()), Input("b", Std_logic()),Input("cin", Std_logic())]
    outputs = [Output("sum", Std_logic()), Output("cout", Std_logic())]

@Architecture
class Arch():
    path = __file__  
    signals = [Signal("x1", Std_logic()), Signal("x2", Std_logic()),Signal("x3", Std_logic())]
    name = "behavior"
    entity = FullAdder


@logic
def logic():
    x1 = a ^ b
    x2 = a and b
    x3 = x1 and cin 
    sum = x1 ^ cin 
    cout = x2 or x3

