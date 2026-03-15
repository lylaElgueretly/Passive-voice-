import streamlit as st

# ── Page config ───────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Year 7 English – Passive Voice",
    page_icon="📰",
    layout="centered",
)

# ── CSS (matches HTML exactly) ────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700;900&family=Source+Serif+4:ital,wght@0,300;0,400;0,600;1,400&family=IBM+Plex+Mono:wght@400;600&display=swap');

.stApp {
    background: #2a1f14 !important;
    background-image:
        radial-gradient(ellipse at 20% 50%, rgba(200,57,43,0.08) 0%, transparent 60%),
        radial-gradient(ellipse at 80% 20%, rgba(37,99,168,0.08) 0%, transparent 60%) !important;
    font-family: 'Source Serif 4', Georgia, serif !important;
}
.block-container {
    background: transparent !important;
    padding-top: 2rem !important;
    padding-bottom: 2rem !important;
    max-width: 780px !important;
}
#MainMenu, footer, header { visibility: hidden !important; }

.stApp p, .stApp li, .stMarkdown p, .stMarkdown li {
    color: #2e2010 !important;
    font-family: 'Source Serif 4', Georgia, serif !important;
}
.stRadio > label, .stSelectbox > label, .stTextInput > label, .stTextArea > label {
    color: #2e2010 !important; font-family: 'IBM Plex Mono', monospace !important;
    font-size: 11px !important; letter-spacing: 0.1em !important; text-transform: uppercase !important;
}
.stRadio div[role="radiogroup"] label p,
.stRadio div[role="radiogroup"] label {
    color: #1a1008 !important;
    font-family: 'Source Serif 4', Georgia, serif !important;
    font-size: 15px !important;
}
.stSelectbox div[data-baseweb="select"] * { color: #1a1008 !important; }
.stSelectbox div[data-baseweb="select"] > div { background: white !important; }
.stTextInput input, .stTextArea textarea {
    background: white !important; color: #1a1008 !important;
    border: 2px solid #ddd !important; border-radius: 6px !important;
    font-family: 'Source Serif 4', Georgia, serif !important; font-size: 15px !important;
}
.stTextInput input:focus, .stTextArea textarea:focus {
    border-color: #2563a8 !important; box-shadow: none !important;
}
.stButton > button {
    background: #1a1008 !important; color: #f5f0e8 !important; border: none !important;
    border-radius: 4px !important; font-family: 'Playfair Display', Georgia, serif !important;
    font-size: 14px !important; font-weight: 700 !important; letter-spacing: 0.03em !important;
    padding: 9px 22px !important;
}
.stButton > button:hover { background: #c8392b !important; }
.stButton > button:disabled { background: #ccc !important; color: #999 !important; }
hr { border-color: #c8b98a !important; margin: 8px 0 !important; }
.stAlert { background-color: #e8dfc8 !important; color: #1a1008 !important; }

/* ── Lesson header ── */
.lesson-header {
    display: flex; align-items: center; justify-content: space-between;
    padding: 10px 18px; background: #1a1008;
    border-radius: 6px 6px 0 0; border-bottom: 3px solid #c9963a;
}
.subject-tag  { font-family: 'IBM Plex Mono', monospace; font-size: 10px; letter-spacing: 0.15em; color: #c9963a !important; text-transform: uppercase; }
.lesson-title { font-family: 'Playfair Display', serif; font-size: 13px; color: #f5f0e8 !important; font-weight: 700; }

/* ── Slide panel ── */
.slide-panel {
    background: #f5f0e8;
    min-height: 460px;
    padding: 36px 44px 28px 52px;
    position: relative; overflow: hidden;
    border-left: 2px solid #e8dfc8; border-right: 2px solid #e8dfc8;
}
.slide-panel::before {
    content: ''; position: absolute; top: 0; left: 0;
    width: 5px; height: 100%;
    background: linear-gradient(to bottom, #c8392b, #2563a8);
}
.slide-number {
    font-family: 'IBM Plex Mono', monospace; font-size: 11px;
    color: #888 !important; letter-spacing: 0.1em; margin-bottom: 8px;
}
.slide-h1 {
    font-family: 'Playfair Display', serif; font-size: 28px; font-weight: 900;
    color: #1a1008 !important; line-height: 1.15; margin-bottom: 20px;
    border-bottom: 2px solid #e8dfc8; padding-bottom: 12px;
}
.slide-h2 {
    font-family: 'Playfair Display', serif; font-size: 18px; font-weight: 700;
    color: #1a1008 !important; margin: 18px 0 8px;
}

/* ── Slide 1 ── */
.breaking-banner {
    background: #c8392b; color: white !important;
    font-family: 'IBM Plex Mono', monospace; font-size: 11px; letter-spacing: 0.12em;
    padding: 5px 12px; display: inline-block; margin-bottom: 16px; border-radius: 2px;
    animation: pulse 2s infinite;
}
@keyframes pulse { 0%,100%{opacity:1} 50%{opacity:0.7} }
.news-box {
    background: white; border: 2px solid #1a1008; border-radius: 4px;
    padding: 20px 24px; margin: 14px 0; box-shadow: 4px 4px 0 #1a1008;
    position: relative; color: #1a1008 !important;
}
.news-box::after { content:'🎙️'; position:absolute; top:-12px; right:14px; font-size:22px; }
.news-box p { color: #1a1008 !important; font-size: 15px; line-height: 1.65; }
.reporter-note {
    background: #e8dfc8; border-left: 4px solid #c9963a;
    padding: 12px 16px; margin-top: 16px; border-radius: 0 4px 4px 0;
    font-style: italic; font-size: 14px; color: #1a1008 !important;
}
.term { background: rgba(201,150,58,0.18); border-radius: 2px; padding: 0 3px; font-weight: 600; color: #1a1008 !important; }

/* ── Slide 2 ── */
.two-col { display: grid; grid-template-columns: 1fr 1fr; gap: 16px; margin: 12px 0; }
.voice-card { border-radius: 6px; padding: 16px; border: 2px solid; color: #1a1008 !important; }
.voice-card.active-card  { border-color: #2563a8; background: #eef4ff; }
.voice-card.passive-card { border-color: #c8392b; background: #fff2f0; }
.voice-card h3 { font-family:'Playfair Display',serif; font-size:15px; font-weight:700; margin-bottom:6px; color:#1a1008 !important; }
.voice-card p  { font-size:13px; color:#1a1008 !important; }
.voice-card .example { font-family:'IBM Plex Mono',monospace; font-size:13px; background:white; border-radius:3px; padding:8px 10px; margin:8px 0; border:1px solid #ddd; color:#1a1008 !important; }
.voice-card .flow { font-size:12px; color:#666 !important; font-style:italic; }
.passive-hidden { font-family:'IBM Plex Mono',monospace; font-size:12px; color:#bbb !important; font-style:italic; padding:8px 10px; border:1px dashed #ddd; border-radius:3px; margin:8px 0; background:#fff2f0; }
.recipe-box { background:#e8dfc8; border-radius:6px; padding:16px 20px; margin-top:14px; color:#1a1008 !important; }
.recipe-box h3 { font-family:'Playfair Display',serif; font-size:15px; font-weight:700; margin-bottom:10px; color:#1a1008 !important; }
.recipe-steps { list-style:none; counter-reset:step; padding:0; }
.recipe-steps li { counter-increment:step; padding:6px 0 6px 32px; position:relative; font-size:14px; border-bottom:1px dashed #c8b98a; color:#1a1008 !important; }
.recipe-steps li:last-child { border-bottom:none; }
.recipe-steps li::before {
    content:counter(step); position:absolute; left:0; top:6px;
    width:20px; height:20px; background:#c9963a; color:white !important;
    border-radius:50%; display:inline-flex; align-items:center; justify-content:center;
    font-family:'IBM Plex Mono',monospace; font-size:11px; font-weight:600;
}

/* ── Slide 3 ── */
.reasons-grid { display:grid; grid-template-columns:1fr 1fr; gap:12px; margin:12px 0; }
.reason-card { background:white; border:1.5px solid #e8dfc8; border-radius:6px; padding:12px 14px; position:relative; }
.reason-num { font-family:'IBM Plex Mono',monospace; font-size:28px; font-weight:600; color:#e8dfc8 !important; position:absolute; top:6px; right:10px; line-height:1; }
.reason-card h3 { font-size:13px; font-weight:700; font-family:'Playfair Display',serif; color:#1a1008 !important; margin-bottom:4px; }
.reason-card p  { font-size:12.5px; color:#444 !important; line-height:1.5; }
.headline-row { display:flex; align-items:stretch; border:1.5px solid #1a1008; border-radius:4px; overflow:hidden; margin-top:10px; }
.hl-content { padding:12px 16px; flex:1; }
.hl-content.informal { background:#fff8f0; border-right:2px dashed #ddd; }
.hl-content.formal   { background:#f0f8ff; }
.hl-content .lbl { font-family:'IBM Plex Mono',monospace; font-size:10px; color:#888 !important; margin-bottom:4px; }
.hl-content p { font-size:14px; font-weight:600; color:#1a1008 !important; }

/* ── Slide 4 quiz ── */
.quiz-label { font-family:'IBM Plex Mono',monospace; font-size:12px; color:#c8392b !important; letter-spacing:0.1em; margin-bottom:10px; }
.sentence-display { background:#1a1008; color:#f5f0e8 !important; font-family:'IBM Plex Mono',monospace; font-size:16px; padding:16px 22px; border-radius:6px; margin:14px 0; border-left:4px solid #c9963a; }

/* ── Slide 5 newspaper ── */
.newspaper-mock { background:white; border:2px solid #1a1008; border-radius:4px; overflow:hidden; box-shadow:4px 4px 0 #1a1008; }
.newspaper-header { background:#1a1008; text-align:center; padding:10px 14px 8px; border-bottom:3px double #c9963a; }
.newspaper-name    { font-family:'Playfair Display',serif; font-size:22px; font-weight:900; letter-spacing:0.04em; color:#f5f0e8 !important; }
.newspaper-tagline { font-family:'IBM Plex Mono',monospace; font-size:9px; letter-spacing:0.12em; color:#c9963a !important; margin-top:2px; }
.headline-display  { padding:20px 24px 14px; min-height:72px; display:flex; align-items:center; justify-content:center; text-align:center; border-bottom:2px solid #e8dfc8; }
.headline-text     { font-family:'Playfair Display',serif; font-size:22px; font-weight:900; color:#1a1008 !important; line-height:1.2; }
.blank  { color:#bbb !important; font-style:italic; }
.filled { color:#c8392b !important; text-decoration:underline wavy #c9963a 1.5px; }
.builder-area { padding:18px 24px; background:white; }
.builder-area h3 { font-family:'Playfair Display',serif; font-size:14px; font-weight:700; margin-bottom:14px; color:#555 !important; }

/* ── Slide 6 Be the Reporter ── */
.challenge-intro {
    background: linear-gradient(135deg, #1a1008 0%, #2a1f14 100%);
    border-radius:8px; padding:18px 22px; margin-bottom:18px;
    position:relative; overflow:hidden;
}
.challenge-intro::after { content:'✍️'; position:absolute; right:16px; top:50%; transform:translateY(-50%); font-size:36px; }
.challenge-intro h2 { color:#c9963a !important; font-size:16px; margin:0 0 6px; font-family:'Playfair Display',serif; }
.challenge-intro p  { font-size:13.5px; line-height:1.6; color:#d0c8b8 !important; max-width:78%; }
.prompt-card { background:white; border:1.5px solid #e8dfc8; border-radius:6px; padding:12px 14px; margin-bottom:4px; }
.prompt-card.selected { border-color:#c8392b !important; background:#fff5f4 !important; box-shadow:2px 2px 0 #c8392b; }
.active-sent { font-family:'IBM Plex Mono',monospace; font-size:11.5px; color:#c8392b !important; margin-bottom:4px; font-weight:600; }
.hint-text   { font-size:11.5px; color:#888 !important; }
.write-label { font-family:'IBM Plex Mono',monospace; font-size:10px; letter-spacing:0.1em; color:#888 !important; display:block; margin-bottom:5px; text-transform:uppercase; }
.writing-feedback { border-radius:6px; padding:12px 16px; font-size:13.5px; line-height:1.6; margin-top:12px; }
.writing-feedback.good    { background:#eafaf1; border:1.5px solid #1a8c4e; color:#1a5c34 !important; }
.writing-feedback.partial { background:#fffbe8; border:1.5px solid #c9963a; color:#6b4d0e !important; }
.writing-feedback.error   { background:#fff0ee; border:1.5px solid #c0392b; color:#7b1a0e !important; }

/* ── Feedback boxes ── */
.fb { border-radius:6px; padding:12px 16px; font-size:14px; line-height:1.5; margin-top:10px; }
.fb.ok  { background:#eafaf1 !important; border:1.5px solid #1a8c4e; color:#1a5c34 !important; }
.fb.bad { background:#fff0ee !important; border:1.5px solid #c0392b; color:#7b1a0e !important; }
.fb.mid { background:#fffbe8 !important; border:1.5px solid #c9963a; color:#6b4d0e !important; }
.fb strong, .fb em { color:inherit !important; }

/* ── Nav bar ── */
.nav-bar {
    background:#e8dfc8; border-top:2px solid #c8b98a;
    border-left:2px solid #e8dfc8; border-right:2px solid #e8dfc8;
    border-radius:0 0 6px 6px; padding:12px 20px;
    display:flex; align-items:center; justify-content:center; gap:8px;
}
.dot { width:10px; height:10px; border-radius:50%; background:#c8b98a; display:inline-block; transition:all 0.2s; }
.dot.active  { background:#c8392b; transform:scale(1.3); }
.dot.visited { background:#2563a8; }
</style>
""", unsafe_allow_html=True)

# ── Session state ─────────────────────────────────────────────────────────────
defaults = {
    "slide": 1,
    "passive_revealed": False,
    "q1_show": False, "q2_show": False, "q3_show": False,
    "q1_done": False, "q2_done": False, "q3_done": False,
    "q1_correct": False, "q2_correct": False, "q3_correct": False,
    "q1_fb": False, "q2_fb": False, "q3_fb": False,
    "hl_checked": False, "hl_obj": "", "hl_verb": "", "hl_pp": "",
    "reporter_prompt": None,
    "hint_shown": False,
    "writing_checked": False,
    "writing_ans_stored": "",
    "writing_fb_shown": False,
}
for k, v in defaults.items():
    if k not in st.session_state:
        st.session_state[k] = v

slide = st.session_state.slide

# ── Progress dots ─────────────────────────────────────────────────────────────
def nav_dots(current, total=6):
    html = ""
    for i in range(1, total + 1):
        cls = "dot active" if i == current else ("dot visited" if i < current else "dot")
        html += f'<span class="{cls}"></span>'
    return html

# ── Lesson header ─────────────────────────────────────────────────────────────
st.markdown("""
<div class="lesson-header">
  <span class="subject-tag">Year 7 · English Language</span>
  <span class="lesson-title">Mastering Passive Voice</span>
</div>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
# SLIDE 1 — The Scene of the Crime
# ══════════════════════════════════════════════════════════════════════════════
if slide == 1:
    st.markdown("""
    <div class="slide-panel">
      <div class="slide-number">01 / 06 — Introduction</div>
      <div class="slide-h1">The Scene of the Crime</div>
      <div class="breaking-banner">🔴 BREAKING NEWS · LIVE COVERAGE</div>
      <div class="news-box">
        <p><em>"We're coming to you live from the Royal Museum, where a priceless masterpiece
        vanished just minutes ago. The security guards are baffled. Someone stole the painting,
        but we don't know who… yet."</em></p>
      </div>
      <div class="reporter-note">
        <strong>Reporter's Note:</strong> In news reports, we often focus on <em>what happened</em>
        rather than <em>who did it</em>. This is where the <span class="term">Passive Voice</span>
        becomes our most powerful tool.
      </div>
      <p style="margin-top:16px; font-size:14px; color:#666;">
        Over the next six slides, you will learn how passive voice is formed, why journalists
        love it, and how to use it yourself. Let's begin.
      </p>
    </div>
    """, unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
# SLIDE 2 — Active vs Passive  (passive example hidden until revealed)
# ══════════════════════════════════════════════════════════════════════════════
elif slide == 2:
    if st.session_state.passive_revealed:
        passive_inner = """
          <div class="example">"The painting was stolen (by the thief)."</div>
          <div class="flow">Object → Was/Were + Past Participle</div>"""
    else:
        passive_inner = """
          <div class="passive-hidden">
            [ Click "👁️ Reveal Passive Example" below to see the passive sentence ]
          </div>"""

    st.markdown(f"""
    <div class="slide-panel">
      <div class="slide-number">02 / 06 — Grammar Basics</div>
      <div class="slide-h1">Active vs. Passive: The Basics</div>
      <div class="two-col">
        <div class="voice-card active-card">
          <h3>🔵 Active Voice</h3>
          <p>The subject <em>performs</em> the action.</p>
          <div class="example">"The thief stole the painting."</div>
          <div class="flow">Subject (Doer) → Action → Object</div>
        </div>
        <div class="voice-card passive-card">
          <h3>🔴 Passive Voice</h3>
          <p>The subject is <em>acted upon</em>.</p>
          {passive_inner}
        </div>
      </div>
    </div>
    """, unsafe_allow_html=True)

    if not st.session_state.passive_revealed:
        if st.button("👁️ Reveal Passive Example"):
            st.session_state.passive_revealed = True
            st.rerun()
    else:
        st.markdown("""
        <div style="background:#f5f0e8; border-left:2px solid #e8dfc8; border-right:2px solid #e8dfc8; padding:0 44px 28px 52px;">
          <div class="recipe-box">
            <h3>📋 The Recipe for Passive Voice</h3>
            <ol class="recipe-steps">
              <li><strong>Move the Object</strong> to the front of the sentence.</li>
              <li><strong>Add 'to be'</strong> (is, are, was, were) in the correct tense.</li>
              <li><strong>Change the main verb</strong> to its <span class="term">Past Participle</span>
                  (eaten, seen, stolen…).</li>
              <li>The <strong>doer (agent)</strong> is optional — add "by [someone]" only when needed.</li>
            </ol>
          </div>
        </div>
        """, unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
# SLIDE 3 — The Journalist's Secret
# ══════════════════════════════════════════════════════════════════════════════
elif slide == 3:
    st.markdown("""
    <div class="slide-panel">
      <div class="slide-number">03 / 06 — Why Use It?</div>
      <div class="slide-h1">The Journalist's Secret</div>
      <div class="reasons-grid">
        <div class="reason-card">
          <span class="reason-num">1</span>
          <h3>Focus on the Victim / Action</h3>
          <p>When the event or victim matters more than who caused it.</p>
        </div>
        <div class="reason-card">
          <span class="reason-num">2</span>
          <h3>Objectivity</h3>
          <p>Makes reports sound more formal, neutral, and scientific.</p>
        </div>
        <div class="reason-card">
          <span class="reason-num">3</span>
          <h3>The Doer is Unknown</h3>
          <p>Perfect for crime stories when we don't know who acted.</p>
        </div>
        <div class="reason-card">
          <span class="reason-num">4</span>
          <h3>To Avoid Blame</h3>
          <p>Hides responsibility — e.g., <em>"Mistakes were made."</em></p>
        </div>
      </div>
      <div class="slide-h2">Compare These Headlines</div>
      <div class="headline-row">
        <div class="hl-content informal">
          <div class="lbl">Informal / Active</div>
          <p>"Someone smashed a window at the library!"</p>
        </div>
        <div class="hl-content formal">
          <div class="lbl">Formal / Passive (Journalistic)</div>
          <p>"Library window smashed in late-night incident."</p>
        </div>
      </div>
    </div>
    """, unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
# SLIDE 4 — Practice Quiz
# ══════════════════════════════════════════════════════════════════════════════
elif slide == 4:
    st.markdown("""
    <div class="slide-panel">
      <div class="slide-number">04 / 06 — Quick Practice</div>
      <div class="slide-h1">Practice: Reporting the Facts</div>
    </div>
    """, unsafe_allow_html=True)

    def quiz_block(n, prompt, sentence, options, correct_idx, fb_ok, fb_bad):
        st.markdown(f'<div class="quiz-label">QUESTION {n} OF 3</div>', unsafe_allow_html=True)
        st.markdown(f"**{prompt}**")
        st.markdown(f'<div class="sentence-display">{sentence}</div>', unsafe_allow_html=True)

        if not st.session_state[f"q{n}_show"]:
            if st.button("👁️ Show Answer Options", key=f"show_{n}"):
                st.session_state[f"q{n}_show"] = True
                st.rerun()
        else:
            if not st.session_state[f"q{n}_done"]:
                choice = st.radio("Choose the correct passive sentence:", options,
                                  key=f"q{n}_radio", index=None)
                if st.button("✔️ Submit Answer", key=f"submit_{n}"):
                    if choice is not None:
                        st.session_state[f"q{n}_done"]    = True
                        st.session_state[f"q{n}_correct"] = (choice == options[correct_idx])
                        st.rerun()
            else:
                # Show locked selection
                locked_idx = correct_idx if st.session_state[f"q{n}_correct"] else \
                             ([i for i in range(len(options)) if i != correct_idx][0])
                st.radio("Your answer:", options, key=f"q{n}_radio",
                         index=locked_idx, disabled=True)

                if not st.session_state[f"q{n}_fb"]:
                    if st.button("💬 Reveal Feedback", key=f"fb_{n}"):
                        st.session_state[f"q{n}_fb"] = True
                        st.rerun()
                else:
                    if st.session_state[f"q{n}_correct"]:
                        st.markdown(f'<div class="fb ok">✅ <strong>Correct!</strong> {fb_ok}</div>',
                                    unsafe_allow_html=True)
                    else:
                        st.markdown(f'<div class="fb bad">❌ <strong>Not quite.</strong> {fb_bad}</div>',
                                    unsafe_allow_html=True)

    quiz_block(1,
        "Convert this Active sentence to Passive:",
        '"Police arrested the suspect."',
        ['"The suspect arrested police."',
         '"The suspect was arrested."',
         '"Arrested was the suspect."'],
        correct_idx=1,
        fb_ok='"The suspect" (the object) moves to the front, and "was arrested" '
              '(was + past participle of <em>arrest</em>) follows. Well done!',
        fb_bad='Remember the recipe: move the object to the front, then add '
               '<em>was/were</em> + past participle. The answer is: <em>"The suspect was arrested."</em>',
    )
    st.divider()
    quiz_block(2,
        "Convert this sentence to Passive Voice:",
        '"The curator displayed the painting."',
        ['"The curator was displayed the painting."',
         '"The painting was displayed by the curator."',
         '"The painting displayed the curator."'],
        correct_idx=1,
        fb_ok='"The painting" moves to the front, "was displayed" is the passive verb, '
              'and "by the curator" tells us the doer.',
        fb_bad='The correct passive is: <em>"The painting was displayed by the curator."</em> '
               'The object becomes the new subject.',
    )
    st.divider()
    quiz_block(3,
        "Which sentence is in the Passive Voice?",
        "Select the passive sentence below:",
        ['"Witnesses filmed the incident."',
         '"The incident was filmed by witnesses."',
         '"The witnesses ran away quickly."'],
        correct_idx=1,
        fb_ok='"The incident was filmed by witnesses" is passive — "was filmed" '
              '(to be + past participle) is the give-away. Ready for the Headline Builder!',
        fb_bad='The passive sentence is: <em>"The incident was filmed by witnesses."</em> '
               'Look for the <em>was/were + past participle</em> pattern.',
    )

# ══════════════════════════════════════════════════════════════════════════════
# SLIDE 5 — Headline Builder
# ══════════════════════════════════════════════════════════════════════════════
elif slide == 5:
    st.markdown("""
    <div class="slide-panel">
      <div class="slide-number">05 / 06 — Headline Builder</div>
      <div class="slide-h1">Writing Challenge: The Headline Maker</div>
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)
    with col1:
        obj  = st.selectbox("Select object",
                            ["— choose —", "A rare diamond", "The museum gates", "Security cameras"])
    with col2:
        verb = st.selectbox("Select verb to be",
                            ["— choose —", "is", "was", "were"])
    with col3:
        pp   = st.selectbox("Select past participle",
                            ["— choose —", "finding", "find", "found"])

    ov = "" if obj  == "— choose —" else obj
    vv = "" if verb == "— choose —" else verb
    pv = "" if pp   == "— choose —" else pp

    obj_html  = f'<span class="filled">{ov}</span>'   if ov else '<span class="blank">___ ___</span>'
    verb_html = f'<span class="filled">{vv}</span>'   if vv else '<span class="blank">___</span>'
    pp_html   = f'<span class="filled">{pv}</span>'   if pv else '<span class="blank">___</span>'

    st.markdown(f"""
    <div class="newspaper-mock">
      <div class="newspaper-header">
        <div class="newspaper-name">The Daily Gazette</div>
        <div class="newspaper-tagline">All the News That's Fit to Passive-ify</div>
      </div>
      <div class="headline-display">
        <div class="headline-text">{obj_html}&nbsp;{verb_html}&nbsp;{pp_html}</div>
      </div>
      <div class="builder-area">
        <h3>Build your passive headline by selecting each part above.</h3>
      </div>
    </div>
    """, unsafe_allow_html=True)

    if st.button("Check My Headline →", disabled=not (ov and vv and pv)):
        st.session_state.hl_checked = True
        st.session_state.hl_obj  = ov
        st.session_state.hl_verb = vv
        st.session_state.hl_pp   = pv

    if st.session_state.hl_checked:
        o = st.session_state.hl_obj
        v = st.session_state.hl_verb
        p = st.session_state.hl_pp
        agree   = {"A rare diamond": "was", "The museum gates": "were", "Security cameras": "were"}
        ok_pp   = (p == "found")
        ok_verb = (v == agree.get(o, ""))
        if ok_pp and ok_verb:
            st.markdown(
                f'<div class="fb ok">✅ <strong>Excellent headline!</strong> '
                f'"{o} {v} {p}" is a perfect passive construction. Object first, correct '
                f'<em>to be</em>, and the right past participle. You\'re ready for Fleet Street!</div>',
                unsafe_allow_html=True)
        elif ok_pp and not ok_verb:
            st.markdown(
                f'<div class="fb mid">🟡 <strong>Almost!</strong> The past participle is right '
                f'(<em>found ✓</em>), but "{o}" needs <em>{agree.get(o,"")}</em>, '
                f'not <em>{v}</em>, to agree in number.</div>',
                unsafe_allow_html=True)
        else:
            st.markdown(
                f'<div class="fb bad">❌ <strong>Check the verb form.</strong> '
                f'<em>{p}</em> is not a past participle. The past participle of '
                f'<em>find</em> is <strong>found</strong>. Try again!</div>',
                unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
# SLIDE 6 — Be the Reporter!
# ══════════════════════════════════════════════════════════════════════════════
elif slide == 6:
    st.markdown("""
    <div class="slide-panel">
      <div class="slide-number">06 / 06 — Your Turn</div>
      <div class="slide-h1">Be the Reporter!</div>
      <div class="challenge-intro">
        <h2>Writing Challenge</h2>
        <p>Choose an active sentence below and rewrite it using <strong>passive voice</strong>.
        Imagine you're filing your report for the evening news.</p>
      </div>
    </div>
    """, unsafe_allow_html=True)

    # Prompt data: id → (display sentence, correct passive phrase, hint)
    prompts = {
        1: ("A chef cooked the meal.",       "the meal was cooked",     "Think: what is the object here?"),
        2: ("Workers built the bridge.",      "the bridge was built",    "Use <em>were</em> + past participle"),
        3: ("The storm destroyed the town.",  "the town was destroyed",  "The town becomes the new subject"),
        4: ("Doctors discovered the cure.",   "the cure was discovered", "Great for a formal news report"),
    }

    sel = st.session_state.reporter_prompt

    # ── Prompt cards in 2-column grid ────────────────────────────────────────
    col_a, col_b = st.columns(2)
    for i, (pid, (sentence, _, hint)) in enumerate(prompts.items()):
        col = col_a if i % 2 == 0 else col_b
        with col:
            card_cls = "prompt-card selected" if sel == pid else "prompt-card"
            st.markdown(f"""
            <div class="{card_cls}">
              <div class="active-sent">Active: "{sentence}"</div>
              <div class="hint-text">💡 {hint}</div>
            </div>
            """, unsafe_allow_html=True)
            btn_txt = "✅ Selected" if sel == pid else "Select"
            if st.button(btn_txt, key=f"pick_{pid}", use_container_width=True):
                st.session_state.reporter_prompt    = pid
                st.session_state.hint_shown         = False
                st.session_state.writing_checked    = False
                st.session_state.writing_fb_shown   = False
                st.session_state.writing_ans_stored = ""
                st.rerun()

    if sel is None:
        st.info("👆 Select one of the active sentences above to get started.")

    else:
        sentence_txt, correct_phrase, hint_txt = prompts[sel]
        st.divider()

        # Step 1 – optional hint
        if not st.session_state.hint_shown:
            if st.button("💡 Show Hint", key="hint_btn"):
                st.session_state.hint_shown = True
                st.rerun()
        else:
            st.markdown(
                f'<div class="reporter-note"><strong>💡 Hint:</strong> {hint_txt}</div>',
                unsafe_allow_html=True)

        # Step 2 – write answer
        st.markdown('<span class="write-label">Your passive sentence:</span>',
                    unsafe_allow_html=True)
        user_ans = st.text_area(
            label="hidden_label",
            label_visibility="collapsed",
            placeholder='Write your passive version here… e.g. "The meal was cooked by a chef."',
            key="reporter_ans",
            height=90,
        )

        # Step 3 – check answer
        if st.button("Check My Answer", key="check_ans",
                     disabled=not (user_ans or "").strip()):
            st.session_state.writing_checked    = True
            st.session_state.writing_ans_stored = user_ans
            st.session_state.writing_fb_shown   = False
            st.rerun()

        # Step 4 – reveal feedback
        if st.session_state.writing_checked:
            if not st.session_state.writing_fb_shown:
                if st.button("💬 Reveal Feedback", key="reveal_fb"):
                    st.session_state.writing_fb_shown = True
                    st.rerun()
            else:
                ans = st.session_state.writing_ans_stored.lower().strip()
                has_passive_verb = any(w in ans for w in ["is ", "are ", "was ", "were "])
                is_correct       = correct_phrase in ans
                eg               = correct_phrase.capitalize() + " by [someone]."

                if is_correct:
                    st.markdown(
                        '<div class="writing-feedback good">'
                        '✅ <strong>Excellent work!</strong> Your sentence uses the passive voice '
                        'correctly — the object has moved to the front and you\'ve used '
                        '<em>was/were + past participle</em>. A real journalist\'s technique!'
                        '</div>', unsafe_allow_html=True)
                    st.balloons()
                elif has_passive_verb:
                    st.markdown(
                        '<div class="writing-feedback partial">'
                        '🟡 <strong>Good start!</strong> You\'ve included a passive verb '
                        '(was/were) ✓ — double-check that the original <em>object</em> is now '
                        'the subject of your sentence, and that the past participle is correct.'
                        '</div>', unsafe_allow_html=True)
                else:
                    st.markdown(
                        f'<div class="writing-feedback error">'
                        f'❌ <strong>Keep trying!</strong> Remember the recipe: move the object '
                        f'to the front, add <em>was/were</em>, then the past participle. '
                        f'For example: <em>"{eg}"</em>'
                        f'</div>', unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
# Navigation bar
# ══════════════════════════════════════════════════════════════════════════════
st.markdown(f"""
<div class="nav-bar">
  {nav_dots(slide)}
</div>
""", unsafe_allow_html=True)

col_back, col_mid, col_next = st.columns([1, 2, 1])

with col_back:
    if st.button("← Back", disabled=(slide == 1), use_container_width=True):
        st.session_state.slide -= 1
        st.rerun()

with col_mid:
    st.markdown(
        f"<div style='text-align:center;font-family:IBM Plex Mono,monospace;"
        f"font-size:12px;color:#c8b98a;padding-top:6px;'>Slide {slide} of 6</div>",
        unsafe_allow_html=True)

with col_next:
    if slide < 6:
        if st.button("Next →", use_container_width=True):
            st.session_state.slide += 1
            st.rerun()
    else:
        if st.button("🔄 Start Again", use_container_width=True):
            for k in list(st.session_state.keys()):
                del st.session_state[k]
            st.rerun()
