att
# 🎶 Auto Túnel - Gerador de Melodias Inteligente

> Uma ferramenta CLI em Python para gerar, tocar e exportar melodias baseadas em escalas musicais.

O **Auto Túnel** é um gerador algorítmico que utiliza teoria musical para criar sequências melódicas únicas. Ele permite ouvir o resultado em tempo real e exportar para formatos compatíveis com DAWs (FL Studio, Ableton, etc).

## 🚀 Funcionalidades

- 🎹 **Geração Inteligente:** Cria melodias baseadas em tons e escalas (Maior, Menor, Pentatônica).
- 🔊 **Playback em Tempo Real:** Escute a melodia gerada instantaneamente.
- 💾 **Exportação WAV:** Gera arquivos de áudio de alta qualidade na pasta `melodias/`.
- 🎼 **Exportação MIDI:** Gera arquivos MIDI prontos para uso em qualquer DAW na pasta `midi/`.
- 🎛️ **Customização:** Escolha o BPM, a quantidade de notas, o tom base e a oitava.

## 🛠️ Tecnologias Utilizadas

- **Python 3.11+**
- **Poetry** (Gerenciamento de dependências)
- **Numpy & Scipy** (Processamento de áudio e geração de ondas)
- **MidiUtil** (Criação de arquivos MIDI)
- **SimpleAudio** (Reprodução de áudio)

## 📦 Como Instalar

Este projeto utiliza o **Poetry** para gerenciar as dependências.

1. Clone o repositório:
   
   ```bash
   git clone [https://github.com/srGabrielx/AutoTunel.git](https://github.com/srGabrielx/AutoTunel.git)
   cd AutoTunel ```

2. Instale as dependências:
  
  ```bash
  poetry install```

3. Para rodar o programa, utilize o comando:

  ```bash
  poetry run python main.py ```


Siga as instruções no terminal:

1. Escolha o **Tom** (ex: C, F#, G).
2. Escolha a **Escala** (maior, menor, pentatonica).
3. Defina o **BPM** e o **número de notas**.
4. Escolha se deseja Tocar, Salvar MIDI ou Salvar WAV.

## 📂 Estrutura do Projeto

* `main.py`: Arquivo principal (Menu e interação com usuário).
* `engine.py`: Motor de áudio e lógica de geração.
* `config.py`: Dicionários de configuração musical.
* `melodias/`: Pasta onde os arquivos .wav são salvos.
* `midi/`: Pasta onde os arquivos .mid são salvos.

 ```
Desenvolvido por **srGabrielx** 🎧
 ```
