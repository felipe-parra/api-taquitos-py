from flask import Response
from flask.json import jsonify
from db import get_db

info_taquito = ["id", "name", "rate", "image"]


def insert_taquito(name, rate, image):
    db = get_db()
    cursor = db.cursor()
    query = "INSERT INTO taquitos(name, rate, image) VALUES(?,?,?)"
    cursor.execute(query, [name, rate, image])
    db.commit()
    cursor.close()
    return {
        "name": name,
        "rate": rate,
        "image": image,
    }


def update_taquito(id, name, rate, image):
    db = get_db()
    cursor = db.cursor()
    query = "UPDATE taquitos SET name = ?, rate=? image=? WHERE id = ?"
    cursor.execute(query, [name, rate, image, id])
    db.commit()
    cursor.close()
    return True


def delete_taquito(id):
    db = get_db()
    cursor = db.cursor()
    query = "DELETE FROM taquitos WHERE id = ?"
    cursor.execute(query, [id])
    db.commit()
    cursor.close()
    return True


def get_by_id(id):
    db = get_db()
    cursor = db.cursor()
    query = "SELECT id, name, rate, image FROM taquitos WHERE id = ?"
    res = cursor.execute(query, [id]).fetchone()
    data_res = dict(zip(info_taquito, res))
    taquito_res = {"msg": "listed one taquito", "data": data_res}
    cursor.close()
    return taquito_res


def get_taquitos():
    """function to get all taquitos"""
    taquitos = []
    db = get_db()
    cursor = db.cursor()
    query = "SELECT id, name, rate, image FROM taquitos"
    data = cursor.execute(query).fetchall()
    for row in data:
        taquito_dict = dict(zip(info_taquito, row))
        taquitos.append(taquito_dict)
    taquito_res = {"msg": "listed taquitos", "data": taquitos}
    cursor.close()
    return taquito_res


def len_taquitos():
    db = get_db()
    cursor = db.cursor()
    query = "SELECT COUNT()FROM taquitos"
    numberOfTaquitos = cursor.execute(query).fetchone()[0]
    cursor.close()
    return numberOfTaquitos