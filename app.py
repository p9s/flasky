from flask import Flask
from flask import request
from flask import current_app

app = Flask(__name__)



@app.route( '/' )
def index():
    user_agent = request.headers.get( 'User-Agent' )

    response = make_response( '<h1>Hello Flask</h1>' )
    response.set_cookie( 'anawer', '42' )
    return response


@app.route( '/user/<name>' )
def user(name):
    return 'User: {}!'.format( name )


# app.add_url_rule( '/', 'index', index )


#  @app.route( '/user/<name>' )
#  def user( name ):
#      return '<h1>Hello, {}!</h1>'.format( name )
#  
#  # int string float path
#  # path 可以包含正斜线, 其它与 string 类似
#  @app.route( '/user/<int:id>' )
