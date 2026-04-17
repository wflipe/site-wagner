file_path = r"c:\Users\wagner.lima\Downloads\2026-1\Wagner 2026\Antigravity\Site Wagner\index.html"

with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
    lines = f.readlines()

# Correção por números de linha exatos baseados na visualização anterior
# Linha 621: SECRETÁRIA
lines[620] = '                    <span class="tag mb-4 md:mb-6 opacity-0 hero-tag">[ IA ESPECIALIZADA // SECRETÁRIA VIRTUAL ]</span>\n'
# Linha 622: recepção
lines[621] = '                    <span class="hl-word hl-ghost"><span class="hl-inner">Sua recepção</span></span>\n'
# Linha 623: perde pacientes
lines[622] = '                    <span class="hl-word hl-ghost"><span class="hl-inner">perde pacientes</span></span>\n'

# Correção de contraste na seção do Wagner
for i in range(len(lines)):
    lines[i] = lines[i].replace('text-white', 'text-fg')
    lines[i] = lines[i].replace('text-white/70', 'text-fg/70')
    lines[i] = lines[i].replace('text-white/60', 'text-fg/60')
    lines[i] = lines[i].replace('rgba(255,255,255,0.3)', 'rgba(13,31,31,0.3)')

with open(file_path, 'w', encoding='utf-8') as f:
    f.writelines(lines)

print("Linhas específicas corrigidas.")
