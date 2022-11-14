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
make build up
```

# Como pegar uma cifra?

Com o projeto rodando, você pode abrir o navegador com a seguinte URL:

http://localhost:3000/cifras/artists/coldplay/songs/the-scientist

Ou se preferir obter o json da música pelo terminal, execute:

```console
curl localhost:3000/cifras/artists/coldplay/songs/the-scientist
```
