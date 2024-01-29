from PythonToVhdlConverter.basic_converter import Entity, Input, Output, Signal, Architecture
from PythonToVhdlConverter.data_types import Bit, Std_logic, Std_logic_vector
from PythonToVhdlConverter.to_vhdl import save_to_file
from PythonToVhdlConverter.logic_converter import nand, xnor, nor, sra, sla, logic, process
import time

@Entity
class mux4x1():
    is_component = True
    name = "mux4x1"
    inputs = [Input("inp0", Std_logic()),Input("inp1", Std_logic()),Input("inp2", Std_logic()),Input("inp3", Std_logic()),Input("s", Std_logic_vector(2))] 
    outputs = [Output("opt", Std_logic())]

@Architecture   
class Arch():
    path = __file__
    signals = []
    name = "behavior"
    entity = mux4x1
@logic
def logic():
    @process
    def process(inp0,inp1,inp2,inp3,s):
        match s:
            case " 00 " :
                opt = inp0
            case  " 01 " :
                opt = inp1
            case  " 10 "  :
                opt = inp2
            case  " 11 "  :
                opt = inp3

  

