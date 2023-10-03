from flask import jsonify

from app.models.player import Player

def create(request, mongo_client):
    players = mongo_client.webrestapidb.players
    body = request.get_json()
    player = Player(body.get('name'), body.get('position'), body.get('age'))
    player.save(players)
    return jsonify({"data": player.__repr__()}), 201

def delete(player_id, mongo_client):
    player = Player.get(player_id, mongo_client.webrestapidb.players.find())
    if player:
        player.delete(mongo_client.webrestapidb.players)
        return jsonify({"data": [player.__repr__() for player in mongo_client.webrestapidb.players.find()]}), 410
    return jsonify({"data": "Player not found!"}), 404

def list(request, mongo_client):
    name_filter = request.args.get('name')
    position_filter = request.args.get('position')
    age_filter = request.arg.get('age')

    filtered_players = mongo_client.webrestapidb.players.find()

    if name_filter:
        filtered_players = [player for player in filtered_players if player.get("name") == name_filter]
        return jsonify({"data": [player.__repr__() for player in filtered_players]}), 200
    
    if position_filter:
        filtered_players = [player for player in filtered_players if player.get("position") == position_filter]
        return jsonify({"data": [player.__repr__() for player in filtered_players]}), 200
    
    if age_filter:
        filtered_players = [player for player in filtered_players if player.get("position") == age_filter]
        return jsonify({"data": [player.__repr__() for player in filtered_players]}), 200

    return jsonify({"data": [pdf.__repr__() for pdf in filtered_players]}), 200

def get(player_id, mongo_client):
    player = Player.get(player_id, mongo_client.webrestapidb.players.find())
    if player:
        return jsonify({"data": player.__repr__()}), 200
    return jsonify({"data": "Player not found!"}), 404

def patch(player_id, request, mongo_client):
    player = Player.get(player_id, mongo_client.webrestapidb.players.find())
    if player:
        body = request.get_json()
        player.update(body, player.name, mongo_client.webrestapidb.players)
        return jsonify({"data": player.__repr__()}), 200
    return jsonify({"data": "Player not found!"}), 404