from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        ad = request.form['ad']
        email = request.form['email']
        print(f"Yeni qeydiyyat: Ad - {ad}, Email - {email}")
        return render_template('thanks.html', ad=ad, email=email)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)


