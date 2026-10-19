# Born Apparel Studio brand book — final edition: panels + visual layer.
# Executed inside build_book.py (shares SVG, ANI, KIT, PNG, DL, TITLE, datauri, rd).
# Visual language = the brand's documents: chapter openers with the giant stage
# wordmark bleeding off the edge, ledgers with hairlines instead of cards,
# ink and red full-bleed bands, Bodoni for voice, Jost for reading, Space Mono for data.
import os

# definitive tokens (Paper #F1F1EC / Ink #151517) applied to the inline marks
def _tok(s): return s.replace("#1B1720", "#151517").replace("#F2EEE6", "#F1F1EC")
SVG = {k: _tok(v) for k, v in SVG.items()}
ANI = {k: _tok(v) for k, v in ANI.items()}
GIANT = {k: _tok(rd(f"{S}/giant/{k}.svg")) for k in
         ["g_born_ink", "g_born_paper", "g_sketch_ink", "g_stitch_paper", "g_stitch_ink", "g_sketch_paper", "concept"]}
FACE = {"Bodoni5": ("BodoniModa-Medium.ttf", 500), "BodoniI": ("BodoniModa-Italic.ttf", 400)}
FACES = "".join(
    f"@font-face{{font-family:'{n}';src:url({datauri(f'{S}/fonts/{f}', 'font/ttf')}) format('truetype');"
    f"font-weight:{w};font-style:normal;font-display:swap}}\n" for n, (f, w) in FACE.items())

CHAPTERS = [("brand", "Brand"), ("logo", "Logo"), ("color", "Color"), ("type", "Typography"),
            ("apps", "Applications"), ("desc", "Downloads")]

# ------------------------------------------------------------------ helpers
def opener(n, title, sub, tone, giant=None, extra=""):
    g = f'<div class="op__giant" aria-hidden="true">{GIANT[giant]}</div>' if giant else ""
    return (f'<header class="op op--{tone} bleed"><div class="op__in inr">'
            f'<div class="op__top"><span class="lab k">{n} &middot; {CHAPTERS[int(n)-1][1]}</span>'
            f'<span class="lab">Born Apparel Studio &middot; Brand Book</span></div>'
            f'<h1 class="op__h">{title}<i>.</i></h1><p class="op__sub">{sub}</p>{extra}</div>{g}</header>')

def sh(k, title, dot=True):
    return f'<div class="sh"><span class="k">{k}</span><h2>{title}{"<i>.</i>" if dot else ""}</h2></div>'

def cols(items, n=None, cls=""):
    n = n or len(items)
    rd_ = ' class="rd"'
    return (f'<div class="cols cols--{n} {cls}">' + "".join(
        f'<div{rd_ if r else ""}><span class="k">{k}</span><h3>{h}</h3>{b}</div>'
        for k, h, b, r in items) + '</div>')

def tape_svg():
    """A tailor's tape: 60 ticks, the last fifteen (BORN) in red."""
    W, s = 1200, 20
    g = ['<svg class="tape" viewBox="0 0 1200 96" preserveAspectRatio="none" aria-hidden="true">',
         '<rect x="0" y="0" width="1200" height="96" fill="var(--paper)"/>']
    for i in range(61):
        x = min(i * s, W - 1)
        big, mid = i % 10 == 0, i % 5 == 0
        L = 34 if big else 22 if mid else 12
        c = "var(--red)" if i >= 45 else "var(--ink)"
        w = 2.4 if big else 1.2
        g.append(f'<line x1="{x}" y1="0" x2="{x}" y2="{L}" stroke="{c}" stroke-width="{w}"/>'
                 f'<line x1="{x}" y1="96" x2="{x}" y2="{96-L}" stroke="{c}" stroke-width="{w}"/>')
    g.append('</svg>')
    return "".join(g)

def tape_timeline():
    """The client journey measured on the tape."""
    nums = "".join(f'<span style="left:{i/60*100:.3f}%"{" class=r" if i >= 45 else ""}>{i}</span>' for i in range(0, 61, 10))
    return ('<div class="tl"><div class="tl__lab">'
            '<div><span class="k">1&ndash;3 weeks</span><b>Sketched</b><p>The Briefing</p></div>'
            '<div><span class="k">2&ndash;6 months</span><b>Stitched</b><p>The Development</p></div>'
            '<div class="rd"><span class="k">4&ndash;8 weeks</span><b>BORN</b><p>Production Oversight</p></div>'
            f'</div>{tape_svg()}<div class="tl__n">{nums}</div></div>')

toc = '<nav class="toc" aria-label="Chapters">' + "".join(
    f'<a href="#{k}" data-tab="{k}"><span class="k">0{i}</span>{lab}</a>' for i, (k, lab) in enumerate(CHAPTERS, 1)) + '</nav>'

# ------------------------------------------------------------------ 01 BRAND
brand = f"""
<section class="panel active" id="p-brand" role="tabpanel" aria-labelledby="t-brand">
{opener("01", "The brand is the process", "Sketched. Stitched. BORN. &mdash; From idea to life.", "paper", "g_born_ink",
        toc + '<button class="replaybtn" id="replayBtn" type="button">Watch the mark come to life</button>')}

<div class="sx">{sh("01", "The brand at a glance")}<div class="body">
 <dl class="lg">
  <dt>Name</dt><dd>Born Apparel Studio</dd>
  <dt>Logo</dt><dd>The BORN wordmark <small>BORN Studio</small></dd>
  <dt>Category</dt><dd>Full Service Apparel Development Studio</dd>
  <dt>Founder</dt><dd>Mar&iacute;a Batres</dd>
  <dt>Value proposition</dt><dd>Strategic Process and Design</dd>
  <dt>Master claim</dt><dd>Sketched. Stitched. <span class="r">BORN.</span></dd>
  <dt>Tagline</dt><dd><em>From idea to life</em></dd>
  <dt>Essence</dt><dd>Maturing a fashion idea into a manufacturable product</dd>
  <dt>What it sells</dt><dd>Confidence</dd>
  <dt>Archetype</dt><dd>Creator + Caregiver</dd>
  <dt>Ideal client</dt><dd>Emerging founder with vision and capital, no factory network</dd>
 </dl></div></div>

<div class="sx">{sh("02", "An apparel studio that does Strategic Process and Design")}<div class="body ins">
 <p class="lead">Mar&iacute;a knows what the problem costs <em>before she draws</em>, and how to prevent it.</p>
 <div><p class="p">Born Apparel Studio was founded by Mar&iacute;a, who learned the craft on the production floors of Portugal, Spain, Los Angeles and Austria: how garments are cut and sewn, where they break, and what makes a tech pack executable. The typical designer draws something pretty and throws the problem over the wall to the factory.</p>
 <p class="p">Theater and opera costume-making added one more standard: construction that holds up under real, repeated use, not just on a hanger.</p></div>
</div></div>

<div class="sx">{sh("03", "What BORN is, and what it is not")}<div class="body">
 <div class="split">
  <div class="pa"><span class="lab">BORN is</span><ul>
   <li>A studio that takes an idea to a manufacturable product</li>
   <li>Discovery, tech pack, factory match, samples, fitting, bulk oversight</li>
   <li>Factory-floor technical judgment</li>
   <li>A product brand: consistent aesthetic, voice and touchpoints</li></ul></div>
  <div class="ik"><span class="lab">BORN is not</span><ul>
   <li><b>A factory</b>it does not cut or sew</li>
   <li><b>A sourcing agency</b>it does not buy materials for the client</li>
   <li><b>An incubator</b>it does not invest capital or take equity</li>
   <li><b>A creative design studio</b>it does not lead the conceptual aesthetic</li></ul></div>
 </div></div></div>

<div class="sx">{sh("04", "Three filters against three fears")}<div class="body">
 <p class="lead">The client does not buy a tech pack. They buy the certainty that their first product will exist, <em>without the business breaking along the way.</em></p>
 {cols([("01","Viability",'<p class="q">Can it exist in the physical world?</p>',False),
        ("02","Cost",'<p class="q">Does it leave margin without sacrificing quality?</p>',False),
        ("03","Usability",'<p class="q">Does it work on the body, not just on the sample?</p>',False)], cls="cols--big")}
 <p class="p" style="margin-top:1.6rem">What BORN really sells is <b>confidence</b>. The tech pack, the sample and the oversight are its tangible forms.</p>
</div></div>

<div class="sx">{sh("05", "Four attributes, read at first glance")}<div class="body">
 {cols([("01","Editorial","<p>A serious fashion publication, not an agency.</p>",False),
        ("02","Technical","<p>The rigor of the tech pack: measurement, tolerance, every line with a reason.</p>",False),
        ("03","Tactile","<p>Paper, thread and measuring tape: the brand is felt in the hand before it is read.</p>",False),
        ("04","In process","<p>It changes state with the product: from sketch to stitch to life.</p>",False)])}
 <dl class="lg lg--sm" style="margin-top:2rem">
  <dt>The balance point</dt><dd>The factory is the origin; the brand is its editorial version.</dd>
  <dt>Never</dt><dd class="nope"><span>a branding agency</span> &middot; cold minimal sans, loose capital words</dd>
  <dt>Never</dt><dd class="nope"><span>a literal factory</span> &middot; industrial grids, corporate blues, machines</dd>
 </dl>
</div></div>

<div class="band bleed"><div class="inr">
 <div class="sh sh--d"><span class="k">06</span><h2>The claim is the process<i>.</i></h2></div>
 <p class="claim">Sketched. Stitched. <i>BORN.</i></p>
 <p class="tagl">From idea to life.</p>
 <div class="cols cols--4 cols--d">
  <div><span class="k">Proposals &amp; brief</span><h3>Sketched to be BORN</h3><p>Brief, moodboard, sketches, tech pack</p></div>
  <div><span class="k">Development</span><h3>Stitched to be BORN</h3><p>Samples in development, fittings, work in progress</p></div>
  <div><span class="k">Pre-production</span><h3>Made to be BORN</h3><p>Pre-production sample and size set</p></div>
  <div class="rd"><span class="k">Production</span><h3>Born to be made</h3><p>Approved product, ready for bulk</p></div>
 </div>
 <p class="p p--d" style="margin-top:2rem">In running text the name is always <b>Born Apparel Studio</b>. <b>BORN</b> goes in capitals when it names the brand or the final phase; a finished deliverable can be &ldquo;a BORN&rdquo;.</p>
</div></div>

<div class="sx">{sh("07", "Voice and tone")}<div class="body">
 {cols([("Archetype","Creator","<p>Pushes the idea toward its best version. Never just executes the brief &mdash; it questions it, improves it, takes it one step further.</p>",False),
        ("Archetype","Caregiver","<p>Protects the founder from costly mistakes. Says &ldquo;don&rsquo;t do this&rdquo; when it sees it, even if it costs the sale.</p>",False)], cls="cols--big")}
 <div class="tone"><span>Direct</span><span>Warm</span><span>Editorial</span><span>Precise</span><span>With judgment</span></div>
 <p class="p" style="margin-top:1.6rem">The answer first, then the explanation. Concrete numbers, realistic deadlines. The warmth comes from the craft, not from hugging.</p>
 <p class="nope nope--list"><span class="lab">Never write</span> <span>amazing</span> <span>solutions</span> <span>end-to-end experience</span> <span>strategic partner</span> <span>take your brand to the next level</span> <span>revolutionise</span> <span>made with love</span> <span>emojis</span></p>
</div></div>

<div class="fullred">
 <p class="fr-k">The promise</p>
 <h2>From idea<br>to life<span class="dk">.</span></h2>
 <p class="fr-s">The client hands over an idea &middot; BORN hands back life</p>
</div>
</section>"""

# ------------------------------------------------------------------ 02 LOGO
def stage(svg, cls=""): return f'<div class="stage {cls}">{svg}</div>'
def capt(b, s, p=""):
    return f'<div class="capt"><b>{b}</b><span>{s}</span>{f"<p>{p}</p>" if p else ""}</div>'

logo = f"""
<section class="panel" id="p-logo" role="tabpanel" aria-labelledby="t-logo">
{opener("02", "Double exposure", "The word BORN with its process-ghost behind it. The only thing born in color is the dot.", "ink", "g_stitch_paper")}

<div class="sx">{sh("01", "The primary lockup")}<div class="body">
 <div class="sheet"><i class="cm tl"></i><i class="cm tr"></i><i class="cm bl"></i><i class="cm br"></i>
  <div class="sheet__art">{SVG['wm_principal']}</div>
  <div class="dim"><span>BORN + DOT + TAGLINE</span></div>
 </div>
 <div class="tb">
  <div><span class="lab">Born Apparel Studio</span><span class="wm">BORN<b>.</b></span></div>
  <div><span class="lab">Lockup</span><span class="mono">Primary</span></div>
  <div><span class="lab">Use</span><span class="mono">Every application derives from here</span></div>
  <div><span class="lab">Sheet</span><span class="mono">01</span></div>
 </div>
</div></div>

<div class="sx">{sh("02", "The logotype is the process")}<div class="body">
 <div class="concept">{GIANT['concept']}</div>
 <div class="cols cols--4 letters">
  <div><span class="L">B</span><span class="k">Sketched</span><p>Pencil outline: the idea on paper.</p></div>
  <div><span class="L">O</span><span class="k">Stitched</span><p>Topstitch: tested with thread and needle.</p></div>
  <div><span class="L">R</span><span class="k">Inked</span><p>Solid: resolved and signed.</p></div>
  <div class="rd"><span class="L">N</span><span class="k">BORN</span><p>Born in color: it goes out into the world.</p></div>
 </div>
 <p class="p" style="margin-top:1.4rem">The sketch begins in black and white and comes to life with color.</p>
</div></div>

<div class="sx">{sh("03", "Two signatures in motion")}<div class="body">
 <div class="motion">
  <div><div class="animbox">{ANI['ens']}</div>{capt('Assembly','6 s loop','The sketch draws in and assembles into the final word, then the red dot is born.')}</div>
  <div><div class="animbox">{ANI['bar']}</div>{capt('Sweep','5 s loop','First the sketch; a sweep prints the letters over the process and the red dot lands last.')}</div>
 </div>
</div></div>

<div class="sx">{sh("04", "One mark per phase")}<div class="body">
 <p class="p">One state per phase of the service &mdash; Sketched for proposals and the brief, Stitched for development, BORN for production.</p>
 <div class="stagex">
  <div class="stagex__disp">
   <div class="sx2" data-s="sketch">{SVG['state_sketch']}</div>
   <div class="sx2" data-s="stitch">{SVG['state_stitch']}</div>
   <div class="sx2" data-s="born">{SVG['state_born']}</div>
  </div>
  <div class="stagex__chips">
   <button class="chip" data-s="sketch">01 Sketched</button>
   <button class="chip" data-s="stitch">02 Stitched</button>
   <button class="chip chip--r" data-s="born">03 BORN</button>
   <span class="chip__auto" data-auto>Auto</span>
  </div>
 </div>
</div></div>

<div class="sx">{sh("05", "The icon: the B")}<div class="body">
 <div class="hg hg--4">
  <div>{stage(SVG['ic_negativo'],'stage--sq')}{capt('Negative','Primary','Favicon, avatar, app, seal.')}</div>
  <div>{stage(SVG['ic_construccion'],'stage--sq')}{capt('Construction','Development','Tech packs, work in progress.')}</div>
  <div>{stage(SVG['ic_doble'],'stage--sq')}{capt('Double exposure','Alternate','Solid B with its process-ghost.')}</div>
  <div>{stage(SVG['ic_doble_red'],'stage--sq')}{capt('Red','BORN stage','For the BORN stage and highlights.')}</div>
 </div>
</div></div>

<div class="sx">{sh("06", "On paper, on ink, on red")}<div class="body">
 <p class="p">In negative the word turns ivory; the dot stays red on ink and becomes ink on red to keep contrast.</p>
 <div class="tri">
  <div>{stage(SVG['wm_principal'])}<p class="bgnote">Positive &middot; on Paper</p></div>
  <div>{stage(SVG['wm_principal_neg'],'stage--dark')}<p class="bgnote">Negative &middot; on Ink</p></div>
  <div>{stage(SVG['wm_principal_onred'],'stage--red')}<p class="bgnote">On Rojo Valentino</p></div>
 </div>
 <div class="tri" style="margin-top:1.4rem">
  <div>{stage(SVG['wm_solo'])}<p class="bgnote">Wordmark &middot; on Paper</p></div>
  <div>{stage(SVG['wm_solo_neg'],'stage--dark')}<p class="bgnote">Wordmark &middot; on Ink</p></div>
  <div>{stage(SVG['wm_solo_onred'],'stage--red')}<p class="bgnote">Wordmark &middot; on red</p></div>
 </div>
</div></div>

<div class="sx">{sh("07", "Variants")}<div class="body">
 <div class="hg hg--2">
  <div>{stage(SVG['wm_sin_slogan'])}{capt('No tagline','Black + dot','The primary without the tagline.')}</div>
  <div>{stage(SVG['wm_solo'])}{capt('Wordmark only','Reduced','Most discreet: word and dot only.')}</div>
  <div>{stage(SVG['wm_ecorojo_slogan'])}{capt('Red echo + tagline','Red lines','Process-ghost in red, with tagline.')}</div>
  <div>{stage(SVG['wm_ecorojo'])}{capt('Red echo','Red lines','Process in red, no tagline.')}</div>
 </div>
</div></div>

<div class="sx">{sh("08", "Never")}<div class="body">
 <ol class="nolist">
  <li><span class="k">&times; 01</span>Distort or change the proportions</li>
  <li><span class="k">&times; 02</span>Rotate the lockup</li>
  <li><span class="k">&times; 03</span>Recolor the word &mdash; only the dot is red</li>
  <li><span class="k">&times; 04</span>Crowd the logo &mdash; keep clear space around it</li>
  <li><span class="k">&times; 05</span>Use a stage mark outside its phase</li>
  <li><span class="k">&times; 06</span>Set the logo as words in running text &mdash; write Born Apparel Studio</li>
 </ol>
</div></div>
</section>"""

# ------------------------------------------------------------------ 03 COLOR
SW = [("Paper", "#F1F1EC", "The page", "var(--ink)", 150, True),
      ("Graphite 40", "#ABABB0", "Development &middot; rules", "var(--ink)", 76, False),
      ("Graphite 60", "#78787E", "Development &middot; secondary text", "var(--paper)", 76, False),
      ("Graphite 80", "#3C3C40", "Development &middot; secondary text", "var(--paper)", 76, False),
      ("Ink", "#151517", "Text &middot; dark pages", "var(--paper)", 150, False),
      ("Rojo Valentino", "#C4122E", "Pantone 3546 C &middot; only where it is earned", "var(--paper)", 230, False)]
sw_html = "".join(
    f'<button class="sw swr{" swr--b" if b else ""}" type="button" data-hex="{h}" style="--c:{h};--t:{t};--h:{ht}px">'
    f'<b>{n}</b><span class="role">{r}</span><span class="hex">{h}</span></button>' for n, h, r, t, ht, b in SW)
color = f"""
<section class="panel" id="p-color" role="tabpanel" aria-labelledby="t-color">
{opener("03", "From black &amp; white to black, white and bold", "A sketch begins in pencil. A single red is earned on reaching BORN.", "red", "g_born_paper")}

<div class="sx">{sh("01", "The palette")}<div class="body">
 <div class="swl">{sw_html}</div>
 <p class="note">Tap a color to copy its hex. For print, use Pantone 3546 C directly.</p>
</div></div>

<div class="sx">{sh("02", "Red is earned")}<div class="body">
 <p class="lead">Rojo Valentino is the only color in the system, and it appears only <em>where something is born.</em></p>
 <ol class="nolist nolist--ok">
  <li><span class="k">01</span>The dot of the logo</li>
  <li><span class="k">02</span>Covers and closing pages</li>
  <li><span class="k">03</span>The BORN stage: pre-production sample, size set, bulk</li>
  <li><span class="k">04</span>The one decision that matters on a page &mdash; the recommended factory, an out-of-tolerance measurement, the active milestone, the balance due</li>
 </ol>
 <p class="p" style="margin-top:1.6rem">Totals stay in ink: a big red total reads as debt. Never add red anywhere else.</p>
</div></div>
</section>"""

# ------------------------------------------------------------------ 04 TYPE
def fdl(fam): return f'<a class="fontdl" href="https://fonts.google.com/download?family={fam}" target="_blank" rel="noopener">Google Fonts &#8599;</a>'
typo = f"""
<section class="panel" id="p-type" role="tabpanel" aria-labelledby="t-type">
{opener("04", "Three voices, one wordmark", "Bodoni speaks, Jost reads, Space Mono measures.", "paper", "g_sketch_ink")}

<div class="band bleed"><div class="inr">
 <div class="sh sh--d"><span class="k">01</span><h2>The families<i>.</i></h2></div>
 <div class="spec"><div class="spec-head"><span class="meta">Wordmark &middot; GFS Didot &middot; the word BORN only</span>{fdl('GFS%20Didot')}</div><div class="samp" style="font-family:var(--word);font-size:clamp(3.4rem,11vw,8rem);line-height:1">BORN<span class="r">.</span></div></div>
 <div class="spec"><div class="spec-head"><span class="meta">Voice &middot; Bodoni Moda &middot; headlines, quotes, big figures</span>{fdl('Bodoni%20Moda')}</div><div class="samp" style="font-family:var(--disp);font-weight:500;font-size:clamp(2.2rem,6vw,4.6rem);line-height:1">Sketched. Stitched. BORN.</div><div class="samp" style="font-family:var(--ital);font-size:clamp(1.3rem,2.6vw,2rem);margin-top:.4rem">From idea to life.</div></div>
 <div class="spec"><div class="spec-head"><span class="meta">Reading &middot; Jost &middot; body text and labels</span>{fdl('Jost')}</div><div class="samp" style="font-family:var(--sans);font-size:clamp(1.15rem,2.2vw,1.6rem);line-height:1.45;max-width:34ch">The studio where a fashion idea matures until it becomes a manufacturable product.</div></div>
 <div class="spec"><div class="spec-head"><span class="meta">Technical data &middot; Space Mono &middot; codes, dates, measurements</span>{fdl('Space%20Mono')}</div><div class="samp" style="font-family:var(--mono);font-size:clamp(.9rem,1.8vw,1.15rem);letter-spacing:.05em">PHASE 01 &middot; SKETCHED &middot; TECH PACK v1 &middot; 1&ndash;3 WEEKS</div></div>
</div></div>

<div class="sx">{sh("02", "One job each")}<div class="body">
 <dl class="lg">
  <dt>Bodoni Moda</dt><dd>Headlines, quotes, big figures, names</dd>
  <dt>Jost</dt><dd>Body text and labels &middot; labels never under 7.5&nbsp;pt</dd>
  <dt>Space Mono</dt><dd>Codes, dates, weeks, measurements, references &middot; never sentences</dd>
  <dt>GFS Didot</dt><dd>The word BORN, nothing else</dd>
 </dl>
 <p class="note">All four families are free and open source (SIL Open Font License) and come in the brand kit under Downloads. GFS Didot is the free revival used for the wordmark; Vogue&rsquo;s Didot is proprietary &mdash; if the licensed file is available, it substitutes 1:1.</p>
</div></div>
</section>"""

# ------------------------------------------------------------------ 05 APPS
apps = f"""
<section class="panel" id="p-apps" role="tabpanel" aria-labelledby="t-apps">
{opener("05", "The identity evolves with the service", "The brief speaks in sketch, development in stitch, production in solid with color.", "ink", "g_born_paper")}

<div class="sx">{sh("01", "Three phases, three states")}<div class="body">
 <div class="cols cols--3 phases">
  <div><span class="k">Phase 01</span><div class="ph">{SVG['state_sketch']}</div><h3>Sketched</h3><p>Sketch grid, pencil outline, graphite. Everything is drawn.</p><p class="lab">Proposals &middot; brief &middot; moodboard &middot; tech pack</p></div>
  <div><span class="k">Phase 02</span><div class="ph">{SVG['state_stitch']}</div><h3>Stitched</h3><p>Topstitch, thread. The idea is tested and sewn.</p><p class="lab">Sample tag &middot; fitting &middot; development</p></div>
  <div class="rd"><span class="k">Phase 03</span><div class="ph">{SVG['state_born']}</div><h3>BORN</h3><p>Solid, in color. The product goes out into the world.</p><p class="lab">Hangtag &middot; drop &middot; campaign</p></div>
 </div>
</div></div>

<div class="sx">{sh("02", "The journey, measured")}<div class="body">
 {tape_timeline()}
 <div class="cols cols--3" style="margin-top:2rem;border-top:0">
  <div><ul class="rows"><li>Discovery and the three filters</li><li>Edited moodboard</li><li>Production-ready tech pack</li></ul></div>
  <div><ul class="rows"><li>Factory pairing and contract</li><li>Sample and documented fitting</li><li>Final approved sample</li></ul></div>
  <div><ul class="rows"><li>Size set and signed PPS</li><li>Order and bulk oversight</li><li>Documented handover</li></ul></div>
 </div>
</div></div>

<div class="sx">{sh("03", "The icon per stage")}<div class="body">
 <div class="hg hg--4">
  <div>{stage(SVG['ic_construccion'],'stage--sq')}<p class="bgnote">Sketched &middot; construction</p></div>
  <div>{stage(SVG['ic_doble'],'stage--sq')}<p class="bgnote">Stitched &middot; double exposure</p></div>
  <div>{stage(SVG['ic_doble_red'],'stage--sq')}<p class="bgnote">BORN &middot; red</p></div>
  <div>{stage(SVG['ic_negativo'],'stage--sq stage--dark')}<p class="bgnote">Seal &middot; negative</p></div>
 </div>
 <p class="note">Templates, manuals and client documents built on this system live in the studio&rsquo;s shared Drive.</p>
</div></div>

<div class="fullred">
 <p class="fr-k">The seal</p>
 <h2>Everything is made to be BORN<span class="dk">.</span></h2>
 <p class="fr-s">Sketched to be BORN &middot; Stitched to be BORN &middot; Made to be BORN</p>
</div>
</section>"""

# ------------------------------------------------------------------ 06 DOWNLOADS
def ki_png(key):
    bg = ""
    if key in {"wm_principal_neg", "wm_solo_neg"}: bg = ' style="background:var(--ink)"'
    elif key in {"wm_principal_onred"}: bg = ' style="background:var(--red)"'
    return (f'<div class="ki"><div class="ki__p"{bg}>{SVG[key]}</div>'
            f'<div class="ki__m"><b>{TITLE[key]}</b><span class="ki__f">PNG &middot; transparent</span>'
            f'<div class="dls"><a class="dl" href="{PNG[key]}" download="{DL[key]}">PNG</a>'
            f'<a class="dl dl--ghost" data-open="1" title="Open in a new tab">Open</a></div></div></div>')
def ki_vid(pref, title, dlm, dlw, anim):
    return (f'<div class="ki"><div class="ki__p">{anim}</div>'
            f'<div class="ki__m"><b>{title}</b><span class="ki__f">MP4 + WebM &middot; loop</span>'
            f'<div class="dls"><a class="dl" data-dl="{pref}_mp4" download="{dlm}">MP4</a>'
            f'<a class="dl" data-dl="{pref}_webm" download="{dlw}">WebM</a>'
            f'<a class="dl dl--ghost" data-open="1" title="Open in a new tab">Open</a></div></div></div>')
kit_items = "".join(ki_png(k) for k, _, _ in KIT)
kit_items += ki_vid("ens", "Assembly animation", "BORN-assembly.mp4", "BORN-assembly.webm", ANI['ens'])
kit_items += ki_vid("bar", "Sweep animation", "BORN-sweep.mp4", "BORN-sweep.webm", ANI['bar'])
def _kb(p):
    n = os.path.getsize(p); return f"{n/1048576:.1f} MB" if n > 1048576 else f"{round(n/1024)} KB"
FILES = [
 ("BORN-Brand-Kit.zip", "Complete brand kit", "Every logo in PNG and vector SVG, the two animated signatures and the brand typefaces, in one folder.", "ZIP", True),
 ("BORN-Logos-SVG.zip", "Vector logos", "Primary logo, stage marks and icons as SVG. For print, embroidery, signage and any size.", "ZIP &middot; SVG", False),
 ("BORN-Fonts.zip", "Brand typefaces", "Bodoni Moda, Jost, Space Mono and GFS Didot. Install before opening design files.", "ZIP &middot; TTF &middot; Open Font License", False),
]
files = "".join(
    f'<div class="fl__r{" fl__r--main" if m else ""}"><span class="k">0{i}</span><div><b>{ti}</b><p>{tx}</p><span class="ki__f">{fm} &middot; {_kb("downloads/"+fn)}</span></div>'
    f'<div class="dls"><a class="dl{" dl--big" if m else ""}" href="downloads/{fn}" download="{fn}">Download</a></div></div>'
    for i, (fn, ti, tx, fm, m) in enumerate(FILES, 1))
desc = f"""
<section class="panel" id="p-desc" role="tabpanel" aria-labelledby="t-desc">
{opener("06", "Brand kit", "The public brand, in one place.", "paper", None,
        '<div class="op__tape">' + tape_svg() + '</div>')}

<div class="sx">{sh("01", "Start here")}<div class="body">
 <div class="fl">{files}</div>
 <p class="note">Templates, manuals and client deliverables are working files. They live in the studio&rsquo;s shared Drive, not on this public page.</p>
</div></div>

<div class="sx">{sh("02", "One by one")}<div class="body">
 <div class="kit">{kit_items}</div>
 <p class="note">High-resolution PNG (2700&ndash;4800&nbsp;px), transparent background. Animations as MP4 (universal) and WebM. If your browser blocks a download, Open shows the file in a new tab to save by hand.</p>
</div></div>
</section>"""

# ------------------------------------------------------------------ footer
FOOTER = f"""
<footer class="foot bleed"><div class="inr">
 <p class="lab k">From idea to life</p>
 <p class="foot__claim">Every BORN begins as a sketch<i>.</i></p>
 <p class="fcredit">Born Apparel Studio &middot; Full Service Apparel Development<br>Brand Book &middot; Final edition, October 2026<br>Strategy &amp; brand &mdash; Matisis Consultancy</p>
</div><div class="op__giant" aria-hidden="true">{GIANT['g_born_paper']}</div></footer>"""

# ------------------------------------------------------------------ visual layer
CSS += FACES + r"""
/* ===================== FINAL EDITION · the brand's document language ===================== */
:root{--paper:#F1F1EC;--paper-2:#E8E8E2;--paper-3:#DCDCD5;--ink:#151517;--dark:#151517;--dark-2:#1F1F22;
  --g2:#3A3A3F;--g3:#5B5B61;--g4:#ABABB0;--line:rgba(21,21,23,.16);--line-d:rgba(241,241,236,.22);
  --disp:'Bodoni5','Bodoni6','Times New Roman',serif;--ital:'BodoniI','Bodoni6','Times New Roman',serif;
  --gut:clamp(1.25rem,5vw,3rem);--idx:clamp(2.6rem,7vw,6.5rem)}
body{background:var(--paper);color:var(--ink)}
::selection{background:var(--ink);color:var(--paper)}
.wrap{max-width:1180px;padding-left:max(var(--gut),env(safe-area-inset-left,0px));padding-right:max(var(--gut),env(safe-area-inset-right,0px))}
.panel{padding:0 0 clamp(4rem,10vw,7rem)}
.r{color:var(--red)}
/* full bleed + inner measure */
.bleed{position:relative;margin-left:calc(50% - 50vw);margin-right:calc(50% - 50vw);width:100vw}
.inr{max-width:1180px;margin:0 auto;padding-left:max(var(--gut),env(safe-area-inset-left,0px));padding-right:max(var(--gut),env(safe-area-inset-right,0px))}
/* header: one navigation layer, ink rule */
.top{background:var(--paper);backdrop-filter:none;border-bottom:1px solid var(--ink)}
.top__in{max-width:1180px;padding-top:.7rem;padding-bottom:.7rem;padding-left:max(var(--gut),env(safe-area-inset-left,0px));padding-right:max(var(--gut),env(safe-area-inset-right,0px))}
.brand svg{height:26px}
.tab{font-family:var(--sans7);font-size:.68rem;letter-spacing:.16em;color:var(--g3);border-radius:0;padding:.55rem .7rem}
.tab:hover{background:none;color:var(--ink)}
.tab[aria-selected=true],.tab[aria-selected=true]:hover{background:none;color:var(--ink);box-shadow:inset 0 -2px 0 var(--red)}
.bar{height:1px}
.rdot{display:none!important}
.lab{font-family:var(--sans7);font-size:.7rem;letter-spacing:.16em;text-transform:uppercase;color:var(--g3);line-height:1.5}
.lab.k,.k{color:var(--red)}
.k{font-family:var(--mono);font-size:.74rem;letter-spacing:.06em}
.lab.k{font-family:var(--sans7)}
/* chapter opener */
.op{overflow:hidden;display:flex;flex-direction:column;min-height:clamp(560px,86vh,900px)}
.op--paper{background:var(--paper);color:var(--ink)}
.op--ink{background:var(--ink);color:var(--paper)}
.op--red{background:var(--red);color:var(--paper)}
.op__in{position:relative;z-index:2;width:100%;padding-top:clamp(1.4rem,3.5vw,2.4rem)}
.op__top{display:flex;justify-content:space-between;gap:.6rem 1.4rem;flex-wrap:wrap}
.op--ink .lab,.op--red .lab{color:rgba(241,241,236,.7)}
.op--ink .lab.k{color:var(--red)} .op--red .lab.k{color:var(--paper)}
.op__h{font-family:var(--disp);font-weight:500;font-size:clamp(3.1rem,10vw,9rem);line-height:.92;letter-spacing:-.03em;margin-top:clamp(1.8rem,6vw,4rem);max-width:13ch;text-wrap:balance}
.op__h i{font-style:normal;color:var(--red)}
.op--red .op__h i{color:var(--ink)}
.op__sub{font-family:var(--ital);font-size:clamp(1.25rem,2.6vw,2.05rem);line-height:1.22;margin-top:clamp(.9rem,2vw,1.4rem);max-width:32ch;opacity:.92}
.op__giant{position:relative;z-index:1;margin-top:auto;padding-top:clamp(2rem,6vw,4rem);margin-left:-3vw;width:108vw;margin-bottom:-9.5vw;pointer-events:none}
.op__giant svg{width:100%;height:auto;display:block}
.toc{display:grid;grid-template-columns:repeat(6,minmax(0,1fr));margin-top:clamp(2rem,5vw,3.4rem);border-top:1px solid var(--ink)}
.toc a{display:block;text-decoration:none;padding:.75rem .8rem .2rem 0;font-family:var(--disp);font-weight:500;font-size:clamp(1rem,1.5vw,1.25rem);color:var(--ink);transition:color .2s}
.toc a+a{padding-left:.8rem;border-left:1px solid var(--line)}
.toc a:hover{color:var(--red)}
.toc .k{display:block;margin-bottom:.15rem}
.replaybtn{margin-top:1.4rem;border-radius:0;border:0;border-bottom:1px solid currentColor;padding:.3rem 0;font-family:var(--sans7);font-size:.68rem;letter-spacing:.16em}
.replaybtn:hover{background:none;color:var(--red);border-color:var(--red)}
.op__tape{margin-top:clamp(3rem,10vw,7rem);margin-bottom:clamp(2rem,5vw,3rem)}
/* section rhythm */
.sx{padding-top:clamp(3.6rem,9vw,6.4rem)}
.sh{display:grid;grid-template-columns:var(--idx) minmax(0,1fr);gap:0 1rem;align-items:baseline;border-top:1px solid var(--ink);padding-top:1rem}
.sh .k{font-size:.8rem}
.sh h2{font-family:var(--disp);font-weight:500;font-size:clamp(2rem,4.8vw,3.7rem);line-height:1;letter-spacing:-.02em;text-wrap:balance}
.sh h2 i{font-style:normal;color:var(--red)}
.sh--d{border-color:var(--line-d)}
.body{margin-left:calc(var(--idx) + 1rem);margin-top:clamp(1.5rem,3.4vw,2.6rem);min-width:0}
.p{font-size:clamp(1.02rem,1.25vw,1.14rem);line-height:1.68;color:var(--g2);max-width:62ch}
.p+.p{margin-top:.9rem}
.p b{color:var(--ink);font-weight:500;font-family:var(--sans7)}
.p--d{color:rgba(241,241,236,.74)} .p--d b{color:var(--paper)}
.lead{font-family:var(--disp);font-weight:500;font-size:clamp(1.5rem,3.1vw,2.45rem);line-height:1.16;letter-spacing:-.01em;color:var(--ink);max-width:24ch;text-wrap:balance;margin-bottom:clamp(1.6rem,3.4vw,2.4rem)}
.lead em,.lg em{font-family:var(--ital);font-style:normal}
.note{font-family:var(--sans);font-size:.86rem;letter-spacing:0;color:var(--g3);line-height:1.6;margin-top:1.4rem;max-width:70ch}
/* ledger */
.lg{display:grid;grid-template-columns:minmax(8rem,15rem) minmax(0,1fr);border-bottom:1px solid var(--line)}
.lg dt,.lg dd{border-top:1px solid var(--line);padding:.8rem 0}
.lg dt:first-of-type,.lg dt:first-of-type+dd{border-top-color:var(--ink)}
.lg dt{font-family:var(--sans7);font-size:.7rem;letter-spacing:.15em;text-transform:uppercase;color:var(--g3);padding-right:1rem;display:flex;align-items:center}
.lg dd{font-family:var(--disp);font-weight:500;font-size:clamp(1.15rem,2.1vw,1.65rem);line-height:1.2;color:var(--ink)}
.lg dd small{font-family:var(--sans);font-size:.85rem;color:var(--g3);margin-left:.6rem;letter-spacing:.02em}
.lg--sm dd{font-size:clamp(1.05rem,1.7vw,1.3rem)}
@media(max-width:600px){.lg{grid-template-columns:minmax(0,1fr)}.lg dt{padding-bottom:.2rem}.lg dd{border-top:0;padding-top:0}.lg dt:first-of-type+dd{border-top:0}}
.nope span{text-decoration:line-through;text-decoration-color:var(--red);text-decoration-thickness:2px}
/* columns */
.cols{display:grid;grid-template-columns:repeat(var(--n,3),minmax(0,1fr));border-top:1px solid var(--ink)}
.cols--2{--n:2}.cols--3{--n:3}.cols--4{--n:4}
.cols>div{padding:1.1rem 1.4rem 0 0;min-width:0}
.cols>div+div{padding-left:1.4rem;border-left:1px solid var(--line)}
.cols>div.rd{box-shadow:inset 0 3px 0 var(--red)}
.cols h3{font-family:var(--disp);font-weight:500;font-size:clamp(1.45rem,2.6vw,2.1rem);line-height:1.05;letter-spacing:-.01em;margin-top:.55rem;color:var(--ink)}
.cols p{font-size:.98rem;line-height:1.55;color:var(--g2);margin-top:.55rem}
.cols .q{font-family:var(--ital);font-size:clamp(1.1rem,1.6vw,1.3rem);line-height:1.3;color:var(--ink)}
.cols--big h3{font-size:clamp(2.2rem,5vw,4rem);line-height:.95}
.cols--d{border-top-color:var(--line-d);margin-top:clamp(2.4rem,6vw,4rem)}
.cols--d>div+div{border-left-color:var(--line-d)}
.cols--d h3{color:var(--paper)} .cols--d p{color:rgba(241,241,236,.68)}
@media(max-width:900px){.cols--4{--n:2}.cols--4>div:nth-child(3){padding-left:0;border-left:0}.cols--4>div:nth-child(n+3){margin-top:1.4rem;border-top:1px solid var(--line)}.cols--d>div:nth-child(n+3){border-top-color:var(--line-d)}}
@media(max-width:700px){.cols,.cols--4{--n:1}.cols>div,.cols>div+div{padding:1.1rem 0 1.2rem;border-left:0;margin-top:0}.cols>div+div{border-top:1px solid var(--line)}.cols--d>div+div{border-top-color:var(--line-d)}}
/* origin split */
.ins{display:grid;grid-template-columns:minmax(0,1.05fr) minmax(0,1fr);gap:clamp(1.6rem,5vw,4rem);align-items:start}
.ins .lead{margin:0}
@media(max-width:820px){.ins{grid-template-columns:1fr}}
/* is / is not */
.split{display:grid;grid-template-columns:1fr 1fr}
.split>div{padding:clamp(1.3rem,3vw,2.2rem)}
.split .pa{background:var(--paper-2)}
.split .ik{background:var(--ink);color:var(--paper)}
.split .ik .lab{color:var(--red)}
.split ul{list-style:none;margin-top:1rem}
.split li{font-family:var(--disp);font-weight:500;font-size:clamp(1.1rem,1.8vw,1.4rem);line-height:1.3;padding:.75rem 0;border-top:1px solid var(--line)}
.split .ik li{border-color:var(--line-d);font-family:var(--sans);font-size:1rem;color:rgba(241,241,236,.72)}
.split .ik li b{display:block;font-family:var(--disp);font-weight:500;font-size:clamp(1.1rem,1.8vw,1.4rem);color:var(--paper);margin-bottom:.1rem}
@media(max-width:760px){.split{grid-template-columns:1fr}}
/* ink band */
.band{background:var(--ink);color:var(--paper);margin-top:clamp(3.6rem,9vw,6.4rem);padding-block:clamp(2.4rem,6vw,4rem) clamp(3.4rem,8vw,5.6rem)}
.band .sh h2{color:var(--paper)}
.claim{font-family:var(--disp);font-weight:500;font-size:clamp(3rem,9.5vw,8rem);line-height:.92;letter-spacing:-.03em;margin-top:clamp(2rem,5vw,3.4rem);text-wrap:balance}
.claim i{font-style:normal;color:var(--red)}
.tagl{font-family:var(--ital);font-size:clamp(1.3rem,2.8vw,2.1rem);color:rgba(241,241,236,.8);margin-top:.9rem}
.tone{display:flex;justify-content:space-between;flex-wrap:wrap;gap:.6rem 1.4rem;margin-top:2rem;padding:1rem 0;border-top:1px solid var(--ink);border-bottom:1px solid var(--ink)}
.tone span{font-family:var(--disp);font-weight:500;font-size:clamp(1.15rem,2.2vw,1.7rem)}
.nope--list{display:flex;flex-wrap:wrap;gap:.5rem 1.1rem;align-items:baseline;margin-top:1.6rem;font-size:1rem;color:var(--g2)}
.nope--list .lab{text-decoration:none;color:var(--g3);margin-right:.4rem}
/* red manifesto band */
.fullred{text-align:left;padding:clamp(3.4rem,10vw,7rem) max(var(--gut),calc((100vw - var(--max))/2 + var(--gut)))}
.fullred .fr-k{font-family:var(--sans7);font-size:.7rem;letter-spacing:.16em;opacity:.8}
.fullred h2{font-family:var(--disp);font-weight:500;font-size:clamp(3.2rem,11vw,9.6rem);line-height:.9;letter-spacing:-.03em;max-width:12ch}
.fullred h2 .dk{color:var(--ink)}
.fullred h2 .op{color:inherit}
.fullred .bigdot{display:none}
.fullred p.fr-s{font-family:var(--mono);letter-spacing:.1em;margin-top:1.8rem}
/* logo sheet */
.sheet{position:relative;border:1px solid var(--ink);background:var(--paper);padding:clamp(2.2rem,7vw,5rem) clamp(1.2rem,7vw,6rem) clamp(1.4rem,3.5vw,2.4rem)}
.sheet__art svg{width:100%;height:auto}
.cm{position:absolute;width:18px;height:18px;border-color:var(--ink);border-style:solid;border-width:0}
.cm.tl{top:-10px;left:-10px;border-top-width:1px;border-left-width:1px}
.cm.tr{top:-10px;right:-10px;border-top-width:1px;border-right-width:1px}
.cm.bl{bottom:-10px;left:-10px;border-bottom-width:1px;border-left-width:1px}
.cm.br{bottom:-10px;right:-10px;border-bottom-width:1px;border-right-width:1px}
.dim{display:flex;align-items:center;gap:.9rem;margin-top:clamp(1.4rem,3vw,2.2rem);height:18px;border-left:1px solid var(--ink);border-right:1px solid var(--ink);font-family:var(--mono);font-size:.7rem;letter-spacing:.12em;color:var(--g3)}
.dim::before,.dim::after{content:"";flex:1;height:1px;background:var(--ink)}
.tb{display:grid;grid-template-columns:1.3fr 1fr 1.6fr .5fr;border:1px solid var(--ink);border-top:0}
.tb>div{padding:.7rem .9rem;display:flex;flex-direction:column;justify-content:space-between;gap:.3rem;min-width:0}
.tb>div+div{border-left:1px solid var(--ink)}
.tb .lab{font-size:.62rem}
.tb .wm{font-family:var(--word);font-size:1.3rem;letter-spacing:.03em}.tb .wm b{font-weight:400;color:var(--red)}
.tb .mono{font-family:var(--mono);font-size:.82rem}
@media(max-width:700px){.tb{grid-template-columns:1fr 1fr}.tb>div:nth-child(3){border-left:0}.tb>div:nth-child(n+3){border-top:1px solid var(--ink)}}
.concept{padding:clamp(1rem,4vw,2.6rem) clamp(0rem,6vw,5rem)}
.concept svg{width:100%;height:auto}
.letters .L{display:block;font-family:var(--word);font-size:clamp(2.6rem,6vw,4.4rem);line-height:1;color:var(--ink)}
.letters .rd .L{color:var(--red)}
.letters .k{display:block;margin-top:.5rem}
/* stages, boxes: square, hairline */
.stage{border-radius:0;border:1px solid var(--line);background:var(--paper);transition:none}
.stage:hover{transform:none}
.stage--dark{background:var(--ink);border-color:var(--ink)}
.stage--red{background:var(--red);border-color:var(--red)}
.capt b{font-family:var(--disp);font-weight:500;font-size:1.25rem}
.capt span,.bgnote{font-family:var(--sans7);font-size:.64rem;letter-spacing:.15em;color:var(--g3)}
.capt p{font-size:.92rem}
.motion{gap:clamp(1rem,3vw,2rem)}
.animbox{border-radius:0;border:1px solid var(--line);background:var(--paper)}
.tri{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:0}
.tri .stage{aspect-ratio:16/10;border:0;padding:clamp(1rem,3vw,2rem)}
.tri>div:first-child .stage{border:1px solid var(--line);border-right:0}
@media(max-width:700px){.tri{grid-template-columns:1fr}.tri>div:first-child .stage{border-right:1px solid var(--line)}}
.hg{display:grid;gap:clamp(1rem,2.4vw,1.6rem)}
.hg--4{grid-template-columns:repeat(4,minmax(0,1fr))}.hg--2{grid-template-columns:repeat(2,minmax(0,1fr))}
@media(max-width:820px){.hg--4{grid-template-columns:repeat(2,minmax(0,1fr))}}
@media(max-width:560px){.hg--2{grid-template-columns:1fr}}
.stagex{border-radius:0;border:1px solid var(--ink);background:var(--paper)}
.stagex__disp .sx2{grid-area:1/1;width:min(700px,90%);opacity:0;transform:scale(.985);transition:opacity .5s var(--ease),transform .5s var(--ease)}
.stagex__disp .sx2.on{opacity:1;transform:none}
.stagex__disp .sx2 svg{width:100%;height:auto}
.stagex__chips{gap:0 1.6rem;padding:0 clamp(1rem,3vw,1.6rem);border-top:1px solid var(--ink)}
.chip{border:0;border-radius:0;background:none;padding:1rem 0;font-family:var(--sans7);font-size:.7rem;letter-spacing:.15em;color:var(--g3)}
.chip:hover{color:var(--ink);border:0}
.chip[aria-pressed=true]{background:none;color:var(--ink);box-shadow:inset 0 -2px 0 var(--ink)}
.chip--r[aria-pressed=true]{color:var(--red);box-shadow:inset 0 -2px 0 var(--red)}
.chip__auto{font-family:var(--sans7);font-size:.62rem;letter-spacing:.15em}
.nolist{list-style:none;border-top:1px solid var(--ink);border-bottom:1px solid var(--line)}
.nolist li{display:grid;grid-template-columns:4.2rem minmax(0,1fr);align-items:baseline;padding:.85rem 0;border-top:1px solid var(--line);font-family:var(--disp);font-weight:500;font-size:clamp(1.1rem,2vw,1.5rem);line-height:1.25}
.nolist li:first-child{border-top:0}
/* palette */
.swl{display:flex;flex-direction:column;border-radius:0}
.swr{display:grid;grid-template-columns:minmax(0,1.1fr) minmax(0,1.6fr) auto;align-items:end;gap:.4rem 1.2rem;min-height:var(--h);width:100%;padding:1rem clamp(1rem,2.4vw,1.6rem);background:var(--c);color:var(--t);border:0;border-radius:0;text-align:left;cursor:pointer;font:inherit;transition:padding .25s var(--ease)}
.swr:hover{transform:none;padding-left:clamp(1.4rem,3vw,2.2rem)}
.swr--b{border:1px solid var(--line);border-bottom:0}
.swr b{font-family:var(--sans7);font-weight:500;font-size:.78rem;letter-spacing:.16em;text-transform:uppercase}
.swr .role{font-size:.92rem;opacity:.85}
.swr .hex{font-family:var(--mono);font-size:.86rem}
@media(max-width:600px){.swr{grid-template-columns:1fr auto}.swr .role{display:none}}
/* type specimens on ink */
.band .spec{border-top:1px solid var(--line-d);padding:clamp(1.4rem,3vw,2.2rem) 0;margin-top:0}
.band .spec:first-of-type{margin-top:clamp(1.4rem,3vw,2rem)}
.band .spec .meta{font-family:var(--sans7);font-size:.68rem;letter-spacing:.15em;color:rgba(241,241,236,.62)}
.band .spec .samp{color:var(--paper)}
.fontdl{background:none;border:1px solid var(--line-d);border-radius:0;color:rgba(241,241,236,.8);font-family:var(--sans7);font-size:.62rem;letter-spacing:.14em}
.fontdl:hover{background:var(--paper);color:var(--ink)}
/* applications */
.phases .ph{padding:clamp(1.2rem,3vw,2rem) 0}
.phases .ph{height:clamp(84px,9vw,130px);display:flex;align-items:center;padding:0;margin:1rem 0}
.phases .ph svg{width:100%;height:100%}
.cols p.lab{font-size:.66rem;line-height:1.6;color:var(--g3);margin-top:1rem}
.tl__lab{display:grid;grid-template-columns:1fr 2fr 1fr;border-top:1px solid var(--ink)}
.tl__lab>div{padding:.9rem 1rem 1rem 0}
.tl__lab>div+div{padding-left:1rem;border-left:1px solid var(--line)}
.tl__lab b{display:block;font-family:var(--disp);font-weight:500;font-size:clamp(1.4rem,2.8vw,2.3rem);line-height:1;margin-top:.4rem}
.tl__lab .rd b{color:var(--red)}
.tl__lab p{font-family:var(--ital);font-size:1.05rem;color:var(--g2);margin-top:.25rem}
.tape{display:block;width:100%;height:clamp(56px,7vw,96px);border-top:1px solid var(--ink);border-bottom:1px solid var(--ink)}
.tl__n{position:relative;height:1.6rem;margin-top:.35rem}
.tl__n span{position:absolute;transform:translateX(-50%);font-family:var(--mono);font-size:.7rem;color:var(--g3)}
.tl__n span:first-child{transform:none}.tl__n span:last-child{transform:translateX(-100%)}
.tl__n span.r{color:var(--red)}
.rows{list-style:none}
.rows li{padding:.6rem 0;border-top:1px solid var(--line);font-size:1rem;color:var(--ink)}
.rows li:first-child{border-top:0}
@media(max-width:700px){.tl__lab{grid-template-columns:1fr}.tl__lab>div+div{padding-left:0;border-left:0;border-top:1px solid var(--line)}}
/* downloads */
.fl{border-top:1px solid var(--ink);margin-top:0}
.fl__r{grid-template-columns:var(--idx) minmax(0,1fr) auto;padding:1.3rem 0;align-items:center}
.fl__r .k{align-self:start;padding-top:.45rem}
.fl__r b{font-family:var(--disp);font-weight:500;font-size:clamp(1.4rem,2.6vw,2.1rem);line-height:1.05}
.fl__r--main b{font-size:clamp(1.8rem,4vw,3rem)}
.fl__r p{font-size:1rem;max-width:56ch}
@media(max-width:600px){.fl__r{grid-template-columns:2rem minmax(0,1fr)}.fl__r .dls{grid-column:2}}
.dl{border-radius:0;font-family:var(--sans7);font-size:.66rem;letter-spacing:.15em;padding:.7rem 1.1rem}
.dl--big{font-size:.72rem;padding:1rem 1.6rem;background:var(--red)}
.dl--big:hover{background:var(--ink)}
.dl--ghost{border-color:var(--line)}
.kit{gap:0;border-top:1px solid var(--line);border-left:1px solid var(--line)}
.ki{border-radius:0;border:0;border-right:1px solid var(--line);border-bottom:1px solid var(--line);background:var(--paper)}
.ki:hover{transform:none}
.ki__p{background:var(--paper-2)}
.ki__m b{font-family:var(--disp);font-weight:500;font-size:1.1rem}
.ki__f{font-family:var(--sans7);letter-spacing:.14em}
/* footer */
.foot{background:var(--ink);color:var(--paper);border:0;text-align:left;padding:clamp(3.4rem,9vw,6rem) 0 0;overflow:hidden;display:flex;flex-direction:column}
.foot .lab.k{color:var(--red)}
.foot__claim{font-family:var(--disp);font-weight:500;font-size:clamp(2.2rem,6.5vw,5.4rem);line-height:.95;letter-spacing:-.025em;margin-top:1rem;max-width:14ch}
.foot__claim i{font-style:normal;color:var(--red)}
.foot .fcredit{font-family:var(--mono);font-size:.72rem;letter-spacing:.06em;color:rgba(241,241,236,.6);line-height:1.9;margin-top:2rem}
.foot .op__giant{margin-bottom:-9.5vw}
.foot .inr{width:100%}
.panel:has(> .fullred:last-child){padding-bottom:0}
/* no decorative glow */
.hero::before{display:none}

/* ===================== ONE GRID · 12 columns, one rail, one content axis ===================== */
:root{--max:1320px;--cg:clamp(1rem,2.2vw,2rem)}
.wrap,.inr,.top__in{max-width:var(--max)}
.g12,.sx,.op__in,.band .inr,.fullred,.foot .inr{display:grid;grid-template-columns:repeat(12,minmax(0,1fr));column-gap:var(--cg)}
/* sections: index + title in the rail (cols 1-4), everything else on the content axis (cols 5-12) */
.sx{border-top:1px solid var(--ink);margin-top:clamp(4rem,9vw,7rem);padding-top:1.1rem}
.sh{display:block;border:0;padding:0}
.sx>.sh{grid-column:1/5;display:block;border:0;padding:0;position:sticky;top:4.6rem;align-self:start}
.sh .k{display:block;margin-bottom:.7rem}
.sh h2{font-size:clamp(1.55rem,2.5vw,2.35rem);line-height:1.06;letter-spacing:-.012em;max-width:12ch}
.sx>.body{grid-column:5/13;margin:0}
.lead{font-size:clamp(1.4rem,2.3vw,2.05rem);max-width:26ch;margin-bottom:clamp(1.4rem,3vw,2.2rem)}
.cols h3{font-size:clamp(1.25rem,1.8vw,1.6rem)}
.cols--big h3{font-size:clamp(1.9rem,3.6vw,3.1rem)}
.ins{grid-template-columns:1fr;gap:1.4rem}
.ins .lead{max-width:22ch}
.p{max-width:60ch}
/* opener on the same grid */
.op{min-height:0}
.op__in{padding-top:clamp(1.4rem,3vw,2.2rem);padding-bottom:0}
.op__top,.op__h,.toc,.op__tape{grid-column:1/13}
.op__h{max-width:none;font-size:clamp(3.2rem,8.6vw,8.4rem);margin-top:clamp(2.4rem,7vw,5rem)}
.op__sub{grid-column:5/13;max-width:30ch;margin-top:clamp(1rem,2.4vw,1.6rem)}
.replaybtn{grid-column:5/13;justify-self:start}
.toc{margin-top:clamp(2.4rem,6vw,4rem)}
.op__giant{padding-top:clamp(2.4rem,7vw,5rem)}
/* ink bands */
.band{margin-top:clamp(4rem,9vw,7rem);padding-block:1.1rem clamp(3.4rem,8vw,6rem)}
.band .inr{border-top:1px solid var(--line-d);padding-top:1.1rem}
.band .inr>.sh{grid-column:1/5;border:0;padding:0}
.band .claim,.band .tagl,.band .p--d,.band .spec{grid-column:5/13}
.band .claim{margin-top:0;font-size:clamp(2.8rem,6.6vw,6.2rem)}
.band .cols--d{grid-column:1/13}
.band .spec:first-of-type{margin-top:0;border-top:0;padding-top:0}
/* red manifesto + footer on the grid */
.fullred{padding-top:clamp(3.4rem,8vw,6rem);padding-bottom:clamp(4rem,10vw,7rem)}
.fullred .fr-k{grid-column:1/5;padding-top:.9rem}
.fullred h2,.fullred .fr-s{grid-column:5/13}
.fullred h2{font-size:clamp(3rem,8vw,7.6rem);max-width:none}
.foot .inr>.lab{grid-column:1/5;padding-top:.6rem}
.foot__claim,.foot .fcredit{grid-column:5/13}
.foot__claim{margin-top:0}
/* downloads: the rail carries the index */
.fl__r{grid-template-columns:minmax(0,1fr) auto}
.fl__r>.k{display:none}
.tl__lab{grid-template-columns:1fr 2fr 1fr}
/* the section rule is the only top rule: no double lines at the start of the content */
.sx>.body>:first-child{border-top:0}
.sx>.body>.lg:first-child>dt:first-of-type,.sx>.body>.lg:first-child>dt:first-of-type+dd{border-top:0;padding-top:0}
.sx>.body>.tl:first-child .tl__lab{border-top:0}
.sx>.body>.tl:first-child .tl__lab>div{padding-top:0}
.sx>.body>.fl:first-child>.fl__r:first-child{padding-top:0}
.sx>.body>.cols:first-child>div{padding-top:0}
.sx>.body>.cols:first-child>div.rd{box-shadow:none;position:relative}
.sx>.body>.cols:first-child>div.rd::before{content:"";position:absolute;left:0;right:0;top:calc(-1.1rem - 2px);height:3px;background:var(--red)}
/* tablet and phone: the rail stacks above the content */
@media(max-width:1000px){
 .sx>.sh,.sx>.body,.band .inr>.sh,.band .claim,.band .tagl,.band .p--d,.band .spec,.fullred .fr-k,.fullred h2,.fullred .fr-s,.foot .inr>.lab,.foot__claim,.foot .fcredit,.op__sub,.replaybtn{grid-column:1/13}
 .sx>.sh{position:static;margin-bottom:clamp(1.4rem,4vw,2rem)}
 .sh h2{max-width:20ch}
 .band .inr>.sh{margin-bottom:1.4rem}
 .foot__claim{margin-top:.8rem}
}
/* mobile */
@media(max-width:760px){
 .tabs{background:var(--paper);border-bottom:1px solid var(--ink);box-shadow:none}
 .tab{border-radius:0;font-size:.8rem}
 .tab[aria-selected=true]{box-shadow:inset 3px 0 0 var(--red)}
 .body{margin-left:0}
 .toc{grid-template-columns:repeat(3,minmax(0,1fr))}
 .toc a:nth-child(4){padding-left:0;border-left:0}
 .toc a:nth-child(n+4){border-top:1px solid var(--line)}
 .op{min-height:auto}
}
"""
