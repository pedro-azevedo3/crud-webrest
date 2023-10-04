from flask import jsonify

from app.models.player import Player

def create_player(request, mongo_client):
    players = mongo_client.webrestapidb.players
    body = request.get_json()
    player = Player(body.get('club'),body.get('name'), body.get('age'),  body.get('position'))
    player.save(players)
    return jsonify({"data": player.__repr__()}), 201

def delete_player(player_id, mongo_client):
    player = Player.get(player_id, mongo_client.webrestapidb.players.find())
    if player:
        player.delete(mongo_client.webrestapidb.players)
        return jsonify({"data": [p.__repr__() for p in mongo_client.webrestapidb.players.find()]}), 410
    return jsonify({"data": "Player not found!"}), 404

def list_player(request, mongo_client):
    name_filter = request.args.get('name')

    filtered_players = mongo_client.webrestapidb.players.find()

    if name_filter:
        filtered_players = [{k:str(v) if k == "_id" else v for k, v in player.items()} for player in filtered_players if player.get("name") == name_filter]
        return jsonify({"data": filtered_players}), 200
    return jsonify({"data": [{k:str(v) if k == "_id" else v for k, v in player.items()} for player in filtered_players]}), 200

def get_player(player_id, mongo_client):
    player = Player.get(player_id, mongo_client.webrestapidb.players.find())
    if player:
        return jsonify({"data": player.__repr__()}), 200
    return jsonify({"data": "Player not found!"}), 404

def patch_player(player_id, request, mongo_client):
    player = Player.get(player_id, mongo_client.webrestapidb.players.find())
    if player:
        body = request.get_json()
        player.update(body, player.name, mongo_client.webrestapidb.players)
        return jsonify({"data": player.__repr__()}), 200
    return jsonify({"data": "Player not found!"}), 404