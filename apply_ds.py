import re

file_path = r"c:\Users\wagner.lima\Downloads\2026-1\Wagner 2026\Antigravity\Site Wagner\index.html"

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update .prob-card
content = re.sub(
    r'\.prob-card\s*\{[^}]*\}',
    '.prob-card {\n            padding: 1.5rem 2rem;\n            margin-bottom: 1.5rem;\n            background: var(--bg);\n            border-radius: 0.5rem;\n            border: none;\n            box-shadow: 0px 16px 40px -10px rgba(22, 28, 39, 0.04);\n            transition: background .3s;\n        }',
    content
)
content = re.sub(
    r'\.prob-card:hover\s*\{[^}]*\}',
    '.prob-card:hover {\n            background: #f1f3ff;\n        }',
    content
)

# 2. Update .test-grid & .test-card
content = re.sub(
    r'\.test-grid\s*\{[^}]*\}',
    '.test-grid {\n            display: grid;\n            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));\n            gap: 2rem;\n            background: transparent;\n        }',
    content
)
content = re.sub(
    r'\.test-card\s*\{[^}]*\}',
    '.test-card {\n            background: #ffffff;\n            padding: 3rem 2.5rem;\n            display: flex;\n            flex-direction: column;\n            transition: background .3s;\n            border-radius: .5rem;\n            box-shadow: 0px 16px 40px -10px rgba(22, 28, 39, 0.04);\n            border: none;\n        }',
    content
)
content = re.sub(
    r'\.test-card:hover\s*\{[^}]*\}',
    '.test-card:hover {\n            background: #e3e8f9;\n        }',
    content
)

# 3. Update .stat-item
content = re.sub(
    r'border-right:\s*1px\s*solid\s*var\(--border\);',
    'border-right: none;',
    content
)

# 4. Update .mod-grid & .mod-card
content = re.sub(
    r'\.mod-grid\s*\{[^}]*\}',
    '.mod-grid {\n            display: grid;\n            grid-template-columns: repeat(3, 1fr);\n            gap: 2rem;\n            background: transparent;\n        }',
    content
)
content = re.sub(
    r'\.mod-card\s*\{[^}]*\}',
    '.mod-card {\n            background: #ffffff;\n            padding: 3rem;\n            display: flex;\n            flex-direction: column;\n            transition: background .3s;\n            border-radius: .5rem;\n            box-shadow: 0px 16px 40px -10px rgba(22, 28, 39, 0.04);\n        }',
    content
)
content = re.sub(
    r'\.mod-card\.featured\s*\{[^}]*\}',
    '.mod-card.featured {\n            background: #f1f3ff;\n            box-shadow: 0px 20px 50px -10px rgba(22, 28, 39, 0.08);\n        }',
    content
)
content = re.sub(
    r'\.mod-price\s*\{([^}]*?)border-top:\s*none;([^}]*?)\}',
    r'.mod-price {\1\2}',
    content
)
# remove inline border-top in .mod-price
content = re.sub(r'style="border-top:1px solid rgba[^"]*"', '', content)


# 5. Background shifts instead of inline border-tops for sections
content = re.sub(r'style="border-top:1px solid var\(--border\)[^"]*?"', 'style="background: #f1f3ff;"', content)

# 6. Update Buttons Primary, Secondary, Tertiary
content = re.sub(
    r'\.cta-main\s*\{[^}]*\}',
    '.cta-main {\n            display: inline-flex;\n            align-items: center;\n            gap: 1rem;\n            background: #00677d;\n            color: #ffffff;\n            font-family: \'Space Grotesk\', sans-serif;\n            font-weight: 700;\n            text-transform: uppercase;\n            padding: 1.25rem 2.5rem;\n            border-radius: .5rem;\n            transition: all .3s ease;\n            border: none;\n            letter-spacing: .05em;\n        }',
    content
)
content = re.sub(
    r'\.cta-main:hover\s*\{[^}]*\}',
    '.cta-main:hover {\n            background: #00a1c1;\n            transform: translateY(-2px);\n            box-shadow: 0px 8px 16px -4px rgba(0, 103, 125, 0.2);\n        }',
    content
)
content = re.sub(
    r'\.tag\s*\{[^}]*\}',
    '.tag {\n            font-family: \'Space Grotesk\', sans-serif;\n            font-size: .65rem;\n            text-transform: uppercase;\n            letter-spacing: .15em;\n            padding: .25rem .75rem;\n            border-radius: .125rem;\n            background: #bdc7dc;\n            color: #161c27;\n            display: inline-block;\n        }',
    content
)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("CSS structures updated.")
