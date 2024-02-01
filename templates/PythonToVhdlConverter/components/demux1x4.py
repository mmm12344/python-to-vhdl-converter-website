from PythonToVhdlConverter.basic_converter import Entity, Input, Output, Signal, Architecture
from PythonToVhdlConverter.data_types import Bit, Std_logic, Std_logic_vector
from PythonToVhdlConverter.to_vhdl import save_to_file
from PythonToVhdlConverter.logic_converter import nand, xnor, nor, sra, sla, logic, process
import time


@Entity
class demux1x4():
    is_component = True
    name = "demux1x4"
    inputs = [Input("inp", Std_logic()), Input("s", Std_logic_vector(2))]
    outputs = [Output("opt0", Std_logic()), Output("opt1", Std_logic()), Output("opt2", Std_logic()), Output("opt3", Std_logic())]

@Architecture
class Arch():
    path = __file__
    signals = []
    name = "behavior"
    entity = demux1x4

@logic
def logic():
    @process
    def process(inp, s):
        match s:
            case "00":
                opt0 = inp
                opt1 = '0'
                opt2 = '0'
                opt3 = '0'
            case "01":
                opt0 = '0'
                opt1 = inp
                opt2 = '0'
                opt3 = '0'
            case "10":
                opt0 = '0'
                opt1 = '0'
                opt2 = inp
                opt3 = '0'
            case "11":
                opt0 = '0'
                opt1 = '0'
                opt2 = '0'
                opt3 = inp
