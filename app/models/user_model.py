

def create_user_table(mysql):
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                      id INT AUTO_INCREMENT PRIMARY KEY,
                      username VARCHAR(50) NOT NULL,
                      email VARCHAR(50) NOT NULL)''')
    cursor.close()
    conn.close()