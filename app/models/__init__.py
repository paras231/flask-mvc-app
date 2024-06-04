from .user_model import create_user_table
from .event_model import create_evnt_table

def create_db_tables(mysql):
    create_user_table(mysql)
    create_evnt_table(mysql)
