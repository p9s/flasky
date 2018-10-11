from flask import Flask

app = Flask(__name__)



@app.route( '/' )
def index():
    return '<h1>Hello Flask</h1>'


# app.add_url_rule( '/', 'index', index )


#  @app.route( '/user/<name>' )
#  def user( name ):
#      return '<h1>Hello, {}!</h1>'.format( name )
#  
#  # int string float path
#  # path 可以包含正斜线, 其它与 string 类似
#  @app.route( '/user/<int:id>' )
