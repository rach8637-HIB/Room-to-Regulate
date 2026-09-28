/* Room to Regulate — shared site navigation.
   Builds the global menu (Home · About · Join · Survive · Solve · Shift ·
   Resources · The Room · Partner) on every page, marks the current page,
   and drives the mobile menu. No dependencies. */
(function () {
  'use strict';

  /* load the shared stylesheet (so a page only needs this script tag) */
  if (!document.querySelector('link[data-rtr-nav]')) {
    var css = document.createElement('link');
    css.rel = 'stylesheet';
    css.href = 'nav.css';
    css.setAttribute('data-rtr-nav', '');
    document.head.appendChild(css);
  }

  var INDEX = 'site-index.html';
  var CONTACT = 'mailto:hello@roomtoregulate.org?subject=Partnership%20enquiry';

  var MENUS = {
    survive: {
      head: 'Survive — the moments that knock you down',
      all: INDEX,
      allLabel: 'Browse everything on the site index',
      items: [
        ['survive-1-chaos-ordinary-day.html', 'What Looks Like Chaos on an Ordinary Day'],
        ['survive-2-first-two-minutes.html', 'The First Two Minutes I Never Get'],
        ['survive-3-safe-place.html', "She's the One Place That's Supposed to Feel Safe"],
        ['survive-A-fight-not-about-money.html', "The Fight That Isn't Actually About Money"],
        ['survive-B-glow-shrink.html', 'She Used to Glow. I Watched Her Shrink.'],
        ['survive-C1-know-that-feeling.html', 'I Know Exactly What That Feels Like'],
        ['survive-E1-never-hit-anyone.html', "He's Never Hit Anyone — and Doesn't Get Believed"],
        ['survive-F-space-between.html', 'Keeping the Peace by Staying Quiet'],
        ['survive-G-moon-tides.html', 'He Is the Moon. I Am the Tides.'],
        ['survive-H-no-consequences.html', 'There Are No Consequences That Work'],
        ['survive-I-water-bottles.html', 'Where Do All the Water Bottles Go?'],
        ['survive-firebreathing.html', "I Have a Reason. I Don't Get an Excuse."],
        ['survive-grief.html', 'Looking at Old Photos of Her Laughing'],
        ['survive-homeonly.html', "He's an Angel Everywhere Except With Me"],
        ['survive-nervous-system.html', 'When Her Meltdown Becomes My Emergency']
      ]
    },
    solve: {
      head: 'Solve — what actually helps, tonight',
      all: INDEX,
      allLabel: 'Browse everything on the site index',
      items: [
        ['solve-4-figure-it-out.html', "The 'I'll Figure It Out' Mental Load Pattern"],
        ['solve-5-on-fire.html', 'When Everything Is on Fire at Once'],
        ['solve-A-adhd-spending.html', 'Talking About ADHD Spending Without a Character Attack'],
        ['solve-B-bad-one.html', "When Your Kid Says 'I'm the Bad One'"],
        ['solve-C2-not-built-for-both.html', "The System Wasn't Built for 'Both'"],
        ['solve-E2-what-to-say.html', 'What to Say — To Other Parents, and to Your Kid'],
        ['solve-F-boundaries.html', 'The Space Between Silence and Explosion'],
        ['solve-G-distance.html', 'How to Shorten the Distance the Tide Travels'],
        ['solve-H-buffer.html', "Why the Consequences Aren't Landing"],
        ['solve-I-water-bottles.html', 'The Water Bottle System That Actually Cuts Losses'],
        ['solve-firebreathing.html', 'Own Your ADHD Overload Without Weaponizing It'],
        ['solve-homeonly.html', "Why 'Angel at School' Isn't a Choice to Make Home Hard"],
        ['solve-inherited-stories.html', '"You Just Don\'t Stick With Things"']
      ]
    },
    shift: {
      head: 'Shift — the bigger picture, changed',
      all: INDEX,
      allLabel: 'Browse everything on the site index',
      items: [
        ['shift-6-org-chart.html', 'The Job With No Org Chart, No Backup, No Sick Days'],
        ['shift-C3-gifted-struggling.html', "Gifted and Struggling Isn't a Contradiction"],
        ['shift-D-nobody-wants-to-work.html', "It's Not That Nobody Wants to Work Anymore"],
        ['shift-F-screening-stops.html', 'The Screening Stops at 12 Months. The Dysregulation Does Not.']
      ]
    },
    resources: {
      head: 'Resources — tools, library &amp; references',
      all: INDEX,
      allLabel: 'Open the full site index',
      items: [
        ['resources-outsourcing-personalized.html', 'What Would It Cost to Outsource This? (Interactive)'],
        ['resources-outsourcing-static.html', 'What Would It Cost to Outsource This? (Print Sheet)'],
        ['verified-resources.html', 'Verified Resources'],
        ['whats-changed.html', "What's Actually Changed"],
        ['glossary.html', 'The Room to Regulate Glossary'],
        ['explainer-E3-tells-it-messy.html', 'Explainer: The Kid Who Tells It Messy'],
        [INDEX, 'Full Site Index']
      ]
    },
    partner: {
      head: 'Partner — how we work with others',
      items: [
        ['partner-card-demo.html', 'The Native Partner Card'],
        ['verified-resources.html', 'Our Verified Resource Standards'],
        [CONTACT, 'Partner With Us']
      ]
    }
  };

  /* which top-level menu each page belongs to (first match wins) */
  var GROUP_OF = {};
  Object.keys(MENUS).forEach(function (key) {
    MENUS[key].items.forEach(function (pair) {
      if (pair[0].indexOf('mailto:') === 0) return;
      if (pair[0] === INDEX) return; /* shared by every menu */
      if (!GROUP_OF[pair[0]]) GROUP_OF[pair[0]] = key;
    });
  });

  function currentFile() {
    var p = (location.pathname.split('/').pop() || '').trim();
    if (!p) p = 'index.html';
    return p === 'index.html' ? 'home.html' : p;
  }

  function esc(s) {
    return String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');
  }

  function raw(s) {
    return String(s); /* trusted, hand-authored label markup */
  }

  function menuHTML(key) {
    var spec = MENUS[key];
    var here = currentFile();
    var html = '<span class="rtr-menu-head">' + raw(spec.head) + '</span>';
    spec.items.forEach(function (pair) {
      var cls = 'rtr-menu-item' + (pair[0] === here ? ' current' : '');
      html += '<a class="' + cls + '" href="' + esc(pair[0]) + '"' +
        (pair[0].indexOf('mailto:') === 0 ? ' target="_top"' : '') + '>' + raw(pair[1]) + '</a>';
    });
    if (spec.all) {
      html += '<a class="rtr-menu-all" href="' + esc(spec.all) + '">' + raw(spec.allLabel || 'Full site index') + ' &rarr;</a>';
    }
    return html;
  }

  function ddHTML(key, label) {
    return '<div class="rtr-dd" data-key="' + key + '">' +
      '<button class="rtr-dd-btn" type="button" aria-haspopup="true" aria-expanded="false">' +
      esc(label) + '<i class="rtr-caret" aria-hidden="true"></i></button>' +
      '<div class="rtr-menu">' + menuHTML(key) + '</div></div>';
  }

  function itemHTML(href, label) {
    return '<a class="rtr-item" href="' + esc(href) + '">' + esc(label) + '</a>';
  }

  function navInnerHTML() {
    return '' +
      '<a class="rtr-logo" href="home.html">room to <span>regulate</span></a>' +
      '<div class="rtr-links">' +
      itemHTML('home.html', 'Home') +
      itemHTML('about.html', 'About') +
      itemHTML('community.html', 'Join') +
      ddHTML('survive', 'Survive') +
      ddHTML('solve', 'Solve') +
      ddHTML('shift', 'Shift') +
      ddHTML('resources', 'Resources') +
      itemHTML('the-room.html', 'The Room') +
      ddHTML('partner', 'Partner') +
      '</div>' +
      '<a class="cta-btn rtr-cta" href="community.html#membership">Join us</a>' +
      '<button class="rtr-burger" type="button" aria-expanded="false" aria-controls="rtr-links" aria-label="Open menu">&#9776;</button>';
  }

  function markActive(nav) {
    var here = currentFile();
    var links = nav.querySelectorAll('a.rtr-item[href]');
    for (var i = 0; i < links.length; i++) {
      var file = (links[i].getAttribute('href') || '').split('#')[0].split('/').pop();
      if (file === here) links[i].classList.add('active');
    }
    var group = GROUP_OF[here];
    if (group) {
      var btn = nav.querySelector('.rtr-dd[data-key="' + group + '"] .rtr-dd-btn');
      if (btn) {
        btn.classList.add('active');
        btn.setAttribute('aria-expanded', 'false');
      }
    }
  }

  function closeAll(nav, except) {
    var open = nav.querySelectorAll('.rtr-dd.open');
    for (var i = 0; i < open.length; i++) {
      if (open[i] !== except) {
        open[i].classList.remove('open');
        var b = open[i].querySelector('.rtr-dd-btn');
        if (b) b.setAttribute('aria-expanded', 'false');
      }
    }
  }

  function wire(nav) {
    var dds = nav.querySelectorAll('.rtr-dd');
    for (var i = 0; i < dds.length; i++) {
      (function (dd) {
        var trigger = dd.querySelector('.rtr-dd-btn');
        if (!trigger) return;
        trigger.addEventListener('click', function (e) {
          if (e.metaKey || e.ctrlKey || e.shiftKey || e.altKey) return;
          e.preventDefault();
          var willOpen = !dd.classList.contains('open');
          closeAll(nav, dd);
          dd.classList.toggle('open', willOpen);
          trigger.setAttribute('aria-expanded', willOpen ? 'true' : 'false');
        });
      })(dds[i]);
    }

    document.addEventListener('click', function (e) {
      if (!e.target || !e.target.closest || !e.target.closest('.rtr-dd')) closeAll(nav, null);
    });

    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' || e.keyCode === 27) {
        closeAll(nav, null);
        nav.classList.remove('rtr-open');
        var burger = nav.querySelector('.rtr-burger');
        if (burger) burger.setAttribute('aria-expanded', 'false');
      }
    });

    var burger = nav.querySelector('.rtr-burger');
    if (burger) {
      burger.addEventListener('click', function (e) {
        e.stopPropagation();
        var open = nav.classList.toggle('rtr-open');
        burger.setAttribute('aria-expanded', open ? 'true' : 'false');
        if (!open) closeAll(nav, null);
      });
    }
  }

  function resolveNav() {
    var nav = document.querySelector('nav');
    if (nav) return nav;
    var wrap = document.querySelector('.wrap') || document.body;
    if (!wrap) return null;
    nav = document.createElement('nav');
    wrap.insertBefore(nav, wrap.firstChild);
    return nav;
  }

  function init() {
    var nav = resolveNav();
    if (!nav || nav.getAttribute('data-rtr-built')) return;
    nav.setAttribute('data-rtr-built', '1');
    nav.className = 'rtr-nav';
    nav.innerHTML = navInnerHTML();
    var links = nav.querySelector('.rtr-links');
    if (links) links.id = 'rtr-links';
    markActive(nav);
    wire(nav);
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
