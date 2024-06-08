from flask import Flask, render_template, request, url_for
import ciphers.atbash as atbash
import ciphers.playfair as playfair
import ciphers.hill as hill
import ciphers.columnarTransposition as columnar
import ciphers.rail_fence as rail_fence
import ciphers.affine as affine

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/cipher/<algorithm>', methods=['GET', 'POST'])
def cipher(algorithm):
    result = ""
    text = ""
    if request.method == 'POST':
        text = request.form['text']
        action = request.form['action']

        if algorithm == 'atbash':
            if action == 'encrypt':
                result = atbash.encrypt(text)
            else:
                result = atbash.decrypt(text)
        elif algorithm == 'playfair':
            if action == 'encrypt':
                result = playfair.encrypt(text)
            else:
                result = playfair.decrypt(text)
        elif algorithm == 'affine':
            if action == 'encrypt':
                result = affine.encrypt(text)
            else:
                result = affine.decrypt(text)
        elif algorithm == 'columnar':
            key = request.form['key']
            if action == 'encrypt':
                result = columnar.Enkripsi(text, key)
            else:
                result = columnar.Dekripsi(text, key)
        elif algorithm == 'rail_fence':
            if action == 'encrypt':
                result = rail_fence.encrypt(text)
            else:
                result = rail_fence.decrypt(text)

    return render_template('index.html', algorithm=algorithm, text=text, result=result)

if __name__ == '__main__':
    app.run(debug=True)