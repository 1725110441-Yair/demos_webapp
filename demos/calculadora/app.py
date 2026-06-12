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
        numero_1=0.0
        numero_2=0.0
        resultado=0.0
        return render.calculadora(numero_1, numero_2, resultado)
    
    def POST(self):
        formulario = web.input()
        numero_1 = float(formulario['numero_1'])
        numero_2 = float(formulario['numero_2'])
        if formulario['operacion'] == "sumar":
            resultado = numero_1 + numero_2
        elif formulario['operacion'] == "restar":
            resultado = numero_1 - numero_2
        elif formulario['operacion'] == "multiplicar":
            resultado = numero_1 * numero_2
        elif formulario['operacion'] == "dividir":
            resultado = numero_1 / numero_2
        elif formulario['operacion'] == "raiz_cuadrada":
            raiz_1 = numero_1 ** 0.5
            raiz_2 = numero_2 ** 0.5
            resultado = raiz_1
        elif formulario['operacion'] == "potencia":
            potencia1 = numero_1 * numero_1
            potencia2 = numero_2 * numero_2
            resultado = potencia1
        elif formulario['operacion'] == 'modulo':
            resultado = numero_1 % numero_2
        elif formulario['operacion'] == 'limpiar':
            numero_1 = 0.0
            numero_2 = 0.0
            resultado = 0.0
        return render.calculadora(numero_1, numero_2, resultado)

if __name__ == "__main__":
    app.run()