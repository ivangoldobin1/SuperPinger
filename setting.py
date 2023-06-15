from typing import List, Any

# Лист тестируемых ip адресов
IP_LIST = [
    ["8.8.8.8", "DNS Google"],
    ["192.192.192.192", "Null IP"]
]

# Лист тестируемых доменов
DOMAIN_LIST: List[Any] = [
    ["https://google.ru", "Гугл"],
    ["https://yaрпм32наигуп.ru", "Яндекс"]
]

# https://api.telegram.org/botAPI_TOKEN/getUpdates
CHAT_IDS = [
    ""
]

# В кавычки вставить API для бота полученный от @BotFather
API_TOKEN = '' 

# Время автоматического тестирования в секундах
PING_TIME = 30