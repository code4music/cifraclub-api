# Cifra Club API

Esse projeto cria uma API Rest para obter a cifra
de uma música do [Cifra Club](https://www.cifraclub.com.br).

A ideia é disponibilizar as cifras em formato JSON através de uma
interface de API Rest, para facilitar a interação com outros sistemas
ou criar automações.

O endpoint de API `/artists/:artist/songs/:song` executa um WebDriver do Selenium
para ler a página web e extrair a cifra e meta dados da música, no formato de JSON.

# Como rodar o projeto no seu computador?

Para executar o projeto na sua máquina local, certifique-se
que você tem o docker e docker compose instalados.
E então, execute:

```console
docker-compose build
docker-compose up
```

Esse comando irá subir o projeto em
[localhost:3000](http://localhost:3000).

Para os geeks que usam Makefile, basta executar:

```console
make up
```

# Como pegar uma cifra?

Com o projeto rodando, você pode abrir o navegador com a seguinte URL:

http://localhost:3000/artists/coldplay/songs/the-scientist

Ou se preferir obter o json da música pelo terminal, execute:

```console
curl localhost:3000/artists/coldplay/songs/the-scientist
```

O retorno da API será algo como:

```json
{
  "artist": "Coldplay",
  "name": "The Scientist",
  "youtube_url": "https://www.youtube.com/watch?v=RB-RcX5DS5A"
  "cifraclub_url": "https://www.cifraclub.com.br/coldplay/the-scientist",
  "cifra": [
    "[Intro]  C#m7  A9  E  E9",
    "",
    "[Intro e Primeira Parte]",
    "",
    "Parte 1 de 2",
    "   C#m7              A9",
    "E|------------------------------------------| ",
    "B|-0---0---0---0----0---0---0---0-----------| ",
    "G|-1---1---1---1----2---2---2---2-----------| ",
    "D|-2---2---2---2----2---2---2---2-----------| ",
    "A|-4-4-4-4-4-4-4-4--0-0-0-0-0-0-0-0---------| ",
    "E|------------------------------------------| ",
    "",
    "",
    "Parte 2 de 2",
    "   E                E9",
    "E|------------------------------------------| ",
    "B|-0---0---0---0----0---0---0---0-----------| ",
    "G|-1---1---1---1----1---1---1---1-----------| ",
    "D|-2---2---2---2----4---4---4---4-----------| ",
    "A|------------------------------------------| ",
    "E|-0-0-0-0-0-0-0-0--0-0-0-0-0-0-0-0---------| ",
    "",
    "[Primeira Parte]",
    "",
    "C#m7             A9",
    "     Come up to meet you",
    "              E",
    "Tell you I'm sorry",
    "                    E9        C#m7",
    "You don't know how lovely you are",
    "",
    "          A9",
    "I had to find you",
    "            E",
    "Tell you I need you",
    "               E9       C#m7",
    "Tell you I'll set you apart",
    "",
    "                 A9",
    "Tell me your secrets",
    "                  E",
    "And ask me your questions",
    "             E9           C#m7",
    "Oh, lets go back to the start",
    "",
    "            A9",
    "Running in circles",
    "           E",
    "Coming up tails",
    "             E9",
    "Heads on a science apart",
    "",
    "[Refrão]",
    "",
    "A9                      E",
    "  Nobody said it was easy",
    "              E9             A9",
    "It's such a shame for us to part",
    "                      E",
    "Nobody said it was easy",
    "             E7M(9)        E6      B",
    "No one ever said it would be this hard",
    "",
    "Oh take me back to the start",
    "",
    "[Segunda Parte] E  A9  E  E9",
    "",
    "[Segunda Parte]",
    "",
    "Parte 1 de 5",
    "   A9",
    "E|------------------------------------------| ",
    "B|-0---0---0---0----0---0---0---0-----------| ",
    "G|-2---2---2---2----2---2---2---2-----------| ",
    "D|-2---2---2---2----2---2---2---2-----------| ",
    "A|-0-0-0-0-0-0-0-0--0-0-0-0-0-0-0-0---------| ",
    "E|------------------------------------------| ",
    "",
    "",
    "Parte 2 de 5",
    "   E                E9",
    "E|------------------------------------------| ",
    "B|-0---0---0---0----0---0---0---0-----------| ",
    "G|-1---1---1---1----1---1---1---1-----------| ",
    "D|-2---2---2---2----4---4---4---4-----------| ",
    "A|------------------------------------------| ",
    "E|-0-0-0-0-0-0-0-0--0-0-0-0-0-0-0-0---------| ",
    "",
    "",
    "Parte 3 de 5",
    "   A9",
    "E|------------------------------------------| ",
    "B|-0---0---0---0----0---0---0---0-----------| ",
    "G|-2---2---2---2----2---2---2---2-----------| ",
    "D|-2---2---2---2----2---2---2---2-----------| ",
    "A|-0-0-0-0-0-0-0-0--0-0-0-0-0-0-0-0---------| ",
    "E|------------------------------------------| ",
    "",
    "",
    "Parte 4 de 5",
    "   E               E7M(9)   E6",
    "E|------------------------------------------| ",
    "B|-0---0---0---0----7---7---5---5-----------| ",
    "G|-1---1---1---1----8---8---6---6-----------| ",
    "D|-2---2---2---2----6---6---6---6-----------| ",
    "A|------------------------------------------| ",
    "E|-0-0-0-0-0-0-0-0--0-0-0-0-0-0-0-0---------| ",
    "",
    "",
    "Parte 5 de 5",
    "   B",
    "E|------------------2-----------------------| ",
    "B|-4---4---4---4-5--------------------------| ",
    "G|-4---4---4---4-4--4-----------------------| ",
    "D|-4---4---4---4-4--4-----------------------| ",
    "A|-2-2-2-2-2-2-2-2--2-----------------------| ",
    "E|------------------------------------------| ",
    "",
    "C#m7             A9",
    "     I was just guessing",
    "                E",
    "At numbers and figures",
    "              E9       C#m7",
    "Pulling your puzzles apart",
    "",
    "               A9",
    "Questions of science",
    "              E",
    "Science and progress",
    "                 E9          C#m7",
    "Do not speak as loud as my heart",
    "",
    "             A9",
    "Tell me you love me",
    "               E",
    "Come back and haunt me",
    "          E9           C#m7",
    "Oh and I rush to the start",
    "",
    "            A9",
    "Running in circles",
    "             E",
    "Chasing our tails",
    "        E9        B11/D#",
    "Coming back as we are",
    "",
    "[Refrão]",
    "",
    "A9                       E",
    "   Nobody said it was easy",
    "              E9             A9",
    "It's such a shame for us to part",
    "                      E",
    "Nobody said it was easy",
    "             E7M              E6  B",
    "No one ever said it would be so  hard",
    "                        E  A9  E  E9",
    "I'm going back to the start",
    "",
    "[Final]",
    "",
    "( C#m7  A9  E )",
    "",
    "C#m7    A9             E  E9",
    "     Oh uhhh  uh uh uh uh",
    "C#m7    A9             E  E9",
    "     Oh uhhh  uh uh uh uh",
    "C#m7    A9             E  E9",
    "     Oh uhhh  uh uh uh uh",
    "C#m7    A9             E",
    "     Oh uhhh  uh uh uh uh",
    ""
  ]
}
```
