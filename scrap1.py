import json , sys , hashlib , os , time , urllib3, getpass
batire = []
Bocaeh = []
try:
    import requests
except ImportError:
    print (logo)
    sys.exit()
logo=('''
  ____                    ____              _    
 / ___|  __ _ _ __       | __ )  ___   ___ | | __
 \___ \ / _` | '_ \ _____|  _ \ / _ \ / _ \| |/ /
  ___) | (_| | | | |_____| |_) | (_) | (_) |   < 
 |____/ \__,_|_| |_|     |____/ \___/ \___/|_|\_\
                                                 
''')
def baliho():
    try:
        token = open('cookie/token.log','r').read()
        UserMlebu = requests.get('https://graph.facebook.com/me?access_token=' + token)
        diCeluk = json.loads(UserMlebu.text)
        name = diCeluk['name']
        Bocaeh.append(diCeluk['name'])
        print (logo)
        print ('Anda login menggunakan akun '   '[' + name+ ']')

    except (KeyError,IOError):
        print (logo)


def menu_awal():
    print (logo)
    print ('''
    [  home  ]               [  login ]
                [ recyle ]
    [ logout ]               [  exit  ]
''')


def menu_recyle():
    print ('''
   PILIHAN      INFO
 ---------   ------------------------------------
    [ 01 ]      posts
    [ 02 ]      tagged
    [ 03 ]      photos
    [ 04 ]      albums
    [ 05 ]      videos
    [ 06 ]      friends
    [ 07 ]      friendrequests
    [ 08 ]      subscribedto
    [ 09 ]      inbox
    [ 10 ]      groups

    [ 00 ]      back to main menu
''')


def get(data):
    print ('[*] Generate access token ')

    try:
        os.mkdir('cookie')
    except OSError:
        pass

    b = open('cookie/token.log','w')
    try:
        r = requests.get('https://api.facebook.com/restserver.php',params=data)
        a = json.loads(r.text)

        b.write(a['access_token'])
        b.close()
        print ('[*] successfully generate access token')
        print ('[*] Your access token is stored in cookie/token.log')
        exit()
    except KeyError:
        print ('[!] Failed to generate access token')
        print ('[!] Check your connection / email or password')
        os.remove('cookie/token.log')
        main()
    except requests.exceptions.ConnectionError:
        print ('[!] Failed to generate access token')
        print ('[!] Connection error !!!')
        os.remove('cookie/token.log')
        main()
def id():
    print ('[*] login to your facebook account         ');id = raw_input('[?] Username : ');pwd = getpass.getpass('[?] Password : ');API_SECRET = '62f8ce9f74b12f84c123cc23437a4a32';data = {"api_key":"882a8490361da98702bf97a021ddc14d","credentials_type":"password","email":id,"format":"JSON", "generate_machine_id":"1","generate_session_cookies":"1","locale":"en_US","method":"auth.login","password":pwd,"return_ssl_resources":"0","v":"1.0"};sig = ('api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail='+id+'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword='+pwd+'return_ssl_resources=0v=1.0'+API_SECRET).encode('utf-8')

    sanbook = hashlib.new('md5')
    sanbook.update(sig)
    data.update({'sig':sanbook.hexdigest()})
    get(data)


def mbusek_batire_nyong():
    global token
    os.system('clear')
    try:
        token = open('cookie/token.log','r').read()
    except IOError:
        print ('[!] Failed load access token   ')
        os.remove('cookie/token.log')
        id()
    print ('[!] MOHON TUNGGU SEDANG SCRAP DATA DAHULU')
    celenganeNangKene = requests.get('https://graph.facebook.com/v4.0/me/friends?access_token='+token)
    celenganeDipecahNangBatire = json.loads(celenganeNangKene.text)
    for cingire in celenganeDipecahNangBatire['data']:
        batire.append(cingire['id'])
        print ('\n[ ! ] UNFRIENDS %s dari daftar teman...')%(len(batire)),;sys.stdout.flush();time.sleep(0.0001)
        diPerentahNangKie = requests.delete('https://graph.facebook.com/me/friends?uid={id}&access_token={token}'.format(id=cingire['id'],token=token))
        mlebuneNangKene = json.loads(diPerentahNangKie.text)
        try:
            sing = mlebuneNangKene['error']['message']
            print ('\r[SEKITAR] '+str(len(batire))+' Teman gagal dihapus oleh program Sanbook...')
        except TypeError:
            print ('\r[SEBANYAK] '+str(len(batire))+' Teman berhasil dihapus karena mengecewakan...')
            print ('[*] done')
        except KeyboardInterrupt:
            print ('\r[!] Berhenti')
            recyle()
            
def main():
    global target_id
    try:
        cek = raw_input('Sanbook' ': ')
        if cek.lower() == 'home':
            menu_awal()
            main()
        elif cek.lower() == 'login':
            try:
                open('cookie/token.log')
                print ('[!] an access token already exists')
                cek = raw_input('[?] Are you sure you want to continue [Y/N] ')
                if cek.lower() != 'y':
                    print ('[*] Canceling ')
                    main()
            except IOError:
                pass
            print ('\n' + '[*] Generate Access token facebook [*]'+ '\n')
            print ('[Warn] please turn off your VPN before using this feature !!!')
            id()


        elif cek.lower() == 'recyle':
            
            menu_recyle()
            recyle()


        elif cek.lower() == 'logout':
            
            print ('''[!] Anda telah keluar facebook...''')
            
            a = raw_input("[!] type 'delete' to continue : ")
            
            if a.lower() == 'delete':
                
                try:
                    
                    os.system('rm -rf cookie/token.log')
                    
                    print ('[*] Success delete cookie/token.log')
                    
                    main()
                    
                except OSError:
                    
                    print ('[*] failed to delete cookie/token.log')
                    
                    main()
            else:
                
                print ('[*] failed to delete cookie/token.log')
                
                main()

        elif cek.lower() == 'exit':
            print ("[!] Exiting Program")
            sys.exit()
            
        elif cek.lower() == 'exit':
            print ("[!] SEMOGA BERSIL")
            mbusek_batire_nyong()

        else:
            
            if cek == '':
                main()
            else:
                print ("[!] command '"+cek+"' not found")
                print ('[!] type "help" to show command')
                main()
                
                
    except KeyboardInterrupt:
        main()
    except IndexError:
        print ('[!] invalid parameter on command : ' + cek)
        main()



if __name__ == '__main__':
    baliho()
    
    menu_awal()
    
    main()
