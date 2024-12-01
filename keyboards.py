from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

start_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='price'),
         KeyboardButton(text='about'),
         KeyboardButton(text='BUY')]
    ], resize_keyboard=True)

catalog_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='for beginners', callback_data='beginners' )],
        [InlineKeyboardButton(text='for normal', callback_data='normal')],
        [InlineKeyboardButton(text='for advanced', callback_data='advanced')],
        [InlineKeyboardButton(text='for super advenced', callback_data='super')],
        [InlineKeyboardButton(text='other', callback_data='other')]
    ])

buy_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Buy!', url='ya.ru')]
    ])

buy_2_kb = InlineKeyboardMarkup(row_width=4)
butt_1 = InlineKeyboardButton(text='Book 1', callback_data='product_buying')
butt_2 = InlineKeyboardButton(text='Book 2', callback_data='product_buying')
butt_3 = InlineKeyboardButton(text='Book 3', callback_data='product_buying')
butt_4 = InlineKeyboardButton(text='Book 4', callback_data='product_buying')
buy_2_kb.row(butt_1, butt_2, butt_3, butt_4)