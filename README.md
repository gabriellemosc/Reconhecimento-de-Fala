### README para Projeto de Reconhecimento de Fala

```markdown
# Projeto de Reconhecimento de Fala

Este projeto é uma aplicação simples de reconhecimento de fala usando a biblioteca `speech_recognition` do Python. O programa captura o áudio do microfone, converte a fala em texto e salva o áudio em um arquivo WAV.



## Descrição

O projeto usa a biblioteca `speech_recognition` para capturar áudio do microfone e transcrever a fala em texto. O programa grava o áudio enquanto o usuário fala e para a gravação quando detecta o comando "encerrar gravação". O áudio também é salvo em um arquivo WAV.

## Instalação

Para configurar o projeto em seu ambiente local, siga estas etapas:

1. **Clone o repositório**:
    ```bash
    git clone https://github.com/usuario/nome-do-repositorio.git
    ```

2. **Navegue até o diretório do projeto**:
    ```bash
    cd nome-do-repositorio
    ```

3. **Instale as dependências**:
    ```bash
    pip install -r requirements.txt
    ```

   Crie um arquivo `requirements.txt` com as seguintes dependências:
    ```
    SpeechRecognition
    PyAudio
    ```

   Certifique-se de ter o `PyAudio` instalado, pois é necessário para capturar áudio do microfone.

## Uso

Para usar o projeto, execute o script Python. O programa começará a ouvir o áudio do microfone e converter a fala em texto. Quando o comando "encerrar gravação" for detectado, a gravação será interrompida e o áudio será salvo em um arquivo WAV.

1. **Execute o script**:
    ```bash
    python nome_do_script.py
    ```

2. **Fale para o microfone** e diga "encerrar gravação" quando quiser parar a gravação.

O arquivo de áudio será salvo como `audio.wav` no diretório do projeto.



## Licença

Este projeto está licenciado sob a Licença MIT
