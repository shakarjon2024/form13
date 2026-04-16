from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/form13', methods=['GET', 'POST'])
def form13():
    if request.method == 'POST':
        ism = request.form.get('ism')
        return f"<h2>Ism qabul qilindi: {ism}</h2><br><a href='/'>Orqaga</a>"
    return render_template('form13.html')

if __name__ == '__main__':
    app.run(debug=True)
