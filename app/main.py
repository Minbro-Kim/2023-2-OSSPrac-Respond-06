from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def input():
    return render_template('input.html')

@app.route('/result', methods=['POST', 'GET'])
def result():
    if request.method == 'POST':
        result = dict()
        result['Name'] = request.form.get('name')
        result['Student Number'] = request.form.get('StudentNumber')
        result['University'] = request.form.get('university')
        result['Major'] = request.form.get('major')
        result['Gender'] = request.form.get('Gender')
        email = request.form.get('email')
        domain = request.form.get('domain')
        result['Email'] = email + "@" + domain
        result['Languages'] = ', '.join(request.form.getlist('programmingLanguage')) 
        return render_template('result.html', result=result)

if __name__ == '__main__':
    app.run(debug=True, port=5000)