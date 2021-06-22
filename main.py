from sanic import Sanic
from sanic.response import json

app = Sanic()

@app.route("/")
async def test(request):
    return json({"stay in": "jakarta"})

# app = Sanic('myapp')
# app.config.DB_NAME = 'appdb'
# app.config.DB_USER = 'appuser'

# app = Sanic('myapp')
# app.config.DB_NAME = 'appdb'
# app.config.DB_USER = 'appuser'

# db_settings = {
#     'DB_HOST': 'localhost',
#     'DB_NAME': 'appdb',
#     'DB_USER': 'appuser'
# }
# app.config.update(db_settings)

# db_setting = { 
# 	'DB_HOST' : 'localhost',
# 	'DB_NAME' : 'appdb',
# 	'DB_USER' : 'appuser'
# }

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8011)