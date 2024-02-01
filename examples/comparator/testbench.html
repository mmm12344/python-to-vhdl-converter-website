from PythonToVhdlConverter.basic_converter import Entity, Input, Output, Signal, Architecture, Constant
from PythonToVhdlConverter.data_types import Bit, Std_logic, Std_logic_vector, Integer, Array
from PythonToVhdlConverter.to_vhdl import save_to_file
from PythonToVhdlConverter.logic_converter import nand, xnor, nor, sra, sla, logic, process, rising_edge, falling_edge
import time
import comparator_VHDL as comparator_VHDL

@Entity
class tb_comparator_VHDL():
   name = "tb_comparator_VHDL"
   inputs = []
   outputs = []
   
@Architecture
class Arch():
   path = __file__
   signals = [Signal("A",Std_logic()),Signal("B",Std_logic()),Signal("A_less_B",Std_logic()),Signal("A_equal_B",Std_logic()),
              Signal("A_greater_B",Std_logic())]
   name = "behavior"
   entity = tb_comparator_VHDL 
   

@logic
def logic():
    uut = comparator_VHDL( A , B , A_less_B , A_equal_B , A_greater_B )
    @process
    def process():
        for i in range(0, 3):
          A = to_std_logic_vector( to_unsigned( i , 2 ) )
          B = to_std_logic_vector( to_unsigned(i + 1 , 2) )
          time.sleep(20)

        for i in range(0,3):
          A = to_std_logic_vector( to_unsigned(i + 1 , 2) )
          B = to_std_logic_vector( to_unsigned( i , 2 ) )
          time.sleep(20)

        for i in range(0,3):
          A = to_std_logic_vector( to_unsigned( i , 2 ) )
          B = to_std_logic_vector( to_unsigned( i , 2 ) )
          time.sleep(20)  
        time.sleep()
          


save_to_file()