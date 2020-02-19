import random
import socket
import subprocess
import sys
import os
import time
from datetime import datetime
#dilarang recode
#Coded By Z03
#Kalo Pengen Bisa Ya Belajar Lah Tod!!
os.system("clear")
I='\33[0;32m'
GL='\33[32;1m'
B='\33[0;36m'
BL='\33[36;1m'	
M='\33[31;1m'	
P='\33[37;1m'	
D='\33[30;1m'
Y='\33[33;1m'	
YL='\33[1;33m'
print
subprocess.call('clear', shell=True)
time.sleep(1)
print "\33[1;33m    .hh+`                               -sd+  "    
print "\33[1;33m    ydhhmy/`   `..--.`     `---.`    -oddymd-     "
print "\33[1;33m    h/oyoyydyymhoosyhdho/yddhysosmdsdhysoy:h:     "
print "\33[1;33m    /d` -o+osds/+ooooymNMNhsooo+/+dyooo+` /d`     "
print "\33[1;33m     +h-`:o+/`` ``/-   :o`  `/.. ``-+++../d.      "
print "\33[1;33m      yNoo..+o.`.h/d-os/y-m.y+y:-`/s/`/oyN-       "
print "\33[1;33m     oy`  /hNo-s/o.: oohh+h` +:/oo`mNs.  :h.      "
print "\33[1;33m    os` : :/sh+o+/.` +:  .s. .:/s/sys:`.. :h.     "
print "\33[1;33m   /mo:s.-:-`+s+:o/d:-.` ..-oh:++:y: -o`+s-dh`    "
print "\33[1;33m    h`m`:s  /ymhdyo/-:-. -::-osdhmds. .y o+//     "
print "\33[1;33m   /o:N++:`/:s-:`so` ... --  .y--.+/+``s:dh`h     "
print "\33[1;33m  `dd+do+d .:`/yhd/:/-.-.`.+-:yymo`: .+d`Ny/m+   "
print "\33[1;33m  `+o o- ++   ohso. :/-..-:+` /ssh:  -y` h``d-    "
print "\33[1;33m  `d`.dh+.sy` sms:.` `s` /:  `-+hm- :h/:yd+ +o    "
print "\33[1;33m  od:  :yNy/o-/Nmo.`  `sd-   `:hNh./+oNm+.  sd.   "
print "\33[1;33m  -+//++:+hdo.`yNNs`h++/+/+y/.mNN/`+ddo::o///+    "
print "\33[1;33m    -oo/:-``/do`yNs.y::+s/:/s-hN-:do. .:/+s/`     "
print "\33[1;33m      `+yho` -hh.myd/   .   domood/. :yhs-        "
print "\33[1;33m       `.-/oso-`.oyNm-  `  sNyN.``+so/:.``        "
print "\33[1;33m             `+y-:dm:.`` ``:+hm +s-               "
print "\33[1;33m               `yomhs/++//+/hdhs/                 "
print "\33[1;33m                y `:///oy+//:-`-+                 "
print "\33[1;33m                -hy-`       .:ds`                 "
print "\33[1;33m                  `syys-`:ysy/`                   "
print "\33[1;33m                     `./o-.`                      "
time.sleep(2)
os.system('xdg-open https://github.com/kingcracker')
print "\33[36;1m\n\n(*)TOOLS : \33[32;1mWebsite Scanner"
time.sleep(1)
print "\33[33;1m<=========================================>"
time.sleep(1)
print "\33[36;1m(*)CREATOR & AUTHOR : \33[32;1mZ03"
time.sleep(1)
print "\33[33;1m<=========================================>"
time.sleep(1)
print "\33[36;1m(*)GITHUB : \33[32;1mhttps://github.com/kingcraker"
time.sleep(1)
print "\33[33;1m<=========================================>"
time.sleep(1)
print "\33[36;1m(*)CONTACT : \33[32;1mthecyberr31@gmail.com"
time.sleep(1)
print "\33[33;1m<=========================================>"
time.sleep(2)
print "\33[36;1mTOOLS INI DIBUAT SENDIRI ANTI RECODE CLUB2"
time.sleep(1)
print "\33[33;1m<=========================================>"
def tulis(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
#Buatnya Susah Kentod
        time.sleep(random.random() * 0.1)
#Tapi Boleh Pelajari Source Codenya :)
#Baik Kan Gw Cok :v
tulis('\33[36;1m\n\n(*)TOOLS INI MEMBUTUHKAN WAKTU AGAK LAMA\nSo Tinggal Yt/Musikan Dulu Aja v:')
print
print "\33[32;1m<=========================================>"
rs = raw_input("[=Masukan Hostname/web Nya=> ")
rsIP  = socket.gethostbyname(rs)

print "-" * 60
print "Sabar Cok, IP  Hostname/Website=>", rsIP
print "-" * 60

t1 = datetime.now()
try:
    for port in range(1,10):  
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((rsIP, port))
        if result == 0:
            print "Port {}: 	 Open".format(port)
        sock.close()

except KeyboardInterrupt:
    sys.exit()

except socket.gaierror:
    print 'Sorry,Hostname Tidak Bisa Diselesaikan.'
    sys.exit()

except socket.error:
    print "Tidak Dapat Connect Ke Server"
    sys.exit()

t2 = datetime.now()

total =  t2 - t1

print '@Scanning Completed => ', total

