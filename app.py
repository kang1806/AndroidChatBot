from flask import Flask, request
from flask_restful import Resource, Api
from model import bot

app = Flask(__name__)
api = Api(app)

class BotResponse(Resource):

    def get(self):
        # Using GET Requests
        msg = request.args.get("msg")
        response = bot.get_response(msg)
        return {"response" : response.text}

api.add_resource(BotResponse, "/bot")

if __name__ == "__main__":
    app.run(debug=True)
