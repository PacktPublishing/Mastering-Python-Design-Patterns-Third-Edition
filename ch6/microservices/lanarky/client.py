import click
import sys
from lanarky.clients import StreamingClient


args = sys.argv[1:]
if len(args) == 1:
    message = args[0]

    client = StreamingClient()
    for event in client.stream_response(
        "POST",
        "/chat",
        params={"stream": "false"},
        json={"messages": [dict(role="user", content=message)]},
    ):
        print(f"{event.event}: {event.data}")
else:
    print("You need to pass a message!")
