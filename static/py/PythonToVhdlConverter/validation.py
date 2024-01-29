from .data_types import Bit, Std_logic, Std_logic_vector, Integer, Array



data_types = [Bit, Std_logic, Std_logic_vector, Integer, Array]






def validate_data_types(data_type):
    for item in data_types:
        if(type(data_type) == item):
            return True
    raise Exception(f"type:  {data_type.__repr__()} is not supported")