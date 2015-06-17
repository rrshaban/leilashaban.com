from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return app.send_static_file('index.html')

if __name__ == '__main__':
    app.run(debug=True)
    
# http://api.giphy.com/v1/gifs/search?q=thizz&api_key=dc6zaTOxFJmzC
