"""Initialization of Flask app."""
from app_backend import app
from cheroot import wsgi

if __name__ == '__main__':
    # app.run(host='0.0.0.0', port=2201)

    addr = '0.0.0.0', 2201
    server = wsgi.Server(addr, app, request_queue_size=32)

    try:
        server.start()
        print(f'\n\nСервер cheroot запущен по адресу \n {addr}\n\n')
    except KeyboardInterrupt:
        server.stop()
