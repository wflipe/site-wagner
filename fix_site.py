import os

file_path = r"c:\Users\wagner.lima\Downloads\2026-1\Wagner 2026\Antigravity\Site Wagner\index.html"

replacements = {
    "SECRETÃ RIA": "SECRETÁRIA",
    "recepÃ§Ã£o": "recepção",
    "CLÃ NICA MÃ‰DICA": "CLÍNICA MÉDICA",
    "comeÃ§ou": "começou",
    "NÃ£o": "Não",
    "recepÃ§Ã£o": "recepção",
    "SaÃºde": "Saúde",
    "EmpresÃ¡rio": "Empresário",
    "MÃ DIA": "MÍDIA",
    "EducaÃ§Ã£o": "Educação",
    "BilÃ­ngue": "Bilíngue",
    "OPERAÃ‡ÃƒO": "OPERAÇÃO",
    "inteligÃªncia": "inteligência",
    "ColÃ©gio": "Colégio",
    "text-white": "text-fg",
    "text-white/70": "text-fg/70",
    "text-white/60": "text-fg/60",
    "text-white/50": "text-fg/50",
    "text-white/30": "text-fg/30",
    "rgba(255,255,255,0.3)": "rgba(13,31,31,0.3)",
    "rgba(255,255,255,.2)": "rgba(13,31,31,.2)",
    "text-white/70": "text-fg/70"
}

with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
    content = f.read()

for old, new in replacements.items():
    content = content.replace(old, new)

# Specific fix for the ghost text contrast
content = content.replace("-webkit-text-stroke: 1px rgba(13, 31, 31, .15)", "-webkit-text-stroke: 1.5px rgba(13, 31, 31, .3)")

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Fix applied successfully.")
