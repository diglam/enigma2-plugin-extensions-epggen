# for localized messages
import enigma
from Screens.Screen import Screen
from Components.ActionMap import ActionMap
from ui import EPGgenConfig

from Plugins.Plugin import PluginDescriptor


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
