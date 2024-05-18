#!/usr/bin/env Python3

from flask import Flask

# from meters import routes
from meters.routes import meter_routes


app = Flask(__name__)

app.config['SECRET_KEY'] = 'this is secret'


# Meter Routes
app.register_blueprint(meter_routes)


@app.route('/')
def index():
    _html = '''
<h1>Meter Data API</h1>
<body>
    <a href="http://127.0.0.1:5000/meters">Meter API.</a>
</body>
'''
    return _html


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
