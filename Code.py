import pymysql
import os
import time
os.chdir("/home/pi/Desktop/IMage_sql")#Enter the path where the images needs to be stored
pymysql.install_as_MySQLdb()
import MySQLdb

db = MySQLdb.connect("Host","Username","password","databasename" )
cursor = db.cursor()

while(True):
    try:
        os.system("raspistill -o img1.jpg")
        print("Written")
    except:
        print("Unable to take image")
    with open("img1.jpg",'rb') as file:
        binary=file.read()
        sql="UPDATE CAMERA SET Image = %s WHERE sno = 1" #make an entry in the table with sno 1
        print(len(binary))
        try:
            cursor.execute(sql,(binary))
            db.commit()
            print("sql written")
        except:
            db.rollback()
            print("SQL update failed for image")
    time.sleep(2)  
db.close()
