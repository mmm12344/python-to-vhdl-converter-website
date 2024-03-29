from pyscript import document
from pyweb import pydom
from js import editorSessions, resultsConsole, AddResultTab, DeleteAllResultTabs, window, ActivateConsoleTab
import importlib, traceback, sys, os




def add_lines_to_console(lines):
    value = resultsConsole.getValue()
    resultsConsole.setValue(value + '\n' + lines+'\n')
    
def add_command_to_console(line):
    value = resultsConsole.getValue()
    resultsConsole.setValue(value + '\n' + "User > "+ line + '\n')
    
def add_errors_to_console(trace):
    value = resultsConsole.getValue()
    resultsConsole.setValue(value + '\n' + trace+'\n')
    
def add_warning_to_console(line):
    value = resultsConsole.getValue()
    resultsConsole.setValue(value + '\n' + 'Warning: ' + line + '\n')
    


def RunConverter(event):
    DeleteAllResultTabs()
    
    ActivateConsoleTab()
    
    if not os.path.exists('./PythonToVhdlConverter/__init__.py'):
        with open('./PythonToVhdlConverter/__init__.py', 'w') as f:
            f.writelines(['components = []\n', 'files = []\n', 'from .tokens import *\n'])
    
    tabs = pydom['#editor-div .nav-pills .nav-link']
    tab_names = []
    for tab in tabs:
        tab_names.append(tab.html)
        
    parent_tap_index = -1
    tab_contents = []
    index = 0
    for session in editorSessions:
        session_value = session.getValue()
        tab_contents.append(session_value)
        if "save_to_file()" in session_value:
            parent_tap_index = index
        index+=1
        
      
    for index in range(len(tab_names)):
        with open(tab_names[index]+'.py', 'w') as f:
            f.write(tab_contents[index])
            
            
    add_command_to_console(f'python {tab_names[parent_tap_index]}.py')
    
    if parent_tap_index == -1:
        add_errors_to_console('Please make Sure that you have the function "save_to_file()" at the end of the file that you want to be converted.')
        return

    add_lines_to_console("Converting files....")
    
    try:
        module = importlib.import_module(tab_names[parent_tap_index])
        importlib.reload(module)
        add_lines_to_console("Conversion Successfull !!")
    except BaseException as e:
        add_errors_to_console(traceback.format_exc())
        return
        
    result_dir = tab_names[parent_tap_index]+'__results/'
    
    for name in tab_names:
        try:
            with open(result_dir+name+'.vhdl', 'r') as f:
                AddResultTab(name ,f.read())
        except:
            add_warning_to_console(name + " is either empty or undefined.")
    
    
            
            
            
        
    
    
        
    
        
    
        
    
    
    
    