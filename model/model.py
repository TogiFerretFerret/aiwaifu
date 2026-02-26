from google import genai
from google.genai import types
from google.genai.types import Type
import model.config
conf=model.config.Config()
client = genai.Client(
    http_options={"api_version": "v1beta"},
    api_key=conf.api_key
)
