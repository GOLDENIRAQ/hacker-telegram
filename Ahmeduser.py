import webbrowser
import os , requests , time , random , sys , datetime
import pyfiglet
from webbrowser import open as Open
from datetime import datetime

current_time = datetime.now()
expiry_time = datetime.strptime('2030-12-31 00:00:00.000', '%Y-%m-%d %H:%M:%S.%f')

if current_time > expiry_time:
    print('̶ا̶لــ̶ا̶د̶ا̶ه ̶ا̶̶نـ̶تـ̶ه̶تـ ̶مـ̶ه̶لــ̶تـ̶ه̶ا ̶ا̶لــ̶تـ̶جـࢪ̶يـ̶بـ̶يـ̶ه ̶يـ̶حـ̶بـ̶يـ ♡゙. .')
    exit(0)


E = '\033[1;31m'
G = '\033[1;35m'
Z = '\033[1;31m' #احمر
X = '\033[2;31m' #اصفر
Z1 = '\033[2;31m' #احمر ثاني
F = '\033[2;32m' #اخضر
A = '\033[2;34m'#ازرق
C = '\033[2;35m' #وردي
B = '\033[2;36m'#سمائي
Y = '\033[1;34m' #ازرق فاتح
M = '\x1b[1;37m'#ابیض
S = '\033[1;33m'
U = '\x1b[1;37m'#ابیض
BRed = '\x1b[1;31m'
BGreen = '\x1b[1;32m'
BYellow = '\x1b[1;33m'
R = '\x1b[1;34m'
BPurple = '\x1b[1;35m'
BCyan = '\x1b[1;36m'
BWhite = '\x1b[1;37m'

abc ='ABCDEFGHIJKLMNOPQRSTUVWXYZ_1234567890'

abc1 ='ABCDEFGHIJKLMNOPQRSTUVWXYZ'


W = "\033[0m" ;G = '\033[32;1m';R = '\033[31;1m'
A = "\033[1;91m";B = "\033[1;90m";C = "\033[1;97m"
E = "\033[1;92m";H = "\033[1;93m";K = "\033[1;94m"
L = "\033[1;95m";M = "\033[1;94m"

Open("https://t.me/rnryr")

F =  '\033[1;34m'
    
 
print(X+'''
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
│o │01│ يوزر تليجرام خماسي مميز

│o │02│يوزر تليجرام شبه ثلاثي

│o │03│يوزر تليجرام شبه رباعي مميز

│o │04│يوزرات بوتات مميزه
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━''')

cho = input(B+' : اختار رقم للاستمرار [☟] ')

print('\n\n')
Open("https://t.me/rnryr")

tok = os.environ.get("GOLD_TOKEN")
ID = os.environ.get("GOLD_ID")

print('================')
Open("https://t.me/rnryr")

if cho == '1'or cho =='01':

    while True:
       v1 = str(''.join((random.choice(abc1) for i in range(1))))
       v2 = str(''.join((random.choice(abc) for i in range(1))))
       v3 = str(''.join((random.choice(abc) for i in range(1))))

       user1 = (v1+v1+v1+v2+v3)
       user2 = (v1+v1+v2+v3+v1)
       user3 = (v1+v2+v3+v1+v1)
       user4 = (v1+v3+v2+v2+v2)
       hamo010 = (user1, user2, user3, user4)
       user = random.choice(hamo010)
       url = requests.get(f'https://t.me/{user}').text
       if 'tgme_username_link' in url:
            requests.get(f'https://api.telegram.org/bot{tok}/sendMessage?chat_id={ID}&text=UsEr TeleGraM ↬ ⦗ @{user} ⦘\n\nby : @rnryr ')

            print(f' \033[1;32m {user}')



       else:



            print(f' \033[1;31m NOT AVAILABLE : {user}')



if cho == '2'or cho =='02':



    while True:



        v1 = str(''.join((random.choice(abc1) for i in range(1))))



        v2 = str(''.join((random.choice(abc) for i in range(1))))



        v3 = str(''.join((random.choice(abc) for i in range(1))))



        user = (v1+'_'+v2+'_'+v3)



        url = requests.get(f'https://t.me/{user}').text



        if 'tgme_username_link' in url:



            requests.get(f'https://api.telegram.org/bot{tok}/sendMessage?chat_id={ID}&text=UsEr TeleGraM ↬ ⦗ @{user} ⦘\n\nby : @rnryr ')



            print(f' \033[1;32m {user}')



        else:



            print(f' \033[1;31m NOT AVAILABLE : {user}')



if cho == '3'or cho =='03':



    while True:



        v1 = str(''.join((random.choice(abc1) for i in range(1))))



        v2 = str(''.join((random.choice(abc) for i in range(1))))



        v3 = str(''.join((random.choice(abc) for i in range(1))))



        user1 = (v1+'_'+v2+'_'+v2+'_'+v2)



        user2 = (v1+'_'+v2+'_'+v1+'_'+v1)



        user3 = (v1+'_'+v1+'_'+v2+'_'+v1)



        user4 = (v1+'_'+v1+'_'+v1+'_'+v2)



        hamo010 = (user1, user2, user3, user4)



        user = random.choice(hamo010)



        url = requests.get(f'https://t.me/{user}').text



        if 'tgme_username_link' in url:



            requests.get(f'https://api.telegram.org/bot{tok}/sendMessage?chat_id={ID}&text=(<^>) user tele ~> @{user}\n\nby : @rnryr ')



            print(f' \033[1;32m {user}')



        else:



            print(f' \033[1;31m NOT AVAILABLE : {user}')



if cho == '4'or cho =='04':



    while True:



        v1 = str(''.join((random.choice(abc1) for i in range(1))))



        v2 = str(''.join((random.choice(abc) for i in range(1))))



        v3 = str(''.join((random.choice(abc) for i in range(1))))



        user1 = (v1+v2+v3+'_bot')



        user2 = (v1+v2+v3+'bot')



        user3 = (v1+v1+v2+v2+'bot')



        user4 = (v1+v2+v2+v1+'bot')



        hamo010 = (user1, user2, user3, user4)



        user = random.choice(hamo010)



        url = requests.get(f'https://t.me/{user}').text



        if 'tgme_username_link' in url:



            requests.get(f'https://api.telegram.org/bot{tok}/sendMessage?chat_id={ID}&text=(<^>) user tele ~> @{user}\n\nby :  ')



            print(f' \033[1;32m {user}')



        else:



            print(f' \033[1;31m NOT AVAILABLE : {user}')



if cho == '5'or cho =='05':



    while True:



        user = str(''.join((random.choice(abc) for i in range(4))))



        url = 'https://www.instagram.com/accounts/web_create_ajax/attempt/'



        head = {



'accept': '*/*',



'accept-encoding': 'gzip, deflate, br',



'accept-language': 'en-US,en;q=0.9',



'content-length': '1176',



'content-type': 'application/x-www-form-urlencoded',



'cookie': 'ig_cb=2; ig_did=BB52B198-B05A-424E-BA07-B15F3D4C3893; mid=YAlcaQALAAHzmX6nvD8dWMRVYFCO; shbid=15012; rur=PRN; shbts=1612894029.7666144; csrftoken=CPKow8myeXW9AuB3Lny0wNxx0EzoDQoI',



'origin': 'https://www.instagram.com',



'referer':'https://www.instagram.com/',



'sec-ch-ua': '"Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"',



'sec-ch-ua-mobile': '?0',



'sec-ch-ua-platform': "Windows",



'sec-fetch-dest': 'empty',



'sec-fetch-mode': 'cors',



'sec-fetch-site': 'same-site',



'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36',



'x-asbd-id':'198387' ,



'x-csrftoken': 'CPKow8myeXW9AuB3Lny0wNxx0EzoDQoI',



'x-ig-www-claim': 'hmac.AR0Plwj5om112fwzrrYnMNjMLPnyWfFFq1tG7MCcMv5_vN9M',



'x-instagram-ajax': '72bda6b1d047',



'x-requested-with': 'XMLHttpRequest'



}



        data = {



'email' : 'a@gmail.com',



'username': (f'{user}'),



'first_name': 'AA',



'opt_into_one_tap': 'false'



}  



        uS = requests.post(url, headers=head, data=data).text



        Uss =  ('{"account_created": false, "errors": {"email": [{"message": "Too many accounts are using a@gmail.com.", "code": "email_sharing_limit"}], "__all__": [{"message": "Create a password at least 6 characters long.", "code": "too_short_password"}]}, "dryrun_passed": false, "username_suggestions": [], "status": "ok", "error_type": "form_validation_error"}')



        if Uss in uS:



            requests.get(f'https://api.telegram.org/bot{tok}/sendMessage?chat_id={ID}&text=(<^>) user instagram ~> {user}\n\nby :  ')



            print(f' \033[1;32m {user}')



        else:



            time.sleep(1)



            print(f' \033[1;31m NOT AVAILABLE : {user}')



if cho == '6'or cho =='06':



    while True:



        v1 = str(''.join((random.choice(abc) for i in range(1))))



        v2 = str(''.join((random.choice(abc) for i in range(1))))



        v3 = str(''.join((random.choice(abc) for i in range(1))))



        v4 = str(''.join((random.choice(abc) for i in range(1))))



        hhh = '._'



        v5 = str(''.join((random.choice(hhh) for i in range(1))))



        user1 = (v5+v1+v2+v3+v4)



        user2 = (v1+v5+v2+v3+v4)



        user3 = (v1+v2+v5+v3+v4)



        user4 = (v1+v2+v3+v5+v4)



        hamo010 = (user1, user2, user3, user4)



        user = random.choice(hamo010)



        url = 'https://www.instagram.com/accounts/web_create_ajax/attempt/'



        head = {



'accept': '*/*',



'accept-encoding': 'gzip, deflate, br',



'accept-language': 'en-US,en;q=0.9',



'content-length': '1176',



'content-type': 'application/x-www-form-urlencoded',



'cookie': 'ig_cb=2; ig_did=BB52B198-B05A-424E-BA07-B15F3D4C3893; mid=YAlcaQALAAHzmX6nvD8dWMRVYFCO; shbid=15012; rur=PRN; shbts=1612894029.7666144; csrftoken=CPKow8myeXW9AuB3Lny0wNxx0EzoDQoI',



'origin': 'https://www.instagram.com',



'referer':'https://www.instagram.com/',



'sec-ch-ua': '"Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"',



'sec-ch-ua-mobile': '?0',



'sec-ch-ua-platform': "Windows",



'sec-fetch-dest': 'empty',



'sec-fetch-mode': 'cors',



'sec-fetch-site': 'same-site',



'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36',



'x-asbd-id':'198387' ,



'x-csrftoken': 'CPKow8myeXW9AuB3Lny0wNxx0EzoDQoI',



'x-ig-www-claim': 'hmac.AR0Plwj5om112fwzrrYnMNjMLPnyWfFFq1tG7MCcMv5_vN9M',



'x-instagram-ajax': '72bda6b1d047',



'x-requested-with': 'XMLHttpRequest'



}



        data = {



'email' : 'a@gmail.com',



'username': (f'{user}'),



'first_name': 'AA',



'opt_into_one_tap': 'false'



}  



        uS = requests.post(url, headers=head, data=data).text



        Uss =  ('{"account_created": false, "errors": {"email": [{"message": "Too many accounts are using a@gmail.com.", "code": "email_sharing_limit"}], "__all__": [{"message": "Create a password at least 6 characters long.", "code": "too_short_password"}]}, "dryrun_passed": false, "username_suggestions": [], "status": "ok", "error_type": "form_validation_error"}')



        if Uss in uS:



            requests.get(f'https://api.telegram.org/bot{tok}/sendMessage?chat_id={ID}&text=(<^>) user instagram ~> {user}\n\nby :  ')



            print(f' \033[1;32m {user}')



        else:



            time.sleep(1)



            print(f' \033[1;31m NOT AVAILABLE : {user}')



if cho == '7'or cho =='07':



    while True:



        user = str(''.join((random.choice(abc) for i in range(5))))



        url = 'https://www.instagram.com/accounts/web_create_ajax/attempt/'



        head = {



'accept': '*/*',



'accept-encoding': 'gzip, deflate, br',



'accept-language': 'en-US,en;q=0.9',



'content-length': '1176',



'content-type': 'application/x-www-form-urlencoded',



'cookie': 'ig_cb=2; ig_did=BB52B198-B05A-424E-BA07-B15F3D4C3893; mid=YAlcaQALAAHzmX6nvD8dWMRVYFCO; shbid=15012; rur=PRN; shbts=1612894029.7666144; csrftoken=CPKow8myeXW9AuB3Lny0wNxx0EzoDQoI',



'origin': 'https://www.instagram.com',



'referer':'https://www.instagram.com/',



'sec-ch-ua': '"Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"',



'sec-ch-ua-mobile': '?0',



'sec-ch-ua-platform': "Windows",



'sec-fetch-dest': 'empty',



'sec-fetch-mode': 'cors',



'sec-fetch-site': 'same-site',



'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36',



'x-asbd-id':'198387' ,



'x-csrftoken': 'CPKow8myeXW9AuB3Lny0wNxx0EzoDQoI',



'x-ig-www-claim': 'hmac.AR0Plwj5om112fwzrrYnMNjMLPnyWfFFq1tG7MCcMv5_vN9M',



'x-instagram-ajax': '72bda6b1d047',



'x-requested-with': 'XMLHttpRequest'



}



        data = {



'email' : 'a@gmail.com',



'username': (f'{user}'),



'first_name': 'AA',



'opt_into_one_tap': 'false'



}  



        uS = requests.post(url, headers=head, data=data).text



        Uss =  ('{"account_created": false, "errors": {"email": [{"message": "Too many accounts are using a@gmail.com.", "code": "email_sharing_limit"}], "__all__": [{"message": "Create a password at least 6 characters long.", "code": "too_short_password"}]}, "dryrun_passed": false, "username_suggestions": [], "status": "ok", "error_type": "form_validation_error"}')



        if Uss in uS:



            requests.get(f'https://api.telegram.org/bot{tok}/sendMessage?chat_id={ID}&text=(<^>) user instagram ~> {user}\n\nby :  ')



            print(f' \033[1;32m {user}')



        else:



            time.sleep(1)



            print(f' \033[1;31m NOT AVAILABLE : {user}')



if cho == '8'or cho =='08':



    while True:



        hea = {'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 



 'accept-encoding':'gzip, deflate, br', 



 'accept-language':'en-US,en;q=0.9,ar;q=0.8', 



 'cache-control':'max-age=0', 



 'sec-ch-ua':'" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"', 



 'sec-ch-ua-mobile':'?0', 



 'sec-fetch-dest':'document', 



 'sec-fetch-mode':'navigate', 



 'sec-fetch-site':'same-origin', 



 'sec-fetch-user':'?1', 



 'upgrade-insecure-requests':'1', 



 'user-agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'}



        user = str(''.join((random.choice(abc) for i in range(4))))



        tiko = f'https://www.tiktok.com/@{user}?'



        reqsnd = requests.get(tiko, headers=hea).status_code



        if reqsnd == 404:



            requests.get(f'https://api.telegram.org/bot{tok}/sendMessage?chat_id={ID}&text=(<^>) user tik tok ~> {user}\n\nby :  ')



            print(f' \033[1;32m {user}')



        elif reqsnd == 200:



            print(f' \033[1;31m NOT AVAILABLE : {user}')



if cho == '10':



    while True:



        hea = {'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 



 'accept-encoding':'gzip, deflate, br', 



 'accept-language':'en-US,en;q=0.9,ar;q=0.8', 



 'cache-control':'max-age=0', 



 'sec-ch-ua':'" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"', 



 'sec-ch-ua-mobile':'?0', 



 'sec-fetch-dest':'document', 



 'sec-fetch-mode':'navigate', 



 'sec-fetch-site':'same-origin', 



 'sec-fetch-user':'?1', 



 'upgrade-insecure-requests':'1', 



 'user-agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'}



        user = str(''.join((random.choice(abc) for i in range(5))))



        tiko = f'https://www.tiktok.com/@{user}?'



        reqsnd = requests.get(tiko, headers=hea).status_code



        if reqsnd == 404:



            requests.get(f'https://api.telegram.org/bot{tok}/sendMessage?chat_id={ID}&text=(<^>) user tik tok ~> {user}\n\nby :  ')



            print(f' \033[1;32m {user}')



        elif reqsnd == 200:



            print(f' \033[1;31m NOT AVAILABLE : {user}')



if cho == '9'or cho =='09':



    while True:



        hea = {'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 



 'accept-encoding':'gzip, deflate, br', 



 'accept-language':'en-US,en;q=0.9,ar;q=0.8', 



 'cache-control':'max-age=0', 



 'sec-ch-ua':'" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"', 



 'sec-ch-ua-mobile':'?0', 



 'sec-fetch-dest':'document', 



 'sec-fetch-mode':'navigate', 



 'sec-fetch-site':'same-origin', 



 'sec-fetch-user':'?1', 



 'upgrade-insecure-requests':'1', 



 'user-agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'}



        v1 = str(''.join((random.choice(abc) for i in range(1))))



        v2 = str(''.join((random.choice(abc) for i in range(1))))



        v3 = str(''.join((random.choice(abc) for i in range(1))))



        v4 = str(''.join((random.choice(abc) for i in range(1))))



        hhh = '._'



        v5 = str(''.join((random.choice(hhh) for i in range(1))))



        user2 = (v1+v5+v2+v3+v4)



        user3 = (v1+v2+v5+v3+v4)



        user4 = (v1+v2+v3+v5+v4)



        hamo010 = (user2, user3, user4)



        user = random.choice(hamo010)



        tiko = f'https://www.tiktok.com/@{user}?'



        reqsnd = requests.get(tiko, headers=hea).status_code



        if reqsnd == 404:



            requests.get(f'https://api.telegram.org/bot{tok}/sendMessage?chat_id={ID}&text=(<^>) user tik tok ~> {user}\n\nby :  ')



            print(f' \033[1;32m {user}')



        elif reqsnd == 200:



            print(f' \033[1;31m NOT AVAILABLE : {user}')
