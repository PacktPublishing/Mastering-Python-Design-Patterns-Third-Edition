# python -m pip install "lanarky[openai]"

import os

from lanarky import Lanarky
from lanarky.adapters.openai.resources import ChatCompletionResource
from lanarky.adapters.openai.routing import OpenAIAPIRouter

# Set the OPENAI_API_KEY environment variable in your shell
# or pass it through the following line
# os.environ["OPENAI_API_KEY"] = "Your OpenAI API key here"

app = Lanarky()
router = OpenAIAPIRouter()


@router.post("/chat")
def chat(stream: bool = True) -> ChatCompletionResource:
    system = "You are a sassy assistant"
    return ChatCompletionResource(stream=stream, system=system)


app.include_router(router)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app)