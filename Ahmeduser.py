import random
import  requests
from telebot import types
import telebot

Token = os.environ.get("GOLD_TOKEN")

GOLD = types.InlineKeyboardButton(text ="قم بضغط لبدء التشغيل ⚡️",callback_data = "GOLD")

bot = telebot.TeleBot(Token)
@bot.message_handler(commands=["start"])
def start(message):
         T5Hbut1 = types.InlineKeyboardMarkup()
         T5Hbut1.row_width = 2
         T5Hbut1.add(GOLD)
         photo = f"t.me/{message.from_user.username}"
         tag = f"[{message.from_user.first_name}]({photo})"
         text = f"""اهلا بك ! {tag} في بوت تشكير يوزرات انستغرام  🐉"""
         bot.send_photo(message.chat.id,photo,text ,
 parse_mode="Markdown",reply_markup=T5Hbut1)
          

@bot.callback_query_handler(lambda call:True)
def call(call): 
  if call.data == "GOLD":
   messag=bot.send_message(chat_id=call.message.chat.id,text=""" ما هو اسمك  ⤷ """)   
   bot.register_next_step_handler(messag,T5Hus,messag.id) 
   T5Hrand(call.message)
def T5Hrand(number):
    GoLd = "1234567890qwertyuiopasdfghjklzxcvbnm"
    a = str("".join(random.choice(GoLd)for x in range(1)))
    b = str("".join(random.choice(GoLd)for x in range(1)))
    c = str("".join(random.choice(GoLd)for x in range(1)))
    T5HuS= a+b+'_'+c+a
    return T5HuS
def T5Hus(message,id):
 GoodUser =0
 BadUser = 0
 userl=4
 name = message.text
 
 
 while True:
  
  username = T5Hrand(userl)
  rrT5H = requests.post("https://www.instagram.com/accounts/web_create_ajax/attempt/",headers={'Host':'www.instagram.com','content-length':'70','sec-ch-ua':'"Chromium";v="106",','x-ig-app-id':'936619743392459','x-ig-www-claim':'hmac.AR3-jjxWxD7osd7WtAM_c6iLQHDvlDZucbWWVQ38t2tPdF3t','sec-ch-ua-mobile':'?0','x-instagram-ajax':'de83d85cf90c','user-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36','viewport-width':'980','content-type':'application/x-www-form-urlencoded','accept':'*/*','x-requested-with':'XMLHttpRequest','x-asbd-id':'198387','x-csrftoken':'NEhRd2uaYf6774IYrUuw6svzofnU3COW','sec-ch-prefers-color-scheme':'dark','sec-ch-ua-platform':'"Linux"','origin':'https://www.instagram.com','sec-fetch-site':'same-origin','sec-fetch-mode':'cors','sec-fetch-dest':'empty','referer':'https://www.instagram.com/accounts/emailsignup/','accept-language':'ar-IQ,ar;q=0.9,en-UM;q=0.8,en;q=0.7,ar-AE;q=0.6,en-US;q=0.5'},data={"email":"email=T5H@gmail.com+","username":username,"first_name":"T5H","opt_into_one_tap":"false"}).text
  if "username_is_taken" in rrT5H:
   BadUser +=1   
   
  else:
    GoodUser+=1
    
    h = "https://t.me/OTOO9/42"
    bot.send_video(message.chat.id,h,caption=f'''*
⌯ Come ! {name} Im Hit The User 🥇
⌯ Username ⤷ @{username}
⌯ Click ⤷ {BadUser}
⌯ Dev : ⤷ @T_5_H *''',parse_mode="markdown")
   
  DoN =types.InlineKeyboardButton(text=f"شغال : {GoodUser}", callback_data="GoodUser1")
  Usavariable  =types.InlineKeyboardButton(text=f"يوزر: {username}", callback_data="User")
  BaD =types.InlineKeyboardButton(text=f"غير شغال : {BadUser}", callback_data="BadUser1")
  T5Hbut = types.InlineKeyboardButton(text="G O L D", callback_data="bad")
  T5Hbut2 = types.InlineKeyboardMarkup()
  T5Hbut2.row_width = 2
  T5Hbut2.add(Usavariable)
  T5Hbut2.add(DoN,BaD)
  T5Hbut2.add(T5Hbut)
  
  
  bot.edit_message_text(chat_id=message.chat.id,message_id=id,text="""
The Bot is Working...♻️
Dev ⤷ [G O L D](t.me/T_5_H)
""",parse_mode="markdown",disable_web_page_preview = 'true',reply_markup=T5Hbut2)
 

bot.infinity_polling()
