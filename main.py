# Importamos as configurações e as funções do motor
from config import TONS, ESCALAS
import engine 

if __name__ == "__main__":
    print("\n🎶 Auto Tunel - Gerador de Melodias 🎶\n")

    try:
        # 1. Coleta de dados
        tom_input = input("Escolha o tom (ex: C, D#, A): ").upper()
        if tom_input not in TONS:
            tom_input = "C"
            print("⚠️ Tom inválido, usando C.")
            
        escala_input = input("Escolha a escala (maior, menor, pentatonica): ").lower()
        if escala_input not in ESCALAS:
            escala_input = "menor"
            print("⚠️ Escala inválida, usando menor.")

        qtd_notas = int(input("Quantas notas? (ex: 16): "))
        bpm_input = int(input("BPM? (ex: 120): "))

        # 2. Processamento (Chama o motor)
        melodia = engine.gerar_melodia(tom_input, escala_input, qtd_notas)
        melodia_legivel = engine.traduzir_notas(melodia)
        
        print("\n🤖 Valores MIDI:", melodia)
        print("🎼 Notas Musicais:", melodia_legivel)

        # 3. Menu de Ação
        print("\n1️⃣ Tocar melodia")
        print("2️⃣ Exportar MIDI")
        print("3️⃣ Exportar Áudio (WAV)")
        escolha = input("O que deseja fazer? ")

        nome_base = f"melodia_{tom_input}_{escala_input}"

        if escolha == "1":
            engine.tocar_melodia(melodia, bpm_input)
        elif escolha == "2":
            engine.salvar_midi(melodia, bpm_input, nome_base + ".mid")
        elif escolha == "3":
            engine.salvar_wav(melodia, bpm_input, nome_base + ".wav")
        else:
            print("❌ Opção inválida.")
            
    except ValueError:
        print("❌ Erro: Digite apenas números onde for pedido.")