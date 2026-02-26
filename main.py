from google import genai
from google.genai import types
from google.genai.types import Type
import model.config
import asyncio
conf = model.config.Config()
client = genai.Client(http_options={"api_version": "v1beta"}, api_key=conf.api_key)
async def run():
    async with (client.aio.live.connect(model=conf.model, config=conf.liveConfig) as session, asyncio.TaskGroup() as taskGroup):
if __name__ == "__main__":
    asyncio.run(run())
