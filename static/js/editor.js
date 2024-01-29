

var editorSessions = [];



AddEditorSession();




var resultsConsole = ace.edit("results-console");
resultsConsole.setTheme("ace/theme/chrome")
resultsConsole.session.setMode("ace/mode/powershell");

resultsConsole.setOptions({
    autoScrollEditorIntoView: true,
    copyWithEmptySelection: true,
    wrap: true,
    fontSize: 20,  
    setReadOnly: true,
});



function MakeAllTapsDeactivated(){
    $("#editor-div .activated").removeClass('activated').addClass('deactivated');

}

function TapFormElement(){
    return '<form onSubmit="return ChangeTapName(this)"><input type="text" name="tapName"><input type="button" value="" hidden></form>';
}


function ChangeTapName(tab){
    var value = $(tab)[0][0].value;
    var parent = $(tab).parent();
    parent.html('<a href="#" class="nav-link">'+value+'</a>');
    return false;
}

function AddTap(){
    tapHtml = '<li class="nav-item activated d-flex flex-column" ondblclick="AddFormToTab(this)" onclick="ActivateTab(this)">'+TapFormElement()+'</li>';
    MakeAllTapsDeactivated();
    $("#editor-div .nav-pills").append(tapHtml);
    AddEditorSession();
    
}

function AddFormToTab(tab){
    $(tab).html(TapFormElement());
}

function ActivateTab(tab){
    MakeAllTapsDeactivated();
    $(tab).removeClass('deactivated').addClass('activated');
    var index = $(tab).index();
    SwitchEditorSession(index);
}

function DeactivateEditors(){
    $('#editor-div .editor').removeClass('activated').addClass('deactivated');
}

function SwitchEditorSession(index){
    DeactivateEditors();
    $('#editor-div #editor'+index).removeClass('deactivated').addClass('activated');
}

function AddEditorSession(){
    DeactivateEditors();
    var editorIdName = 'editor' + editorSessions.length;
    editorHtml = '<div class="editor" id="'+editorIdName+'">from PythonToVhdlConverter.basic_converter import Entity, Input, Output, Signal, Architecture, Constant\nfrom PythonToVhdlConverter.data_types import Bit, Std_logic, Std_logic_vector, Integer, Array\nfrom PythonToVhdlConverter.to_vhdl import save_to_file\nfrom PythonToVhdlConverter.logic_converter import nand, xnor, nor, sra, sla, logic, process, rising_edge, falling_edge\nimport time</div>';
    $("#run").before(editorHtml);
    var editor = ace.edit(editorIdName);
    editor.setTheme("ace/theme/dracula");
    editor.session.setMode("ace/mode/python");
    editor.setOptions({
        autoScrollEditorIntoView: true,
        copyWithEmptySelection: true,
        wrap: true,
        fontSize: 20  
    });
    editorSessions.push(editor);
}


function GetTabInfo(index){
    tabName = $('#editor nav-pills')[0][index][0].value;
    tabContent = editorSessions[index].getValue();
    return tabName, tabContent;
}






