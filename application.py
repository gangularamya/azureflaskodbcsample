from flask import Flask
import pyodbc

server='pythontestmysql.mysql.database.azure.com'
database='person'
username='username@pythontestmysql'
password='Password1'

app = Flask(__name__)

conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor=conn.cursor()

@app.route("/")
def hello():
    SQLCommand = ("INSERT INTO dbo.employee "
                 "(name, age, place) "
                 "VALUES (?,?,?)")
    Values = ['t','3','t']
    cursor.execute(SQLCommand,Values)
    conn.commit()
    conn.close()

    return "Hello World!"    

if __name__ == "__main__":
    app.run() 
   
