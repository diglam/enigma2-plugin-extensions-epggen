# for localized messages
"""EPGgen->plugin."""

import enigma
from enigma import eServiceCenter
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


class EPGgenConfig(ConfigListScreen, Screen):
    if HD:
        skin = """
        <screen position="center,center" size="600,500" \
            title="EPGgen Configuration (HD skin)" >
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
            title="EPGgen Configuration (SD skin)" >
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
        self.skin = EPGgenConfig.skin
        self.setup_title = _("EPGgen Configuration")
        Screen.__init__(self, session)
        self["status"] = Label()
        self["statusbar"] = Label()
        self["key_red"] = Button(_("Cancel"))
        self["key_green"] = Button(_("Save"))
        self["key_yellow"] = Button(_("Manual"))
        self["key_blue"] = Button(_("Sources"))
        self["myActionMap"] = ActionMap(["SetupActions", "ColorActions"],
                                        {
            "yellow": self.doManual,
            "cancel": self.close  # RC Command "cancel" to close your Screen
        }, -1)

    def doManual(self, **kwargs):
        print "\n[EPGgen] -> doManual\n"
        self.session.open(EPGgenManual, kwargs["servicelist"])

        bouquet = self.servicelist.bouquet_root
        serviceHandler = eServiceCenter.getInstance()
        bouquetlist = serviceHandler.list(bouquet)
        bouquet = bouquetlist.getNext()
        servicelist = serviceHandler.list(bouquet)
        print servicelist


class EPGgenManual(Screen):
    "gasdgasgdasgadg Manual"
    skin = """
    <screen name="EPGgenManual" position="center,center" size="600,430" \
            title="EPGgen Manual" >
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
        self["status"] = Label()
        self["statusbar"] = Label()
        self["key_red"] = Button(_("Cancel"))
        self["key_green"] = Button(_("Save"))
        self["key_yellow"] = Button(_("Manual"))
        self["key_blue"] = Button(_("Sources"))
        self["myActionMap"] = ActionMap(["SetupActions"],
                                        {
            "cancel": self.close  # RC Command "cancel" to close your Screen
        }, -2)
        self.setTitle(_("EPGgen Manual"))


def main(session, **kwargs):
    print "\n<<<<<<< EPGgen started >>>>>>>\n"

    session.open(EPGgenConfig)


def Plugins(**kwargs):
    return PluginDescriptor(
        name="EPGgen",
        description="EPG generator from satellite services",
        where=PluginDescriptor.WHERE_PLUGINMENU,
        icon="plugin.png",
        fnc=main)
