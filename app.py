from flask import Flask, jsonify

app = Flask(
    import_name=__name__,
    static_url_path='/static',
    static_folder='./static',
)
app.config.from_file('config.json', load=json.load)

