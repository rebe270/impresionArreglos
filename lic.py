from flask import Flask, render_template

app = Flask(__name__)

licenciaturas = ["EFN", "AGR", "TU", "GHT", "CP"]

def imprimir_licenciaturas():
    return licenciaturas

@app.route("/")
def index():
    licenciaturas_lista = imprimir_licenciaturas()
    return render_template("index.html", licenciaturas=licenciaturas_lista)

if __name__ == "__main__":
    app.run(debug=True)


