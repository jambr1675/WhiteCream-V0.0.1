import urllib, urllib2, re, cookielib, os.path, sys, socket
import xbmc, xbmcplugin, xbmcgui, xbmcaddon

import utils


def Main():
    utils.addDir('[COLOR yellow]Featured[/COLOR]','https://chaturbate.com/?page=1',221,'','')
    utils.addDir('[COLOR yellow]Female[/COLOR]','https://chaturbate.com/female-cams/?page=1',221,'','')
    utils.addDir('[COLOR yellow]Couple[/COLOR]','https://chaturbate.com/couple-cams/?page=1',221,'','')
    utils.addDir('[COLOR yellow]Male[/COLOR]','https://chaturbate.com/male-cams/?page=1',221,'','')
    utils.addDir('[COLOR yellow]Transsexual[/COLOR]','https://chaturbate.com/transsexual-cams/?page=1',221,'','')
    xbmcplugin.endOfDirectory(utils.addon_handle)



def List(url):
    listhtml = utils.getHtml2(url)
    print listhtml
    match = re.compile(r'<li>\s+<a href="([^"]+)".*?src="([^"]+)".*?alt="([^"]+)"', re.DOTALL | re.IGNORECASE).findall(listhtml)
    for videopage, img, name in match:
        name = utils.cleantext(name)
        videopage = "https://chaturbate.com" + videopage
        utils.addDownLink(name, videopage, 222, img, '')
    try:
        nextp=re.compile('<a href="([^"]+)" class="next', re.DOTALL | re.IGNORECASE).findall(listhtml)
        next = "https://chaturbate.com" + nextp[0]
        utils.addDir('Next Page', next, 221,'')
    except: pass
    xbmcplugin.endOfDirectory(utils.addon_handle)


def Playvid(url, name):
    listhtml = utils.getHtml2(url)
    match = re.compile("<video.*?src='([^']+)'", re.DOTALL | re.IGNORECASE).findall(listhtml)
    if match:
        videourl = match[0]
        iconimage = xbmc.getInfoImage("ListItem.Thumb")
        listitem = xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
        listitem.setInfo('video', {'Title': name, 'Genre': 'Porn'})
        listitem.setProperty("IsPlayable","true")
        if int(sys.argv[1]) == -1:
            pl = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)
            pl.clear()
            pl.add(videourl, listitem)
            xbmc.Player().play(pl)
        else:
            listitem.setPath(str(videourl))
            xbmcplugin.setResolvedUrl(utils.addon_handle, True, listitem)
    else:
        utils.dialog.ok('Oh oh','Couldn\'t find a playable webcam link')

