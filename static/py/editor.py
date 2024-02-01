from pyscript import document
from pyweb import pydom
from js import editorSessions, resultsConsole, AddResultTab, DeleteAllResultTabs, window
import importlib, traceback, sys, os




def add_lines_to_console(lines):
    
    resultsConsole.insert(lines+'\n')
    
def add_command_to_console(line):
    resultsConsole.insert("User > "+ line + '\n')
    
def add_errors_to_console(trace):
    resultsConsole.insert(trace+'\n')
    


def RunConverter(event):
    DeleteAllResultTabs()
    
    tabs = pydom['#editor-div .nav-link']
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
        
      
    for index in range(len(tab_names)-1):
        with open(tab_names[index]+'.py', 'w') as f:
            f.write(tab_contents[index])
            
    print('hi') 
            
    add_command_to_console(f'python {tab_names[parent_tap_index]}.py')
    
    if parent_tap_index == -1:
        add_errors_to_console('Please make Sure that you have the function "save_to_file()" at the end of the file that you want to be converted.')
        return

    add_lines_to_console("Converting files....")
    
    try:
        module = importlib.import_module(tab_names[parent_tap_index])
        importlib.reload(module)
        add_lines_to_console("Convertion Successfull !!")
    except BaseException as e:
        add_errors_to_console(traceback.format_exc())
        return
        
    result_dir = tab_names[parent_tap_index]+'__results/'
    
    for name in tab_names:
        with open(result_dir+name+'.vhdl', 'r') as f:
            AddResultTab(name ,f.read())
    
    
            
            
            
        
    
    
        
    
        
    
        
    
    
    
    