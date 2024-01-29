from pyscript import document
from pyweb import pydom
from js import editorSessions


def RunConverter(event):
    
    tabs = pydom['#editor-div .nav-link']
    tab_names = []
    for tab in tabs:
        tab_names.append(tab.html)
        
    tab_contents = []
    for session in editorSessions:
        tab_contents.append(session.getValue())
    
    