from PythonToVhdlConverter.basic_converter import Entity, Input, Output, Signal, Architecture
from PythonToVhdlConverter.data_types import Bit, Std_logic, Std_logic_vector
from PythonToVhdlConverter.to_vhdl import save_to_file
from PythonToVhdlConverter.logic_converter import nand, xnor, nor, sra, sla, logic, process
import time

@Entity
class encoder4to2():
    is_component = True
    name = "encoder4to2"
    inputs = [Input("a", Std_logic_vector(4))]
    outputs = [Output("b", Std_logic_vector(2))]

@Architecture   
class Arch():
    path = __file__
    signals = []
    name = "behavior"
    entity = encoder4to2

@logic
def logic():
    @process
    def process(a):
        if a == " 1000 " :
            b = " 00 "
        elif a == " 0100 " :
            b = " 01 "
        elif a == " 0010 " :
            b = " 10 "
        elif a == " 0001 " :
            b = " 11 "        
        else :
            b = " xx "

        