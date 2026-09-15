#!/usr/bin/env python3
"""
OT Güvenliği Rehberi - Belge Denetim Betiği

Bu betik depodaki Markdown belgelerini çevrimdışı olarak denetler:
- UTF-8 kodlaması
- Tek H1 başlık kuralı
- Kapatılmamış kod blokları (```)
- Tablo sütun sayısı tutarlılığı
- Göreli dosya bağlantılarının ve başlık çapalarının (#) varlığı
- Satır sonu gereksiz boşluk denetimi (isteğe bağlı/bilgilendirme)

Kullanım:
    python3 scripts/check_docs.py [--strict-whitespace]
"""

import sys
import os
import re
import argparse
import unicodedata

# Windows konsolunda UTF-8 çıktısını destekle
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

def slugify(text):
    """GitHub Markdown başlık çapa (anchor) slug formatı."""
    text = text.strip().lower()
    # Bağlantı ve Markdown biçimlendirmelerini kaldır
    text = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', text)
    text = re.sub(r'[*_`~]', '', text)
    # Noktalama işaretlerini kaldır (harf, rakam, boşluk ve tireyi koru)
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'\s+', '-', text)
    return text

def check_documents(root_dir, strict_whitespace=False):
    errors = []
    warnings = []
    
    # Tüm depo dosyalarını dizinle
    all_files = set()
    for dp, dn, fns in os.walk(root_dir):
        rel_dp = os.path.relpath(dp, root_dir).replace('\\', '/')
        # .git, .claude, .gemini ve __pycache__ dizinlerini yoksay (.github hariç)
        if (rel_dp.startswith('.git') and not rel_dp.startswith('.github')) or \
           rel_dp.startswith('.claude') or rel_dp.startswith('.gemini') or \
           '__pycache__' in rel_dp:
            continue
        for fn in fns:
            full = os.path.join(dp, fn)
            rel = os.path.relpath(full, root_dir).replace('\\', '/')
            all_files.add(rel)

    md_files = [f for f in sorted(all_files) if f.endswith('.md')]
    heading_cache = {}

    # 1. Başlıkları ve temel kuralları tara
    for rel in md_files:
        full = os.path.join(root_dir, rel.replace('/', os.sep))
        try:
            with open(full, 'rb') as fp:
                raw = fp.read()
            content = raw.decode('utf-8')
        except UnicodeDecodeError as e:
            errors.append(f"{rel}: UTF-8 kodlama hatası: {e}")
            continue

        lines = content.split('\n')

        # H1 başlık kontrolü
        h1_lines = [(i + 1, l) for i, l in enumerate(lines) if re.match(r'^#\s+', l)]
        if len(h1_lines) == 0:
            errors.append(f"{rel}: Dosyada H1 (#) başlığı bulunamadı.")
        elif len(h1_lines) > 1:
            errors.append(f"{rel}:{h1_lines[1][0]}: Birden fazla H1 başlığı bulundu ({len(h1_lines)} adet).")

        # Başlık çapalarını önbelleğe al
        headings = []
        for line in lines:
            m = re.match(r'^(#{1,6})\s+(.*)', line)
            if m:
                headings.append(slugify(m.group(2)))
        heading_cache[rel] = headings

        # Kapatılmamış kod blokları kontrolü
        in_code_block = False
        code_start = 0
        for i, l in enumerate(lines, 1):
            if l.strip().startswith('```'):
                if not in_code_block:
                    in_code_block = True
                    code_start = i
                else:
                    in_code_block = False
        if in_code_block:
            errors.append(f"{rel}:{code_start}: Kapatılmamış kod bloğu (```).")

        # Tablo sütun sayısı kontrolü
        in_table = False
        table_cols = 0
        for i, l in enumerate(lines, 1):
            stripped = l.strip()
            if stripped.startswith('|') and stripped.endswith('|'):
                cols = len(re.findall(r'(?<!\\)\|', stripped)) - 1
                if not in_table:
                    in_table = True
                    table_cols = cols
                else:
                    if cols != table_cols:
                        errors.append(f"{rel}:{i}: Tablo sütun uyuşmazlığı (beklenen: {table_cols}, bulunan: {cols}).")
            else:
                in_table = False
                table_cols = 0

        # Satır sonu boşluk kontrolü
        for i, l in enumerate(lines, 1):
            # Dosya sonundaki tek \r atlanabilir
            line_no_cr = l.rstrip('\r')
            if line_no_cr.endswith(' ') or line_no_cr.endswith('\t'):
                msg = f"{rel}:{i}: Satır sonunda gereksiz boşluk var."
                if strict_whitespace:
                    errors.append(msg)
                else:
                    warnings.append(msg)

    # 2. Göreli bağlantıları ve çapaları denetle
    link_re = re.compile(r'\[([^\]]+)\]\(([^)]+)\)')
    for rel in md_files:
        full = os.path.join(root_dir, rel.replace('/', os.sep))
        with open(full, 'r', encoding='utf-8', errors='replace') as fp:
            content = fp.read()

        lines = content.split('\n')
        in_code = False
        for lno, line in enumerate(lines, 1):
            if line.strip().startswith('```'):
                in_code = not in_code
                continue
            if in_code:
                continue

            for m in link_re.finditer(line):
                text, url = m.groups()
                url = url.strip()

                # Dış bağlantıları atla
                if url.startswith('http://') or url.startswith('https://') or url.startswith('mailto:'):
                    continue

                parts = url.split('#', 1)
                target_file_rel = parts[0]
                target_anchor = parts[1] if len(parts) > 1 else None

                if target_file_rel:
                    curr_dir = os.path.dirname(rel)
                    resolved = os.path.normpath(os.path.join(curr_dir, target_file_rel)).replace('\\', '/')
                    if resolved not in all_files:
                        errors.append(f"{rel}:{lno}: Hedef dosya bulunamadı: [{text}]({url}) -> '{resolved}'")
                    elif target_anchor and resolved.endswith('.md'):
                        target_slugs = heading_cache.get(resolved, [])
                        if target_anchor not in target_slugs:
                            warnings.append(f"{rel}:{lno}: Başlık çapası bulunamadı: #{target_anchor} (Hedef: {resolved})")
                else:
                    if target_anchor:
                        current_slugs = heading_cache.get(rel, [])
                        if target_anchor not in current_slugs:
                            warnings.append(f"{rel}:{lno}: Dosya içi başlık çapası bulunamadı: #{target_anchor}")

    return md_files, errors, warnings

def main():
    parser = argparse.ArgumentParser(description="OT Güvenliği Rehberi Belge Denetimi")
    parser.add_argument("--strict-whitespace", action="store_true", help="Satır sonu boşluklarını hata say")
    args = parser.parse_args()

    # Proje kök dizini (scripts klasörünün bir üstü)
    script_dir = os.path.dirname(os.path.abspath(__file__))
    root_dir = os.path.abspath(os.path.join(script_dir, ".."))

    print(f"Denetim başlatılıyor: {root_dir}")
    md_files, errors, warnings = check_documents(root_dir, args.strict_whitespace)

    print(f"\nİncelenen Markdown dosya sayısı: {len(md_files)}")

    if warnings and not errors:
        print(f"Uyarı sayısı: {len(warnings)}")
        for w in warnings[:10]:
            print(f"  [UYARI] {w}")
        if len(warnings) > 10:
            print(f"  ... ve {len(warnings) - 10} uyarı daha.")

    if errors:
        print(f"\nHATA BULUNDU ({len(errors)} adet):")
        for e in errors:
            print(f"  [HATA] {e}")
        sys.exit(1)
    else:
        print("\n✅ Tüm biçim, bağlantı ve yapı kuralları başarıyla doğrulandı.")
        sys.exit(0)

if __name__ == "__main__":
    main()
