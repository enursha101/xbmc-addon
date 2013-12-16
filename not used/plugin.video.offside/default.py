import urllib,urllib2,sys,re,xbmcplugin,xbmcgui,xbmcaddon,xbmc,os
import datetime
import time
from t0mm0.common.net import Net
import tvguide

PLUGIN='plugin.video.offside'
ADDON = xbmcaddon.Addon(id=PLUGIN)
deletepy = xbmc.translatePath(os.path.join(ADDON.getAddonInfo('path'),ADDON.getSetting('delete')))
image='http://www.xunitytalk.com/oss/'
country=os.path.join(ADDON.getAddonInfo('path'),'resources','country')
auth=ADDON.getSetting('auth')
forOffset=tvguide.offset_time()
forOffset_gmt=tvguide.offset_gmt()
print '####################################'


    
net=Net()




def OPEN_URL(url):
    req = urllib2.Request(url, headers={'User-Agent' : "Magic Browser"}) 
    con = urllib2.urlopen( req )
    link= con.read()
    return link


if ADDON.getSetting('user')=='':
    dialog = xbmcgui.Dialog()
    dialog.ok("OffSide Streams", "You Now Need To Input", "Your [COLOR yellow]Username[/COLOR]")
    search_entered = ''
    keyboard = xbmc.Keyboard(search_entered, 'OffSide Streams')
    keyboard.doModal()
    if keyboard.isConfirmed():
        search_entered = keyboard.getText() 
    ADDON.setSetting('user',search_entered)
    
    dialog.ok("OffSide Streams", "You Now Need To Input", "Your [COLOR yellow]Password[/COLOR]")
    search_entered = ''
    keyboard = xbmc.Keyboard(search_entered, 'OffSide Streams')
    keyboard.doModal()
    if keyboard.isConfirmed():
        search_entered = keyboard.getText() 
    ADDON.setSetting('pass',search_entered)
    
    countryselect=['USA','Europe']
    server=['0','1']
    region=server[xbmcgui.Dialog().select('Please Select Server', countryselect)]
    ADDON.setSetting('server',region)
    
    
    
def DownloaderClass(url,dest):
    dp = xbmcgui.DialogProgress()
    dp.create("OffSide Streams","Downloading",'[COLOR yellow]UPDATING NEW PLUGIN[/COLOR]')
    urllib.urlretrieve(url,dest,lambda nb, bs, fs, url=url: _pbhook(nb,bs,fs,url,dp))
 
def _pbhook(numblocks, blocksize, filesize, url=None,dp=None):
    try:
        percent = min((numblocks*blocksize*100)/filesize, 100)
        dp.update(percent)
    except:
        percent = 100
        dp.update(percent)
    if dp.iscanceled(): 
        raise Exception("Canceled")
        dp.close()
        
        
    
updatetxt='http://xbmc-hub-repo.googlecode.com/svn/maintenance_do_not_touch/hubmaintenance/update.txt'    
site='http://offsidestreams.com/site/live-tv/'
calendar='https://www.google.com/calendar/embed?showTitle=0&showPrint=0&showTabs=0&showCalendars=0&mode=AGENDA&height=600&wkst=2&bgcolor=%23FFFFFF&src=synxtv%40gmail.com&color=%23875509&ctz='+ADDON.getSetting('timezone')
datapath = xbmc.translatePath(ADDON.getAddonInfo('profile'))
cookie_path = os.path.join(datapath, 'cookies')
cookie_jar = os.path.join(cookie_path, "offside_new.lwp")
    

def LOGIN():
    loginurl = 'http://offsidestreams.com/site/wp-login.php'
    username    =ADDON.getSetting('user')
    password =ADDON.getSetting('pass')
    
    data     = {'pwd': password,
                                            'log': username,
                                            'wp-submit': 'Log In','redirect_to':'http://offsidestreams.com/site','testcookie':'1'}
    headers  = {'Host':'offsidestreams.com',
                                            'Origin':'http://offsidestreams.com',
                                            'Referer':'http://offsidestreams.com/site/wp-login.php',
                                                    'X-Requested-With':'XMLHttpRequest'}
    html = net.http_POST(loginurl, data, headers)
    
    if os.path.exists(cookie_path) == False:
            os.makedirs(cookie_path)
    net.save_cookies(cookie_jar)
    
    
if os.path.exists(cookie_jar) == False:
        LOGIN()


def server():
    quality = ADDON.getSetting('server')
    if quality == '0':
        return 'http://offsidestreams.com/site/nl-channels.js'
    elif quality == '1':
        return 'http://offsidestreams.com/site/nl-channels.js'

def CATEGORIES():
    addDir('[COLOR red]Full Match Replays HD[/COLOR]','url',3,'','','','')
    try:
        link = OPEN_URL(server())
        link = link.split('window.channels =')[1]
        match = re.findall('"title": "(.+?)".+?"file": "(.+?)",',link,re.M|re.DOTALL)
        for _name,url in match:
            iconimage=image+_name.replace(' ','%20').replace('i/H','i-H')+'.png'
            if ADDON.getSetting('tvguide')=='true':
                try:
                    name=_name+'[COLOR yellow]%s[/COLOR]'% tvguide.tvguide(_name)
                except:
                    name=_name
            else:
                name=_name
            addDir(name,url,2,iconimage,'False','',_name)
        xbmcplugin.addSortMethod(int(sys.argv[1]), xbmcplugin.SORT_METHOD_VIDEO_TITLE)            
    except:
        dialog = xbmcgui.Dialog()
        dialog.ok("[COLOR yellow]OffSide Streams [/COLOR]","[COLOR red]Login ERROR! [/COLOR]", "Do You Have An Account Set Up ?", "[COLOR yellow]www.offsidestreams.com[/COLOR]")
        xbmc.executebuiltin("XBMC.Container.Update(path,replace)")
        xbmc.executebuiltin("XBMC.ActivateWindow(Home)")
        
        
def offset_time(name):
    quality = ADDON.getSetting(name)
    if quality == '0':
        return '-12'
    elif quality == '1':
        return '-11'
    elif quality == '2':
        return '-10'
    elif quality == '3':
        return '-9'
    elif quality == '4':
        return '-8'
    elif quality == '5':
        return '-7'
    elif quality == '6':
        return '-6'
    elif quality == '7':
        return '-5'
    elif quality == '8':
        return '-4'
    elif quality == '9':
        return '-3'
    elif quality == '10':
        return '-2'
    elif quality == '11':
        return '-1'
    elif quality == '12':
        return '0'
    elif quality == '13':
        return '+1'
    elif quality == '14':
        return '+2'
    elif quality == '15':
        return '+3'
    elif quality == '16':
        return '+4'
    elif quality == '17':
        return '+5'
    elif quality == '18':
        return '+6'
    elif quality == '19':
        return '+7'
    elif quality == '20':
        return '+8'
    elif quality == '21':
        return '+9'
    elif quality == '22':
        return '+10'
    elif quality == '23':
        return '+11'
    elif quality == '24':
        return '+12'
        
        
def month(name):
    print name
    if 'Jan' in name:
        return '01'
    elif 'Feb' in name:
        return '02'
    elif 'Mar' in name:
        return '03'
    elif 'Apr' in name:
        return '04'
    elif 'May' in name:
        return '05'
    elif 'Jun' in name:
        return '06'
    elif 'Jul'in name:
        return '07'
    elif 'Aug' in name:
        return '08'
    elif 'Sep' in name:
        return '09'
    elif 'Oct' in name:
        return '10'
    elif 'Nov' in name:
        return '11'
    elif 'Dec' in name:
        return '12'
        
def _ret_time(start):
    start = getTime(start)

    return start.strftime('%d-%m-%Y')
        
        
def schedule(name,url,iconimage):
    name=iconimage.split('06/')[1].replace('.png','')
    if 'COLOR' in name:
         name=name.split('[')[0]
         For_Name=name
    else:
         For_Name=name
         
    For_Name=name
         
    if 'Al Jazeera' in For_Name:
        url    =  'http://www.en.aljazeerasport.tv/fragment/aljazeera/fragments/components/ajax/channelList/channel/plus%s/maxRecords/0'%(name.split('  ')[1])  
        link   =  OPEN_URL(url).replace('\n','').replace('  ','')
        link   =  link.split('<h')[1]
        _date  =  re.compile('>(.+?) (.+?) (.+?)<span class="arrow">', re.M|re.DOTALL).findall(link)
        day    =  _date[0][0]
        _month =  month(_date[0][1])
        year   =  _date[0][2]
        
        
        if '+' in forOffset:
            Z= forOffset.split('+')[1]
        elif '-' in forOffset:
            Z= forOffset.split('-')[1]
            
        pattern='<td class="eventsCell hardAlign">(.+?)</td.+?<td class="category">(.+?)</td>.+?<td class="startTime">(.+?):(.+?)</td>'
        match = re.compile(pattern, re.M|re.DOTALL).findall(link)
        for game,league,hour,minute in match:
        
            if '+' in forOffset:
            
                t   =   datetime.datetime(int(year), int(_month) , int(day), int(hour), int(minute), 00)
                t  +=   datetime.timedelta(hours = int(Z))
                
            if '-' in forOffset:
            
                t   =   datetime.datetime(int(year), int(_month) , int(day), int(hour), int(minute), 00)
                t  -=   datetime.timedelta(hours = int(Z))
                
            else:
                t  =    datetime.datetime(int(year), int(_month) , int(day), int(hour), int(minute), 00)
                
                
                
            #hour=int(hour)+int(ADDON.getSetting('timefrom'))
            game_league=game+' ('+league+')'
            _name_='[COLOR white][%s]-[/COLOR][COLOR yellow][B]%s[/B][/COLOR]'%(t.strftime('%H:%M'),game_league)
            addDir(_name_,'url',2,iconimage.replace('  ',' +').replace(' ','%20'),'True','',name)

    elif 'Sky' in For_Name:
        url=tvguide.fulltvguide(name)
        link=OPEN_URL(url)
        _date  =  re.compile('<!-- produced for the bleb.org TV system at .+? (.+?) (.+?) .+? (.+?) -->', re.M|re.DOTALL).findall(link)
        day    =  _date[0][1]
        _month =  month(_date[0][0])
        year   =  _date[0][2]
        
        match=re.findall('<title>(.+?)</title>.+?<start>(.+?)</start>',link,re.M|re.DOTALL)
        for _name,start in match:
            hour=start[0:2]
            minute=start[2:4]
            if '+' in forOffset_gmt:
                Z   =   forOffset_gmt.split('+')[1]
                t   =   datetime.datetime(int(year), int(_month) , int(day), int(hour), int(minute), 00)+ datetime.timedelta(hours = int(Z))
                time  =    t.strftime('%H:%M')
                
            elif '-' in forOffset_gmt:
                Z= forOffset_gmt.split('-')[1]
                t   =   datetime.datetime(int(year), int(_month) , int(day), int(hour), int(minute), 00)- datetime.timedelta(hours = int(Z))
                t  =    t.strftime('%H:%M')
                time  =    t.strftime('%H:%M')
            else:
                t  =    datetime.datetime(int(year), int(_month) , int(day), int(hour), int(minute), 00)
                time  =    t.strftime('%H:%M')
                
            name_='[COLOR white][%s]-[/COLOR][COLOR yellow][B]%s[/B][/COLOR]'%(time,_name)
            addDir(name_,url,2,iconimage.replace(' ','%20').replace('i/H','i-H'),'True','',For_Name)
    else:
        dialog = xbmcgui.Dialog()
        dialog.ok("OffSide Streams", '',"Sorry No Schedule Found", "")
        xbmc.executebuiltin('XBMC.Container.Update(%s?mode=None&url=None,replace)'%sys.argv[0])
        
        
def maxVideoQuality():
    quality = ADDON.getSetting("maxVideoQuality")
    if quality == '0':
        return '480p'
    elif quality == '1':
        return '720p'
    elif quality == '2':
        return '1080p'
        
        
        
def REPLAY():
        ok=True
        cmd = 'plugin://plugin.video.footballreplays/'
        xbmc.executebuiltin('XBMC.Container.Update(%s)' % cmd)
        return ok
 
        
 
    
def OPEN_MAGIC(url):
    req = urllib2.Request(url)
    req.add_header('User-Agent' , "Magic Browser")
    response = urllib2.urlopen(req)
    link=response.read()
    response.close()
    return link
        
        
        
        
        
    
def fullguide(name,url,iconimage,description):
    description=description.split('[COLOR yellow]')[0]
    url=tvguide.fulltvguide(description)
    link=OPEN_URL(url)
    match=re.findall('<title>(.+?)</title>.+?<start>(.+?)</start>',link,re.M|re.DOTALL)
    for _name,start in match:
        hours=start[0:2]+':'+start[2:4]
        name_='[COLOR white][%s]-[/COLOR][COLOR yellow][B]%s[/B][/COLOR]'%(hours,_name)
        addDir(name_,url,2,iconimage.replace(' ','%20').replace('i/H','i-H'),'True','',description)
    xbmcplugin.addSortMethod(int(sys.argv[1]), xbmcplugin.SORT_METHOD_TITLE)      
        
        
def Grab_Day(date):
    year, month, day = (int(x) for x in date.split('-'))    
    ans=datetime.date(year,month,day)
    return (ans.strftime("%a"))
        
    
def PLAY_STREAM(name,url,iconimage,play,description):
    dp = xbmcgui.DialogProgress()
    
    if play=='True':
        dp.create("Offside Streams","Starting To Stream.....",description, ' ')
        desc=description.replace('%20',' ').replace('i-H','i/H').replace('  ',' +')
        link = OPEN_URL(server())
        link = link.split('"title": "')
        r='"file": "(.+?)",'
        for p in link:
            if desc in p:
                match = re.findall(r,p,re.M|re.DOTALL)
                rtmp=match[0]
                import base64
                print '###############  AUTH   WORKING         #####################'
                stream_url='%s swfUrl=http://p.jwpcdn.com/6/7/jwplayer.flash.swf app=liveedge?wmsAuthSign=%s pageUrl=%s timeout=10'%(rtmp.replace('" + urlkey1 + "',base64.b64decode(auth)),base64.b64decode(auth),site)
                liz=xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
                liz.setInfo( type="Video", infoLabels={ "Title": description} )
                liz.setProperty("IsPlayable","true")
                pl = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)
                pl.clear()
                pl.add(stream_url, liz)
                xbmc.Player().play(pl)
                if not xbmc.Player() .isPlaying():
                    try:
                            import base64
                            print '###############  AUTH   EXCEPT   WITHOUT LOGIN     #####################'
                            net.set_cookies(cookie_jar)
                            html = net.http_GET(site).content
                            var = re.findall('urlkey1 = "(.+?)"',html,re.M|re.DOTALL)
                            ADDON.setSetting('auth',var[0].encode('base64','strict'))
                            stream_url='%s swfUrl=http://p.jwpcdn.com/6/7/jwplayer.flash.swf app=liveedge?wmsAuthSign=%s pageUrl=%s timeout=10'%(rtmp.replace('" + urlkey1 + "',var[0]),var[0],site)
                            liz=xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
                            liz.setInfo( type="Video", infoLabels={ "Title": description} )
                            liz.setProperty("IsPlayable","true")
                            pl = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)
                            pl.clear()
                            pl.add(stream_url, liz)
                            xbmc.Player().play(pl)
                    except:
                            import base64
                            print '###############  AUTH  EXCEPT WITH LOGIN       #####################'
                            LOGIN()
                            net.set_cookies(cookie_jar)
                            html = net.http_GET(site).content
                            var = re.findall('urlkey1 = "(.+?)"',html,re.M|re.DOTALL)
                            ADDON.setSetting('auth',var[0].encode('base64','strict'))
                            stream_url='%s swfUrl=http://p.jwpcdn.com/6/7/jwplayer.flash.swf app=liveedge?wmsAuthSign=%s pageUrl=%s timeout=10'%(rtmp.replace('" + urlkey1 + "',var[0]),var[0],site)
                            liz=xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
                            liz.setInfo( type="Video", infoLabels={ "Title": description} )
                            liz.setProperty("IsPlayable","true")
                            pl = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)
                            pl.clear()
                            pl.add(stream_url, liz)
                            xbmc.Player().play(pl)
                dp.close()
    else:
        dp.create("Offside Streams","Starting To Stream.....",name, ' ')
        import base64
        print '###############  AUTH   WORKING         #####################'
        stream_url='%s swfUrl=http://p.jwpcdn.com/6/7/jwplayer.flash.swf app=liveedge?wmsAuthSign=%s pageUrl=%s timeout=10'%(url.replace('" + urlkey1 + "',base64.b64decode(auth)),base64.b64decode(auth),site)
        liz=xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": description} )
        liz.setProperty("IsPlayable","true")
        pl = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)
        pl.clear()
        pl.add(stream_url, liz)
        xbmc.Player().play(pl)
        if not xbmc.Player() .isPlaying():
            try:
	            import base64
	            print '###############  AUTH   EXCEPT   WITHOUT LOGIN     #####################'
	            net.set_cookies(cookie_jar)
	            html = net.http_GET(site).content
	            var = re.findall('urlkey1 = "(.+?)"',html,re.M|re.DOTALL)
	            ADDON.setSetting('auth',var[0].encode('base64','strict'))
	            stream_url='%s swfUrl=http://p.jwpcdn.com/6/7/jwplayer.flash.swf app=liveedge?wmsAuthSign=%s pageUrl=%s timeout=10'%(url.replace('" + urlkey1 + "',var[0]),var[0],site)
	            liz=xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
	            liz.setInfo( type="Video", infoLabels={ "Title": description} )
	            liz.setProperty("IsPlayable","true")
	            pl = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)
	            pl.clear()
	            pl.add(stream_url, liz)
	            xbmc.Player().play(pl)
            except:
	            import base64
	            print '###############  AUTH  EXCEPT WITH LOGIN       #####################'
	            LOGIN()
	            net.set_cookies(cookie_jar)
	            html = net.http_GET(site).content
	            var = re.findall('urlkey1 = "(.+?)"',html,re.M|re.DOTALL)
	            ADDON.setSetting('auth',var[0].encode('base64','strict'))
	            stream_url='%s swfUrl=http://p.jwpcdn.com/6/7/jwplayer.flash.swf app=liveedge?wmsAuthSign=%s pageUrl=%s timeout=10'%(url.replace('" + urlkey1 + "',var[0]),var[0],site)
	            liz=xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
	            liz.setInfo( type="Video", infoLabels={ "Title": description} )
	            liz.setProperty("IsPlayable","true")
	            pl = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)
	            pl.clear()
	            pl.add(stream_url, liz)
	            xbmc.Player().play(pl)
        dp.close()
            
        
def EXIT():
        xbmc.executebuiltin("XBMC.Container.Update(path,replace)")
        xbmc.executebuiltin("XBMC.ActivateWindow(Home)")
        
         
            
            
            
            
                     
        
        
    
def get_params():
        param=[]
        paramstring=sys.argv[2]
        if len(paramstring)>=2:
                params=sys.argv[2]
                cleanedparams=params.replace('?','')
                if (params[len(params)-1]=='/'):
                        params=params[0:len(params)-2]
                pairsofparams=cleanedparams.split('&')
                param={}
                for i in range(len(pairsofparams)):
                        splitparams={}
                        splitparams=pairsofparams[i].split('=')
                        if (len(splitparams))==2:
                                param[splitparams[0]]=splitparams[1]
                                
        return param

def addDir(name,url,mode,iconimage,play,date,description,page=''):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(iconimage)+"&play="+urllib.quote_plus(play)+"&date="+urllib.quote_plus(date)+"&description="+urllib.quote_plus(description)+"&page="+str(page)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name,"Premiered":date,"Plot":description} )
        menu=[]
        menu.append(('[COLOR yellow]Schedule[/COLOR]','XBMC.Container.Update(%s?mode=200&url=None&description=%s&name=%s&play=False&iconimage=%s)'% (sys.argv[0],description,name,iconimage)))
        liz.addContextMenuItems(items=menu, replaceItems=False)
        if mode == 2000 or mode==2:
            ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=False)
        else:
            ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz)
        return ok
 
        
#below tells plugin about the views                
def setView(content, viewType):
        # set content type so library shows more views and info
        if content:
                xbmcplugin.setContent(int(sys.argv[1]), content)
        if ADDON.getSetting('auto-view') == 'true':#<<<----see here if auto-view is enabled(true) 
                xbmc.executebuiltin("Container.SetViewMode(%s)" % ADDON.getSetting(viewType) )#<<<-----then get the view type
                      
               
params=get_params()
url=None
name=None
mode=None
iconimage=None
date=None
description=None
page=None

try:
        url=urllib.unquote_plus(params["url"])
except:
        pass
try:
        name=urllib.unquote_plus(params["name"])
except:
        pass
try:
        iconimage=urllib.unquote_plus(params["iconimage"])
except:
        pass
try:        
        mode=int(params["mode"])
except:
        pass
try:
        play=urllib.unquote_plus(params["play"])
except:
        pass
try:
        date=urllib.unquote_plus(params["date"])
except:
        pass
try:
        description=urllib.unquote_plus(params["description"])
except:
        pass
try:        
        page=int(params["page"])
except:
        pass
   
        
#these are the modes which tells the plugin where to go
if mode==None or url==None or len(url)<1:
        print ""
        CATEGORIES()
               
elif mode==2:
        PLAY_STREAM(name,url,iconimage,play,description)
        
elif mode==3:
        REPLAY()
        
elif mode==200:
        schedule(name,url,iconimage)
        
elif mode==201:
        fullguide(name,url,iconimage,description)
        
elif mode==2001:
        ADDON.openSettings()
        
        
elif mode==2000:
        PLAYSTREAM(name,url,iconimage)
       
xbmcplugin.endOfDirectory(int(sys.argv[1]))
