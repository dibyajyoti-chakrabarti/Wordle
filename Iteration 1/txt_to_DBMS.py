import mysql.connector as mc
from mysql.connector import Error



file = open("C:\Debbo 12A\Wordle\guessBank.txt",'r')
content = file.read()
file.close()

wordList=content.split('\n')
try:
    #Connecting variables for DBMS
    connectCredentials = {
        'user' : 'root',
        'password' : 'iCode69!',
        'database': 'wordle',
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
        
        for i in wordList:
            command = "insert into valid_words values (\""+i+"\");"
            cursor.execute(command)
            #print(command)
 
        
       
# Only useful if error while connecting
except Error as e:
    print("Error while connecting")

#Closing connections 
finally:
    if conn.is_connected():
        cursor.close()
        conn.close()
    print("Done")


file=open("C:\Debbo 12A\Wordle\wordBank.txt",'r')
content=file.read()
file.close()

string=''
for i in content:
    if i == ' ':
        i='\n'
    string+=i
wordBank=string.split('\n')

try:
    #Connecting variables for DBMS
    connectCredentials = {
        'user' : 'root',
        'password' : 'iCode69!',
        'database': 'wordle',
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
        
        for i in wordBank:
            command = "insert into word_bank values (\""+i+"\");"
            cursor.execute(command)
            #print(command)

        for i in wordBank:
            command = "insert into valid_words values (\""+i+"\");"
            cursor.execute(command)
        
       
# Only useful if error while connecting
except Error as e:
    print("Error while connecting")

#Closing connections 
finally:
    if conn.is_connected():
        cursor.close()
        conn.close()
    print("Done")


