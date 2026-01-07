import numpy as np
import simpleaudio as sa
from midiutil import MIDIFile
from scipy.io.wavfile import write
import random
import os  
from config import TONS, ESCALAS

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
    sa.play_buffer(audio, 1, 2, fs).wait_done()

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