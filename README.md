🎶 Auto Túnel – Gerador Inteligente de Melodias

> Ferramenta em Python para gerar, reproduzir e exportar melodias baseadas em escalas musicais.



O Auto Túnel é um gerador algorítmico que aplica teoria musical para criar sequências melódicas únicas. A ferramenta permite ouvir o resultado em tempo real e exportar os arquivos para formatos compatíveis com DAWs como FL Studio, Ableton Live, entre outras.


---

🚀 Funcionalidades

🎹 Geração Inteligente
Criação de melodias baseadas em tons e escalas (Maior, Menor e Pentatônica).

🔊 Playback em Tempo Real
Reprodução instantânea da melodia gerada.

💾 Exportação WAV
Geração de arquivos de áudio em alta qualidade na pasta melodias/.

🎼 Exportação MIDI
Criação de arquivos MIDI prontos para uso em qualquer DAW, salvos na pasta midi/.

🎛️ Customização Total
Definição de BPM, quantidade de notas, tom base e oitava.



---

🛠️ Tecnologias Utilizadas

Python 3.11+

Poetry – Gerenciamento de dependências

NumPy & SciPy – Processamento de áudio e geração de ondas

MIDIUtil – Criação de arquivos MIDI

SimpleAudio – Reprodução de áudio em tempo real



---

📦 Como Instalar

Este projeto utiliza o Poetry para gerenciar dependências.

1. Clone o repositório

git clone
https://github.com/srGabrielx/AutoTunel.git
cd AutoTunel

2. Instale as dependências

pip install poetry

3. Execute o programa

poetry run python main.py


---

🧭 Como Usar

Siga as instruções exibidas no terminal:

1. Escolha o Tom (ex: C, F#, G).


2. Selecione a Escala (maior, menor ou pentatônica).


3. Defina o BPM e o número de notas.


4. Escolha a ação desejada:

Tocar a melodia

Salvar em MIDI

Salvar em WAV





---

📂 Estrutura do Projeto

AutoTunel/
│
├── main.py        # Arquivo principal (menu e interação com o usuário)
├── engine.py      # Motor de áudio e lógica de geração
├── config.py      # Configurações e dicionários musicais
│
├── melodias/      # Arquivos .wav gerados
└── midi/          # Arquivos .mid gerados


---

Desenvolvido por srGabrielx 🎧


---
Att