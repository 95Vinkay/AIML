from flask import Flask, render_template, request  # devloping web application using Python

app = Flask(__name__)

@app.route('/')
def home():
    query = request.args.get('query')
    if query !=None:
        response = 'We got query'
        
    else:
         response = ''
      
   

   
    #return "This is coming from Flask"
    return render_template('index.html', result=response)

@app.route('/chatbot')
def chat():
    return "<h2>Chat Bot</h2>"

app.run(debug = True)
