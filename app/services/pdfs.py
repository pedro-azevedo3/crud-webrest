from flask import jsonify

from app.models.pdfs import PDF

pdfs = [PDF(name = 'Leandro', url = 'google.com', user = 2, id = 2)]

def create(request):
    body = request.get_json()
    obj = PDF(body.get('name'), body.get('url'), body.get('user'), body.get('id'))
    pdfs.append(obj)
    return jsonify({"data": obj.__repr__()}), 201

def delete(id):
    for index, pdf in enumerate(pdfs):
        if pdf.id == id:
            del pdfs[index]
    return jsonify({"data": [p.__repr__() for p in pdfs]}), 410

def list(request):
    return jsonify({"data": [p.__repr__() for p in pdfs]}), 200

# GET by ID
def get(id):
    for index, pdf in enumerate(pdfs):
        if pdf.id == id:
            return jsonify({"data": pdfs[index].__repr__()})
    return jsonify({"data": "PDF NOT FOUND"})

# UPDATE on the PDF's list
def patch(id, request):
    body = request.get_json()
    for index, pdf in enumerate(pdfs):
        if pdf.id == id:
            return jsonify({"data": pdfs[index].update(body).__repr__()})
    return jsonify({"data": "PDF NOT FOUND"})