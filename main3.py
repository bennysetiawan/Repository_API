from sanic import Sanic
from sanic.response import json
from sanic.response import text

import mysql.connector

app = Sanic()

# mydb = mysql.connector.connect(
#   host="localhost",
#   user="bennys",
#   passwd="123456789",
#   database="dbsanic02")

#print(mydb) 
# mycursor = mydb.cursor()

# mycursor.execute("CREATE TABLE customers VARCHAR (255), address VARCHAR(255))")


@app.route("/")
async def test(request):
    return json({"stay in": "jakarta"})

@app.route("/list")
async def test(request):
	mydb = mysql.connector.connect(
		host='0.0.0.0',
		user="root",
		passwd="123456789",
		database="Database01")
    #return json({"HALAMAN": "REGISTER"})
	mycursor = mydb.cursor()

	mycursor.execute("SELECT * FROM test")
	myresult = mycursor.fetchall() #type list

	dict_datanya = dict(myresult) 


	return json(dict_datanya)

# -----------------------
# from flask import send_file

# @app.route('/get_image')
# def get_image():
#     if request.args.get('type') == '1':
#        filename = 'ok.gif'
#     else:
#        filename = 'error.gif'
#     return send_file(filename, mimetype='image/gif')
# ------------------------

# @app.route("/login")
async def test(request):
    return json({"HALAMAN" : "login"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9000)