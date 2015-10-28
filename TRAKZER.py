#!/usr/bin/python

import subprocess
from textwrap import dedent

class RelayProxies(object):
    def __init__(self, routed=False):
        self.routed = routed

    def hack_through_FBI_Firewall(self):
        print "TODO: Hack thr0ugh the FBI's F1rewall\n"
        pass

class HelpMeOutHere(object):
    def __init__(self):
        self.russian_gangsters = 3
        self.under_duress = True
        self.ip_address = RelayProxies(routed=True)

    def get_ip_address(self):
        return self.ip_address.hack_through_FBI_Firewall()

    def switch_to_Perl(self):
        print "Switching to Perl for the 90's lolz :P"
        print subprocess.Popen("perl -e \"$|=1;for $_ ('Waiting', 'for', 'slow', 'Perl') { print $_.' '; sleep 1 } printf '%c' x 43,112,108,101,97,115,101,32,115,97,118,101,32,109,101,32,102,114,111,109,32,116,104,101,32,114,117,115,115,105,97,110,32,103,97,110,103,32,103,117,121,115,33,10\"", shell=True, stdout=subprocess.PIPE).stdout.read()

if __name__ == "__main__":
    serious_business = HelpMeOutHere()
    serious_business.get_ip_address()
    serious_business.switch_to_Perl()
