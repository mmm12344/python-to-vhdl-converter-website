from PythonToVhdlConverter.basic_converter import Entity, Input, Output, Signal, Architecture
from PythonToVhdlConverter.data_types import Bit, Std_logic, Std_logic_vector
from PythonToVhdlConverter.to_vhdl import save_to_file
from PythonToVhdlConverter.logic_converter import nand, xnor, nor, sra, sla, logic, process
import time

@Entity
class mux8x1():
    is_component = True
    name = "mux8x1"
    inputs = [Input("inp0", Std_logic()),Input("inp1", Std_logic()),Input("inp2", Std_logic()),Input("inp3", Std_logic()),Input("inp4", Std_logic()),Input("inp5", Std_logic()),Input("inp6", Std_logic()),Input("inp7", Std_logic()),Input("s", Std_logic_vector(3))]
    outputs = [Output("opt", Std_logic())]
 
@Architecture     
class Arch():
    path = __file__
    signals = []
    name = "behavior"
    entity = mux8x1
@logic
def logic():
    @process
    def process(inp0,inp1,inp2,inp3,inp4,inp5,inp6,inp7,s):
        match s:
            case " 000 " :
                opt = inp0
            case  " 001 " :
                opt = inp1
            case  " 010 "  :
                opt = inp2
            case  " 011 "  :
                opt = inp3
            case " 100 " :
                opt = inp4
            case  " 101 " :
                opt = inp5
            case  " 110 "  :
                opt = inp6
            case  " 111 "  :
                opt = inp7
