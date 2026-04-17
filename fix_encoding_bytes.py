import os

file_path = r"c:\Users\wagner.lima\Downloads\2026-1\Wagner 2026\Antigravity\Site Wagner\index.html"

# Mapeamento de sequências de bytes corrompidas para caracteres corretos
replacements = {
    "SECRETÃ RIA": "SECRETÁRIA",
    "recepÃ§Ã£o": "recepção",
    "CLÃ NICA": "CLÍNICA",
    "MÃ‰DICA": "MÉDICA",
    "comeÃ§ou": "começou",
    "NÃ£o": "Não",
    "SaÃºde": "Saúde",
    "EmpresÃ¡rio": "Empresário",
    "Ã": "í", # Caso comum de erro em "Mídia" ou "Líder"
    "MÃ DIA": "MÍDIA",
    "EducaÃ§Ã£o": "Educação",
    "BilÃ­ngue": "Bilíngue",
    "OPERAÃ‡ÃƒO": "OPERAÇÃO",
    "inteligÃªncia": "inteligência",
    "ColÃ©gio": "Colégio",
    "â€œ": "“",
    "â€": "”",
    "Â·": "·",
    "Ãª": "ê"
}

with open(file_path, 'rb') as f:
    content = f.read()

# Substituição por bytes para evitar problemas de encoding na leitura
for old, new in replacements.items():
    content = content.replace(old.encode('utf-8'), new.encode('utf-8'))
    # Também tentar substituir as sequências que podem ter sido lidas errado antes
    try:
        content = content.replace(old.encode('latin1'), new.encode('utf-8'))
    except:
        pass

with open(file_path, 'wb') as f:
    f.write(content)

print("Correção de encoding finalizada via processamento de bytes.")
