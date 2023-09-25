from flask import jsonify

from app.models.player import Player, players

def create(request):
    body = request.get_json()
    website = Player(body.get('id'), body.get('user'), body.get('link'))
    website.save(players)
    return jsonify({"data": website.__repr__()}), 201

def delete(player_id):
    player = Player.get(players, player_id)
    if player:
        player.delete(players)
        return jsonify({"data": [player.__repr__() for player in players]}), 410
    return jsonify({"data": "Website not found!"}), 404

def list(request):
    return jsonify({"data": [p.__repr__() for p in players]}), 200

def get(player_id):
    website = Player.get(players, player_id)
    if website:
        return jsonify({"data": players.__repr__()}), 200
    return jsonify({"data": "Website not found!"}), 404

def patch(website_id, request):
    player = Player.get(players, website_id)
    if player:
        body = request.get_json()
        player.update(body)
        return jsonify({"data": player.__repr__()}), 200
    return jsonify({"data": "Website not found!"}), 404