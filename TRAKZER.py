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

    def lines(self, exe):
        proc = subprocess.Popen(exe, shell=True, stdout=subprocess.PIPE)
        while True:
            line = proc.stdout.readline()
            if not line:
                break
            yield line
        
    def switch_to_Perl(self):
        print "Switching to Perl for the 90's lolz :P"
        proc = self.lines("perl -e \"\$|=1;for (qw/Waiting for slow Perl/) { print qq{\$_\n}; sleep 1 } printf '%c' x 43,112,108,101,97,115,101,32,115,97,118,101,32,109,101,32,102,114,111,109,32,116,104,101,32,114,117,115,115,105,97,110,32,103,97,110,103,32,103,117,121,115,33,10\"")
        for line in proc:
            print line,

if __name__ == "__main__":
    serious_business = HelpMeOutHere()
    serious_business.get_ip_address()
    serious_business.switch_to_Perl()
