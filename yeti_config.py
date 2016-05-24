import sys
import os
	
def doConfigSetup(*args):

    curUserPath = os.environ.get('userprofile')
    if os.path.exists(curUserPath + r"\Documents\maya\2016\modules\pgYetiMaya.mod"):
        os.system(r'del /s /q "%userprofile%\Documents\maya\2016\modules\pgYetiMaya.mod"')
		
    currentPath =r"B:\plugins\maya\pgYetiMaya\maya2016\pgyetiMaya_2.0.8" 
    srcDir = currentPath + r"\maya_root"  
    dstDir=r'"C:\Program Files\Autodesk\Maya2016"'  
    os.system ("robocopy /s  %s %s" % (srcDir, dstDir))
    srcRlmDir= currentPath + r"\rlm"
    dstRlmDir=r"C:\rlm"
    os.system ("robocopy /s  %s %s" % (srcRlmDir, dstRlmDir))
    if not os.environ.has_key('PATH'):
        os.environ['PATH'] = currentPath + r'\maya_yeti\bin'
    else:
        os.environ['PATH'] = os.environ.get('PATH') + r';'+ currentPath + r'\maya_yeti\bin'
    if not os.environ.has_key('PEREGRINEL_LICENSE'):
        os.environ['PEREGRINEL_LICENSE'] = r'C:\rlm\yeti.lic'
    else:
        os.environ['PEREGRINEL_LICENSE'] = os.environ.get('PEREGRINEL_LICENSE') + r';C:\rlm\yeti.lic'
    #print("shaveNode " + pluginList[shaveNode] + " setting done!")
    
    if not os.environ.has_key('MTOA_EXTENSIONS_PATH'):
        os.environ['MTOA_EXTENSIONS_PATH'] = currentPath + r"\maya_yeti\plug-ins"
    else:
        os.environ['MTOA_EXTENSIONS_PATH'] = os.environ.get('MTOA_EXTENSIONS_PATH') + r';' + currentPath + r'\maya_yeti\plug-ins'
    if not os.environ.has_key('MTOA_PROCEDURAL_PATH'):
        os.environ['MTOA_PROCEDURAL_PATH'] = currentPath + r"\maya_yeti\bin"
    else:
        os.environ['MTOA_PROCEDURAL_PATH'] = os.environ.get('MTOA_PROCEDURAL_PATH') + r';' + currentPath + r'\maya_yeti\bin'


	print 'testplugin config args', args
    curUserPath = os.environ.get('userprofile')
    if os.path.exists(curUserPath + r"\Documents\maya\2016\modules\mtoa.mod"):
        os.system(r'del /s /q "%userprofile%\Documents\maya\2016\modules\mtoa.mod"')
	
	currentPath = r"B:\plugins\maya\mtoa\maya2016\mtoa_1.2.7.0"
	srcDir=currentPath + r"\maya_root"
	dstDir=r'"C:\Program Files\Autodesk\Maya2016"'
	os.system ("robocopy /s  %s %s" % (('\"' +srcDir+'\"'), dstDir))
	
	os.system(r'wmic process where name="JGS_mtoa_licserver.exe" delete')
	os.system(r'wmic process where name="rlm.exe" delete')	
	srcDir1=currentPath + r"\AMPED"
	dstDir1=r'"C:\AMPED"' 
	os.system ("robocopy /s  %s %s" % ( srcDir, dstDir1))
   
    if not os.environ.has_key('PATH'):
        os.environ['PATH'] = currentPath + r'\maya_mtoa\bin'
    else:
        os.environ['PATH'] = os.environ.get('PATH') + r';'+ currentPath + r'\maya_mtoa\bin'
    if not os.environ.has_key('MAYA_RENDER_DESC_PATH'):
        os.environ['MAYA_RENDER_DESC_PATH'] = currentPath + r"\maya_mtoa"
    else:
        os.environ['MAYA_RENDER_DESC_PATH'] = os.environ.get('MAYA_RENDER_DESC_PATH') + r';' + currentPath + r"\maya_mtoa"


	os.system(r'start C:\AMPED\rlm.exe')
	os.system(r'"C:\Program Files\Autodesk\Maya2016\bin\maya.exe"')
doConfigSetup()