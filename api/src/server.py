from sanic import Sanic
from sanic.response import text

app = Sanic("API")

@app.get("/")
async def hello_api(request):
    return text("Hello, from api.")
 
if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=3000,
        debug=True,
        auto_reload=True
    )