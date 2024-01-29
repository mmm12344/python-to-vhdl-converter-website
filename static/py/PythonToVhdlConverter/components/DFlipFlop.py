from PythonToVhdlConverter.basic_converter import Entity, Input, Output, Signal, Architecture
from PythonToVhdlConverter.data_types import Bit, Std_logic, Std_logic_vector
from PythonToVhdlConverter.to_vhdl import save_to_file
from PythonToVhdlConverter.logic_converter import nand, xnor, nor, sra, sla, logic, process, rising_edge, falling_edge
import time

@Entity
class DFlipFlop():
    is_component = True
    name = "DFlipFlop"
    inputs = [Input("clock", Std_logic()), Input("d", Std_logic())]
    outputs = [Output("q", Std_logic())]

@Architecture
class Arch():
    path = __file__
    signals = []
    name = "behavior"
    entity = DFlipFlop

@logic
def logic():
    @process
    def process(clock):
        if rising_edge(clock):
            q = d
