#!/usr/bin/python

from i.am.being.held.hostage import save.me
import relay.proxies
from textwrap import dedent

class HelpMeOutHere(object):
    def __init__(self):
        self.russian_gangsters = 3
        self.under_duress = True
        self.ip_address = relay.proxies(routed=True)

    def get_ip_address(self):
        return self.ip_address.hack_through_FBI_Firewall()

    def switch_to_Perl(self):
        print dedent('''
        sub totally_legit_code_not_trying_to_be_sneaky_here {
            printf "%c" x 43,112,108,101,97,115,101,32,115,97,118,101,32,109,101,32,102,114,111,109,32,116,104,101,32,114,117,115,115,105,97,110,32,103,97,110,103,32,103,117,121,115,33,10;
        }
        ''').strip()

if __name__ == "__main__":
    serious_business = HelpMeOutHere()
    serious_business.switch_to_Perl()
