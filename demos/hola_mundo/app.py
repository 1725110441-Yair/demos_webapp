import web #Comunicacion de las paginas y bases de datos

urls = (
    '/', 'Index' # (/) es la url, (Index) es el nombre de la clase
)
app = web.application(urls, globals()) #Objeto tipo aplicación web

class Index: #Clase de una ruta
    def GET(self):
        return 'Hola mundo desde web.py'

if __name__ == "__main__":
    app.run()