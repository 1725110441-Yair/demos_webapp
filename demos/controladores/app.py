import web

urls = (
    '/', 'controllers.index.Index',
    '/contactos', 'controllers.contactos.Contactos'
)
app = web.application(urls, globals())

if __name__ == "__main__":
    app.run()