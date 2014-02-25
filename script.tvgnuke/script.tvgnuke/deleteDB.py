
import os
import xbmc
import xbmcgui
import xbmcaddon

def deleteDB():
    try:
        xbmc.log("[script.tvgnuke] Deleting database...", xbmc.LOGDEBUG)
        dbPath = xbmc.translatePath(xbmcaddon.Addon(id = 'script.tvgnuke').getAddonInfo('profile'))
        dbPath = os.path.join(dbPath, 'source.db')

        delete_file(dbPath)
        
        passed = not os.path.exists(dbPath)

        if passed: 
            xbmc.log("[script.tvgnuke] Deleting database...PASSED", xbmc.LOGDEBUG)
        else:
            xbmc.log("[script.tvgnuke] Deleting database...FAILED", xbmc.LOGDEBUG)

        return passed

    except Exception, e:
        xbmc.log('[script.tvgnuke] Deleting database...EXCEPTION', xbmc.LOGDEBUG)
        return False

def delete_file(filename):
    tries = 10
    while os.path.exists(filename) and tries > 0: 
        try:             
            os.remove(filename) 
            break 
        except: 
            tries -= 1 

if __name__ == '__main__':
    if deleteDB():
        d = xbmcgui.Dialog()
        d.ok('NUKE TV GUIDE', 'Database successfully deleted.', 'It will be re-created next time', 'you start the guide')    
    else:
        d = xbmcgui.Dialog()
        d.ok('NUKE TV GUIDE', 'Failed to delete database.', 'Database may be locked,', 'please restart XBMC and try again')    


