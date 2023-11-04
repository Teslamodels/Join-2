import psycopg2
from psycopg2 import Error


def insert_category(Title, Description):
    try:
        connection = psycopg2.connect(user = 'postgres', password = 'postgres', host = 'localhost', port = 5432, database = 'Join')
        cursor = connection.cursor()

        cursor.execute("""INSERT INTO Category(Title, Description)
                       VALUES(%s, %s);""", (Title, Description))

        connection.commit()
        
        print("The mission is successully done")

    except(Exception, Error) as error:
        print("Error", error)

    finally:
        if connection:
            cursor.close()
            connection.close()
            print("Successfully closed!")