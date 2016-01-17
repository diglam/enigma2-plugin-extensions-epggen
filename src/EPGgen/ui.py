"""EPGgen->ui."""

import enigma
from Screens.Screen import Screen
from Components.Label import Label
from Components.ActionMap import ActionMap
from Components.ConfigList import ConfigListScreen


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
            title="EPGgen Configuration HD skin" >
        <widget name="myLabel" position="10,60" \
            size="200,40" font="Regular;20"/>
        </screen>"""
    else:
        skin = """
        <screen position="center,center" size="600,430" \
            title="EPGgen Configuration SD skin" >
        <widget name="myLabel" position="10,60" \
            size="200,40" font="Regular;20"/>
        </screen>"""

    def __init__(self, session, args=None):
        self.session = session
        Screen.__init__(self, session)
        self["myLabel"] = Label("Hello World ;-)")
        self["myActionMap"] = ActionMap(["SetupActions"],
                                        {
            "cancel": self.close  # RC Command "cancel" to close your Screen
        }, -1)
