import numpy as np
import simpleaudio as sa
from midiutil import MIDIFile
from scipy.io.wavfile import write
import random
import os
import platform
import tempfile
from config import TONS, ESCALAS

# --- Tradução de Notas ---
REVERSO_TONS = {v: k for k, v in TONS.items()}

def traduzir_notas(notas_midi):
    """Converte números numéricos/MIDI em notas musicais legíveis (ex: 53 -> 'F4')"""
    resultado = []
    for nota in notas_midi:
        nome = REVERSO_TONS[nota % 12]
        oitava = nota // 12
        resultado.append(f"{nome}{oitava}")
    return resultado

# --- Gerando melodia base ---
def gerar_melodia(tom, escala, notas=16, oitava=4):
    base = TONS[tom]
    padrao = ESCALAS[escala]
    notas_geradas = []

    for _ in range(notas):
        grau = random.choice(padrao)
        valor_midi = base + grau + (oitava * 12)
        notas_geradas.append(valor_midi)
    return notas_geradas

# --- Gera os dados da onda ---
def gerar_onda(notas, bpm=120):
    fs = 44100
    duracao = 60 / bpm
    silencio = np.zeros(int(fs * 0.05), dtype=np.int16)
    onda_total = np.array([], dtype=np.int16)

    for valor_midi in notas:
        freq = 440 * (2 ** ((valor_midi - 69) / 12))
        t = np.linspace(0, duracao, int(fs * duracao), False)
        onda = np.sin(freq * t * 2 * np.pi)
        
        envelope = np.concatenate([np.linspace(0, 1, 100), np.ones(len(onda)-200), np.linspace(1, 0, 100)])
        if len(envelope) == len(onda):
            onda = onda * envelope

        onda = (onda * 32767).astype(np.int16)
        onda_total = np.concatenate((onda_total, onda, silencio))
    
    return fs, onda_total

# --- Funções de Ação ---
def tocar_melodia(notas, bpm=120):
    fs, audio = gerar_onda(notas, bpm)
    print("🎵 Tocando...")
    
    try:
        # Tenta usar o simpleaudio primeiro
        sa.play_buffer(audio, 1, 2, fs).wait_done()
    except Exception as e:
        print(f"⚠️ Erro no SimpleAudio: {e}")
        print("🔧 Acionando método alternativo nativo do sistema...")
        
        # Cria um arquivo temporário de áudio
        temp_dir = tempfile.gettempdir()
        temp_wav = os.path.join(temp_dir, "temp_melodia.wav")
        write(temp_wav, fs, audio)
        
        # Reproduz usando recursos nativos dependendo do SO
        sistema = platform.system()
        try:
            if sistema == "Windows":
                import winsound
                winsound.PlaySound(temp_wav, winsound.SND_FILENAME)
            elif sistema == "Darwin": # macOS
                os.system(f"afplay {temp_wav}")
            else: # Linux
                os.system(f"aplay {temp_wav}")
        except Exception as fallback_error:
            print(f"❌ Não foi possível reproduzir o áudio: {fallback_error}")
            print("💡 Dica: Verifique se as caixas de som/fones estão conectados e funcionando.")
        finally:
            # Limpa o arquivo temporário após tentar tocar
            if os.path.exists(temp_wav):
                os.remove(temp_wav)

def salvar_wav(notas, bpm, nome_arquivo):
    # Define a pasta e cria se não existir
    pasta = "melodias"
    if not os.path.exists(pasta):
        os.makedirs(pasta)
    
    # Cria o caminho completo (pasta/arquivo.wav)
    caminho_completo = os.path.join(pasta, nome_arquivo)
    
    fs, audio = gerar_onda(notas, bpm)
    write(caminho_completo, fs, audio)
    print(f"✅ Áudio salvo em: {caminho_completo}")

def salvar_midi(notas, bpm, nome_arquivo):
    # Define a pasta e cria se não existir
    pasta = "midi"
    if not os.path.exists(pasta):
        os.makedirs(pasta)

    # Cria o caminho completo (pasta/arquivo.mid)
    caminho_completo = os.path.join(pasta, nome_arquivo)

    mid = MIDIFile(1)
    mid.addTempo(0, 0, bpm)
    tempo = 0
    for nota in notas:
        mid.addNote(0, 0, nota, tempo, 1, 100)
        tempo += 1
    
    with open(caminho_completo, "wb") as f:
        mid.writeFile(f)
    print(f"✅ MIDI salvo em: {caminho_completo}")