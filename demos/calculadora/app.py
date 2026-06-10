import web

urls = (
    '/', 'Index',
    '/calculadora', 'Calculadora'
)
app = web.application(urls, globals())
render = web.template.render('views')

class Index:
    def GET(self):
        return render.index()
    
class Calculadora:
    def GET(self):
        return render.calculadora()
    
    def POST(self):
        formulario = web.input()
        numero1 = int(formulario.numero1)
        numero2 = int(formulario.numero2)
        suma = numero1 + numero2
        return render.calculadora(resultado=suma)

if __name__ == "__main__":
    app.run()