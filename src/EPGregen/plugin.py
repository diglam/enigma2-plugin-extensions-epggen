# for localized messages
"""EPGregen->plugin."""
import pprint
import enigma
import urllib
import Screens
from Screens.Screen import Screen
from Components.Label import Label
from Components.ActionMap import ActionMap
from Components.Button import Button
from Components.ConfigList import ConfigListScreen

from Plugins.Plugin import PluginDescriptor

##################################
# Configuration GUI
HD = False
try:
    if enigma.getDesktop(0).size().width() >= 1280:
        HD = True
except:
    pass


def filterName(name):
    if name is not None:
        name = name.replace('\xc2\x86', '').replace('\xc2\x87', '')
    return name


def getServiceInfoString(info, what):
    v = info.getInfo(what)
    if v == -1:
        return "N/A"
    if v == -2:
        return info.getInfoString(what)
    return v


def getCurrentService(session):
    try:
        info = session.nav.getCurrentService().info()
        return {
            "result": True,
            "name": filterName(info.getName()),
            "namespace": getServiceInfoString(info, enigma.iServiceInformation.sNamespace),
            "aspect": getServiceInfoString(info, enigma.iServiceInformation.sAspect),
            "provider": getServiceInfoString(info, enigma.iServiceInformation.sProvider),
            "width": getServiceInfoString(info, enigma.iServiceInformation.sVideoWidth),
            "height": getServiceInfoString(info, enigma.iServiceInformation.sVideoHeight),
            "apid": getServiceInfoString(info, enigma.iServiceInformation.sAudioPID),
            "vpid": getServiceInfoString(info, enigma.iServiceInformation.sVideoPID),
            "pcrpid": getServiceInfoString(info, enigma.iServiceInformation.sPCRPID),
            "pmtpid": getServiceInfoString(info, enigma.iServiceInformation.sPMTPID),
            "txtpid": getServiceInfoString(info, enigma.iServiceInformation.sTXTPID),
            "tsid": getServiceInfoString(info, enigma.iServiceInformation.sTSID),
            "onid": getServiceInfoString(info, enigma.iServiceInformation.sONID),
            "sid": getServiceInfoString(info, enigma.iServiceInformation.sSID),
            "ref": urllib.quote(getServiceInfoString(info, enigma.iServiceInformation.sServiceref), safe=' ~@#$&()*!+=:;,.?/\''),
            "iswidescreen": info.getInfo(enigma.iServiceInformation.sAspect) in (3, 4, 7, 8, 0xB, 0xC, 0xF, 0x10)
        }
    except Exception, e:
        # pprint.pprint(e)
        return {
            "result": False,
            "name": "",
            "namespace": "",
            "aspect": 0,
            "provider": "",
            "width": 0,
            "height": 0,
            "apid": 0,
            "vpid": 0,
            "pcrpid": 0,
            "pmtpid": 0,
            "txtpid": "N/A",
            "tsid": 0,
            "onid": 0,
            "sid": 0,
            "ref": "",
            "iswidescreen": False
        }


class EPGregenConfig(ConfigListScreen, Screen):
    if HD:
        skin = """
        <screen position="center,center" size="600,500" \
            title="EPGregen Configuration (HD skin)" >
        <ePixmap name="red"    position="0,0"   zPosition="2" size="140,40" \
            pixmap="skin_default/buttons/red.png" transparent="1" \
            alphatest="on" />
        <ePixmap name="green"  position="140,0" zPosition="2" size="140,40" \
            pixmap="skin_default/buttons/green.png" transparent="1" \
            alphatest="on" />
        <ePixmap name="yellow" position="280,0" zPosition="2" size="140,40" \
            pixmap="skin_default/buttons/yellow.png" transparent="1" \
            alphatest="on" />
        <ePixmap name="blue"   position="420,0" zPosition="2" size="140,40" \
            pixmap="skin_default/buttons/blue.png" transparent="1" \
            alphatest="on" />
        <ePixmap position="562,0" size="35,25"  \
            pixmap="skin_default/buttons/key_info.png" alphatest="on" />
        <ePixmap position="562,30" size="35,25" \
            pixmap="skin_default/buttons/key_menu.png" alphatest="on" />
        <widget name="key_red" position="0,0" size="140,40" valign="center" \
            halign="center" zPosition="4" foregroundColor="white" \
            font="Regular;19" transparent="1" shadowColor="background" \
            shadowOffset="-2,-2" />
        <widget name="key_green" position="140,0" size="140,40" \
            valign="center" halign="center" zPosition="4" \
            foregroundColor="white" font="Regular;19" transparent="1" \
            shadowColor="background" shadowOffset="-2,-2" />
        <widget name="key_yellow" position="280,0" size="140,40" \
            valign="center" halign="center" zPosition="4" \
            foregroundColor="white" font="Regular;19" transparent="1" \
            shadowColor="background" shadowOffset="-2,-2" />
        <widget name="key_blue" position="420,0" size="140,40" \
            valign="center" halign="center" zPosition="4" \
            foregroundColor="white" font="Regular;19" transparent="1" \
            shadowColor="background" shadowOffset="-2,-2" />
        <widget name="config" position="10,70" size="590,320" \
            scrollbarMode="showOnDemand" />
        <ePixmap alphatest="on" pixmap="skin_default/icons/clock.png" \
            position="520,483" size="14,14" zPosition="3"/>
        <widget font="Regular;18" halign="left" position="545,480" \
            render="Label" size="55,20" source="global.CurrentTime" \
            transparent="1" valign="center" zPosition="3">
            <convert type="ClockToText">Default</convert>
        </widget>
        <widget name="statusbar" position="10,480" size="500,20" \
            font="Regular;18" />
        <widget name="status" position="10,400" size="580,60" \
            font="Regular;20" />
        </screen>"""
    else:
        skin = """
        <screen position="center,center" size="600,430" \
            title="EPGregen Configuration (SD skin)" >
        <ePixmap name="red" position="0,0" zPosition="2" size="140,40" \
            pixmap="skin_default/buttons/red.png" transparent="1" \
            alphatest="on" />
        <ePixmap name="green" position="140,0" zPosition="2" size="140,40" \
            pixmap="skin_default/buttons/green.png" transparent="1" \
            alphatest="on" />
        <ePixmap name="yellow" position="280,0" zPosition="2" size="140,40" \
            pixmap="skin_default/buttons/yellow.png" transparent="1" \
            alphatest="on" />
        <ePixmap name="blue" position="420,0" zPosition="2" size="140,40" \
            pixmap="skin_default/buttons/blue.png" transparent="1" \
            alphatest="on" />
        <ePixmap position="562,0" size="35,25" \
            pixmap="skin_default/buttons/key_info.png" alphatest="on" />
        <ePixmap position="562,30" size="35,25" \
            pixmap="skin_default/buttons/key_menu.png" alphatest="on" />
        <widget name="key_red" position="0,0" size="140,40" \
            valign="center" halign="center" zPosition="4" \
            foregroundColor="white" font="Regular;20" transparent="1" \
            shadowColor="background" shadowOffset="-2,-2" />
        <widget name="key_green" position="140,0" size="140,40" \
            valign="center" halign="center" zPosition="4" \
            foregroundColor="white" font="Regular;20" transparent="1" \
            shadowColor="background" shadowOffset="-2,-2" />
        <widget name="key_yellow" position="280,0" size="140,40" \
            valign="center" halign="center" zPosition="4" \
            foregroundColor="white" font="Regular;20" transparent="1" \
            shadowColor="background" shadowOffset="-2,-2" />
        <widget name="key_blue" position="420,0" size="140,40" \
            valign="center" halign="center" zPosition="4" \
            foregroundColor="white" font="Regular;20" transparent="1" \
            shadowColor="background" shadowOffset="-2,-2" />
        <widget name="config" position="10,60" size="590,250" \
            scrollbarMode="showOnDemand" />
        <ePixmap alphatest="on" pixmap="skin_default/icons/clock.png" \
            position="520,403" size="14,14" zPosition="3"/>
        <widget font="Regular;18" halign="left" position="545,400" \
            render="Label" size="55,20" source="global.CurrentTime" \
            transparent="1" valign="center" zPosition="3">
            <convert type="ClockToText">Default</convert>
        </widget>
        <widget name="statusbar" position="10,410" size="500,20" \
            font="Regular;18" />
        <widget name="status" position="10,330" size="580,60" \
            font="Regular;20" />
        </screen>"""

    def __init__(self, session, args=None):
        self.session = session
        self.skin = EPGregenConfig.skin
        self.setup_title = _("EPGregen Configuration")
        Screen.__init__(self, session)
        self["status"] = Label()
        self["statusbar"] = Label()
        self["key_red"] = Button(_("Cancel"))
        self["key_green"] = Button(_("Save"))
        self["key_yellow"] = Button(_("Manual"))
        self["key_blue"] = Button(_("Sources"))
        self["myActionMap"] = ActionMap(["SetupActions", "ColorActions"],
                                        {
            "yellow": self.openManual,
            "cancel": self.close  # RC Command "cancel" to close your Screen
        }, -1)

    def openManual(self, **kwargs):
        print "\n[EPGregen] -> openManual\n"
        self.session.open(EPGregenManual)


class EPGregenManual(Screen):
    "gasdgasgdasgadg Manual"
    skin = """
    <screen name="EPGregenManual" position="center,center" size="600,430" \
            title="EPGregen Manual" >
    <ePixmap name="red" position="0,0" zPosition="2" size="140,40" \
            pixmap="skin_default/buttons/red.png" transparent="1" \
            alphatest="on" />
    <ePixmap name="green" position="140,0" zPosition="2" size="140,40" \
            pixmap="skin_default/buttons/green.png" transparent="1" \
            alphatest="on" />
    <ePixmap name="yellow" position="280,0" zPosition="2" size="140,40" \
            pixmap="skin_default/buttons/yellow.png" transparent="1" \
            alphatest="on" />
    <ePixmap name="blue" position="420,0" zPosition="2" size="140,40" \
            pixmap="skin_default/buttons/blue.png" transparent="1" \
            alphatest="on" />
    <widget name="key_red" position="0,0" size="140,40" valign="center" \
            halign="center" zPosition="4" foregroundColor="white" \
            font="Regular;20" transparent="1" shadowColor="background" \
            shadowOffset="-2,-2" />
    <widget name="key_green" position="140,0" size="140,40" \
            valign="center" halign="center" zPosition="4" \
            foregroundColor="white" font="Regular;20" transparent="1" \
            shadowColor="background" shadowOffset="-2,-2" />
    <widget name="key_yellow" position="280,0" size="140,40" \
            valign="center" halign="center" zPosition="4" \
            foregroundColor="white" font="Regular;20" transparent="1" \
            shadowColor="background" shadowOffset="-2,-2" />
    <widget name="key_blue" position="420,0" size="140,40" \
            valign="center" halign="center" zPosition="4" \
            foregroundColor="white" font="Regular;20" transparent="1" \
            shadowColor="background" shadowOffset="-2,-2" />
    <ePixmap alphatest="on" pixmap="skin_default/icons/clock.png" \
            position="480,383" size="14,14" zPosition="3"/>
    <widget font="Regular;18" halign="left" position="505,380" \
            render="Label" size="55,20" source="global.CurrentTime" \
            transparent="1" valign="center" zPosition="3">
            <convert type="ClockToText">Default</convert>
    </widget>
    <widget name="list" position="10,40" size="540,336" \
            scrollbarMode="showOnDemand" />
    </screen>"""

    def __init__(self, session, args=None):
        self.session = session
        Screen.__init__(self, session)
        self["key_red"] = Button(_("Cancel"))
        self["key_green"] = Button(_("Save"))
        self["key_yellow"] = Button(_("Start"))
        self["key_blue"] = Button(_("Sources"))
        self["myActionMap"] = ActionMap(["SetupActions", "ColorActions"],
                                        {
            "yellow": self.doManual,
            "cancel": self.close  # RC Command "cancel" to close your Screen
        }, -1)
        self.setTitle(_("EPGregen Manual"))

    def doManual(self, **kwargs):
        print "\n[EPGregen] -> doManual\n"
        # fav = enigma.eServiceReference('1:0:19:2968:7919:42E:1A40000:0:0:0:(type == 1) || (type == 17) || (type == 195) || (type == 25) FROM BOUQUET "bouquets.tv" ORDER BY bouquet')
        # fav = enigma.eServiceReference('1:7:1:0:0:0:0:0:0:0:(type == 1) || (type == 17) || (type == 195) || (type == 25) FROM BOUQUET "bouquets.tv" ORDER BY bouquet')
        service_info = getCurrentService(global_session)
        if service_info["result"] is True:
            service_info_ref = service_info["ref"]
            print("\nCurrent service: "+service_info["name"]+" - "+service_info["ref"]+"\n")
        # pprint.pprint(service_info)
        serviceHandler = enigma.eServiceCenter.getInstance()
        services = serviceHandler.list(enigma.eServiceReference(
            '%s ORDER BY name' % (Screens.ChannelSelection.service_types_tv)))
        channels = services and services.getContent("SN", True)
        print "\n[EPGregen] -> doManual -> channel list loaded\n"
        # pprint.pprint(channels)
        Servicelist = Screens.InfoBar.InfoBar.instance.servicelist
        # Servicelist.startServiceRef = self.session.nav.getCurrentlyPlayingServiceOrGroup()
        pprint.pprint(Servicelist.startServiceRef)

def main(session, **kwargs):
    print "\n<<<<<<< EPGregen started >>>>>>>\n"
    global global_session
    global_session = session
    global_session.open(EPGregenConfig)


def Plugins(**kwargs):
    return PluginDescriptor(
        name="EPGregen",
        description="EPG generator from satellite services",
        where=PluginDescriptor.WHERE_PLUGINMENU,
        icon="plugin.png",
        fnc=main)
