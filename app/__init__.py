from flask import Flask

app = Flask(__name__)
from app import restEndpoint
from app import player

# from endpoints import playerEndpoint

player.initilzation()
