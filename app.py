from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/produtos")
def produtos():
    return render_template("produtos.html")

@app.route("/jogos")
def jogos():
    return render_template("jogos.html")

# ESTE BLOCO DEVE FICAR SEMPRE POR ÚLTIMO:
if __name__ == "__main__":
    app.run(debug=True)