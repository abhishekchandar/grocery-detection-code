import psycopg2

from config import config

# conn = psycopg2.connect(database=DB_NAME,user=USER_NAME,password=PWD,host=HOST)

def create_tables():
    """ create tables in the PostgreSQL database"""
    command ="CREATE TABLE vendors (vendor_id SERIAL PRIMARY KEY,item_num VARCHAR(255) NOT NULL, date DATE NOT NULL, time TIME NOT NULL)"
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params) #database=params[0],user=params[1],password=params[2],host=params[3]
        cur = conn.cursor()

        cur.execute(command)
        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

def insertRecord(item_num,date,time):
    sql = """INSERT INTO vendors(item_num,date,time) VALUES(%s, %s, %s) RETURNING vendor_id"""
    conn = None
    vendor_id = None
    try:
        params = config()
        conn = psycopg2.connect(**params) #database=params[0],user=params[1],password=params[2],host=params[3]
        cur = conn.cursor()
        
        print(item_num)
        cur.execute(sql,(item_num,date,time))
        vendor_id = cur.fetchone()[0]
        conn.commit()
        cur.close()
    except (Exception,psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
    print('success insertion!')

    return vendor_id

if __name__ == '__main__':

    # DB_NAME = "yolo_data"
    # USER_NAME = "rm_user"
    # PWD = "dbpassword"
    # HOST = "localhost"

    # params = (DB_NAME,USER_NAME,PWD,HOST)



    # create_tables()
    # insertRecord(1,dt_string,time_string)
    print('insert success!')
