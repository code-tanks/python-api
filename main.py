from tanks import my_tank
from fastapi import FastAPI, Request

app = FastAPI()

bot = my_tank.create_tank()


@app.get("/ping")
def ping():
    return "pong"


@app.get("/request_commands")
def request_commands():
    bot.run()

    commands = bot.commands[:]

    bot.commands.clear()

    return commands


@app.get("/request_commands_by_event")
async def request_commands_by_event(info: Request):
    event = await info.json()
    bot.on_event(event['event_type'], event['info'])

    commands = bot.commands[:]

    bot.commands.clear()

    return commands
