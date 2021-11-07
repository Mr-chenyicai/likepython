from flask import Flask
app = Flask(__name__)
@app.route('/helloword',methods = ['GET'])
def index():
    return 'Hello,Word!'
if __name__ == '__main__':
    app.run()