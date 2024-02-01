from PythonToVhdlConverter.basic_converter import Entity, Input, Output, Signal, Architecture, Constant
from PythonToVhdlConverter.data_types import Bit, Std_logic, Std_logic_vector, Integer, Array
from PythonToVhdlConverter.to_vhdl import save_to_file
from PythonToVhdlConverter.logic_converter import nand, xnor, nor, sra, sla, logic, process, rising_edge, falling_edge
import time

@Entity
class comparator_VHDL():
   is_component = True
   name = "comparator_VHDL"
   inputs = [Input("A", Std_logic_vector(2)), Input("b", Std_logic_vector(2))]
   outputs = [Output("A_less_B", Std_logic()),Output("A_equal_B", Std_logic()),Output("A_greater_B", Std_logic())]
   
@Architecture
class Arch():
   path = __file__
   signals = [Signal("tmp1",Std_logic()),Signal("tmp2",Std_logic()),Signal("tmp3",Std_logic()),Signal("tmp4",Std_logic()),
              Signal("tmp5",Std_logic()),Signal("tmp6",Std_logic()),Signal("tmp7",Std_logic()),Signal("tmp8",Std_logic())]
   name = "comparator_structural"
   entity = comparator_VHDL 
   

@logic
def logic():
    tmp1 = A[1] |xnor| B[1]
    tmp2 = A[0] |xnor| B[0]
    A_equal_B = tmp1 and tmp2

    tmp3 = ( (not A[0] )  and ( not A[1] ) )  and B[0]
    tmp4 = not A[1] and  B[1]
    tmp5 = not A[0]  and  B[1] and  B[0]
    A_less_B = tmp3 or tmp4 or tmp5

    tmp6 = not B[0] and not B[1] and A[0]
    tmp7 = not B[1] and A[1]
    tmp8 = not B[0] and A[1] and A[0]
    A_greater_B = tmp6 or tmp7 or tmp8