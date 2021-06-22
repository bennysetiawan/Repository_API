from sanic import Sanic
from sanic.response import json
from sanic.response import text
import mysql.connector

app = Sanic()

mydb = mysql.connector.connect(
  host="0.0.0.0",
  user="bennys",
  passwd="123456789"
)

#print(mydb) 
mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE customers VARCHAR (255), address VARCHAR(255))")


@app.route("/")
async def test(request):
    return json({"stay in": "jakarta"})

@app.route("/register")
async def test(request):
    return json({"HALAMAN": "REGISTER"})

@app.route("/login")
async def test(request):
    return json({"HALAMAN" : "login"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)