from flask import jsonify

from app.models.pdfs import PDF


def create(request):
    body = request.get_json()
    obj = PDF(body.get('name'), body.get('url'), body.get('user'))
    return jsonify({"data": obj.__repr__()}), 201

def patch(request):
    return jsonify({"data": ""})

def delete(request):
    return jsonify({"data": ""})

def get(request):
    return jsonify({"data": ""})