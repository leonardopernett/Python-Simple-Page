from  flask import Flask,render_template

#initialization
app = Flask(__name__)

#router
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return  render_template('about.html')


#server 
app.run(debug=True)