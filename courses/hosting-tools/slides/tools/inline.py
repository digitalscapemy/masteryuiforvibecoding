"""Make every slide self-contained, so it opens anywhere (server, file://, file preview).

Shared files live in slides/assets/. In a slide, reference them normally:
  <link rel="stylesheet" href="assets/dock.css">
  <script src="assets/slide-no.js"></script>
  <img src="assets/repo-public.png">
Run:  python tools/inline.py      (from the slides folder)
Each reference is replaced by the file's content, tagged with data-src, so running
the script again after editing an asset refreshes every slide.
"""
import base64, glob, os, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
def read(p): return open(os.path.join(ROOT, p), encoding='utf-8').read()
def b64(p):
    ext = p.rsplit('.', 1)[-1].lower()
    mime = {'png': 'image/png', 'jpg': 'image/jpeg', 'jpeg': 'image/jpeg', 'webp': 'image/webp', 'svg': 'image/svg+xml'}[ext]
    return 'data:%s;base64,%s' % (mime, base64.b64encode(open(os.path.join(ROOT, p), 'rb').read()).decode())

for fn in sorted(glob.glob(os.path.join(ROOT, 'hosting-slide-*.html'))):
    s = open(fn, encoding='utf-8').read(); before = s
    # stylesheets: <link href="assets/x.css"> or an earlier inlined <style data-src="assets/x.css">
    s = re.sub(r'<link rel="stylesheet" href="(assets/[^"]+\.css)">',
               lambda m: '<style data-src="%s">\n%s</style>' % (m[1], read(m[1])), s)
    s = re.sub(r'<style data-src="(assets/[^"]+)">.*?</style>',
               lambda m: '<style data-src="%s">\n%s</style>' % (m[1], read(m[1])), s, flags=re.S)
    # scripts
    s = re.sub(r'<script src="(assets/[^"]+\.js)"></script>',
               lambda m: '<script data-src="%s">\n%s</script>' % (m[1], read(m[1])), s)
    s = re.sub(r'<script data-src="(assets/[^"]+)">.*?</script>',
               lambda m: '<script data-src="%s">\n%s</script>' % (m[1], read(m[1])), s, flags=re.S)
    # images
    s = re.sub(r'src="(assets/[^"]+\.(?:png|jpe?g|webp|svg))"',
               lambda m: 'data-asset="%s" src="%s"' % (m[1], b64(m[1])), s)
    s = re.sub(r'data-asset="(assets/[^"]+)" src="data:[^"]*"',
               lambda m: 'data-asset="%s" src="%s"' % (m[1], b64(m[1])), s)
    if s != before:
        open(fn, 'w', encoding='utf-8').write(s)
    print(os.path.basename(fn), 'updated' if s != before else 'unchanged')
