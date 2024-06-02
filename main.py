from flask import Flask
from user.router import router as user_router
from user_async.router import router as user_async_router
from loader_io.router import router as loader_io_router
from hello_world.router import router as hello_world_router

app = Flask(__name__)
app.register_blueprint(user_router)
app.register_blueprint(user_async_router)
app.register_blueprint(loader_io_router)
app.register_blueprint(hello_world_router)


if __name__ == "__main__":
    app.run(debug=True)
