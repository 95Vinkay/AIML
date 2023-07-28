from flask import Flask, render_template, request  # devloping web application using Python
from nltk.chat.util  import Chat

que1 = r'how are you'
ans1 = ['all well','I am good','Awesome']

que2 = r'what can you do'
ans2 = ['I can reply to your queries','I am here to answer to your question','I can chat with you']

que3 = r'what is your name'
ans3 = ['My name is Chatty','I am Chatty']


que4 = r'(.*)mausam(.*)ba[a]*rish'  # aaj mausam kaisa hai, kya baarish hogi?
ans4 = ['it looks it will rain today','baarish ka mausam hai','baarish ho sakti hai mausam kharab hai']


qa_pair = [
    (que1, ans1),
    (que2, ans2),
    (que3, ans3),
    (que4, ans4),
]
chatbot = Chat(qa_pair)
 
app = Flask(__name__)

@app.route('/')
def home():
    global chatbot
    query = request.args.get('query')
    if query !=None:
        response =chatbot.respond(query )
        if response == None:
            response = 'Sorry I am not sure'
        
    else:
         response = ''
      
     #return "This is coming from Flask"
    return render_template('index.html', result=response)

@app.route('/chatbot')
def chat():
    return "<h2>Chat Bot</h2>"

app.run(debug = True)