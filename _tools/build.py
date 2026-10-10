"""assets/css/style.css'i küçültüp index.html içindeki <style id="inline-css"> etiketine gömer.

CSS'te değişiklik yaptıktan sonra repo kökünde çalıştırın:  python _tools/build.py
(_ ile başlayan klasörleri GitHub Pages yayınlamaz.)
"""
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def minify(css):
    css = re.sub(r'/\*.*?\*/', '', css, flags=re.S)
    css = re.sub(r'\s+', ' ', css)
    css = re.sub(r'\s*([{};:,>])\s*', r'\1', css)
    return css.replace(';}', '}').strip()


def main():
    css = open(os.path.join(ROOT, 'assets', 'css', 'style.css'), encoding='utf-8').read()
    inline = minify(css).replace('url(../fonts/', 'url(assets/fonts/')
    path = os.path.join(ROOT, 'index.html')
    html = open(path, encoding='utf-8').read()
    html, n = re.subn(r'<style id="inline-css">.*?</style>', lambda m: '<style id="inline-css">' + inline + '</style>', html, flags=re.S)
    if n != 1:
        raise SystemExit('index.html içinde <style id="inline-css"> bulunamadı')
    open(path, 'w', encoding='utf-8', newline='\n').write(html)
    print('Gömülü CSS güncellendi:', len(inline), 'bayt')


if __name__ == '__main__':
    main()
