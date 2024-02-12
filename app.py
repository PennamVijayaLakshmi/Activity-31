from flask import Flask,request
from model import predict_model

app=Flask(__name__)

@app.route('/')
def basic():
    return 'api server started'
@app.route('/soil',methods=['get'])
def soil():
    value=request.args.get('soil')
    print(value)
    value=int(value)
    response=predict_model(value)
    return {'msg':response}
if __name__=="__main__":
    app.run('0.0.0.0',port=5001)