import typer
import os
import requests
import decorating

CIFRACLUB_API_URL = os.getenv("CIFRACLUB_API_URL", "http://localhost:3000")
app = typer.Typer()

@app.command()
def get(artist: str, song: str):
    get_endpoint = CIFRACLUB_API_URL + f"/artists/{artist}/songs/{song}"
    with decorating.writing(delay=0.02):
        print(f"Carregando música {song} do artista {artist}...")
    with decorating.animated("carregando cifra"):
        response = requests.get(get_endpoint)
    response_json = response.json()
    for text_line in response_json["cifra"]:
        print(text_line)


if __name__ == '__main__':
    app()
