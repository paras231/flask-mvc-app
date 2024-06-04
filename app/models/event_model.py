


def create_evnt_table(mysql):
    conn =  mysql.connect()
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS events (
                      id INT AUTO_INCREMENT PRIMARY KEY,
                      event_name VARCHAR(50) NOT NULL,
                      event_code VARCHAR(50) NOT NULL)''')
    cursor.close()
    conn.close()