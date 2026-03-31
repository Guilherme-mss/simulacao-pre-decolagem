import random

print("===== SIMULAÇÃO DE PRÉ-DECOLAGEM =====\n")

# =========================
# TELEMETRIA ALEATÓRIA
# =========================
temp_interna = random.uniform(10, 35)
temp_externa = random.uniform(-60, 60)
integridade = random.choices([1, 0], weights=[90, 10])[0]
carga = random.randint(50, 100)
pressao = random.uniform(3, 7)
modulos = random.choices(["OK", "FALHA"], weights=[85, 15])[0]

print("===== TELEMETRIA =====")
print(f"Temperatura interna: {temp_interna:.2f} °C")
print(f"Temperatura externa: {temp_externa:.2f} °C")
print(f"Integridade estrutural: {integridade}")
print(f"Carga: {carga}%")
print(f"Pressão: {pressao:.2f} bar")
print(f"Módulos críticos: {modulos}")

# =========================
# ANÁLISE ENERGÉTICA
# =========================
capacidade_total = 1000  # kWh
perdas = 50
consumo_decolagem = 300

energia_disponivel = capacidade_total * (carga / 100)
energia_util = energia_disponivel - perdas

print("\n===== ANÁLISE ENERGÉTICA =====")
print(f"Energia disponível: {energia_disponivel:.2f} kWh")
print(f"Energia útil: {energia_util:.2f} kWh")
print(f"Consumo estimado na decolagem: {consumo_decolagem} kWh")

# =========================
# VERIFICAÇÃO DA MISSÃO
# =========================
erros = []

if integridade == 0:
    erros.append("Falha estrutural")

if carga < 70:
    erros.append("Carga abaixo do mínimo (70%)")

if temp_interna < 18 or temp_interna > 27:
    erros.append("Temperatura interna fora do padrão")

if temp_externa < -50 or temp_externa > 50:
    erros.append("Temperatura externa fora do padrão")

if pressao < 4 or pressao > 6:
    erros.append("Pressão inadequada")

if modulos != "OK":
    erros.append("Falha nos módulos críticos")

if energia_util < consumo_decolagem:
    erros.append("Energia insuficiente para decolagem")

# =========================
# RESULTADO FINAL
# =========================
print("\n===== RESULTADO =====")

if erros:
    print("Status: DECOLAGEM ABORTADA ")
    print("\nMotivos:")
    for erro in erros:
        print(f"- {erro}")
else:
    print("Status: PRONTO PARA DECOLAR")

# ==============
# ANÁLISE POR IA
# ==============
print("\n===== ANÁLISE INTELIGENTE =====")

if not erros:
    print("Sistema operando dentro dos parâmetros ideais.")
else:
    print("Foram detectadas anomalias críticas no sistema.")

# Sugestões automáticas
for erro in erros:
    if "energia" in erro.lower():
        print("- Sugestão: aumentar carga ou reduzir consumo.")
    if "pressão" in erro.lower():
        print("- Sugestão: verificar sistema de pressurização.")
    if "temperatura" in erro.lower():
        print("- Sugestão: ajustar controle térmico.")
    if "estrutural" in erro.lower():
        print("- Sugestão: realizar inspeção estrutural imediata.")
    if "módulos" in erro.lower():
        print("- Sugestão: revisar módulos críticos.")
