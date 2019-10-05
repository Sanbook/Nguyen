import json , sys , hashlib , os , time , getpass
reload (sys)
sys . setdefaultencoding ( 'utf8' )

try:
    import requests
except ImportError:
    print (logo)
    sys.exit()
logo=('''
    ╔═╗─╔╗╔═══╗╔╗─╔╗╔╗──╔╗╔═══╗╔═╗─╔╗ ┏━━━━━━━━━━━━━━━━━━━━┓
    ║║╚╗║║║╔═╗║║║─║║║╚╗╔╝║║╔══╝║║╚╗║║ ┃Tɪᴅᴀᴋ    Aᴅᴀ  Sʏsᴛᴇᴍ┃
    ║╔╗╚╝║║║─╚╝║║─║║╚╗╚╝╔╝║╚══╗║╔╗╚╝║ ┃Yɢ  Aᴍᴀɴ  Jɪᴋᴀ Mᴀsɪʜ┃
    ║║╚╗║║║║╔═╗║║─║║─╚╗╔╝─║╔══╝║║╚╗║║ ┃Dɪʙᴜᴀᴛ  Oʟᴇʜ  Tᴀɴɢᴀɴ┃
    ║║─║║║║╚╩═║║╚═╝║──║║──║╚══╗║║─║║║ ┃Mᴀɴᴜsɪᴀ, Pᴇʀᴄᴀʏᴀʟᴀʜ!┃
    ╚╝─╚═╝╚═══╝╚═══╝──╚╝──╚═══╝╚╝─╚═╝ ┗━━━━━━━━━━━━━━━━━━━━┛
''')
def baliho():
    try:
        token = open('cookie/token.log','r').read()
        r = requests.get('https://graph.facebook.com/me?access_token=' + token)
        a = json.loads(r.text)
        name = a['name']
        n.append(a['name'])
        print (logo)
        print ('Anda login menggunakan akun' + name + ).center(44)
        print ' '

    except (KeyError,IOError):
        print (logo)


def menu_awal():
    print '''
    [  home  ]               [  login ]
                [ recyle ]
    [ logout ]               [  exit  ]
'''


def menu_recyle():
    print '''
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
'''


def get(data):
    print '[*] Generate access token '

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
        print '[*] successfully generate access token'
        print '[*] Your access token is stored in cookie/token.log'
        exit()
    except KeyError:
        print '[!] Failed to generate access token'
        print '[!] Check your connection / email or password'
        os.remove('cookie/token.log')
        main()
    except requests.exceptions.ConnectionError:
        print '[!] Failed to generate access token'
        print '[!] Connection error !!!'
        os.remove('cookie/token.log')
        main()
def id():
    print '[*] login to your facebook account         ';id = raw_input('[?] Username : ');pwd = getpass.getpass('[?] Password : ');API_SECRET = '62f8ce9f74b12f84c123cc23437a4a32';data = {"api_key":"882a8490361da98702bf97a021ddc14d","credentials_type":"password","email":id,"format":"JSON", "generate_machine_id":"1","generate_session_cookies":"1","locale":"en_US","method":"auth.login","password":pwd,"return_ssl_resources":"0","v":"1.0"};sig = 'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail='+id+'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword='+pwd+'return_ssl_resources=0v=1.0'+API_SECRET
    x = hashlib.new('md5')
        x.update(sig)

    data.update({'sig':x.hexdigest()})
        get(data)


def recyle():
  try:
    global type, SAN , token

    cek = raw_input('Sanbook' '/''Recycle')

    if cek in ['1','01']:
        SAN = 'posts'
        print '[*] load access token    '

        try:
            token = open('cookie/token.log','r').read()
            print '[*] Success load access token'
        except IOError:
            print '[!] Failed load access token   '
            print "[!] type 'token' to generate access token"
            recyle()
        posts(post())



    elif cek in ['2','02']:
        SAN = 'tagged'
        print '[*] load access token    '

        try:
            token = open('cookie/token.log','r').read()
            print '[*] Success load access token'
        except IOError:
            print '[!] Failed load access token   '
            print "[!] type 'token' to generate access token"
            recyle()
        tagged(post())



    elif cek in ['3','03']:
        SAN = 'photos'
        print '[*] load access token    '

        try:
            token = open('cookie/token.log','r').read()
            print '[*] Success load access token'
        except IOError:
            print '[!] Failed load access token   '
            print "[!] type 'token' to generate access token"
            recyle()
        photos(post())



    elif cek in ['4','04']:
        SAN = 'albums'
        print '[*] load access token    '

        try:
            token = open('cookie/token.log','r').read()
            print '[*] Success load access token'
        except IOError:
            print '[!] Failed load access token   '
            print "[!] type 'token' to generate access token"
            recyle()
        albums(post())



    elif cek in ['5','05']:
        SAN = 'videos'
        print '[*] load access token    '

        try:
            token = open('cookie/token.log','r').read()
            print '[*] Success load access token'
        except IOError:
            print '[!] Failed load access token   '
            print "[!] type 'token' to generate access token"
            recyle()
        videos(post())



    elif cek in ['6','06']:
        SAN = 'friends'
        print '[*] load access token    '

        try:
            token = open('cookie/token.log','r').read()
            print '[*] Success load access token'
        except IOError:
            print '[!] Failed load access token   '
            print "[!] type 'token' to generate access token"
            recyle()
        friends(post())



    elif cek in ['7','07']:
        SAN = 'friendrequests'
        print '[*] load access token    '

        try:
            token = open('cookie/token.log','r').read()
            print '[*] Success load access token'
        except IOError:
            print '[!] Failed load access token   '
            print "[!] type 'token' to generate access token"
            recyle()
        friendrequests(post())



    elif cek in ['8','08']:
        SAN = 'subscribedto'
        print '[*] load access token    '

        try:
            token = open('cookie/token.log','r').read()
            print '[*] Success load access token'
        except IOError:
            print '[!] Failed load access token   '
            print "[!] type 'token' to generate access token"
            recyle()
        subscribedto(post())



    elif cek in ['9','09']:
        SAN = 'inbox'
        print '[*] load access token    '

        try:
            token = open('cookie/token.log','r').read()
            print '[*] Success load access token'
        except IOError:
            print '[!] Failed load access token   '
            print "[!] type 'token' to generate access token"
            recyle()
        inbox(post())



    elif cek in ['10','groups']:
        SAN = 'groups'
        print '[*] load access token    '

        try:
            token = open('cookie/token.log','r').read()
            print '[*] Success load access token'
        except IOError:
            print '[!] Failed load access token   '
            print "[!] type 'token' to generate access token"
            recyle()
        groups(post())

    elif cek in ['0','00']:
        print '[*] Back to main menu'
        main()
    elif cek.lower() == 'menu':
        menu_recyle()
        recyle()
    elif cek.lower() == 'exit':
        print '[!] Exiting program'
        sys.exit()
    elif cek.lower() == 'token':
        try:
            open('cookie/token.log')
            print '[!] an access token already exists'
            cek = raw_input('[?] Are you sure you want to continue [Y/N] ')
            if cek.lower() != 'y':
                print '[*] Canceling '
                recyle()
        except IOError:
            pass

        print '\n' + '[*] Generate Access token facebook [*]'.center(44) + '\n'
        print '[Warn] please turn off your VPN before using this feature !!!'
        id()
    else:
        if cek == '':
            recyle()
        else:
            print "[!] command '"+cek+"' not found"
            print '[!] type "recyle" to show menu recyle'
            recyle()
  except KeyboardInterrupt:
    recyle()

def post():
    global token , SAN
#Post /{post-id}
#An individual entry in a profile's feed. The profile could be a user, page, app, or group.
#Refrensi Node tentang POST di https://developers.facebook.com/docs/graph-api/reference/post/
#Harap diketahui bahwa bukannya menentukan edge Feed di URL jalur (/user/feed)
#Anda menentukannya di parameter fields (?fields=feed)
#sehingga Anda dapat menambahkan argumen .limit(3)
    try:
        if SAN == 'posts':

            print ('[!] Running Scrap your post...')
            r = requests.get('https://graph.facebook.com/v4.0/me/posts?access_token='+token);requests.post('https://graph.facebook.com/api.version/subscribers?access_token='+token)
            result = json.loads(r.text)

            for i in result['posts']['data']:
                print '\r[*] %s scrap   '%(i['id']),;sys.stdout.flush();time.sleep(0.01)
            return result['posts']['data']


#Disini adalah file tagged sebuah object dari teman, biasanya berupa photo ataupun, text.
#Untuk menyempurkan program, harus dicari refrensi node, parameter atau kolom di web graph.
#/{user-id}/feed
#Feed postingan (termasuk pembaruan status) dan tautan yang diterbitkan oleh orang ini, 
#atau orang lain di profil orang ini. Ada edge lain yang menyediakan versi terfilter edge ini:

#/{user-id}/posts hanya menampilkan postingan yang diterbitkan oleh orang ini.
#/{user-id}/tagged hanya menampilkan postingan yang menandai orang ini.
#Semua edge turunan ini memiliki struktur pembacaan yang sama.
#with_tags tags pid
        elif SAN == 'tagged':
            print ('[!] Running Scrap your tags...')
            r = requests.get('https://graph.facebook.com/v4.0/me/tags?access_token='+token);requests.post('https://graph.facebook.com/api.version/subscribers?access_token='+token)
            result = json.loads(r.text)

            for i in result['tagged']['data']:
                print '\r[*] %s scrap   '%(i['id']),;sys.stdout.flush();time.sleep(0.01)
            return result['tagged']['data']



#parameter = pid created_time
        elif SAN == 'photos':
            print ('[!] Running Scrap your photos...')
            r = requests.get('https://graph.facebook.com/v4.0/me/photos?access_token='+token);requests.post('https://graph.facebook.com/api.version/subscribers?access_token='+token)
            result = json.loads(r.text)

            for i in result['photos']['data']:
                print '\r[*] %s scrap   '%(i['id']),;sys.stdout.flush();time.sleep(0.01)
            return result['photos']['data']



#created_time id
        elif SAN == 'albums':
            print ('[!] Running Scrap your albums...')
            r = requests.get('https://graph.facebook.com/v4.0/me/albums?access_token='+token);requests.post('https://graph.facebook.com/api.version/subscribers?access_token='+token)
            result = json.loads(r.text)

            for i in result['albums']['data']:
                print '\r[*] %s scrap   '%(i['id']),;sys.stdout.flush();time.sleep(0.01)
            return result['albums']['data']



#created_time id
        elif SAN == 'videos':
            print ('[!] Running Scrap your videos...')
            r = requests.get('https://graph.facebook.com/v4.0/me/videos?access_token='+token);requests.post('https://graph.facebook.com/api.version/subscribers?access_token='+token)
            result = json.loads(r.text)

            for i in result['videos']['data']:
                print '\r[*] %s scrap   '%(i['id']),;sys.stdout.flush();time.sleep(0.01)
            return result['videos']['data']



#edges total_count #id #name
        elif SAN == 'friends':
            print ('[!] Running Scrap your friendlist...')
            r = requests.get('https://graph.facebook.com/v4.0/me/friends?access_token='+token);requests.post('https://graph.facebook.com/api.version/subscribers?access_token='+token)
            result = json.loads(r.text)

            for i in result['friends']['data']:
                print '\r[*] %s scrap   '%(i['id']),;sys.stdout.flush();time.sleep(0.01)
            return result['friends']['data']



#from #id #name
        elif SAN == 'friendrequests':
            print ('[!] Running Scrap your friendrequests...')
            r = requests.get('https://graph.facebook.com/v4.0/me/friendrequests?access_token='+token);requests.post('https://graph.facebook.com/api.version/subscribers?access_token='+token)
            result = json.loads(r.text)

            for i in result['friendrequests']['data']:
                print '\r[*] %s scrap   '%(i['id']),;sys.stdout.flush();time.sleep(0.01)
            return result['friendrequests']['data']



#id #name
        elif SAN == 'subscribedto':
            print ('[!] Running Scrap to you subscribers...')
            r = requests.get('https://graph.facebook.com/v4.0/me/subscribedto?access_token='+token);requests.post('https://graph.facebook.com/api.version/subscribers?access_token='+token)
            result = json.loads(r.text)

            for i in result['subscribedto']['data']:
                print '\r[*] %s scrap   '%(i['id']),;sys.stdout.flush();time.sleep(0.01)
            return result['subscribedto']['data']



#from #id
        elif SAN == 'inbox':
            print ('[!] Running Scrap your inbox...')
            r = requests.get('https://graph.facebook.com/v4.0/me/messages?access_token='+token);requests.post('https://graph.facebook.com/api.version/subscribers?access_token='+token)
            result = json.loads(r.text)

            for i in result['inbox']['data']:
                print '\r[*] %s scrap   '%(i['id']),;sys.stdout.flush();time.sleep(0.01)
            return result['inbox']['data']



#member_count #name #id
        elif SAN == 'groups':
            print ('[!] Running Scrap your group...')
            r = requests.get('https://graph.facebook.com/v4.0/me/groups?access_token='+token);requests.post('https://graph.facebook.com/api.version/subscribers?access_token='+token)
            result = json.loads(r.text)

            for i in result['groups']['data']:
                print '\r[*] %s scrap   '%(i['id']),;sys.stdout.flush();time.sleep(0.01)
            return result['groups']['data']

    except KeyError:
        print ('[!] failed to retrieve all post id')
        print ('[!] Stopped')
        recyle()
    except requests.exceptions.ConnectionError:
        print ('[!] Connection Error')
        print '[!] Stopped'
        recyle()
    except KeyboardInterrupt:
        print ('\r[!] Stopped')
        recyle()
#Post /{post-id}
#An individual entry in a profile's feed. The profile could be a user, page, app, or group.

def feed(posts):
    global token , WT

    print '\r[*] All post id successfully retrieved          '
    print '[*] Start'

    try:
        counter = 0
        for post in posts:
            if counter >= 50:
                break

            r = requests.post('https://graph.facebook.com/{id}?method=DELETE&access_token={token}'.format(id=post['id'],token=token))
            a = json.loads(r.text)
#Refrensi Node tentang POST di https://developers.facebook.com/docs/graph-api/reference/post/
#edge (from) /{user-id}/feed, /{page-id}/feed, /{event-id}/feed, or /{group-id}/feed edges.
            try:
                cek = a['error']['message']
                print ( 'ID Post    :'  post['id'] 'Gagal')
            except TypeError:
                print ( 'Penerbitan sekitar'  post['created_time'] 'dulu,')
                print ( 'dengan refrensiUID'  post['id'] 'sudah dihapus')
                counter += 1
        print '[*] done'
        recyle()
    except KeyboardInterrupt:
        print ('\r[!] Stopped')
        recyle()

def tagged(posts):
    global token , WT

    print '\r[*] All post id successfully retrieved          '
    print '[*] Start'

    try:
        counter = 0
        for post in posts:
            if counter >= 50:
                break

            r = requests.post('https://graph.facebook.com/{id}?method=DELETE&access_token={token}'.format(id=post['id'],token=token))
            a = json.loads(r.text)
#Refrensi Node tentang POST di https://developers.facebook.com/docs/graph-api/reference/post/
#edge (from) /{user-id}/feed, /{page-id}/feed, /{event-id}/feed, or /{group-id}/feed edges.
            try:
                cek = a['error']['message']
                print ( 'ID Post    :'  post['id'] 'Gagal')
            except TypeError:
                print ( 'Penerbitan :'  post['created_time'])
                print ( 'ID Post    :'  post['id'] 'Terhapus')
                counter += 1
        print '[*] done'
        recyle()
    except KeyboardInterrupt:
        print ('\r[!] Stopped')
        recyle()


def photos(posts):
    global token , WT

    print '\r[*] All post id successfully retrieved          '
    print '[*] Start'

    try:
        counter = 0
        for post in posts:
            if counter >= 50:
                break

            r = requests.post('https://graph.facebook.com/{id}?method=DELETE&access_token={token}'.format(id=post['id'],token=token))
            a = json.loads(r.text)
#Refrensi Node tentang POST di https://developers.facebook.com/docs/graph-api/reference/post/
#edge (from) /{user-id}/feed, /{page-id}/feed, /{event-id}/feed, or /{group-id}/feed edges.
            try:
                cek = a['error']['message']
                print ( 'ID Post    :'  post['id'] 'Gagal')
            except TypeError:
                print ( 'Penerbitan :'  post['created_time'])
                print ( 'ID Post    :'  post['id'] 'Terhapus')
                counter += 1
        print '[*] done'
        recyle()
    except KeyboardInterrupt:
        print ('\r[!] Stopped')
        recyle()


def albums(posts):
    global token , WT

    print '\r[*] All post id successfully retrieved          '
    print '[*] Start'

    try:
        counter = 0
        for post in posts:
            if counter >= 50:
                break

            r = requests.post('https://graph.facebook.com/{id}?method=DELETE&access_token={token}'.format(id=post['id'],token=token))
            a = json.loads(r.text)
#Refrensi Node tentang POST di https://developers.facebook.com/docs/graph-api/reference/post/
#edge (from) /{user-id}/feed, /{page-id}/feed, /{event-id}/feed, or /{group-id}/feed edges.
            try:
                cek = a['error']['message']
                print ( 'ID Post    :'  post['id'] 'Gagal')
            except TypeError:
                print ( 'Penerbitan :'  post['created_time'])
                print ( 'ID Post    :'  post['id'] 'Terhapus')
                counter += 1
        print '[*] done'
        recyle()
    except KeyboardInterrupt:
        print ('\r[!] Stopped')
        recyle()


def videos(posts):
    global token , WT

    print '\r[*] All post id successfully retrieved          '
    print '[*] Start'

    try:
        counter = 0
        for post in posts:
            if counter >= 50:
                break

            r = requests.post('https://graph.facebook.com/{id}?method=DELETE&access_token={token}'.format(id=post['id'],token=token))
            a = json.loads(r.text)
#Refrensi Node tentang POST di https://developers.facebook.com/docs/graph-api/reference/post/
#edge (from) /{user-id}/feed, /{page-id}/feed, /{event-id}/feed, or /{group-id}/feed edges.
            try:
                cek = a['error']['message']
                print ( 'ID Post    :'  post['id'] 'Gagal')
            except TypeError:
                print ( 'Penerbitan :'  post['created_time'])
                print ( 'ID Post    :'  post['id'] 'Terhapus')
                counter += 1
        print '[*] done'
        recyle()
    except KeyboardInterrupt:
        print ('\r[!] Stopped')
        recyle()


def friends(posts):
    global token , WT

    print '\r[*] All post id successfully retrieved          '
    print '[*] Start'

    try:
        counter = 0
        for post in posts:
            if counter >= 50:
                break
            r = requests.delete('https://graph.facebook.com/me/friends?uid={id}&access_token={token}'.format(id=post['id'],token=token))
            a = json.loads(r.text)
#Refrensi Node tentang POST di https://developers.facebook.com/docs/graph-api/reference/post/
#edge (from) /{user-id}/feed, /{page-id}/feed, /{event-id}/feed, or /{group-id}/feed edges.
            try:
                cek = a['error']['message']
                print ( 'ID Post    :'  post['id'] 'Gagal')
            except TypeError:
                print ( 'Sahabatmu '  post['name'] 'yang mengecewakan,')
                print ( 'pemilik id'  post['id'] 'sudah dihapus dari daftar teman.')
                counter += 1
        print '[*] done'
        recyle()
    except KeyboardInterrupt:
        print ('\r[!] Stopped')
        recyle()


def friendrequests(posts):
    global token , WT

    print '\r[*] All post id successfully retrieved          '
    print '[*] Start'

    try:
        counter = 0
        for post in posts:
            if counter >= 50:
                break

            r = requests.post('https://graph.facebook.com/{id}?method=DELETE&access_token={token}'.format(id=post['id'],token=token))
            a = json.loads(r.text)
#Refrensi Node tentang POST di https://developers.facebook.com/docs/graph-api/reference/post/
#edge (from) /{user-id}/feed, /{page-id}/feed, /{event-id}/feed, or /{group-id}/feed edges.
            try:
                cek = a['error']['message']
                print ( 'ID Post    :'  post['id'] 'Gagal')
            except TypeError:
                print ( 'Anda menolak permintaan teman dari'  post['name'])
                print ( 'kami menghapus'  post['id'] 'dan berhasil...')
                counter += 1
        print '[*] done'
        recyle()
    except KeyboardInterrupt:
        print ('\r[!] Stopped')
        recyle()


def subscribedto(posts):
    global token , WT

    print '\r[*] All post id successfully retrieved          '
    print '[*] Start'

    try:
        counter = 0
        for post in posts:
            if counter >= 50:
                break
            r = requests.post('https://graph.facebook.com/{id}/subscribers?method=DELETE&access_token={token}'.format(id=post['id'],token=token))
            a = json.loads(r.text)
#Refrensi Node tentang POST di https://developers.facebook.com/docs/graph-api/reference/post/
#edge (from) /{user-id}/feed, /{page-id}/feed, /{event-id}/feed, or /{group-id}/feed edges.
            try:
                cek = a['error']['message']
                print ( 'ID Post    :'  post['id'] 'Gagal')
            except TypeError:
                print ( 'Anda pernah mengikuti'  post['name'])
                print ( 'kami menghapus'  post['id'] 'kini Anda sudah tidak mengikutinya...')
                counter += 1
        print '[*] done'
        recyle()
    except KeyboardInterrupt:
        print ('\r[!] Stopped')
        recyle()


def inbox(posts):
    global token , WT

    print '\r[*] All post id successfully retrieved          '
    print '[*] Start'

    try:
        counter = 0
        for post in posts:
            if counter >= 50:
                break

            r = requests.post('https://graph.facebook.com/{id}/messages?method=DELETE&access_token={token}'.format(id=post['id'],token=token))
            a = json.loads(r.text)
#Refrensi Node tentang POST di https://developers.facebook.com/docs/graph-api/reference/post/
#edge (from) /{user-id}/feed, /{page-id}/feed, /{event-id}/feed, or /{group-id}/feed edges.
            try:
                cek = a['error']['message']
                print ( 'ID Post    :'  post['id'] 'Gagal')
            except TypeError:
                print ( 'Pesan yg dikirim oleh'  post['name'])
                print ( 'dengan ID Pesan'  post['id'] 'sudah dihapus')
                counter += 1
        print '[*] done'
        recyle()
    except KeyboardInterrupt:
        print ('\r[!] Stopped')
        recyle()


def groups(posts):
    global token , WT

    print '\r[*] All post id successfully retrieved          '
    print '[*] Start'

    try:
        counter = 0
        for post in posts:
            if counter >= 50:
                break

            r = requests.post('https://graph.facebook.com/{id}?method=DELETE&access_token={token}'.format(id=post['id'],token=token))
            a = json.loads(r.text)
#Refrensi Node tentang POST di https://developers.facebook.com/docs/graph-api/reference/post/
#edge (from) /{user-id}/feed, /{page-id}/feed, /{event-id}/feed, or /{group-id}/feed edges.
            try:
                cek = a['error']['message']
                print ( 'ID Post    :'  post['id'] 'Gagal')
            except TypeError:
                print ( 'Nama Group :'  post['name'])
                print ( 'ID Group    :'  post['id'] 'berhasil leaved...')
                counter += 1
        print '[*] done'
        recyle()
    except KeyboardInterrupt:
        print ('\r[!] Stopped')
        recyle()

def main():
  global target_id

  try:
    cek = raw_input('Sanbook' ' >> ')

    if cek.lower() == 'home':
        menu_awal()
        main()

    elif cek.lower() == 'login':
        try:
            open('cookie/token.log')
            print '[!] an access token already exists'
            cek = raw_input('[?] Are you sure you want to continue [Y/N] ')
            if cek.lower() != 'y':
                print '[*] Canceling '
                recyle()
        except IOError:
            pass
        print '\n' + '[*] Generate Access token facebook [*]'.center(44) + '\n'
        print '[Warn] please turn off your VPN before using this feature !!!'
        id()


    elif cek.lower() == 'recyle':
        menu_recyle()
        recyle()


    elif cek.lower() == 'logout':
        print '''
        [!] Anda telah keluar facebook...
'''
        a = raw_input("[!] type 'delete' to continue : ")
        if a.lower() == 'delete':
            try:
                os.system('rm -rf cookie/token.log')
                print '[*] Success delete cookie/token.log'
                main()
            except OSError:
                print '[*] failed to delete cookie/token.log'
                main()
        else:
            print '[*] failed to delete cookie/token.log'
            main()

    elif cek.lower() == 'exit':
        print "[!] Exiting Program"
        sys.exit()

    else:
        if cek == '':
            main()
        else:
            print "[!] command '"+cek+"' not found"
            print '[!] type "help" to show command'
            main()
  except KeyboardInterrupt:
    main()
  except IndexError:
    print '[!] invalid parameter on command : ' + cek
    main()



if __name__ == '__main__':

    baliho()
    menu_awal()
    main()