import random
from telegram import Update, ReplyKeyboardMarkup, KeyboardButton, update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import requests


TOKEN = '6917219030:AAFcjgrlmZZQ8kYv_8htzcne_8FUi2cllQA'
EXCHANGERATE_API_KEY = '49bbbdf84d605feeb2f6d651'
ALPHA_VANTAGE_API_KEY = 'YEEL9R99DW0Z2JSR'

def start(update: Update, context: CallbackContext) -> None:
    user = update.message.from_user
    emoji = "🤖"
    update.message.reply_text(
        f"{emoji} Здравствуй, {user.first_name}! Я финансовый бот STS. Выберите интересующую вас функцию:",
        reply_markup=get_keyboard()
    )

def back(update: Update, context: CallbackContext) -> None:
    user = update.message.from_user
    emoji = "🤖"
    update.message.reply_text(
        " Выберите интересующую вас функцию:",
        reply_markup=get_keyboard()
    )

def currency_rates(update: Update, context: CallbackContext) -> None:
    chat_id = update.message.chat_id
    keyboard = [
        [KeyboardButton("🇺🇸 Доллар в тенге")],
        [KeyboardButton("🇪🇺 Евро в тенге")],
        [KeyboardButton("🇷🇺 Рубль в тенге")],
        [KeyboardButton("🇬🇧 Фунт стерлинга в тенге")],
        [KeyboardButton("🇦🇪 Арабский дирхам в тенге")],
        [KeyboardButton("🇰🇬 Киргизский сом в тенге")],
        [KeyboardButton("🇺🇦 Украинская гривна в тенге")],
        [KeyboardButton("🇨🇳 Китайский юань в тенге")],
        [KeyboardButton("🇰🇷 Южнокорейская вона в тенге")],
        [KeyboardButton("назад")],
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    update.message.reply_text("Выберите валюту для просмотра курса:", reply_markup=reply_markup)

def get_exchange_rate(base_currency: str, target_currency: str) -> float:
    url = f'https://api.exchangerate-api.com/v4/latest/{base_currency}'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        rate = data['rates'][target_currency]
        return rate
    else:
        return None

def show_exchange_rate(update: Update, context: CallbackContext, base_currency: str, target_currency: str) -> None:
    chat_id = update.message.chat_id
    rate = get_exchange_rate(base_currency, target_currency)

    if rate is not None:
        message = f'Курс {base_currency} в {target_currency}: {rate:.2f}'
    else:
        message = "Ошибка при запросе курса валюты."

    update.message.reply_text(message)

import requests

def get_crypto_rate() -> str:   #crypto
    url = f'https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,ETH,ETC,XMR,SOL,USDT,BNB,DOGE,XRP,AVAX&tsyms=KZT'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        BTC = data['DISPLAY']['BTC']['KZT']['PRICE']
        ETH = data['DISPLAY']['ETH']['KZT']['PRICE']
        ETC = data['DISPLAY']['ETC']['KZT']['PRICE']
        XMR = data['DISPLAY']['XMR']['KZT']['PRICE']
        SOL = data['DISPLAY']['SOL']['KZT']['PRICE']
        USDT = data['DISPLAY']['USDT']['KZT']['PRICE']
        BNB = data['DISPLAY']['BNB']['KZT']['PRICE']
        DOGE = data['DISPLAY']['DOGE']['KZT']['PRICE']
        XRP = data['DISPLAY']['XRP']['KZT']['PRICE']
        AVAX = data['DISPLAY']['AVAX']['KZT']['PRICE']


        text = f'BTC = {BTC}\n'
        text += f'ETH = {ETH}\n'
        text += f'ETC = {ETC}\n'
        text += f'XMR = {XMR}\n'
        text += f'SOL = {SOL}\n'
        text += f'USDT = {USDT}\n'
        text += f'BNB = {BNB}\n'
        text += f'DOGE = {DOGE}\n'
        text += f'XRP = {XRP}\n'
        text += f'AVAX = {AVAX}\n'

        return text
    else:
        return None

def show_snp_prices(update: Update, context: CallbackContext) -> None:
    # Добавьте здесь логику для получения и отображения стоимости акций S&P500
    update.message.reply_text("Здесь вы увидите стоимость акций S&P500.")

def get_snp_prices() -> str:
    base_url = 'https://www.alphavantage.co/query'
    function = 'TIME_SERIES_DAILY'
    symbol = '^GSPC'  # Тикер S&P500
    api_key = ALPHA_VANTAGE_API_KEY

    params = {
        'function': function,
        'symbol': symbol,
        'apikey': api_key,
    }

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        data = response.json()

        # Извлеките необходимые данные, например, цену закрытия:
        last_refreshed = data['Meta Data']['3. Last Refreshed']
        close_price_today = data['Time Series (Daily)'][last_refreshed]['4. close']

        return f'Цена S&P 500 на {last_refreshed}: {close_price_today}'
    else:
        return 'Ошибка при запросе стоимости акций S&P 500.'


def get_snp_rate(base_currency: str, target_currency: str) -> float:   #S&P500
    url = f'https://financialmodelingprep.com/api/v3/sp500_constituent (APIkey ) {base_currency}'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        rate = data['rates'][target_currency]
        return rate
    else:
        return None

def handle_stock_choice(update: Update, context: CallbackContext) -> None:
    chosen_stock = update.message.text.upper()
    chat_id = update.message.chat_id

    if chosen_stock == 'НАЗАД':
        start(update, context)
    elif chosen_stock == 'S&P 500':
        # Добавьте действие для показа стоимости акций S&P500
        show_snp_prices(update, context)
    else:
        show_stock_price(update, context, chosen_stock)



def handle_currency_choice(update: Update, context: CallbackContext) -> None:
    chosen_currency = update.message.text.lower()
    base_currency = 'KZT'  # Валюта, относительно которой смотрим курс

    currency_mapping = {
        '🇺🇸 доллар в тенге': 'USD',
        '🇪🇺 евро в тенге': 'EUR',
        '🇷🇺 рубль в тенге': 'RUB',
        '🇬🇧 фунт стерлинга в тенге': 'GBP',
        '🇦🇪 арабский дирхам в тенге': 'AED',
        '🇰🇬 киргизский сом в тенге': 'KGS',
        '🇺🇦 украинская гривна в тенге': 'UAH',
        '🇨🇳 китайский юань в тенге': 'CNY',
        '🇰🇷 южнокорейская вона в тенге': 'KRW',
    }

    if chosen_currency in currency_mapping:
        show_exchange_rate(update, context, currency_mapping[chosen_currency], base_currency)
    else:
        update.message.reply_text("Выберите валюту из списка.")



def crypto_rates(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(get_crypto_rate()) #res

import requests

def get_price(symbol: str) -> str:   #S&P500
    url = f'https://finnhub.io/api/v1/quote?symbol={symbol}'
    headers_test = {'X-Finnhub-Token': 'cleip31r01qnc24e5vi0cleip31r01qnc24e5vig'}
    response = requests.get(url, headers=headers_test)
    rate = response.json()
    return rate


def snp_prices(update: Update, context: CallbackContext) -> None:
    # text = f'3M Co.' + get_price('AAPL')
    text = 'Please check headers'
   # text += f'Abbott Laboratories ' + get_price('abt')

    #3M Co. - mmm
    #Abbott Laboratories - abt
    #AbbVie Inc - abbv
    #Accenture plc - acn
    #Alphabet C (ex Google) - goog
    #Altria Inc. - mo
    #Amazon - amzn
    #AMD (Advanced Micro Devices) Inc. - amd
    #American Electric Power Co. Inc. - aep
    #American Express Co. - axp
    #American International Group (AIG) Inc. - aig
    #Adobe - adbe

    update.message.reply_text(text)

def financial_advice(update: Update, context: CallbackContext) -> None:
    advice_list = [
        "✅ Регулярно откладывайте часть своего дохода на сбережения, чтобы создать финансовый запас на случай неожиданных расходов.",
        "✅ Инвестируйте в разнообразные активы, чтобы уменьшить риски и повысить потенциальную доходность вашего портфеля.",
        "✅ Составьте бюджет и придерживайтесь его, чтобы эффективно управлять своими финансами.",
        "✅ Деньги - это круто.",
        "✅ А когда не делали?!",
        "✅ Безделье - игрушка дьявола.",
        "✅ Избегайте долгов с высокими процентными ставками и стремитесь к полному погашению кредитов.",
        "✅ Постоянно обучайтесь финансовой грамотности, чтобы принимать более обоснованные решения о своих финансах.",
        "✅ Создайте аварийный фонд, соответствующий 3-6 месяцам ваших ежемесячных расходов, чтобы быть готовым к финансовым неурядицам.",
        "✅ При выборе страховки обратите внимание не только на стоимость, но и на покрытие, чтобы обеспечить себя и свою семью в случае несчастного случая.",
        "✅ Изучайте рынок перед покупкой крупных товаров, чтобы получить лучшие предложения и сэкономить деньги.",
        "✅ Рассмотрите возможность дополнительного заработка через пассивный доход или фриланс, чтобы увеличить свой финансовый потенциал.",
        "✅ Оцените свои финансовые цели и разработайте конкретный план достижения каждой из них.",
        "✅ Планируйте пенсию с ранних лет, вкладывая средства в пенсионные счета или инвестиционные фонды.",
        "✅ Установите цели по погашению долгов и строго придерживайтесь этого плана, чтобы избежать финансовых трудностей.",
        "✅ Сравнивайте процентные ставки перед тем, как брать кредиты или ипотеку, чтобы выбрать наилучшие условия.",
        "✅ Избегайте чрезмерных трат на ненужные вещи; оцените, действительно ли покупка необходима.",
        "✅ Не стесняйтесь обращаться за профессиональным финансовым советом, чтобы принимать информированные решения по управлению своими финансами."
    ] #список рандом советов

    selected_advice = random.choice(advice_list)

    # Сохраняем выбранный совет в контексте
    context.user_data['financial_advice'] = selected_advice

    update.message.reply_text(selected_advice)



def get_keyboard():
    keyboard = [
        [KeyboardButton("Курсы валют")],
        [KeyboardButton("Курсы криптовалют")],
        [KeyboardButton("Стоимость акций")],
        [KeyboardButton("Финансовый совет")],  # Новая кнопка для финансового совета
    ]
    return ReplyKeyboardMarkup(keyboard, resize_keyboard=True)


def main() -> None:
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.regex('^Финансовый совет$'), financial_advice))
    dp.add_handler(MessageHandler(Filters.regex('^Курсы валют$'), currency_rates))
    dp.add_handler(MessageHandler(Filters.regex(
        '^🇺🇸 Доллар в тенге$|^🇪🇺 Евро в тенге$|^🇷🇺 Рубль в тенге$|^🇬🇧 Фунт стерлинга в тенге$|^🇦🇪 Арабский дирхам в тенге$|^🇰🇬 Киргизский сом в тенге$|^🇺🇦 Украинская гривна в тенге$|^🇨🇳 Китайский юань в тенге$|^🇰🇷 Южнокорейская вона в тенге$'),
                                  handle_currency_choice))
    dp.add_handler(MessageHandler(Filters.regex('^Курсы криптовалют$'), crypto_rates))
    dp.add_handler(MessageHandler(Filters.regex('^назад$'), back))
    dp.add_handler(MessageHandler(Filters.regex('^Стоимость акций$'), snp_prices))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
