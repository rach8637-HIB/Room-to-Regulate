#!/usr/bin/env python3
"""Rebuild the Room to Regulate navigation bar across every static page.

Adds: shared nav.css / nav.js, a dropdown nav (Home, About, Join, Survive,
Solve, Shift, Resources, The Room, Partner), removes the site-index
"Core pages" section and gives the partner card its own "Partner" section.
"""
import html as htmlmod
import pathlib
import re
import sys

ROOT = pathlib.Path('/workspace/app/frontend/public')
MIRROR = pathlib.Path('/workspace/app/frontend/index.html')

PAGES = sorted(ROOT.glob('*.html'))

SPECIAL_TOP = {
    'home.html': 'Home',
    'index.html': 'Home',
    'about.html': 'About',
    'community.html': 'Join',
    'the-room.html': 'The Room',
    'partner-card-demo.html': 'Partner',
}

RESOURCE_ITEMS = [
    ('resources-outsourcing-personalized.html', 'What Would It Cost to Outsource This?'),
    ('resources-outsourcing-static.html', 'What Would It Cost to Outsource This? (Print Sheet)'),
    ('verified-resources.html', 'Verified Resource Library'),
    ("whats-changed.html", "What's Actually Changed?"),
    ('glossary.html', 'Glossary'),
    ('explainer-E3-tells-it-messy.html', 'Explainer: The Kid Who Tells It Messy'),
    ('site-index.html', 'Full Site Index'),
]

GROUP_OF = {}          # filename -> top-level nav key
MENU_ITEMS = {}        # top-level nav key -> [(href, label)]


def label_for(path):
    """Human-readable menu label: the page's <h1>, cleaned and shortened."""
    s = path.read_text(encoding='utf-8')
    m = re.search(r'<h1[^>]*>(.*?)</h1>', s, re.S | re.I)
    if not m:
        m = re.search(r'<title>(.*?)</title>', s, re.S | re.I)
    text = m.group(1) if m else path.stem
    text = re.sub(r'<[^>]+>', '', text)
    text = htmlmod.unescape(text)
    text = re.sub(r'\s+', ' ', text).strip()
    # drop trailing brand suffixes such as " | room to regulate"
    text = re.split(r'\s+[|–—]\s+(?:room to regulate|Room to Regulate)\s*$', text)[0].strip()
    if len(text) > 62:
        text = text[:61].rstrip() + '...'
    return text


def build_menus():
    pillars = {'Survive': 'survive-', 'Solve': 'solve-', 'Shift': 'shift-'}
    for key, prefix in pillars.items():
        items = []
        for p in PAGES:
            if not p.name.startswith(prefix):
                continue
            if key == 'Shift' and p.name == 'whats-changed.html':
                continue
            items.append((p.name, label_for(p)))
            GROUP_OF[p.name] = key
        items.sort(key=lambda t: t[0])
        MENU_ITEMS[key] = items

    MENU_ITEMS['Resources'] = []
    for fname, label in RESOURCE_ITEMS:
        MENU_ITEMS['Resources'].append((fname, label))
        GROUP_OF[fname] = 'Resources'

    # Anything not yet surfaced stays reachable through Resources.
    covered = set(GROUP_OF) | set(SPECIAL_TOP) | {'partner-card-demo.html'}
    leftovers = [p for p in PAGES if p.name not in covered]
    for p in leftovers:
        MENU_ITEMS['Resources'].append((p.name, label_for(p)))
        GROUP_OF[p.name] = 'Resources'
    return leftovers


ORDER = ['Home', 'About', 'Join', 'Survive', 'Solve', 'Shift', 'Resources', 'The Room', 'Partner']
DROPDOWNS = {'Survive', 'Solve', 'Shift', 'Resources'}


def nav_html(current_file):
    """Full replacement <nav> markup with the active item marked."""
    if current_file.name == 'index.html':
        home_href = 'home.html'
    else:
        home_href = 'home.html'
    top_target = GROUP_OF.get(current_file.name) or SPECIAL_TOP.get(current_file.name, '')

    def link(href):
        # the Vite root mirror lives one level up in the source tree but is
        # published at the same flat root, so relative hrefs stay identical.
        return href if current_file.name != 'index.html' else href

    parts = []
    parts.append('<nav class="rtr-nav" id="rtr-nav">')
    parts.append('<a class="rtr-logo%s" href="%s">room to <span>regulate</span></a>'
                 % (' current' if top_target == 'Home' else '', link(home_href)))
    parts.append('<button class="rtr-burger" aria-label="Open menu" aria-expanded="false">&#9776;</button>')
    parts.append('<div class="rtr-links">')

    for key in ORDER:
        if key in DROPDOWNS:
            items = MENU_ITEMS[key]
            active = ' active' if top_target == key else ''
            btn = ('<button class="rtr-dd-btn%s" aria-expanded="false" aria-haspopup="true">%s'
                   '<span class="rtr-caret" aria-hidden="true"></span></button>' % (active, key))
            links = []
            for href, label in items:
                cur = ' current' if href == current_file.name else ''
                links.append('<a class="rtr-menu-item%s" href="%s">%s</a>'
                             % (cur, link(href), htmlmod.escape(label, quote=False)))
            parts.append('<div class="rtr-dd%s">%s<div class="rtr-menu" role="menu">%s</div></div>'
                         % (active, btn, ''.join(links)))
        else:
            href = {'Home': home_href,
                    'About': 'about.html',
                    'Join': 'community.html',
                    'The Room': 'the-room.html',
                    'Partner': 'partner-card-demo.html'}[key]
            active = ' active' if top_target == key else ''
            parts.append('<a class="rtr-item%s" href="%s">%s</a>' % (active, link(href), key))

    parts.append('<a class="cta-btn rtr-cta" href="community.html">Join us</a>')
    parts.append('</div>')
    parts.append('</nav>')
    return '\n'.join(parts)


NAV_CSS = """/* Room to Regulate — shared navigation bar */
nav.rtr-nav {
  position: relative;
  display: flex;
  align-items: center;
  justify-content: space-between;
  flex-wrap: wrap;
  gap: 12px 18px;
  max-width: 1140px;
  margin: 0 auto;
  padding: 16px clamp(18px, 4vw, 32px);
  background: transparent;
  font-family: 'Inter', sans-serif;
}
nav.rtr-nav * { box-sizing: border-box; }
.rtr-logo {
  font-family: 'Fraunces', serif !important;
  font-weight: 600;
  font-size: 22px;
  color: #423E45;
  text-decoration: none;
  margin: 0 !important;
  flex: 0 0 auto;
}
.rtr-logo span { color: #3D6772; }
.rtr-logo.active { color: #3D6772; }
.rtr-links {
  display: flex;
  align-items: center;
  flex-wrap: wrap;
  gap: 4px 20px;
}
.rtr-item,
.rtr-dd-btn {
  appearance: none;
  border: 0;
  background: none;
  padding: 6px 0;
  font: inherit;
  font-size: 14px;
  font-weight: 500;
  color: #423E45;
  opacity: .78;
  text-decoration: none;
  cursor: pointer;
  white-space: nowrap;
  transition: opacity .15s ease, color .15s ease;
}
.rtr-item:hover, .rtr-dd-btn:hover { opacity: 1; color: #3D6772; }
.rtr-item.active, .rtr-dd-btn.active { opacity: 1; color: #3D6772; font-weight: 600; }
.rtr-dd { position: relative; display: inline-flex; }
.rtr-caret {
  display: inline-block;
  margin-left: 6px;
  width: 7px; height: 7px;
  border-right: 1.6px solid currentColor;
  border-bottom: 1.6px solid currentColor;
  transform: rotate(45deg) translateY(-2px);
  opacity: .6;
}
.rtr-menu {
  display: none;
  position: absolute;
  top: calc(100% + 10px);
  left: 0;
  z-index: 80;
  width: 340px;
  max-width: calc(100vw - 36px);
  max-height: 68vh;
  overflow-y: auto;
  padding: 10px;
  background: #fff;
  border: 1px solid #ECE7DF;
  border-radius: 14px;
  box-shadow: 0 18px 44px rgba(66, 62, 69, .14);
}
.rtr-menu::before {
  content: "";
  position: absolute;
  top: -6px; left: 22px;
  width: 10px; height: 10px;
  background: #fff;
  border-left: 1px solid #ECE7DF;
  border-top: 1px solid #ECE7DF;
  transform: rotate(45deg);
}
.rtr-dd.open .rtr-menu { display: block; }
@media (hover: hover) and (pointer: fine) {
  .rtr-dd:hover .rtr-menu,
  .rtr-dd:focus-within .rtr-menu { display: block; }
}
.rtr-menu-item {
  display: block;
  padding: 9px 12px;
  border-radius: 9px;
  font-size: 13.5px;
  line-height: 1.4;
  color: #4A454A;
  text-decoration: none;
}
.rtr-menu-item + .rtr-menu-item { margin-top: 1px; }
.rtr-menu-item:hover { background: #EFF3F1; color: #3D6772; }
.rtr-menu-item.current { background: #F3EBEC; color: #8B6C74; font-weight: 600; }
.rtr-burger {
  display: none;
  appearance: none;
  border: 1px solid #ECE7DF;
  background: #fff;
  border-radius: 10px;
  padding: 6px 11px;
  font-size: 17px;
  line-height: 1;
  color: #423E45;
  cursor: pointer;
  order: 3;
}
.rtr-cta { flex: 0 0 auto; margin-left: 4px; }
@media (max-width: 1024px) {
  .rtr-burger { display: block; }
  .rtr-links {
    display: none;
    order: 4;
    width: 100%;
    flex-direction: column;
    align-items: stretch;
    gap: 0;
    padding-top: 10px;
  }
  nav.rtr-nav.rtr-open .rtr-links { display: flex; }
  .rtr-links > .rtr-item { padding: 12px 2px; border-bottom: 1px solid rgba(66, 62, 69, .07); }
  .rtr-dd { display: block; width: 100%; border-bottom: 1px solid rgba(66, 62, 69, .07); }
  .rtr-dd-btn { width: 100%; text-align: left; padding: 12px 2px; }
  .rtr-menu {
    position: static;
    width: 100%;
    max-width: none;
    max-height: none;
    overflow: visible;
    padding: 0 0 10px 12px;
    background: transparent;
    border: 0;
    border-radius: 0;
    box-shadow: none;
  }
  .rtr-menu::before { display: none; }
  .rtr-dd.open .rtr-menu { display: block; }
  .rtr-menu-item { padding: 9px 8px; }
  .rtr-menu-item:hover { background: #EFF3F1; }
  .rtr-cta { margin: 14px 0 0; text-align: center; }
}
"""

NAV_JS = """(function () {
  var nav = document.getElementById('rtr-nav');
  if (!nav) return;
  var dds = Array.prototype.slice.call(nav.querySelectorAll('.rtr-dd'));
  function closeAll(except) {
    dds.forEach(function (dd) {
      if (dd === except) return;
      dd.classList.remove('open');
      var b = dd.querySelector('.rtr-dd-btn');
      if (b) b.setAttribute('aria-expanded', 'false');
    });
  }
  dds.forEach(function (dd) {
    var btn = dd.querySelector('.rtr-dd-btn');
    if (!btn) return;
    btn.addEventListener('click', function (e) {
      e.preventDefault();
      e.stopPropagation();
      var willOpen = !dd.classList.contains('open');
      closeAll(dd);
      dd.classList.toggle('open', willOpen);
      btn.setAttribute('aria-expanded', willOpen ? 'true' : 'false');
    });
  });
  document.addEventListener('click', function () { closeAll(null); });
  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape') { closeAll(null); nav.classList.remove('rtr-open'); }
  });
  var burger = nav.querySelector('.rtr-burger');
  if (burger) {
    burger.addEventListener('click', function (e) {
      e.stopPropagation();
      var open = nav.classList.toggle('rtr-open');
      burger.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
  }
})();
"""

NAV_RE = re.compile(r'<nav\b[^>]*>.*?</nav>', re.S | re.I)
ASSET_RE = re.compile(r'href="nav\.css"|src="nav\.js"')
SCRIPT_RE = re.compile(r'<script[^>]*src="nav\.js"[^>]*>\s*</script>', re.S | re.I)


LINK_TAG = '<link rel="stylesheet" href="/nav.css">'
SCRIPT_TAG = '<script src="/nav.js" defer></script>'


def inject_assets(s):
    if '/nav.css' not in s:
        if re.search(r'</head>', s, re.I):
            s = re.sub(r'</head>', LINK_TAG + '\n' + SCRIPT_TAG + '\n</head>', s, count=1, flags=re.I)
        else:
            s = re.sub(r'<body', LINK_TAG + '\n' + SCRIPT_TAG + '\n<body', s, count=1, flags=re.I)
    elif not re.search(r'src="/nav\.js"', s):
        s = re.sub(r'(<link rel="stylesheet" href="/nav\.css">)',
                   r'\1\n' + SCRIPT_TAG, s, count=1, flags=re.I)
    return s


def fix_site_index(s):
    # 1. drop the "Core pages" section entirely (its content now lives in the nav bar)
    core = re.search(r'\n\s*<div class="section">\s*<div class="section-label">Core pages</div>.*?</div>\s*</div>',
                     s, re.S)
    if core:
        s = s.replace(core.group(0), '\n', 1)
    # 2. the partner card gets its own section instead of sitting under resources
    partner_card = re.search(r'\s*<a href="partner-card-demo\.html" class="link-card">.*?</a>', s, re.S)
    card_html = partner_card.group(0).strip() if partner_card else (
        '<a href="partner-card-demo.html" class="link-card">'
        '<span class="lc-pillar">partner</span>'
        '<div class="lc-title">Native Partner Card &amp; Disclosure — Example</div></a>')
    if partner_card:
        s = s.replace(partner_card.group(0), '\n    ', 1)
    if 'id="section-partner"' not in s:
        partner_section = ('\n  <div class="section" id="section-partner">\n'
                           '    <div class="section-label">Partner</div>\n'
                           '    <div class="link-grid">\n      '
                           + card_html +
                           '\n    </div>\n  </div>\n')
        s = s.replace('\n</div>\n</body>', partner_section + '</div>\n</body>', 1)
    s = s.replace('<div class="section-label">Real information &amp; fact-checking</div>',
                  '<div class="section-label">Verified information &amp; fact-checking</div>', 1)
    s = s.replace('Every page on roomtoregulate.org in one place.',
                  'Every page on roomtoregulate.org in one place. The nav bar carries all of it too — '
                  'Survive, Solve, Shift and Resources open straight into their full article lists.', 1)
    return s


def main():
    leftovers = build_menus()
    targets = list(PAGES) + [MIRROR]
    changed = []
    for path in targets:
        original = path.read_text(encoding='utf-8')
        s = original
        replacement = nav_html(path)
        if NAV_RE.search(s):
            s = NAV_RE.sub(lambda m: replacement, s, count=1)
        else:
            s = re.sub(r'(<div class="wrap">\s*)(<div class="logo">)',
                       r'\1' + replacement.replace('\\', '\\\\') + r'\n  \2', s, count=1, flags=re.S)
            if replacement not in s:
                s = re.sub(r'(<body[^>]*>)', r'\1\n' + replacement.replace('\\', '\\\\'), s, count=1, flags=re.I)
        s = inject_assets(s)
        if path.name == 'site-index.html':
            s = fix_site_index(s)
        if s != original:
            path.write_text(s, encoding='utf-8')
            changed.append(path.name)

    # public/nav.css was authored separately; only (re)write the behaviour file.
    (ROOT / 'nav.js').write_text(NAV_JS, encoding='utf-8')

    print('nav rebuilt on %d files' % len(changed))
    for key in ORDER:
        count = len(MENU_ITEMS.get(key, []))
        print('  %-10s %s' % (key, ('%d items' % count) if count else 'direct link'))
    print('extra pages folded into Resources:', ', '.join(p.name for p in leftovers) or 'none')
    missing = [p.name for p in PAGES
               if p.name not in set(GROUP_OF) and p.name not in SPECIAL_TOP]
    print('pages NOT reachable from the nav:', ', '.join(missing) or 'none')
    no_nav = [p.name for p in targets if p.name not in changed and 'rtr-nav' not in p.read_text(encoding='utf-8')]
    print('files still without the new nav:', ', '.join(no_nav) or 'none')


if __name__ == '__main__':
    sys.exit(main())
