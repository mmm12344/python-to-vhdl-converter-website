from PythonToVhdlConverter.basic_converter import Entity, Input, Output, Signal, Architecture
from PythonToVhdlConverter.data_types import Bit, Std_logic, Std_logic_vector
from PythonToVhdlConverter.to_vhdl import save_to_file
from PythonToVhdlConverter.logic_converter import nand, xnor, nor, sra, sla, logic, process
import time

@Entity
class encoder8to3():
    is_component = True
    name = "encoder8to3"
    inputs = [Input("a", Std_logic_vector(8))]
    outputs = [Output("b", Std_logic_vector(3))]

@Architecture  
class Arch():
    path = __file__
    signals = []
    name = "behavior"
    entity = encoder8to3

@logic
def logic():
    @process
    def process(a):
        if a == "00000001" :
            b = "000"
        elif a == "00000010" :
            b = "001"
        elif a == "00000100" :
            b = "010"
        elif a == "00001000" :
            b = "011"
        elif a == "00010000" :
            b = "100"
        elif a == "00100000" :
            b = "101"
        elif a == "01000000" :
            b = "110"
        elif a == "10000000" :
            b = "111"               
        else :
            b = " xxx "

        