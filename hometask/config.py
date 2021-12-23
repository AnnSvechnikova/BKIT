from enum import  Enum

#токен бота
TOKEN = '5037268913:AAHDueSGRATmwFeWYNISf9KikpCKJDV1HwY'

#файл базы данных Vedis
db_file = "db.vdb"

# Ключ записи в БД для текущего состояния
CURRENT_STATE = "CURRENT_STATE"

# Состояния автомата
class States(Enum):
    STATE_START = "STATE_START"  # Начало нового диалога
    STATE_PLACE = "STATE_PLACE" # желаемое место
    STATE_IS_ACTIVE = "STATE_IS_ACTIVE" # активный отдых или нет
    STATE_QUANTITY = "STATE_QUANTITY" # размер компании
