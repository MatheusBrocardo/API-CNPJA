from database.settings import conn

def CheckDataBaseConnection():
    try:
        cursor = conn.cursor()
        execute = "select 1 from dual" 
        cursor.execute(execute)
        result = cursor.fetchone()
        cursor.close()
    except Exception as error:
        return False
    return True