# copyright 2008 OsaMa -ITQPDA

import appuifw, audio, os,e32
import db,time
from graphics import *
import powlite_fm as fm
def ar(x):return x.decode('utf8')

settings = db.set(save=1)
#========================
#   app info    
appuifw.app.screen='normal'
appuifw.app.body = b = appuifw.Text()
b.style = appuifw.STYLE_BOLD
appuifw.app.body.color=0x0000ff
b.add(ar('      ITQPDA SoundREC. v1.0\n===========================\n      Author: Osamadj.\n                For\n      http://www.i-tich.net\n          English by:\n        ~: ITQPDA Team :~\n                  For\n   www.ipmart-forum.com \n'))



#========================
osamadir=u'E:\\itqpda\\'
try:
    if not os.path.exists(osamadir):  
       os.makedirs(osamadir)
    else:
         pass
except:
      appuifw.note(u"Couldn't create the directory!", "error")

def std():
     date = time.strftime('_%d%m%Y_%H_%M_%S')
     appuifw.note(ar('you are Recording in ( ')+settings.TYPE+u" ) Format","info")

     filename =u'E:\\itqpda\\rec'+date+u'.'+settings.TYPE

    # create your icons for the listbox content  
     icon1 = appuifw.Icon(u"e:\\system\\apps\\itqpda-s_r\\osama.mbm", 38, 39)
     icon2 = appuifw.Icon(u"e:\\system\\apps\\itqpda-s_r\\osama.mbm", 04, 05)
     icon3 = appuifw.Icon(u"e:\\system\\apps\\itqpda-s_r\\osama.mbm", 10, 11)

     icon5 = appuifw.Icon(u"e:\\system\\apps\\itqpda-s_r\\osama.mbm", 40, 41)
     icon6 = appuifw.Icon(u"e:\\system\\apps\\itqpda-s_r\\osama.mbm", 10, 11)
     icon4 = appuifw.Icon(u"e:\\system\\apps\\itqpda-s_r\\osama.mbm",12,13)

# create your content list of your listbox including the icons to be used for each entry
     entries = [(ar('   Record'), icon1),(ar('   Play  >'), icon5),(ar('   Stop  []'), icon3),
           (ar('   Open Song'), icon4),(ar('   Record Type'), icon2)]

     def set_type():
         tp = appuifw.popup_menu([u'1- amr', u'2- wav'], ar('Type of recorded Sound'))
         if tp==0:
           settings.TYPE = u'amr'
           std()
         elif tp==1:
           settings.TYPE = u'wav'
           std()

     def rec():
         global S
         S=audio.Sound.open(filename)
         S.record()
         appuifw.query(ar('Recording.......\nPress OK to stop recording'), "query")
         S.stop()


     def play():
         global S
         try:
             S=audio.Sound.open(filename)
            
             S.play()
             appuifw.note(ar('Playing'),"info")
             std()
         except:
             appuifw.note(ar('Record first a sound!'),"error")


     def stop():
         global S
         S.stop()

         S.close()
         appuifw.note(ar('Stopped'),"info")
         std()

     def open():
          appuifw.note(ar('Please Select a Sound '))
          filem = fm.manager()
          spa = filem.AskUser(path=u'e:\\sounds', find='file',ext=[(u'.amr'),(u'.wav'),(u'.mp3')])
          if spa:
                 if spa[-1] == '\\':
                    spa=spa[:-1]
                 if spa[-1] == '\\':
                    spa=spa[:-1]
          filename = spa
          global S
          try:
              S=audio.Sound.open(spa)
            
              S.play()
              appuifw.note(ar('Playing'),"info")
          except:
              appuifw.note(ar('Select a Sound!'),"error")

# create the listbox callback handler
     def fun():
        index = lb.current()
        if index ==0:rec()
        elif index ==1:play()
        elif index ==2:stop()
        elif index ==3:open()
        elif index ==4:set_type()
    

     lb = appuifw.Listbox(entries,fun)

     appuifw.app.body = lb




def opgal():
    e32.start_exe(u"z:\\system\\programs\\apprun.exe",ar("\"Z:\\System\\Apps\\MediaGallery\\MediaGallery.app\" "))

def about():
    appuifw.note(ar('Programed By\n  .: OsaMa :.'),"info")
    appuifw.note(ar('Keep visit\n  .: www.i-tich.net :.'),"info")

def exit():
    app_lock.signal()
    

appuifw.app.menu=[(ar('Media Center'),std),(ar('Open Gallery'),opgal),(ar('About'),about),(ar('Exit'),exit)]

appuifw.app.exit_key_handler = exit
app_lock = e32.Ao_lock()
app_lock.wait()