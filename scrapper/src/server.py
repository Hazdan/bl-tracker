from sanic import Sanic
from sanic.response import text

app = Sanic("SCRAPPER")

@app.get("/")
async def hello_scrapper(request):
    return text("Hello, from scrapper.")
 

if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=5500,
        debug=True,
        auto_reload=True
    )