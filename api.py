#/usr/bin/python3
"""
    API REST con Python 3 y SQLite 3
    by Felipe Parra
"""

from flask import render_template
from db import create_tables
from flask import Flask, jsonify, request
import taquitos_controller

app = Flask(__name__)


@app.route('/taquitos', methods=["GET"])
def get_taquitos():
    """Get all taquitos"""
    taquitos = taquitos_controller.get_taquitos()
    return jsonify(taquitos)


@app.route('/taquitos', methods=["POST"])
def insert_taquito():
    """Crete a new Taquito :)"""
    taquito_details = request.get_json()
    name = taquito_details["name"]
    rate = taquito_details["rate"]
    image = taquito_details["image"]
    result = taquitos_controller.insert_taquito(name, rate, image)
    return jsonify(result)


@app.route('/taquitos/update', methods=["PUT"])
def update_taquito():
    """Update a Taquito already exists"""
    taquito_details = request.get_json()
    id = taquito_details["id"]
    name = taquito_details["name"]
    rate = taquito_details["rate"]
    image = taquito_details["image"]
    result = taquitos_controller.update_taquito(id, name, rate, image)
    return jsonify({"msg":"Updated successfully"})


@app.route('/taquitos/<id>', methods=["DELETE"])
def delete_taquit(id):
    """Delete a Taquito :("""
    result = taquitos_controller.delete_taquito(id)
    return jsonify(result)


@app.route('/taquitos/<id>', methods=["GET"])
def get_one_taquito(id):
    """Get a taquito by id"""
    result = taquitos_controller.get_by_id(id)
    print("from route", result)
    return jsonify(result)


@app.route('/taquitos/count',methods=["GET"])
def number_of_taquitos():
    """Count how many taquitos has"""
    result = taquitos_controller.len_taquitos()
    return jsonify(result)

@app.after_request
def after_request(response):
    response.headers[
        "Access-Control-Allow-Origin"] = "*"  # Change for a domain
    response.headers["Access-Controll-Credentials"] = "true"
    response.headers["Access-Controll-Methods"] = "POST, GET, PUT, DELETE"
    response.headers[
        "Access-Controll-Headers"] = "Accept, Content-Type, Content-Length, Accept-Encoding, X-CSRF-Token, Authorization"
    return response


@app.errorhandler(404)
def not_found(e):
    # return jsonify(error=str(e)), 404
    return render_template("404.html"), 404


if __name__ == "__main__":
    create_tables()
    """ Here you can change debug and port
    Remember that, in order to makes this API functional, you must set debug in False.
    """
    app.run(host="0.0.0.0", port=80000, debug=True)