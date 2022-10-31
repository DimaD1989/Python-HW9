# import emoji

# # Крестики-нолики

# print("*" * 10, " Игра Крестики-нолики  ", "*" * 10)
# print(emoji.emojize(":hand_with_fingers_splayed:")) 
# board = list(range(1,10))                                                           #cоздаем список,для создания поля

# def draw_board(board):                                                              # заводим функцию для рисования
#    print("-" * 13)                                                                  # выводим 13 "-"
#    for i in range(3):                                                               # создаем цикл,поле на 3 клетки
#       print("|", board[0+i*3], "|", board[1+i*3], "|", board[2+i*3], "|")           # создаем 3 клетки в строке
#       print("-" * 13)

# def input_user(player):                                                             # создаем функцию для коректности ввода пользователя
#    valid = False
#    while not valid:                                                                 # меняет результат, если не верно или наоборот
#       player_answer = input("Куда поставим " + player+"? ")                         # задаем вопрос пользователю о +
#       try:
#          player_answer = int(player_answer)
#       except:                                                                       #  обработка корректности ввода
#          print("Некорректный ввод. Вы уверены, что ввели число?")
#          print(emoji.emojize(":cross_mark:"))
#          continue
#       if player_answer >= 1 and player_answer <= 9:                                 # двойная проверка корректности хода
#          if(str(board[player_answer-1]) not in "XO"):                               # защита от дурака
#             board[player_answer-1] = player
#             valid = True
#          else:
#             print("Эта клетка  занята!")                                         
#       else:
#         print("Некорректный ввод. Введите число от 1 до 9.")
#         print(emoji.emojize(":cross_mark:"))


# def check_win(board):                                                              # функция проверки игрового поля, проверяет, выиграл ли игрок
#    win_coord = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6)) # кортеж выйгрышных кобминации
#    for each in win_coord:                                                          
#        if board[each[0]] == board[each[1]] == board[each[2]]:                       # провекра на выйгрыш
#           return board[each[0]]
#    return False

# def main(board):                                                                    # основная функция игры, которая будет запускать все ранее описанные функции. Данная функция запускает и управляет игровым процессом.
#     count = 0                                                                       # счетчик
#     win = False
#     while not win:
#         draw_board(board)
#         if count % 2 == 0:
#            input_user("X") 
#            print(emoji.emojize(":face_savoring_food:"))
#                                                         # 1 пользователь
#         else:
#            input_user("O")  
#            print(emoji.emojize(":face_exhaling:"))                                                        # 2 пользователь
#         count += 1
#         if count > 4:
#            tmp = check_win(board)                                                   # создаем переменную,чтобы не обращаться к чек вину
#            if tmp:
#               print(tmp, "выиграл!")
#               print(emoji.emojize(":1st_place_medal:"))
#               win = True
#               break
#         if count == 9:
#             print("Ничья!")
#             print(emoji.emojize(":handshake:"))
#             break
#     draw_board(board)                                                               # вызов функции
# main(board)   
#                                                                       # вызов функции
# print(emoji.emojize(":door:"))
# input("Нажмите Enter для выхода!")

# import telebot

# bot = telebot.Telebot ('5503832266:AAHVuUlj6vOR8YbrgEsCrLoceCMeg9BJ2KE')

# value = ' '
# old_value = ' '

# keyboard = telebot.types.InlineKeybeardMarkup()
# keyboard.row(telebot.types.InlineKeybeardButton(' ', callback='no'),
#             telebot.types.InlineKeybeardButton('C', callback='C'),
#             telebot.types.InlineKeybeardButton('<=', callback='<='),
#             telebot.types.InlineKeybeardButton('/', callback='/'))

# keyboard.row(telebot.types.InlineKeybeardButton('7', callback='7'),
#             telebot.types.InlineKeybeardButton('8', callback='8'),
#             telebot.types.InlineKeybeardButton('9', callback='9'),
#              telebot.types.InlineKeybeardButton('*', callback='*'))

# keyboard.row(telebot.types.InlineKeybeardButton('4', callback='4'),
#             telebot.types.InlineKeybeardButton('5', callback='5'),
#             telebot.types.InlineKeybeardButton('6', callback='6'),
#              telebot.types.InlineKeybeardButton('-', callback='-'))

# keyboard.row(telebot.types.InlineKeybeardButton('1', callback='1'),
#             telebot.types.InlineKeybeardButton('2', callback='2'),
#             telebot.types.InlineKeybeardButton('3', callback='3'),
#             telebot.types.InlineKeybeardButton('+', callback='+'))

# keyboard.row(telebot.types.InlineKeybeardButton(' ', callback='no'),
#             telebot.types.InlineKeybeardButton('0', callback='0'),
#             telebot.types.InlineKeybeardButton(',', callback=','),
#             telebot.types.InlineKeybeardButton('=', callback='='))


# @bot.massage_handler(commmands=['stars'], ['calculater'])
# def getMessage(message):
#     global value
#     if value == ' ':
#         bot.send_message(message.from_user.id, '0', reply_markup=keyboard)
#     else:
#         bot.send_message(message.from_user.id, value, reply_markup=keyboard)

# @bot.callback_query_handler(func=lambda call: true)
# def callback_func(query)
#     global value, old_value
#     data = query.data

#     if data == 'no':
#         pass
#     elif data == 'C':
#         value = ' '
#     elif data == '<=':
#         if value != ' ':
#             value = value [:len(value)-1]
#     elif data == '=':
#         try:
#             value = str(eval(value))
#         except:
#             value = 'Ошибка!'
#     else += data

#     if ( value != old_value and value != ' ') or ('0' != old_value and value == ' ') :
#         if value == ' ':
#             bot.edit_message_text(chat_id=query.message.chat.id, message_id=query.message.message_id, text='0', reply_markup=keyborad)
#             old_value = '0'
#         else:
#             bot.edit_message_text(chat_id=query.message.chat.id, message_id=query.message.message_id, text=value,
#                                   reply_markup=keyborad)
#             old_value = value

#     if value == 'Ошибка!': value = ' '


# bot.polling(none_stop=False, interval=0)