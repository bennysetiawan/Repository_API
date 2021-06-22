from sanic import Sanic
from sanic.response import json, text

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

	mycursor.execute("SELECT image FROM akun2")
	myresult = mycursor.fetchall() #type list

	# dict_datanya = dict(myresult) 


	# return json(dict_datanya)

# -----------------------
	for x in range(10);
		file_image = io.BytesIO(myresult[x][0])
		img = image.open(file_image)
		img.save("mypicture"+ str(x)+ ".png")
		return await response.file("mypicture"+ str(x)+ ".png")


# print(myresult[0])
# print (type(myresult[0]))
# image = myresult[0]

# file_like2 = io.BytesIO(myresult[0][0])

# img1 = Image.Open(file_like2)

# img1.save("rotated_picture.jpg")

# return await response.file(img1)

# ------------------------------

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
# async def test(request):
#     return json({"HALAMAN" : "login"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9000)