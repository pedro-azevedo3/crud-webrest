from flask import jsonify

from app.models.club import Club, clubs

def create(request):
    body = request.get_json()
    club = Club(body.get('name'), body.get('id'))
    club.save()
    return jsonify({"data": club.__repr__()}), 201

def delete(club_id):
    club = Club.get(club_id)
    if club:
        club.delete()
        return jsonify({"data": [c.__repr__() for c in clubs]}), 410
    return jsonify({"data": "Club not found!"}), 404

def list(request):
    name_filter = request.args.get('name')
    id_filter = request.args.get('id')

    filtered_clubs = clubs

    if name_filter:
        filtered_clubs = [club for club in filtered_clubs if club.name == name_filter]
        return jsonify({"data": [club.__repr__() for club in filtered_clubs]}), 200

    if id_filter:
        filtered_clubs = [club for club in filtered_clubs if club.id == id_filter]
        return jsonify({"data": [club.__repr__() for club in filtered_clubs]}), 200

    return jsonify({"data": [pdf.__repr__() for pdf in filtered_clubs]}), 200

def get(clubs_id):
    club = Club.get(clubs_id)
    if club:
        return jsonify({"data": club.__repr__()}), 200
    return jsonify({"data": "Club not found!"}), 404

def patch(clubs_id, request):
    club = Club.get(clubs_id)
    if club:
        body = request.get_json()
        club.update(body)
        return jsonify({"data": club.__repr__()}), 200
    return jsonify({"data": "Club not found!"}), 404