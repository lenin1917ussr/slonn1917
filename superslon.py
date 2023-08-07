import time
import logging
import random
from aiogram import Bot, Dispatcher, executor, types

TOKEN = "6534763887:AAEImGbegQN2kTXlBfVSTQx1_dZiEIYNzMw"
#MSG = random.randint(1, 10)
bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot)



@dp.message_handler(commands=['slonik'])
async def start_handler(message:types.message):
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name
    logging.info(f'{user_id=} {user_full_name=}', {time.asctime()})
    await message.reply(f"Зеленый слоник в наш оркестр пришел! {user_full_name}")

    for i in range(1000):
      time.sleep(1)
      ussr = random.randint(1,21)
      if ussr==1:
         MSG = "Ну и как говно, вкусное?"
      if ussr==2:
         MSG = "Пасть свою заткни!"
      if ussr==3:
         MSG ="Чисти чисти, сука!"
      if ussr==4:
         MSG="Начальник, блядь! Начальник! Этот пидорас обосрался, бля! Начальник!"
      if ussr==5: 
         MSG="Какие это были корабли?"
      if ussr==6:
         MSG="Как поспал, братишка? Проголодался наверное, братишка?"
      if ussr==7:
         MSG="Пидорас блядь! Сука, блядь!"
      if ussr==8:
         MSG="АААААААААА,БЛЯТЬ!"
      if ussr==9:
         MSG="Какой самый известный самолет на тихоокеанском театре военных действий?"
      if ussr==10:
         MSG="На работу!"
      if ussr==11:
         await bot.send_sticker(message.from_user.id, sticker="CAACAgIAAxkBAAEJ8TNk0LAcia888QToHOw7hcB50o2hXwACmywAAoNvQUmY-l8-23z13zAE")
      if ussr==12:
         await bot.send_sticker(message.from_user.id, sticker="CAACAgIAAxkBAAEJ8S1k0LAQlvyRYFAtndlSqlbEPxTRQwAC2SgAApjBMEhSLcEhs8xcqzAE")
      if ussr==13:
         await bot.send_sticker(message.from_user.id, sticker="CAACAgIAAxkBAAEJ8Tdk0LAlombG34Z5koV701RT9VjIvwACgC8AAmog-UoigHjKaHxUTDAE")
      if ussr==14:
         await bot.send_sticker(message.from_user.id, sticker="CAACAgIAAxkBAAEJ8S9k0LAWOsVTbKmjmaqS9n9RRATBdgAC7SYAAhZ9OEiOHQSv_W-QAAEwBA")
      if ussr==15:
         MSG = "Ну и как говно, вкусное?"
      if ussr==16:
         MSG = "Пасть свою заткни!"
      if ussr==17:
         MSG ="Чисти чисти, сука!"
      if ussr==18:
         MSG="Я зеленый слоник, я веселый головастик! Я зеленый слоник, я веселый головастик! Тиииик!"
      if ussr==19: 
         MSG="Иди под струю сука, мойся!"
      if ussr==20:
         MSG="Танцуй блядь!"
      if ussr==21:
         MSG="Товарищ капитан, только на меня не спускайте, блять!"
      if ussr==22:
         MSG="А блядь на хуй! Ну, иди сюда сука, блядь! Дерьмо собачье, блядь! А блядь!"
      if ussr==23:
         MSG="Я перед обедом 20 раз отжимался."
            
      await bot.send_message(user_id, MSG)
      
  
   



if __name__ == '__main__':
  executor.start_polling(dp)