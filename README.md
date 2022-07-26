# Cartoon
Código da abordagem desenvolvida em minha pesquisa de mestrado

## Instalação
Crie um ambiente virtual e o ative

```
python3 -m venv env
source env/bin/activate
```

Após clonar este repositório, instalar os requisitos contidos no requirements.txt
```
pip install -r requirements.txt
```

## Cartunizando um vídeo
Para aplicar a cartunização a um vídeo basta chamar o script de cartunização passando
como parâmetro o caminho para o vídeo.

```
python cartoon.py my_video.mp4
```

O vídeo resultante será colocado dentro da pasta output.
