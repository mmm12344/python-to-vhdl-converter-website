from PythonToVhdlConverter.basic_converter import Entity, Input, Output, Signal, Architecture
from PythonToVhdlConverter.data_types import Bit, Std_logic, Std_logic_vector
from PythonToVhdlConverter.to_vhdl import save_to_file
from PythonToVhdlConverter.logic_converter import nand, xnor, nor, sra, sla, logic, process
import time

@Entity
class demux1x8():
    is_component = True
    name = "demux1x8"
    inputs = [Input("inp", Std_logic()), Input("s", Std_logic_vector(3))]
    outputs = [Output("opt0", Std_logic()), Output("opt1", Std_logic()), Output("opt2", Std_logic()), Output("opt3", Std_logic()), Output("opt4", Std_logic()), Output("opt5", Std_logic()), Output("opt6", Std_logic()), Output("opt7", Std_logic())]

@Architecture
class Arch():
    path = __file__
    signals = []
    name = "behavior"
    entity = demux1x8

@logic
def logic():
    @process
    def process(inp, s):
        match s:
            case "000":
                opt0 = inp
                opt1 = '0'
                opt2 = '0'
                opt3 = '0'
                opt4 = '0'
                opt5 = '0'
                opt6 = '0'
                opt7 = '0'
            case "001":
                opt0 = '0'
                opt1 = inp
                opt2 = '0'
                opt3 = '0'
                opt4 = '0'
                opt5 = '0'
                opt6 = '0'
                opt7 = '0'
            case "010":
                opt0 = '0'
                opt1 = '0'
                opt2 = inp
                opt3 = '0'
                opt4 = '0'
                opt5 = '0'
                opt6 = '0'
                opt7 = '0'
            case "011":
                opt0 = '0'
                opt1 = '0'
                opt2 = '0'
                opt3 = inp
                opt4 = '0'
                opt5 = '0'
                opt6 = '0'
                opt7 = '0'
            case "100":
                opt0 = '0'
                opt1 = '0'
                opt2 = '0'
                opt3 = '0'
                opt4 = inp
                opt5 = '0'
                opt6 = '0'
                opt7 = '0'
            case "101":
                opt0 = '0'
                opt1 = '0'
                opt2 = '0'
                opt3 = '0'
                opt4 = '0'
                opt5 = inp
                opt6 = '0'
                opt7 = '0'
            case "110":
                opt0 = '0'
                opt1 = '0'
                opt2 = '0'
                opt3 = '0'
                opt4 = '0'
                opt5 = '0'
                opt6 = inp
                opt7 = '0'
            case "111":
                opt0 = '0'
                opt1 = '0'
                opt2 = '0'
                opt3 = '0'
                opt4 = '0'
                opt5 = '0'
                opt6 = '0'
                opt7 = inp 