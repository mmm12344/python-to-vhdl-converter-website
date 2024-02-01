from PythonToVhdlConverter.basic_converter import Entity, Input, Output, Signal, Architecture
from PythonToVhdlConverter.data_types import Bit, Std_logic, Std_logic_vector
from PythonToVhdlConverter.to_vhdl import save_to_file
from PythonToVhdlConverter.logic_converter import nand, xnor, nor, sra, sla, logic, process, rising_edge, falling_edge
import time

@Entity
class tFlipFlop():
    is_component = True
    name = "tFlipFlop"
    inputs = [Input("clock", Std_logic()), Input("t", Std_logic())]
    outputs = [Output("q", Std_logic())]

@Architecture
class Arch():
    path = __file__
    signals = [Signal("tmp", Std_logic())]
    name = "behavior"
    entity = tFlipFlop

@logic
def logic():
    @process
    def process(clock):
        if rising_edge(clock):
            if t == '0':
                tmp  = tmp  
            elif t == '1' :
                tmp = not tmp
    q = tmp                     
