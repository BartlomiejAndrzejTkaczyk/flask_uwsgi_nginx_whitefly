from flask import Flask, jsonify
from user.router import router as user_router
from user_async.router import router as user_async_router
from loader_io.router import router as loader_io_router

app = Flask(__name__)
app.register_blueprint(user_router)
app.register_blueprint(user_async_router)
app.register_blueprint(loader_io_router)


@app.route('/')
def hello_world():
    return jsonify({'hello_world': 200})


if __name__ == "__main__":
    app.run(debug=True)
