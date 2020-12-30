from gevent import monkey
import cgi
import redis
from flask import Flask, render_template, request
from flask_socketio import SocketIO
from engineio.payload import Payload

monkey.patch_all()
Payload.max_decode_packets = 1024

app = Flask(__name__)
db = redis.StrictRedis('localhost', 6379, 0)
socketio = SocketIO(app)


@app.route('/')
def main():
    return render_template('main.html')


@app.route('/track')
def track():
    print(request.args.get('name'), request.args.get('mobile'))
    data = {
        'track': {
            'name': request.args.get('name'),
            'mobile': request.args.get('mobile'),
            'parent_name': request.args.get('parent_name'),
            'parent_mobile': request.args.get('parent_mobile'),
            'image_url': request.args.get('image_url'),
            'address': request.args.get('address')
        }}
    socketio.emit('msg', data, namespace='/dd')
    return render_template('track.html')


@app.route('/pymeetups/')
def pymeetups():
    return render_template('pymeetups.html')


@socketio.on('connect', namespace='/dd')
def ws_conn():
    c = db.incr('connected')
    socketio.emit('msg', {'count': c}, namespace='/dd')
    socketio.emit('msg', {'track': 'track-data'}, namespace='/dd')


@socketio.on('disconnect', namespace='/dd')
def ws_disconn():
    c = db.decr('connected')
    socketio.emit('msg', {'count': c}, namespace='/dd')


@socketio.on('city', namespace='/dd')
def ws_city(message):
    print(message['city'])
    socketio.emit('city', {'city': cgi.escape(message['city'])},
                  namespace="/dd")


if __name__ == '__main__':
    socketio.run(app, "0.0.0.0", port=5000)
