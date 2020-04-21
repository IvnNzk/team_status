from sanic import Sanic
from sanic.views import HTTPMethodView
from sanic.response import html, json
from sanic_session import Session, InMemorySessionInterface
from jinja2 import Environment, PackageLoader
from sanic_jinja2 import SanicJinja2

app = Sanic(name='app')
jinja = SanicJinja2(app)

session = Session(app, interface=InMemorySessionInterface())

env = Environment(loader=PackageLoader('app', 'templates'))

app.static('/static/', './static/')


class DashboardView(HTTPMethodView):
    async def get(self, request):
        persons = [{'name': 'Ivan Oschepkov', 'status': 'working on <a href="#">#7858389</a>'},]
        return jinja.render('index.html.j2', request, team_members=persons)

class LoginView(HTTPMethodView):
    async def get(self, request):
        return jinja.render('login.html.j2', request)

    async def post(self, request):
        return json({'form_data': request.form})


app.add_route(DashboardView.as_view(), '/')
app.add_route(LoginView.as_view(), '/login')


app.run(host='0.0.0.0', port=8000, debug=True)

