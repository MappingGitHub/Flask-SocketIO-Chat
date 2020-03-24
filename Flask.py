from flask import Flask,render_template,request,redirect,url_for
app = Flask(__name__)


@app.route('/')
def home():
    #return "<h2>Welcome to G5Chat </h2>"
     return render_template('home.html')
@app.route('/chat')
def chat():
    Username=request.args.get('Username')
    Password=request.args.get('Password')
    Room=request.args.get('Room') 
    
    if Username and Password and Room:
         return render_template('chat.html',Username=Username,Password=Password,Room=Room)
    else:
         return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
