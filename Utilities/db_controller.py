from Data.database import Database

db = Database('Data/project.db')

def user_table():
    db.execute_query('''CREATE TABLE IF NOT EXISTS user_data
                    (user_id INTEGER PRIMARY KEY AUTOINCREMENT, 
                    tg_id INTEGER, 
                    user TEXT, 
                    is_admin INTEGER 
                    CHECK(is_admin IN (0,1,2)))''')
    
def add_user(message, is_admin : int = 0):
    user_table()
    user_data = message.from_user
    if user_data.id not in get_user_list():
        db.execute_query("INSERT INTO user_data (tg_id, user, is_admin) VALUES (?,?,?)", (user_data.id, user_data.username, is_admin))

def check_user_list():
    user_table()
    rows = db.execute_query_result('''SELECT * FROM user_data''')
    return "\n".join([', '.join(map(str, row)) for row in rows])

def get_user_list():
    return [item[0] for item in db.execute_query_result("SELECT tg_id FROM user_data")]

def get_admin_list():
    return [item[0] for item in db.execute_query_result("SELECT tg_id FROM user_data WHERE is_admin = 1")]