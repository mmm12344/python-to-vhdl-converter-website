from . import files
import os

def convert_to_vhdl(entity, arch):
    return entity.convert_entity() + "\n" + arch.convert_arch()


def save_to_file():
    folder_name = files[-1]["architicture"].file_name + "__results"
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
    for file in files:
        print(file["architicture"].file_name)
        with open(f"{folder_name}/"+file["architicture"].file_name+".vhdl", "w") as f:
            f.writelines(convert_to_vhdl(file["entity"], file["architicture"]))