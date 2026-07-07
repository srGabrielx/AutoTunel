# 🎶 Auto Túnel – Gerador Inteligente de Melodias

O **Auto Túnel** é uma ferramenta em Python focada em geração algorítmica de música baseada em teoria musical. Através do terminal, o usuário pode escolher tons, escalas, andamento (BPM) e tamanho da sequência para que o sistema gere melodias de forma matemática. O projeto permite ouvir o resultado em tempo real ou exportar os arquivos diretamente para formatos compatíveis com qualquer DAW (como FL Studio, Ableton Live, Logic Pro, etc.).

## 🚀 Funcionalidades

*   **🎹 Geração Baseada em Escalas:** Criação de sequências de notas aleatórias, mas harmonicamente corretas, utilizando dicionários musicais de Tons e Escalas (Maior, Menor e Pentatônica).
*   **🔊 Playback em Tempo Real:** Síntese de áudio imediata por meio de ondas senoidais geradas matematicamente via `NumPy` e reproduzidas sem latência.
*   **💾 Exportação de Áudio (WAV):** Aplicação de um envelope de amplitude simples (ataque e decaimento) nas ondas para evitar estalos, salvando o som renderizado na pasta `melodias/`.
*   **🎼 Exportação de Partitura Digital (MIDI):** Geração de arquivos MIDI universais contendo as informações exatas das notas e do andamento (BPM), salvos de forma organizada na pasta `midi/`.

## 🛠️ Tecnologias Utilizadas

*   **Python 3.11+** — Linguagem base para toda a arquitetura matemática.
*   **Poetry** — Gerenciador de pacotes e ambientes virtuais.
*   **NumPy** — Processamento de arrays e modelagem matemática das frequências das notas.
*   **SciPy (`scipy.io.wavfile`)** — Conversão de dados numéricos em arquivos físicos de áudio (.wav).
*   **SimpleAudio** — Execução do buffer de som diretamente na placa de áudio do computador.
*   **MIDIUtil** — Escrita e estruturação de eventos MIDI para comunicação com DAWs.

## 📦 Instalação e Configuração

Certifique-se de ter o Python instalado na sua máquina. O projeto utiliza o gerenciador **Poetry** para isolar as bibliotecas nas versões corretas.

### 1. Clonar o Repositório
```bash
git clone https://github.com
cd AutoTunel
```

### 2. Instalar o Poetry (Se ainda não tiver)
```bash
pip install poetry
```

### 3. Instalar as Dependências do Projeto
Este comando criará o ambiente virtual isolado e baixará as bibliotecas necessárias listadas no arquivo de configuração:
```bash
poetry install
```

### 4. Executar a Aplicação
Rode o script principal de forma segura pelo ambiente controlado do Poetry:
```bash
poetry run python main.py
```

## 🧭 Como Usar o Sistema

Ao iniciar o programa no terminal, basta seguir o fluxo interativo fornecendo os parâmetros desejados:

1.  **Escolha o Tom:** Digite a nota base desejada (ex: `C`, `D#`, `A`, `F`). O sistema aceita sustenidos e padroniza a entrada em letras maiúsculas.
2.  **Selecione a Escala:** Escolha uma das regras harmônicas configuradas (`maior`, `menor` ou `pentatonica`).
3.  **Defina a Quantidade de Notas:** Escolha quantas notas terá a sua sequência musical (ex: `16`).
4.  **Ajuste o BPM:** Configure a velocidade/andamento da música (ex: `120`).
5.  **Menu de Ações:** Escolha o destino da melodia gerada:
    *   `1` — Tocar a melodia imediatamente nos alto-falantes 🔊
    *   `2` — Exportar para a pasta `midi/` com extensão `.mid` 🎼
    *   `3` — Exportar para a pasta `melodias/` com extensão `.wav` 💾

## 📂 Estrutura Arquitetural do Projeto

```text
AutoTunel/
│
├── config.py         # Dicionários de teoria musical (mapeamento de notas e escalas)
├── engine.py         # Motor de processamento (criação de ondas, playback e exportações)
├── main.py           # Interface de terminal (coleta inputs e exibe os menus de ação)
│
├── .gitignore        # Arquivo de segurança (oculta .venv, __pycache__, mídias locais)
├── pyproject.toml    # Manifesto de dependências e configurações do Poetry
├── poetry.lock       # Registro travado de versões das bibliotecas instaladas
└── requirements.txt  # Lista de pacotes alternativa para instalações via pip padrão
```

## 📄 Licença

Este projeto está sob a licença **MIT**. Você é livre para clonar, modificar, distribuir e utilizar em suas próprias produções musicais!

