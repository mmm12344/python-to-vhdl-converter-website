from PythonToVhdlConverter.basic_converter import Entity, Input, Output, Signal, Architecture
from PythonToVhdlConverter.data_types import Bit, Std_logic, Std_logic_vector
from PythonToVhdlConverter.to_vhdl import save_to_file
from PythonToVhdlConverter.logic_converter import nand, xnor, nor, sra, sla, logic, process
import time

@Entity
class decoder2x4():
    is_component = True
    name = "decoder2x4"
    inputs = [Input("inp", Std_logic_vector(2))]
    outputs = [Output("opt", Std_logic_vector(4))]

@Architecture
class Arch():
    path = __file__
    signals = []
    name = "behavior"
    entity = decoder2x4

@logic
def logic():
    @process
    def process(inp):
        match inp:
            case " 00 " :
                opt = "0001"
            case  " 01 " :
                opt = "0010"
            case  " 10 "  :
                opt = "0100"
            case  " 11 "  :
                opt = "1000"
        