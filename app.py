from flask import Flask, Response
from flask import request
from bot import MessageBot, BotError
from settings import TOKEN

app = Flask(__name__)
bot = MessageBot()


@app.route("/send", methods=['POST'])
def send_message():
    token = request.json.get('token')
    text = request.json.get('text')
    if not text or not token:
        return Response(status=400)

    if token == TOKEN:
        try:
            bot.send_message_to_chats(
                message=text,
                chat_id=request.json.get('chat')
            )
        except BotError as error:
            return Response(response=str(error), status=409)
        except Exception:
            return Response(response=':((', status=409)

        return Response(status=201)

    return Response(status=403)

