from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

persons_list = [
    {
        'name': 'John',
        'surname': 'Johnson',
        'age': 12
    }
]


@app.route('/persons', methods=['GET', 'POST'])
def persons():
    if request.method == 'GET':
        return render_template('index.html', persons=persons_list)
    elif request.method == 'POST':
        persons_list.append(request.form)
        print(url_for('persons'))
        return redirect(url_for('persons'))


app.run(debug=True)