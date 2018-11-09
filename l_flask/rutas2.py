from flask import Flask
from flask import request
app=Flask(__name__)
@app.route('/')
def index():
    return "hola esto es ejemplo 2"


@app.route('/params')
def params():
    #si solo escribes para parama1 te sale eso y no escribsite nada foroo
    param=request.args.get('param1', 'No escribiste nada forro')
    param2 = request.args.get('param2', 'No escribiste nada forro')
    return 'lo que es escribiste es:{}.{}'.format(param,param2)


if (__name__ =='__main__'):
    app.run(debug=True,port=5000)
