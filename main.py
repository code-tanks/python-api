"""Server for running a code-tanks tank
"""

from fastapi import FastAPI, Request
from tanks import my_tank

app = FastAPI()

bot = my_tank.create_tank()


@app.get("/ping")
def ping():
    """Ping route for checking liveness
    """
    return "pong"


@app.get("/request_commands")
def request_commands():
    """Returns buffered commands and then clears them
    """
    bot.run()

    commands = bot.commands[:]

    bot.commands.clear()

    return commands


@app.get("/request_commands_by_event")
async def request_commands_by_event(info: Request):
    """Returns buffered commands by event and then clears them
    """

    event = await info.json()
    bot.on_event(event)

    commands = bot.commands[:]

    bot.commands.clear()

    return commands
