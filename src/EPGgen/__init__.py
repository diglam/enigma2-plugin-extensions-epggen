"""__init___."""
from Components.Language import language
from Tools.Directories import resolveFilename, SCOPE_PLUGINS
# import os
import gettext

PluginLanguageDomain = "EPGgen"
PluginLanguagePath = "Extensions/EPGgen/locale"


def localeinit():
    """localeinit."""
    gettext.bindtextdomain(PluginLanguageDomain, resolveFilename(
        SCOPE_PLUGINS, PluginLanguagePath))


def _(txt):
    t = gettext.dgettext(PluginLanguageDomain, txt)
    if t == txt:
        print "[" + PluginLanguageDomain + "] \
        fallback to default translation for ", txt
        t = gettext.gettext(txt)
    return t

localeinit()
language.addCallback(localeinit)
