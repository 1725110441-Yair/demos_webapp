import web

urls = (
    '/', 'Index',
    '/parametros', 'Parametros'
)
app = web.application(urls, globals())
render = web.template.render('templates')

class Index:
    def GET(self):
        return render.index()
    
class Parametros:
    def GET(self):
        titulo = "Titulo desde Python"
        descripcion = """Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed eros nulla, tincidunt eu ante vel, aliquam semper turpis. Integer tristique erat at nisl consectetur facilisis. Integer ultrices condimentum purus ac elementum. Maecenas purus dolor, vestibulum nec erat in, accumsan rhoncus enim. Nulla turpis erat, luctus ullamcorper ligula tincidunt, mollis porttitor libero. Praesent imperdiet aliquet molestie. Morbi eros libero, lobortis ac interdum nec, aliquet non felis. Aenean mattis magna enim, nec viverra nulla ultricies sit amet. Donec facilisis faucibus libero. 
            Suspendisse non volutpat magna, a eleifend elit. Aenean sed porttitor augue. Suspendisse justo dolor, dictum ac nisl et, pharetra maximus orci. Sed ultrices, dolor nec volutpat consectetur, libero nibh commodo nisl, ut ultricies neque urna eu tellus. Suspendisse maximus, velit sit amet convallis accumsan, leo tortor ullamcorper purus, nec pellentesque arcu ligula eu erat. Donec dapibus magna enim, id egestas lacus molestie et. Fusce sit amet gravida mauris, nec sagittis nisi. Suspendisse accumsan tortor ac euismod efficitur. Sed viverra fringilla enim eget imperdiet. Donec nec lobortis enim, ut suscipit sem. Vestibulum rhoncus semper tellus, id accumsan neque vestibulum at."""
        return render.parametros(titulo, descripcion)

if __name__ == "__main__":
    app.run()