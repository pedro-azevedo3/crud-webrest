from flask import jsonify

from app.models.player import Player, players

def create(request):
    body = request.get_json()
    website = Player(body.get('id'), body.get('name'), body.get('position'), body.get('age'))
    website.save(players)
    return jsonify({"data": website.__repr__()}), 201

def delete(player_id):
    player = Player.get(players, player_id)
    if player:
        player.delete(players)
        return jsonify({"data": [player.__repr__() for player in players]}), 410
    return jsonify({"data": "Website not found!"}), 404

def list(request):
    name_filter = request.args.get('name')
    id_filter = request.args.get('id')
    position_filter = request.args.get('position')
    age_filter = request.arg.get('age')

    filtered_players = players

    if name_filter:
        filtered_clubs = [player for player in filtered_players if players.name == name_filter]
        return jsonify({"data": [player.__repr__() for player in filtered_clubs]}), 200

    if id_filter:
        filtered_clubs = [player for player in filtered_players if players.id == id_filter]
        return jsonify({"data": [player.__repr__() for player in filtered_players]}), 200
    
    if position_filter:
        filtered_clubs = [player for player in filtered_players if players.position == position_filter]
        return jsonify({"data": [player.__repr__() for player in filtered_players]}), 200
    
    if age_filter:
        filtered_clubs = [player for player in filtered_players if players.age == age_filter]
        return jsonify({"data": [player.__repr__() for player in filtered_players]}), 200

    return jsonify({"data": [pdf.__repr__() for pdf in filtered_players]}), 200

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