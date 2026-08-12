import sys
import os
import time
from markitdown import MarkItDown

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

pdf_files = [
    'ipas-ai-junior-cert-textbook-v2.pdf',
    'ipas-ai-mid-cert-textbook-vol1-v3.pdf',
    'ipas-ai-mid-cert-textbook-vol2-v3.pdf',
    'ipas-ai-mid-cert-textbook-vol3-v3.pdf'
]

cwd = r'C:\Users\etrny\.gemini\antigravity\scratch\iPAS_study'
md_engine = MarkItDown()

for pdf in pdf_files:
    pdf_path = os.path.join(cwd, pdf)
    md_name = os.path.splitext(pdf)[0] + '.md'
    md_path = os.path.join(cwd, md_name)
    
    print(f'Starting conversion: {pdf} -> {md_name}...')
    start_time = time.time()
    
    try:
        result = md_engine.convert(pdf_path)
        content = result.text_content
        with open(md_path, 'w', encoding='utf-8') as f:
            f.write(content)
        elapsed = time.time() - start_time
        size_kb = os.path.getsize(md_path) / 1024
        print(f'✅ Converted {pdf} ({size_kb:.1f} KB) in {elapsed:.2f}s')
    except Exception as e:
        print(f'❌ Error converting {pdf}: {e}')

print('All PDF conversions completed!')
