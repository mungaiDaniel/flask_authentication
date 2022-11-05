from flask import Flask, request, make_response
from functools import wraps

app = Flask(__name__)

def auth_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if auth and auth.username == 'username1' and auth.password == 'password':
            return f(*args, **kwargs)
        
        
        return make_response('could not verify', 401, {'WWW-Authenticate': 'Basic realm="Login Required"'})
    
    return decorated

@app.route('/index')
def index():
    if request.authorization and request.authorization.username == 'username' and request.authorization.password == 'password':
        return {"msg": "you are logged in"}
    return make_response('could not verify!', 401, {'www-Authenticate': 'Basic realm="Login Required"'})
@app.route('/page')
@auth_required
def page():
    return '<h1> YOU ARE IN PAGE </h1>'
if __name__ == '__main__':
    app.run(debug=True)