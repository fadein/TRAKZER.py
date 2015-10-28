#!/usr/bin/python

import subprocess

class RelayProxies(object):
    ''' Route my IP address through Relay Proxies because jargon '''
    def __init__(self, routed=False):
        self.routed = routed

    def hack_through_FBI_Firewall(self):
        ''' This part doesn't actually work yet... YOLO
        I sure hope this important message actually gets through! '''
        print "TODO: Hack thr0ugh the FBI's F1rewall\n"
        pass

class TRAKZER(object):
    ''' Luckily for me, these Russian Heroin smugglers don't read english too well
    I suppose that I could have used my Spanish-language abilities to obfuscate
    this, but I don't want to alienate any non-latinos who might see this '''
    def __init__(self):
        self.russian_gangsters = 3
        self.under_duress = True
        self.ip_address = RelayProxies(routed=True)

        # Obligitory hacker banner so my 17yro female haXor peers can
        # see how 13e7 I am
        print '''
*******************************************************************************************
_____________________    _____    ____  __._______________________________
\__    ___/\______   \  /  _  \  |    |/ _|\____    /\_   _____/\______   \\
  |    |    |       _/ /  /_\  \ |      <    /     /  |    __)_  |       _/
  |    |    |    |   \/    |    \|    |  \  /     /_  |        \ |    |   \\
  |____|    |____|_  /\____|__  /|____|__ \/_______ \/_______  / |____|_  /
__________.__      \/     ___ \/_      by\/        \/        \/  .______\/__         .__ 
\__    ___|  |__   ____  /   |   \  ___________  ____   ____   __| _\_____  \__  _  _|  |  
  |    |  |  |  \_/ __ \/    ~    \/  _ \_  __ \/    \_/ __ \ / __ | /   |   \ \/ \/ |  |  
  |    |  |   Y  \  ___/\    Y    (  <_> |  | \|   |  \  ___// /_/ |/    |    \     /|  |__
  |____|  |___|  /\___   \___|_  / \____/|__|  |___|  /\___  \____ |\_______  /\/\_/ |____/
Ver51on 1.0X0r \/     \/       \/   @TheHornedOwl   \/     \/     \/   2015 \/     
*******************************************************************************************
'''
    def get_ip_address(self):
        ''' return my IP address after routing it through Relay Proxies'''
        return self.ip_address.hack_through_FBI_Firewall()

    def lines(self, exe):
        ''' Doing things this way in Python is WAY fast0r than how you'd do
            this in Perl, #LOL!'''
        proc = subprocess.Popen(exe, shell=True, stdout=subprocess.PIPE)
        while True:
            line = proc.stdout.readline()
            if not line:
                break
            yield line
        
    def switch_to_Perl(self):
        ''' I'm trusting that the blonde girl will notice my subtle inside-joke,
            and that the murderous russi4n drug guys can't tell what I'm really
            up to. It's a good thing that I'm writing most of this in Python,
            or else I wouldn't have enough time to meet their arbitrary deadline!!!'''
        print "Switching to Perl for b/c 90's webpages are 31337 lolz :P"
        proc = self.lines("perl -e \"\$|=1;for (qw/Waiting because Perl is slowX0R/) { print qq{\t\$_...\n}; sleep 1 } printf '%c' x 43,112,108,101,97,115,101,32,115,97,118,101,32,109,101,32,102,114,111,109,32,116,104,101,32,114,117,115,115,105,97,110,32,103,97,110,103,32,103,117,121,115,33,10\"")
        for line in proc:
            print line,

if __name__ == "__main__":
    serious_business = TRAKZER()
    serious_business.get_ip_address()
    serious_business.switch_to_Perl()
