from flask import Flask
from flask import render_template
from flask_cors import CORS
from flask_restful import Api
from api.naver_news import Naver
from flask import jsonify#JSON형태의 문자열로 응답시

app=Flask(__name__)
CORS(app)

api = Api(app)
api.add_resource(Naver,'/naver')

if __name__ == '__main__':
    app.run(debug=True,host='127.0.0.1',port=8282)