from sanic import Sanic
from sanic.response import html

from jinja2 import Environment, PackageLoader

env = Environment(loader=PackageLoader('app', 'templates'))

app = Sanic()

app.static('/static/', './static/')


@app.route('/')
async def index(request):
    template = env.get_template('index.html')
    html_content = template.render()
    return html(html_content)


@app.route('/login')
async def login(request):
    template = env.get_template('login.html')
    html_content = template.render()
    return html(html_content)


app.run(host='0.0.0.0', port=8000)

