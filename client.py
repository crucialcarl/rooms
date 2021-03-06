import requests, jsonify, json, time

base_url = 'http://localhost:5000/'

def get_objects_in_room(room_id):
    url = base_url + 'items/'
    request = url + str(room_id)
    r = requests.get(request)
    items = json.loads(r.text)
    return items

def server_status():
    url = base_url + 'serverstatus'
    r = requests.get(url)
    return r.status_code


def create_player(username, location):
    url = base_url + 'createplayer/'
    request = url + str(username) + '/' + str(location)
    r = requests.get(request)
    player = r.text
    return player

def check_player_exists(username):
    url = base_url + 'player/' + str(username)
    r = requests.get(url)
    
    if r.status_code == 200 and r.text:
        return int(r.text)
    return False 
    
 

def who():
    url = base_url + 'who'
    request = url
    r = requests.get(request)
    return r.text 

def move_player_to_room(player_name, room_id):
    url = base_url + 'move/' + str(player_name) + '/' + str(room_id)
    request = url
    r = requests.get(request)
    return r.text

if __name__ == '__main__':
    get_objects_in_room(10)
    create_player('bob', 10)
    who()



