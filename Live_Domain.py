#Author:    Zeyad Azima "zWIZARDz"
#Github:    https://github.com/Zeyad-Azima
#Facebook:  https://www.facebook.com/elkingzeyad.azeem
#Website:   https://cyberatom.org/
#Version:   v0.1

import requests
import os
import threading
from optparse import *
print('''
.____    .__                       ________                        .__        
|    |   |__|__  __ ____           \______ \   ____   _____ _____  |__| ____  
|    |   |  \  \/ // __ \   ______  |    |  \ /  _ \ /     \\__  \ |  |/    \ 
|    |___|  |\   /\  ___/  /_____/  |    `   (  <_> )  Y Y  \/ __ \|  |   |  \
|_______ \__| \_/  \___  >         /_______  /\____/|__|_|  (____  /__|___|  /
        \/             \/                  \/             \/     \/        \/ 
                  @ZeyadAzima
                     v0.1
''')
print("[+] Checking live domains: ")
print('')
def Parse():
    choose = OptionParser()
    choose.add_option("-l","--list",dest="list",help="Sub/domains list to check it")
    choose.add_option("-o","--output",dest="save",help="Save results in file")
    return choose.parse_args()
    if not options.list:
        print('[-] Please use -l and enter the domains list or use --help for more')
    elif options.list == '':
        print("[-] Please enter a domains list to check :(")
    elif options.save == '':
        print('[-] Please enter name for the txt file or use --help for more')


def Check_dir(list, save):
    if os.path.isfile(str(save)):
        print('[-] File: ', str(save), 'is exist')
        exit()
    elif not list:
        print('[-] Please use -l and enter the domains list or use --help for more')
        exit()
    else:
        file = open(list)
        subs = file.read()
        check = subs.splitlines()
        for live in check:
            domain = f'http://{live}'
            try:
                    req = requests.get(domain)
            except requests.ConnectionError:
                pass
            else:
                if not save:
                    if req.status_code == 200:
                        print('[+]:', domain + '/')
                elif save:
                    if req.status_code == 200:
                        print('[+]:', domain + '/')
                        file = open(save,'a')
                        file.write(domain)
                        file.write('/')
                        file.write('\n')
                        file.close()
    print("[+] list "+ save,"check is Done :]")

(options, arguments) = Parse()

def fast():
    thread = threading.Thread(target=Check_dir(options.list, options.save))
    thread.start()
    thread.join()


thread = threading.Thread(target=fast)
thread.start()
thread.join()
