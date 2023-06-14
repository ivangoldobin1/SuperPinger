from typing import List, Any

# Лист тестируемых ip адресов
IP_LIST = [
    "8.8.8.8",
    "8.8.4.4"
]
# Лист тестируемых доменов
DOMAIN_LIST: List[Any] = [
    ["https://google.ru", "Google.ru"],
    ["https://ya.ru", "Ya.ru"]
]

# https://api.telegram.org/botAPI_TOKEN/getUpdates
CHAT_IDS = [
]

# В кавычки вставить API для бота полученный от @BotFather
API_TOKEN = '' 

# Время автоматического тестирования в секундах
PING_TIME = 300