from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    testimonials = [
        {
            "name": "Maria de Oliveira",
            "rating": "⭐⭐⭐⭐⭐",
            "photo": "https://via.placeholder.com/50",
            "comment": "A experiência com o Despacho Rápido foi incrível!"
        },
        {
            "name": "João Silva",
            "rating": "⭐⭐⭐⭐",
            "photo": "https://via.placeholder.com/50",
            "comment": "Ótimo atendimento e rapidez no serviço."
        },
        {
            "name": "Ana Clara",
            "rating": "⭐⭐⭐⭐⭐",
            "photo": "https://via.placeholder.com/50",
            "comment": "Super recomendo, trabalho excelente!"
        }
    ]
    return render_template("index.html", testimonials=testimonials)

if __name__ == "__main__":
    app.run(debug=True)
