import mysql.connector as mc
from mysql.connector import Error


try:
    #Connecting variables for DBMS
    connectCredentials = {
        'user' : 'root',
        'password' : 'iCode69!',
        'database': 'practice',
        'raise_on_warnings': True,
        'autocommit': True
        }
    
    #Connecting to DBMS
    conn = mc.connect(**connectCredentials)

    #When connected
    if conn.is_connected():
        dbInfo = conn.get_server_info()
        print("The server details", dbInfo)

        cursor = conn.cursor()
        
        # 1 line of action
        '''cursor.execute("Select * from table1;")
        ans = cursor.fetchall()
        for i in ans:
            print(i)'''

        # 2 line of action
        cursor.execute("Select s_name,(english + maths + science) as total_mks from table1 order by total_mks desc;")
        contentList = cursor.fetchall()
        for i in contentList:
            print(i)
        
       
# Only useful if error while connecting
except Error as e:
    print("Error while connecting")

#Closing connections 
finally:
    if conn.is_connected():
        cursor.close()
        conn.close()
    print("Done")