from flask import jsonify

from app.models.club import Club

def create(request, mongo_client):
    clubs = mongo_client.webrestapidb.clubs
    body = request.get_json()
    club = Club(body.get('name'))
    club.save(clubs)
    return jsonify({"data": club.__repr__()}), 201

def delete(club_id, mongo_client):
    club = Club.get(club_id, mongo_client.webrestapidb.clubs.find())
    if club:
        club.delete(mongo_client.webrestapidb.clubs)
        return jsonify({"data": [c.__repr__() for c in mongo_client.webrestapidb.clubs.find()]}), 200
    return jsonify({"data": "Club not found!"}), 404

def list(request, mongo_client):
    name_filter = request.args.get('name')
    filtered_clubs = mongo_client.webrestapidb.clubs.find()
    if name_filter:
        filtered_clubs = [{k:str(v) if k == "_id" else v for k, v in club.items()} for club in filtered_clubs if club.get("name") == name_filter]
        return jsonify({"data": filtered_clubs}), 200
    return jsonify({"data": [{k:str(v) if k == "_id" else v for k, v in club.items()} for club in filtered_clubs]}), 200

def get(clubs_id, mongo_client):
    club = Club.get(clubs_id, mongo_client.webrestapidb.clubs.find())
    if club:
        return jsonify({"data": club.__repr__()}), 200
    return jsonify({"data": "Club not found!"}), 404

def patch(clubs_id, request, mongo_client):
    club = Club.get(clubs_id, mongo_client.webrestapidb.clubs.find())
    if club:
        body = request.get_json()
        club.update(body, club.name, mongo_client.webrestapidb.clubs)
        return jsonify({"data": club.__repr__()}), 200
    return jsonify({"data": "Club not found!"}), 404