from sanic import Sanic
from sanic.response import json
from sanic.response import text

app = Sanic()

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