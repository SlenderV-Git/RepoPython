from aiogram.types import Message, ChatMemberUpdated
from Data.database import Database

db = Database('Data/project.db')

def chat_table():
    db.execute_query('''CREATE TABLE IF NOT EXISTS chat_settings
                    (chat_id INTEGER PRIMARY KEY AUTOINCREMENT,
                     tg_chat_id INTEGER,
                     tg_chat_title TEXT)
                     ''')
    
def reg_chat(message : Message | ChatMemberUpdated):
    chat_table()
    db.execute_query('''INSERT INTO chat_settings (tg_chat_id, tg_chat_title) VALUES (?,?)''', (message.chat.id, message.chat.username))
    
def select_chat():
    rows = [item[0] for item in db.execute_query_result("SELECT * FROM chat_settings")]
    print(rows)
    '''if len(rows) < 2:
        return str(rows)
    else:
        return "\n".join(["".join(map(str, row)) for row in rows])'''