# for localized messages
import enigma
from ui import EPGgenConfig


def main(session, **kwargs):
    session.open(EPGgenConfig)
