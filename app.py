from flask import Flask, render_template, jsonify

app = Flask(__name__)


@app.route("/")
def hello_world():
  return render_template('home.html')

@app.route('/')
def home():
    dropdown_options = ['Option 1', 'Option 2', 'Option 3', 'Option 4', 'Option 5']
    return render_template('home.html', dropdown_options=dropdown_options)


# @app.route('/search')
# def search():
 # query = request.args.get('query')
 # return render_template('search_results.html')


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
