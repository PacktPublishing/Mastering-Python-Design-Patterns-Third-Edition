import click

from lanarky.clients import StreamingClient


@click.command()
@click.option("--input", required=True)
@click.option("--stream", is_flag=True)
def main(input: str, stream: bool):
    client = StreamingClient()
    for event in client.stream_response(
        "POST",
        "/chat",
        params={"stream": str(stream).lower()},
        json={"messages": [dict(role="user", content=input)]},
    ):
        print(f"{event.event}: {event.data}")


if __name__ == "__main__":
    main()