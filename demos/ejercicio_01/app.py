import web

urls = (
    '/', 'Index',
    '/usuarios', 'Usuarios',
    '/clientes', 'Clientes'
)
app = web.application(urls, globals())
render = web.template.render('templates')

class Index:
    def GET(self):
        return "Pagina index"
    
class Usuarios:
    def GET(self):
        return "Página de usuarios"
    
class Clientes:
    def GET(self):
        return "Pagina de clientes"

if __name__ == "__main__":
    app.run()