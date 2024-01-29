from PythonToVhdlConverter.basic_converter import Entity, Input, Output, Signal, Architecture
from PythonToVhdlConverter.data_types import Bit, Std_logic, Std_logic_vector
from PythonToVhdlConverter.to_vhdl import save_to_file
from PythonToVhdlConverter.logic_converter import nand, xnor, nor, sra, sla, logic, process, rising_edge, falling_edge
import time

@Entity
class JKFlipFlop():
    is_component = True
    name = "JKFlipFlop"
    inputs = [Input("clock", Std_logic()), Input("j", Std_logic()),Input("k", Std_logic())]
    outputs = [Output("q", Std_logic()),Output("qb", Std_logic())]

@Architecture
class Arch():
    path = __file__
    signals = [Signal("TMP", Std_logic())]
    name = "behavior"
    entity = JKFlipFlop

@logic
def logic():
    TMP == '0'
    @process
    def process(clock):
        if rising_edge(clock):
            if j == '0' and k == '0' :
                TMP = TMP
            elif j == '1' and k == '1' :
                TMP = not TMP
            elif j == '0' and k == '1' : 
                TMP = '0'
            else:
                TMP = '1'
        q = TMP
        qb = not TMP     
