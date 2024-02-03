

var editorSessions = [];
var resultSessions = [];


AddEditorSession();




var resultsConsole = ace.edit("result0");
resultsConsole.setTheme("ace/theme/chrome");
resultsConsole.session.setMode("ace/mode/powershell");
resultsConsole.setHighlightActiveLine(false);
resultsConsole.setReadOnly(true);

resultsConsole.setOptions({
    autoScrollEditorIntoView: true,
    copyWithEmptySelection: true,
    wrap: true,
    fontSize: 17,  
});

resultSessions.push(resultsConsole);






function MakeAllTapsDeactivated(){
    $("#editor-div .activated").removeClass('activated').addClass('deactivated');

}

function TapFormElement(){
    return '<form onSubmit="return ChangeTapName(this)"><input type="text" name="tapName"><input type="button" value="" hidden></form>';
}


function ChangeTapName(tab){
    var value = $(tab)[0][0].value;
    var parent = $(tab).parent();
    parent.html('<a href="javascript:void(0);" class="nav-link">'+value+'</a>');
    parent.css('border-color', '#C252F2');
    return false;
}

function AddTap(){
    tapHtml = '<li class="nav-item activated" ondblclick="AddFormToTab(this)" onclick="ActivateTab(this)">'+TapFormElement()+'</li>';
    MakeAllTapsDeactivated();
    $("#editor-div .nav-pills").append(tapHtml);
    AddEditorSession();
    
}

function AddFormToTab(tab){
    $(tab).html(TapFormElement());
    $(tab).css('border-color', 'lightblue');
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
    editorHtml = '<div class="editor activated" id="'+editorIdName+'">from PythonToVhdlConverter.basic_converter import Entity, Input, Output, Signal, Architecture, Constant\nfrom PythonToVhdlConverter.data_types import Bit, Std_logic, Std_logic_vector, Integer, Array\nfrom PythonToVhdlConverter.to_vhdl import save_to_file\nfrom PythonToVhdlConverter.logic_converter import nand, xnor, nor, sra, sla, logic, process, rising_edge, falling_edge\nimport time</div>';
    $("#run").before(editorHtml);
    var editor = ace.edit(editorIdName);
    editor.setTheme("ace/theme/dracula");
    editor.session.setMode("ace/mode/python");
    editor.setOptions({
        autoScrollEditorIntoView: true,
        copyWithEmptySelection: true,
        wrap: true,
        fontSize: 17,  
    });
    editorSessions.push(editor);
}

function GetTabInfo(index){
    tabName = $('#editor nav-pills')[0][index][0].value;
    tabContent = editorSessions[index].getValue();
    return tabName, tabContent;
}

function DeactivateResults(){
    $('#console-div .result').removeClass('activated').addClass('deactivated');
}

function AddResultSession(value){
    var resultIdName = 'result' + resultSessions.length;
    resultHtml = '<div class="result console-shadow deactivated" id="'+resultIdName+'">'+value+'</div>';
    $("#download").before(resultHtml);
    var result = ace.edit(resultIdName);
    result.setTheme("ace/theme/chrome");
    result.session.setMode("ace/mode/vhdl");
    result.setOptions({
        autoScrollEditorIntoView: true,
        copyWithEmptySelection: true,
        wrap: true,
        fontSize: 20  
    });
    result.setValue(result.getValue());
    resultSessions.push(result);
}

function AddResultTab(name, value){
    tabHtml = '<li class="nav-item deactivated console-shadow" onclick="ActivateResultTab(this)"><a href="javascript:void(0);" class="nav-link">'+name+'</a></li>';
    $('#console-div .nav-pills').append(tabHtml);
    AddResultSession(value);
}

function SwitchResultSession(index){
    DeactivateResults();
    $('#console-div #result'+index).removeClass('deactivated').addClass('activated');
}

function DeactivateResultTabs(){
    $('#console-div .nav-item').removeClass('activated').addClass('deactivated');
}

function ActivateResultTab(tab){
    DeactivateResultTabs();
    $(tab).removeClass('deactivated').addClass('activated');
    SwitchResultSession($(tab).index());
}

function ActivateConsoleTab(){
    ActivateResultTab($('#console-div .nav-pills .nav-item'));
}

function DeleteAllResultTabs(){
    $('#console-div .result').each(function(){
        if(this.id != 'result0'){
            $(this).remove();
        }
    });
    $('#console-div .nav-item').each(function(index){
        if(index != 0){
            $(this).remove();
        }
    });
    temp = resultSessions[0];
    resultSessions = [];
    resultSessions.push(temp);
}















