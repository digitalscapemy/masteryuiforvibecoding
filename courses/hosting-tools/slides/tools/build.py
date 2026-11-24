"""Write every hosting-slide-*.html from tools/data.py, then inline the shared assets.
Run from the slides folder:  python -I tools/build.py
The HTML files are generated: edit tools/data.py (text) or this file (layout), not the HTML.
"""
import html, os, re, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
from data import COURSE, PRICE_NOTE, FAMILIES, TOOLS, COMPARE, CHOOSE, PATH, PROMPT  # noqa: E402

ICONS = {
  'branch': '<circle cx="6" cy="5" r="2.5"/><circle cx="6" cy="19" r="2.5"/><circle cx="18" cy="8" r="2.5"/><path d="M6 7.5v9M18 10.5c0 4.5-7 3.5-11 6.5"/>',
  'cog': '<circle cx="12" cy="12" r="3.5"/><path d="M12 2v3M12 19v3M2 12h3M19 12h3M4.9 4.9 7 7M17 17l2.1 2.1M4.9 19.1 7 17M17 7l2.1-2.1"/>',
  'globe': '<circle cx="12" cy="12" r="10"/><path d="M2 12h20M12 2a15 15 0 0 1 0 20M12 2a15 15 0 0 0 0 20"/>',
  'server': '<rect x="3" y="3" width="18" height="7" rx="2"/><rect x="3" y="14" width="18" height="7" rx="2"/><path d="M7 6.5h.01M7 17.5h.01"/>',
  'terminal': '<rect x="2" y="3" width="20" height="18" rx="3"/><path d="m6 9 4 3-4 3M12 15h6"/>',
  'grid': '<rect x="3" y="3" width="7" height="7" rx="1.5"/><rect x="14" y="3" width="7" height="7" rx="1.5"/><rect x="3" y="14" width="7" height="7" rx="1.5"/><rect x="14" y="14" width="7" height="7" rx="1.5"/>',
  'upload': '<path d="M12 15V3M7 8l5-5 5 5M4 15v4a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2v-4"/>',
  'cart': '<circle cx="9" cy="20" r="1.5"/><circle cx="18" cy="20" r="1.5"/><path d="M2 3h3l3 12h11l2-8H6"/>',
  'link': '<path d="M10 13a5 5 0 0 0 7 0l3-3a5 5 0 0 0-7-7l-1 1M14 11a5 5 0 0 0-7 0l-3 3a5 5 0 0 0 7 7l1-1"/>',
  'cloud': '<path d="M17.5 19H7a5 5 0 1 1 1-9.9A6 6 0 0 1 19.5 11a4 4 0 0 1-2 8z"/>',
  'boxes': '<rect x="3" y="3" width="8" height="8" rx="2"/><rect x="13" y="3" width="8" height="8" rx="2"/><rect x="3" y="13" width="8" height="8" rx="2"/><path d="M17 13v8M13 17h8"/>',
  'home': '<path d="M3 11 12 3l9 8v9a1 1 0 0 1-1 1h-5v-6H9v6H4a1 1 0 0 1-1-1z"/>',
  'target': '<circle cx="12" cy="12" r="10"/><circle cx="12" cy="12" r="5.5"/><circle cx="12" cy="12" r="1.5"/>',
  'plus': '<path d="M12 5v14M5 12h14"/>',
  'minus': '<path d="M5 12h14"/>',
}
ST = {'ok': ('M20 6 9 17l-5-5', 'Yes'), 'part': ('M12 7v6M12 17h.01', 'Partly'), 'no': ('M18 6 6 18M6 6l12 12', 'No')}

def md(t):
    """escape, then **bold**; strings marked with <b> (taglines) are trusted as-is"""
    if '<b>' in t: return t
    return re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', html.escape(t, quote=False))

def icon(name, cls=''):
    return '<svg class="%s" viewBox="0 0 24 24">%s</svg>' % (cls, ICONS[name])

def pill(st, text=None):
    if not st: return '<span class="plain">%s</span>' % md(text)
    path, word = ST[st]
    return '<span class="st %s"><svg viewBox="0 0 24 24"><path d="%s"/></svg>%s</span>' % (st, path, md(text or word))

def table(head, rows, delay=1.1, step=.12, note_col=None):
    th = ''.join('<th>%s</th>' % md(h) for h in head)
    out = []
    for i, r in enumerate(rows):
        tds = ''.join('<td%s>%s</td>' % (' class="note"' if c == note_col else '', cell) for c, cell in enumerate(r))
        out.append('<tr style="animation-delay:%.2fs">%s</tr>' % (delay + i * step, tds))
    return '<table class="tbl"><thead><tr>%s</tr></thead><tbody>%s</tbody></table>' % (th, ''.join(out))

def page(no, title, body, fam=None, hook='', css='', extra=''):
    fam_attr = ' data-fam="%s"' % fam if fam else ''
    chip = ''
    if fam:
        chip = '<div class="fam"><i></i>%s</div>' % FAMILIES[fam][0]
    hook_html = '<p class="hook">%s</p>' % hook if hook else ''
    return '''<!doctype html>
<html lang="en" data-slide="%(no)s"%(fam)s>
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>%(plain)s</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/base.css">
<link rel="stylesheet" href="assets/hosting.css">
<style>%(css)s</style>
</head>
<body>
<div class="stage" id="stage">
  <div class="label"><span>%(course)s</span></div>
  %(chip)s
  <h1 class="title"><span>%(title)s</span></h1>
  <div class="bar"></div>
  %(hook)s
%(body)s
</div>
%(extra)s<script src="assets/base.js"></script>
<script src="assets/slide-no.js"></script>
</body>
</html>
''' % dict(no=no, fam=fam_attr, plain=html.escape(html.unescape(re.sub('<[^>]+>', '', title))), css=css, course=COURSE,
           chip=chip, title=title, hook=hook_html, body=body, extra=extra)

def write(no, doc):
    fn = os.path.join(ROOT, 'hosting-slide-%s.html' % no)
    open(fn, 'w', encoding='utf-8', newline='\n').write(doc)
    return os.path.basename(fn)

def nav(t, on):
    labels = [(t['no'], 'What is it'), (t['no'] + 'A', 'Pros & cons'), (t['no'] + 'B', 'What runs + scale'), (t['no'] + 'C', 'Cost + resources')]
    return '<div class="next">' + ''.join('<span class="%s">%s · %s</span>' % ('on' if i == on else '', n, l) for i, (n, l) in enumerate(labels)) + '</div>'

# ---------- per-tool slides ----------
def s_what(t):
    steps = []
    for i, (ic, label) in enumerate(t['flow']):
        x = 74 + i * 626
        steps.append('<div class="step glass a in-card" style="left:%dpx;animation-delay:%.1fs"><div class="ibox">%s</div><div><b>STEP %d</b><span>%s</span></div></div>'
                     % (x, 1.1 + i * .35, icon(ic), i + 1, md(label)))
        if i < 2:
            steps.append('<div class="arrow in" style="left:%dpx;animation-delay:%.1fs"><svg viewBox="0 0 106 40"><path d="M10 20h82M78 8l14 12-14 12"/></svg></div>'
                         % (x + 520, 1.3 + i * .35))
    pts = ''.join('<li>%s</li>' % md(p) for p in t['points'])
    fam_name, fam_icon = FAMILIES[t['fam']]
    body = '''  %s
  <div class="card glass in-card" style="left:74px;top:520px;width:1080px;height:430px;animation-delay:2s">
    <p class="kick">What it is</p><ul class="big">%s</ul>
  </div>
  <div class="card glass a in-card" style="left:1190px;top:520px;width:656px;height:430px;animation-delay:2.2s">
    <div class="ana">%s<p>%s</p></div>
    <p class="kick" style="margin-top:34px">Best for</p>
    <p class="best">%s</p>
  </div>
  %s''' % (''.join(steps), pts, icon('home'), md(t['analogy']), md(t['bestfor']), nav(t, 0))
    css = ('.big li{font-size:34px;line-height:44px;margin-bottom:30px}'
           '.ana{display:flex;gap:22px;align-items:center}.ana svg{flex:none;width:64px;height:64px;stroke:var(--acc-soft);fill:none;stroke-width:2;stroke-linecap:round;stroke-linejoin:round}'
           '.ana p{margin:0;font-size:32px;line-height:40px;font-weight:700;letter-spacing:-.02em}'
           '.best{margin:0;font-size:30px;line-height:40px;font-weight:500;color:var(--body)}')
    return write(t['no'], page(t['no'], '%s: <em>what is it?</em>' % t['name'], body, t['fam'], t['tagline'], css))

def s_proscons(t):
    def col(items, x, kind, title, ic, d):
        lis = ''.join('<li style="animation-delay:%.2fs">%s</li>' % (d + .3 + i * .18, md(p)) for i, p in enumerate(items))
        return ('<div class="card glass %s in-card pc" style="left:%dpx;top:300px;width:870px;height:650px;animation-delay:%.1fs">'
                '<div class="pch"><span class="dot %s">%s</span>%s</div><ul>%s</ul></div>') % (kind, x, d, kind, icon(ic), title, lis)
    body = col(t['pros'], 74, 'g', 'Pros', 'plus', 1.0) + col(t['cons'], 976, 'r', 'Cons', 'minus', 1.3) + nav(t, 1)
    css = ('.pc li{font-size:33px;line-height:43px;margin-bottom:34px;animation:fadeUp .6s var(--ease) both}'
           '.pc.g li::before{background:var(--green);box-shadow:0 0 8px var(--green-glow)}.pc.r li::before{background:var(--red);box-shadow:0 0 8px var(--red-glow)}'
           '.pch{display:flex;align-items:center;gap:20px;margin-bottom:34px;font-size:44px;font-weight:800;letter-spacing:-.03em}'
           '.dot{width:64px;height:64px;border-radius:50%;display:grid;place-items:center}.dot svg{width:34px;height:34px;fill:none;stroke-width:3.4;stroke-linecap:round}'
           '.dot.g{background:rgba(75,240,60,.14);border:3px solid var(--green)}.dot.g svg{stroke:var(--green)}'
           '.dot.r{background:rgba(240,55,60,.14);border:3px solid var(--red)}.dot.r svg{stroke:#ff8a8d}')
    return write(t['no'] + 'a', page(t['no'] + 'a', '%s: <em>pros &amp; cons</em>' % t['name'], body, t['fam'], '', css))

def s_runs(t):
    rows = [[md(n), pill(st), md(note)] for n, st, note in t['fw']]
    verdict, bullets, good, warn = t['scale']
    lis = ''.join('<li>%s</li>' % md(b) for b in bullets)
    body = '''  <div class="abs in" style="left:54px;top:290px;width:1120px;animation-delay:.9s">%s</div>
  <div class="card glass a in-card" style="left:1210px;top:290px;width:636px;height:670px;animation-delay:1.6s">
    <p class="kick">Long-term scale</p>
    <p class="vd">%s</p>
    <ul class="sc">%s</ul>
    <div class="verdict">%s<span>%s</span></div>
    <div class="verdict">%s<span>%s</span></div>
  </div>
  %s''' % (table(['Framework', 'Support', 'Note'], rows, note_col=2), md(verdict), lis,
           pill('ok', 'Great for'), md(good), pill('part', 'Careful'), md(warn), nav(t, 2))
    css = ('.tbl td:first-child{width:470px}.tbl td:nth-child(2){width:200px}'
           '.vd{margin:0 0 26px;font-size:36px;line-height:44px;font-weight:800;letter-spacing:-.025em}'
           '.sc li{font-size:26px;line-height:34px;margin-bottom:18px}.sc{margin-bottom:22px!important}')
    if len(t['fw']) > 6:
        css += '.tbl td{padding-top:13px;padding-bottom:13px}'
    return write(t['no'] + 'b', page(t['no'] + 'b', '%s: <em>what runs here?</em>' % t['name'], body, t['fam'], '', css))

def s_cost(t):
    rows = [[('<b>%s</b>' % md(c)) if i == 1 else md(c) for i, c in enumerate(r)] for r in t['cost']]
    bill = ''.join('<li>%s</li>' % md(b) for b in t['bill'])
    body = '''  <div class="abs in" style="left:54px;top:290px;width:1060px;animation-delay:.9s">%s<p class="foot">%s</p><p class="foot pn">%s</p></div>
  <div class="card glass a in-card" style="left:1150px;top:290px;width:696px;height:560px;animation-delay:1.6s">
    <p class="kick">What makes the bill go up</p>
    <ul class="bl">%s</ul>
    <div class="tip"><b>Tip</b>%s</div>
  </div>
  <div class="res glass in-card" style="animation-delay:2.1s"><span class="rk">%s Resources</span><p>%s</p></div>''' % (
        table(t['cost_head'], rows), md(t['cost_foot']), PRICE_NOTE, bill, md(t['tip']), icon('server'), md(t['res']))
    css = ('.bl li{font-size:27px;line-height:35px;margin-bottom:20px}'
           '.tip{position:absolute;left:40px;right:40px;bottom:34px;padding:18px 24px;border-radius:18px;background:rgba(255,255,255,.05);'
           'border:1.5px dashed var(--acc);font-size:25px;line-height:32px;font-weight:600}'
           '.tip b{display:inline-block;margin-right:14px;color:var(--acc-soft);text-transform:uppercase;letter-spacing:.08em;font-size:20px}'
           '.pn{font-size:18px;opacity:.75}'
           '.res{position:absolute;left:74px;top:880px;width:1772px;height:130px;display:flex;align-items:center;gap:32px;padding:0 40px}'
           '.rk{flex:none;display:flex;align-items:center;gap:14px;font-size:22px;font-weight:800;letter-spacing:.1em;text-transform:uppercase;color:var(--acc-soft)}'
           '.rk svg{width:38px;height:38px;stroke:var(--acc-soft);fill:none;stroke-width:2;stroke-linecap:round}'
           '.res p{margin:0;font-size:28px;line-height:36px;font-weight:500;color:var(--body)}.res b{color:#fff;font-weight:800}')
    if len(t['cost']) >= 5:
        css += '.tbl td{padding-top:13px;padding-bottom:13px}'
    return write(t['no'] + 'c', page(t['no'] + 'c', '%s: <em>what does it cost?</em>' % t['name'], body, t['fam'], '', css))

# ---------- opening & closing ----------
GROUPS = [
  ('managed', 'Furnished condo', 'Push code, it goes live. No server. Pay for usage.', ['Netlify', 'Vercel', 'Cloudflare'], 'Nothing'),
  ('panel', 'Rented room', 'Classic shared hosting. PHP, email, database. Cheap, old-school.', ['cPanel'], 'A little'),
  ('self', 'Your own land + contractor', 'Rent a VPS, install a panel: your own "Vercel". Cheapest at scale.', ['Easypanel', 'Coolify', 'Dokploy'], 'Everything'),
]
FAM_COL = {'managed': ('#4FA8FF', 'rgba(79,168,255,.5)'), 'panel': ('#FF9F3C', 'rgba(255,159,60,.5)'), 'self': ('#4BF03C', 'rgba(75,240,60,.5)')}

def s_cover():
    cards = []
    for i, (fam, ana, desc, tools, manage) in enumerate(GROUPS):
        c, g = FAM_COL[fam]
        x = 74 + i * 604
        tl = ''.join('<span>%s</span>' % n for n in tools)
        cards.append('''<div class="fc glass in-card" style="left:%dpx;--c:%s;--g:%s;animation-delay:%.1fs">
    <div class="fh">%s<div><small>%s</small><h3>%s</h3></div></div>
    <p>%s</p><div class="tl">%s</div>
    <div class="mg">You manage: <b>%s</b></div></div>''' % (x, c, g, 1.2 + i * .25, icon(FAMILIES[fam][1]), FAMILIES[fam][0], ana, desc, tl, manage))
    css = ('.fc{position:absolute;top:340px;width:564px;height:620px;padding:40px;border-color:var(--c);box-shadow:0 0 26px var(--g),inset 0 0 30px rgba(255,255,255,.04)}'
           '.fh{display:flex;gap:24px;align-items:center;margin-bottom:28px}.fh svg{flex:none;width:84px;height:84px;stroke:var(--c);fill:none;stroke-width:1.8;stroke-linecap:round;stroke-linejoin:round;filter:drop-shadow(0 0 10px var(--g))}'
           '.fh small{display:block;font-size:20px;font-weight:800;letter-spacing:.1em;text-transform:uppercase;color:var(--c)}'
           '.fh h3{margin:4px 0 0;font-size:38px;line-height:44px;font-weight:800;letter-spacing:-.025em}'
           '.fc p{margin:0 0 30px;font-size:29px;line-height:38px;font-weight:500;color:var(--body)}'
           '.tl{display:flex;flex-wrap:wrap;gap:14px}.tl span{padding:12px 24px;border-radius:999px;border:2px solid var(--c);font-size:28px;font-weight:800}'
           '.mg{position:absolute;left:40px;bottom:36px;font-size:26px;font-weight:600;color:var(--soft)}.mg b{color:#fff}'
           '.hook{font-size:40px}')
    return write('00', page('00', 'Where should my app <em>live?</em>', '\n'.join(cards),
                            hook='Seven hosting tools, <b>three families</b>, one question.', css=css))

QUESTIONS = [('What is it?', 'Plain words + who it is for'), ('Pros', 'Why people love it'), ('Cons', 'Where it hurts'),
             ('Long-term scale', 'Still OK when you grow?'), ('PHP & JS support', 'Laravel, WordPress, Next.js…'),
             ('Subscription cost', 'The monthly plan'), ('Usage cost', 'What makes the bill go up'), ('Resources', 'RAM, CPU, quota')]

def s_questions():
    cells = []
    for i, (q, d) in enumerate(QUESTIONS):
        x = 74 + (i % 4) * 448; y = 320 + (i // 4) * 250
        cells.append('<div class="q glass in-card" style="left:%dpx;top:%dpx;animation-delay:%.2fs"><span class="n">%d</span><h3>%s</h3><p>%s</p></div>'
                     % (x, y, 1 + i * .12, i + 1, q, d))
    maps = [('1', 'What is it', '1'), ('1A', 'Pros & cons', '2 + 3'), ('1B', 'What runs + scale', '4 + 5'), ('1C', 'Cost + resources', '6 + 7 + 8')]
    strip = ''.join('<span><b>%s</b> %s <i>(%s)</i></span>' % m for m in maps)
    css = ('.q{position:absolute;width:420px;height:220px;padding:30px 32px}'
           '.q .n{display:grid;place-items:center;width:52px;height:52px;border-radius:14px;border:2px solid var(--green);color:var(--green-soft);font-size:26px;font-weight:800;margin-bottom:18px}'
           '.q h3{margin:0 0 8px;font-size:34px;font-weight:800;letter-spacing:-.025em}.q p{margin:0;font-size:25px;color:var(--soft);font-weight:500}'
           '.map{position:absolute;left:74px;top:850px;width:1772px;display:flex;align-items:center;gap:20px;font-size:26px;font-weight:600;color:var(--body);animation:fadeUp .7s 2.3s var(--ease) both}'
           '.map > b{font-size:22px;letter-spacing:.1em;text-transform:uppercase;color:var(--soft);margin-right:8px}'
           '.map span{padding:16px 24px;border-radius:18px;border:2px solid rgba(255,255,255,.4)}.map span b{color:var(--green-soft);margin-right:6px}.map i{font-style:normal;color:var(--soft);font-size:22px}')
    body = '\n'.join(cells) + '\n  <div class="map"><b>Every tool = 4 slides</b>%s</div>' % strip
    return write('00a', page('00a', 'Same <em>8 questions</em>, every tool', body,
                             hook='So you can compare them side by side.', css=css))

def s_compare():
    head = ['']
    for t in TOOLS:
        c = FAM_COL[t['fam']][0]
        head.append('<span style="color:%s">%s</span>' % (c, t['name']))
    th = ''.join('<th>%s</th>' % h for h in head)
    trs = []
    for i, (q, cells) in enumerate(COMPARE):
        tds = '<td class="q">%s</td>' % q + ''.join('<td>%s</td>' % pill(st, txt) for st, txt in cells)
        trs.append('<tr style="animation-delay:%.2fs">%s</tr>' % (1 + i * .12, tds))
    body = '  <div class="abs in" style="left:54px;top:280px;width:1812px;animation-delay:.8s"><table class="tbl cmp"><thead><tr>%s</tr></thead><tbody>%s</tbody></table></div>' % (th, ''.join(trs))
    css = ('.cmp th{font-size:26px;letter-spacing:-.01em;text-transform:none;font-weight:800;text-align:center}'
           '.cmp td{text-align:center;padding:24px 10px}.cmp td.q{text-align:left;font-size:27px;width:290px;padding-left:20px}'
           '.cmp .st{font-size:20px;padding:7px 14px;gap:7px}.cmp .st svg{width:18px;height:18px}'
           '.plain{font-size:22px;font-weight:700;color:var(--body)}')
    return write('08', page('08', 'All seven, <em>side by side</em>', body, css=css))

def s_choose():
    qs = ''.join('<div class="cq glass in-card" style="top:%dpx;animation-delay:%.2fs"><span class="n">%d</span><div><h3>%s</h3><p>%s</p></div></div>'
                 % (290 + i * 186, 1 + i * .2, i + 1, md(q), md(a)) for i, (q, a) in enumerate(CHOOSE))
    steps = ''.join('<li><b>%s</b><span>%s</span></li>' % (md(a), md(b)) for a, b in PATH)
    body = '''  %s
  <div class="card glass g in-card" style="left:1180px;top:290px;width:666px;height:560px;animation-delay:1.8s">
    <p class="kick" style="color:var(--green-soft)">My path for beginners</p><ol class="path">%s</ol>
  </div>
  <div class="ask abs" style="left:74px;top:868px;width:1772px;animation:fadeUp .8s 2.4s var(--ease) both">
    <div class="term"><svg viewBox="0 0 60 40"><path d="M6 6l16 14L6 34"/><path class="cur" d="M30 34h24"/></svg></div>
    <div class="q"><small>Ask your AI</small><p id="p1">%s</p></div>
    <button class="btn copy" data-copy="#p1">Copy</button>
  </div>''' % (qs, steps, html.escape(PROMPT))
    css = ('.cq{position:absolute;left:74px;width:1070px;height:160px;display:flex;align-items:center;gap:28px;padding:0 36px}'
           '.cq .n{flex:none;display:grid;place-items:center;width:64px;height:64px;border-radius:50%;border:3px solid #fff;font-size:30px;font-weight:800}'
           '.cq h3{margin:0 0 6px;font-size:34px;font-weight:800;letter-spacing:-.025em}.cq p{margin:0;font-size:26px;line-height:33px;color:var(--body);font-weight:500}'
           '.path{margin:0;padding:0;list-style:none;counter-reset:p}.path li{counter-increment:p;position:relative;padding:0 0 16px 70px;margin-bottom:0}'
           '.path li::before{content:counter(p);position:absolute;left:0;top:0;width:46px;height:46px;border-radius:50%;display:grid;place-items:center;background:rgba(75,240,60,.14);border:2px solid var(--green);font-size:22px;font-weight:800}'
           '.path b{display:block;font-size:29px;font-weight:800;letter-spacing:-.02em}.path span{font-size:25px;color:var(--body);font-weight:500}'
           '.ask .q p{font-size:25px;line-height:32px}')
    return write('08a', page('08a', 'Which one should I <em>choose?</em>', body, css=css))

if __name__ == '__main__':
    made = [s_cover(), s_questions()]
    for t in TOOLS:
        made += [s_what(t), s_proscons(t), s_runs(t), s_cost(t)]
    made += [s_compare(), s_choose()]
    print('wrote %d slides' % len(made))
    # keep the deck order in sync
    deck = os.path.join(ROOT, 'hosting-deck.html')
    if os.path.exists(deck):
        s = open(deck, encoding='utf-8').read()
        s = re.sub(r"const SLIDES = \[.*?\];", 'const SLIDES = [%s];' % ','.join("'%s'" % m for m in made), s, flags=re.S)
        open(deck, 'w', encoding='utf-8', newline='\n').write(s)
    subprocess.run([sys.executable, '-I', os.path.join(HERE, 'inline.py')], check=True, stdout=subprocess.DEVNULL)
    print('assets inlined')
