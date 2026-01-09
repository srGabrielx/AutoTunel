# 🎶 Auto Túnel – Gerador Inteligente de Melodias

> **Ferramenta em Python para gerar, reproduzir e exportar melodias baseadas em escalas musicais.**

O **Auto Túnel** é um gerador algorítmico que aplica teoria musical para criar sequências melódicas únicas. A ferramenta permite ouvir o resultado em tempo real e exportar os arquivos para formatos compatíveis com DAWs como FL Studio, Ableton Live, Logic Pro, entre outras.

---

## 🚀 Funcionalidades

* **🎹 Geração Inteligente:** Criação de melodias baseadas em tons e escalas (Maior, Menor e Pentatônica).
* **🔊 Playback em Tempo Real:** Reprodução instantânea da melodia gerada para validação rápida.
* **💾 Exportação WAV:** Geração de arquivos de áudio em alta qualidade salvos automaticamente na pasta `melodias/`.
* **🎼 Exportação MIDI:** Criação de arquivos MIDI universais, prontos para uso em qualquer DAW, salvos na pasta `midi/`.
* **🎛️ Customização Total:** Definição de BPM, quantidade de notas, tom base e oitava.

---

## 🛠️ Tecnologias Utilizadas

* **Linguagem:** Python 3.11+
* **Gerenciador de Pacotes:** Poetry
* **Bibliotecas Principais:**
    * `NumPy` & `SciPy` — Processamento de áudio e geração de ondas.
    * `MIDIUtil` — Criação e formatação de arquivos MIDI.
    * `SimpleAudio` — Reprodução de áudio em tempo real (baixa latência).

---

## 📦 Instalação e Uso

Este projeto utiliza o **Poetry** para garantir que todas as dependências sejam instaladas nas versões corretas.

### 1. Clone o repositório

    git clone https://github.com/srGabrielx/AutoTunel.git
    cd AutoTunel

### 2. Instale o Poetry (caso não tenha)

    pip install poetry

### 3. Instale as dependências do projeto
Este passo é fundamental para baixar as bibliotecas listadas no `pyproject.toml`.

    poetry install

### 4. Execute o programa

    poetry run python main.py

---

## 🧭 Como Usar

Siga as instruções interativas exibidas no terminal:

1.  **Escolha o Tom** (ex: C, F#, G).
2.  **Selecione a Escala** (Maior, Menor ou Pentatônica).
3.  **Defina o BPM** e o **número de notas** da sequência.
4.  **Escolha a ação desejada:**
    * [1] Tocar a melodia 🔊
    * [2] Salvar em MIDI 🎼
    * [3] Salvar em WAV 💾

---

## 📂 Estrutura do Projeto

    AutoTunel/
    │
    ├── main.py        # Arquivo principal (menu e interação com o usuário)
    ├── engine.py      # Motor de áudio e lógica de geração algorítmica
    ├── config.py      # Configurações globais e dicionários de teoria musical
    │
    ├── melodias/      # Pasta de saída para arquivos .wav
    └── midi/          # Pasta de saída para arquivos .mid

---
att
<div align="center">
    Desenvolvido por <strong>srGabrielx</strong>
</div>
