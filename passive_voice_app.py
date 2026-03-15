import streamlit as st

# ── Page config ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Year 7 English – Passive Voice",
    page_icon="📰",
    layout="centered",
)

# ── Custom CSS ────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700;900&family=Source+Serif+4:wght@400;600&family=IBM+Plex+Mono:wght@400;600&display=swap');

html, body, [class*="css"] {
    font-family: 'Source Serif 4', Georgia, serif;
    background-color: #f5f0e8;
}

/* Header strip */
.lesson-header {
    background: #1a1008;
    color: #f5f0e8;
    padding: 12px 20px;
    border-radius: 8px 8px 0 0;
    border-bottom: 3px solid #c9963a;
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 0;
}
.lesson-header .tag  { font-family: 'IBM Plex Mono', monospace; font-size: 11px; letter-spacing: .12em; color: #c9963a; }
.lesson-header .title { font-family: 'Playfair Display', serif; font-size: 14px; }

/* Slide wrapper */
.slide-box {
    background: #f5f0e8;
    border: 2px solid #1a1008;
    border-top: none;
    border-radius: 0 0 8px 8px;
    padding: 28px 36px 24px;
    box-shadow: 4px 4px 0 #1a1008;
    margin-bottom: 18px;
}

/* Slide number */
.slide-num { font-family: 'IBM Plex Mono', monospace; font-size: 11px; color: #888; letter-spacing: .1em; margin-bottom: 8px; }

/* Slide title */
h2.slide-title {
    font-family: 'Playfair Display', serif !important;
    font-size: 26px !important;
    font-weight: 900 !important;
    color: #1a1008 !important;
    border-bottom: 2px solid #e8dfc8;
    padding-bottom: 10px;
    margin-bottom: 16px;
}

/* Breaking news pulse */
.breaking {
    display: inline-block;
    background: #c8392b;
    color: white;
    font-family: 'IBM Plex Mono', monospace;
    font-size: 11px;
    letter-spacing: .12em;
    padding: 4px 12px;
    border-radius: 2px;
    margin-bottom: 14px;
    animation: pulse 2s infinite;
}
@keyframes pulse { 0%,100%{opacity:1} 50%{opacity:.7} }

/* News quote box */
.news-box {
    background: white;
    border: 2px solid #1a1008;
    border-radius: 4px;
    padding: 18px 22px;
    box-shadow: 3px 3px 0 #1a1008;
    margin-bottom: 14px;
    font-style: italic;
}

/* Reporter note */
.reporter-note {
    background: #e8dfc8;
    border-left: 4px solid #c9963a;
    padding: 12px 16px;
    border-radius: 0 4px 4px 0;
    font-size: 14px;
    font-style: italic;
}

/* Voice cards */
.voice-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 14px; margin: 12px 0; }
.v-card { border-radius: 6px; padding: 14px; border: 2px solid; }
.v-card.active  { border-color: #2563a8; background: #eef4ff; }
.v-card.passive { border-color: #c8392b; background: #fff2f0; }
.v-card h4 { font-family: 'Playfair Display', serif; font-size: 15px; font-weight: 700; margin-bottom: 6px; }
.v-card .ex { font-family: 'IBM Plex Mono', monospace; font-size: 12.5px; background: white; border: 1px solid #ddd; border-radius: 3px; padding: 7px 10px; margin: 7px 0; }
.v-card .flow { font-size: 12px; color: #666; font-style: italic; }

/* Recipe box */
.recipe { background: #e8dfc8; border-radius: 6px; padding: 14px 18px; margin-top: 14px; }
.recipe h4 { font-family: 'Playfair Display', serif; font-size: 15px; font-weight: 700; margin-bottom: 10px; }
.recipe ol { padding-left: 18px; }
.recipe li { font-size: 14px; padding: 3px 0; border-bottom: 1px dashed #c8b98a; }
.recipe li:last-child { border: none; }

/* Reason cards */
.reason-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 10px; margin: 12px 0; }
.r-card { background: white; border: 1.5px solid #e8dfc8; border-radius: 6px; padding: 12px 14px; }
.r-card h4 { font-size: 13px; font-weight: 700; font-family: 'Playfair Display', serif; margin-bottom: 4px; }
.r-card p  { font-size: 12.5px; color: #444; }

/* Headline comparison */
.hl-compare { display: grid; grid-template-columns: 1fr 1fr; gap: 0; border: 1.5px solid #1a1008; border-radius: 4px; overflow: hidden; margin-top: 12px; }
.hl-cell { padding: 12px 14px; }
.hl-cell.inf  { background: #fff8f0; border-right: 2px dashed #ddd; }
.hl-cell.frm  { background: #f0f8ff; }
.hl-cell .lbl { font-family: 'IBM Plex Mono', monospace; font-size: 10px; color: #888; margin-bottom: 4px; }
.hl-cell p    { font-size: 14px; font-weight: 600; }

/* Newspaper mock */
.newspaper { background: white; border: 2px solid #1a1008; border-radius: 4px; overflow: hidden; box-shadow: 4px 4px 0 #1a1008; }
.np-header  { background: #1a1008; color: #f5f0e8; text-align: center; padding: 10px 14px; border-bottom: 3px double #c9963a; }
.np-name    { font-family: 'Playfair Display', serif; font-size: 22px; font-weight: 900; }
.np-tag     { font-family: 'IBM Plex Mono', monospace; font-size: 9px; letter-spacing: .12em; color: #c9963a; }
.np-headline { padding: 18px 22px; text-align: center; font-family: 'Playfair Display', serif; font-size: 22px; font-weight: 900; border-bottom: 2px solid #e8dfc8; min-height: 60px; }

/* Feedback boxes */
.fb { border-radius: 6px; padding: 12px 16px; font-size: 14px; line-height: 1.5; margin-top: 10px; }
.fb.ok  { background: #eafaf1; border: 1.5px solid #1a8c4e; color: #1a5c34; }
.fb.bad { background: #fff0ee; border: 1.5px solid #c0392b; color: #7b1a0e; }
.fb.mid { background: #fffbe8; border: 1.5px solid #c9963a; color: #6b4d0e; }

/* Nav bar */
.nav-bar { display: flex; justify-content: space-between; align-items: center; background: #e8dfc8; border: 2px solid #c8b98a; border-radius: 6px; padding: 10px 16px; margin-top: 4px; }
.nav-bar .pager { font-family: 'IBM Plex Mono', monospace; font-size: 12px; color: #888; }

.term { background: rgba(201,150,58,.18); border-radius: 2px; padding: 0 3px; font-weight: 600; }
</style>
""", unsafe_allow_html=True)

# ── Session state ─────────────────────────────────────────────────────────────
if "slide" not in st.session_state:
    st.session_state.slide = 1

defaults = {
    "q1_done": False, "q2_done": False, "q3_done": False,
    "q1_correct": False, "q2_correct": False, "q3_correct": False,
    "q1_show": False, "q2_show": False, "q3_show": False,
    "q1_fb_show": False, "q2_fb_show": False, "q3_fb_show": False,
    "hl_checked": False,
    "writing_checked": False,
    "writing_fb_show": False,
    "selected_prompt": None,
}
for k, v in defaults.items():
    if k not in st.session_state:
        st.session_state[k] = v

slide = st.session_state.slide

# ── Shared header ─────────────────────────────────────────────────────────────
st.markdown("""
<div class="lesson-header">
  <span class="tag">YEAR 7 · ENGLISH LANGUAGE</span>
  <span class="title">Mastering Passive Voice</span>
</div>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
# SLIDE 1 – Introduction
# ══════════════════════════════════════════════════════════════════════════════
if slide == 1:
    st.markdown("""
    <div class="slide-box">
      <div class="slide-num">01 / 06 — Introduction</div>
      <h2 class="slide-title">The Scene of the Crime</h2>
      <div class="breaking">🔴 BREAKING NEWS · LIVE COVERAGE</div>
      <div class="news-box">
        <p><em>"We're coming to you live from the Royal Museum, where a priceless masterpiece vanished just minutes ago.
        The security guards are baffled. Someone stole the painting, but we don't know who… yet."</em></p>
      </div>
      <div class="reporter-note">
        <strong>Reporter's Note:</strong> In news reports, we often focus on <em>what happened</em> rather than
        <em>who did it</em>. This is where the <span class="term">Passive Voice</span> becomes our most powerful tool.
      </div>
      <p style="margin-top:14px; font-size:14px; color:#666;">
        Over the next six slides you will learn how passive voice is formed, why journalists love it,
        and how to use it yourself. Let's begin!
      </p>
    </div>
    """, unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
# SLIDE 2 – Grammar Basics
# ══════════════════════════════════════════════════════════════════════════════
elif slide == 2:
    st.markdown("""
    <div class="slide-box">
      <div class="slide-num">02 / 06 — Grammar Basics</div>
      <h2 class="slide-title">Active vs. Passive: The Basics</h2>
      <div class="voice-grid">
        <div class="v-card active">
          <h4>🔵 Active Voice</h4>
          <p style="font-size:13px;">The subject <em>performs</em> the action.</p>
          <div class="ex">"The thief stole the painting."</div>
          <div class="flow">Subject (Doer) → Action → Object</div>
        </div>
        <div class="v-card passive">
          <h4>🔴 Passive Voice</h4>
          <p style="font-size:13px;">The subject is <em>acted upon</em>.</p>
          <div class="ex">"The painting was stolen (by the thief)."</div>
          <div class="flow">Object → Was/Were + Past Participle</div>
        </div>
      </div>
      <div class="recipe">
        <h4>📋 The Recipe for Passive Voice</h4>
        <ol>
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
# SLIDE 3 – Why use it?
# ══════════════════════════════════════════════════════════════════════════════
elif slide == 3:
    st.markdown("""
    <div class="slide-box">
      <div class="slide-num">03 / 06 — Why Use It?</div>
      <h2 class="slide-title">The Journalist's Secret</h2>
      <div class="reason-grid">
        <div class="r-card">
          <h4>1 · Focus on the Victim / Action</h4>
          <p>When the event or victim matters more than who caused it.</p>
        </div>
        <div class="r-card">
          <h4>2 · Objectivity</h4>
          <p>Makes reports sound more formal, neutral, and scientific.</p>
        </div>
        <div class="r-card">
          <h4>3 · The Doer is Unknown</h4>
          <p>Perfect for crime stories when we don't know who acted.</p>
        </div>
        <div class="r-card">
          <h4>4 · To Avoid Blame</h4>
          <p>Hides responsibility — e.g., <em>"Mistakes were made."</em></p>
        </div>
      </div>
      <strong style="font-family:'Playfair Display',serif;">Compare These Headlines</strong>
      <div class="hl-compare">
        <div class="hl-cell inf">
          <div class="lbl">Informal / Active</div>
          <p>"Someone smashed a window at the library!"</p>
        </div>
        <div class="hl-cell frm">
          <div class="lbl">Formal / Passive (Journalistic)</div>
          <p>"Library window smashed in late-night incident."</p>
        </div>
      </div>
    </div>
    """, unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
# SLIDE 4 – Quiz  (answers hidden until student clicks to reveal)
# ══════════════════════════════════════════════════════════════════════════════
elif slide == 4:
    st.markdown("""
    <div class="slide-box">
      <div class="slide-num">04 / 06 — Quick Practice</div>
      <h2 class="slide-title">Practice: Reporting the Facts</h2>
    </div>
    """, unsafe_allow_html=True)

    # ── helper
    def quiz_block(qnum, prompt, sentence, options, correct_idx, fb_ok, fb_bad):
        """Render one quiz question with hidden options and hidden feedback."""
        show_key   = f"q{qnum}_show"
        done_key   = f"q{qnum}_done"
        correct_key= f"q{qnum}_correct"
        fb_key     = f"q{qnum}_fb_show"
        radio_key  = f"q{qnum}"

        st.markdown(f"**Question {qnum} of 3** — {prompt}")
        st.code(sentence, language=None)

        # Step 1 – reveal options
        if not st.session_state[show_key]:
            if st.button("👁️ Show Answer Options", key=f"show_btn_{qnum}"):
                st.session_state[show_key] = True
                st.rerun()
        else:
            # Step 2 – pick & submit
            if not st.session_state[done_key]:
                choice = st.radio("Choose the correct passive sentence:", options,
                                  key=radio_key, index=None)
                if st.button("✔️ Submit Answer", key=f"submit_btn_{qnum}"):
                    if choice is not None:
                        st.session_state[done_key]   = True
                        st.session_state[correct_key]= (choice == options[correct_idx])
                        st.rerun()
            else:
                # Show which was chosen, greyed out
                st.radio("Your answer:", options, key=radio_key,
                         index=options.index(
                             options[correct_idx]
                             if st.session_state[correct_key]
                             else options[
                                 [i for i in range(len(options)) if i != correct_idx][0]
                             ]
                         ), disabled=True)

                # Step 3 – reveal feedback
                if not st.session_state[fb_key]:
                    if st.button("💬 Reveal Feedback", key=f"fb_btn_{qnum}"):
                        st.session_state[fb_key] = True
                        st.rerun()
                else:
                    if st.session_state[correct_key]:
                        st.markdown(f'<div class="fb ok">✅ <strong>Correct!</strong> {fb_ok}</div>',
                                    unsafe_allow_html=True)
                    else:
                        st.markdown(f'<div class="fb bad">❌ <strong>Not quite.</strong> {fb_bad}</div>',
                                    unsafe_allow_html=True)

    quiz_block(
        1,
        "Convert this Active sentence to Passive:",
        '"Police arrested the suspect."',
        ["The suspect arrested police.",
         "The suspect was arrested.",
         "Arrested was the suspect."],
        correct_idx=1,
        fb_ok='"The suspect" (the object) moves to the front, and "was arrested" (was + past participle of <em>arrest</em>) follows. Well done!',
        fb_bad='Remember the recipe: move the object to the front, then add <em>was/were</em> + past participle. The answer is: <em>"The suspect was arrested."</em>',
    )

    st.divider()

    quiz_block(
        2,
        "Convert this sentence to Passive Voice:",
        '"The curator displayed the painting."',
        ["The curator was displayed the painting.",
         "The painting was displayed by the curator.",
         "The painting displayed the curator."],
        correct_idx=1,
        fb_ok='"The painting" moves to the front, "was displayed" is the passive verb, and "by the curator" tells us the doer.',
        fb_bad='The correct passive is: <em>"The painting was displayed by the curator."</em> The object becomes the new subject.',
    )

    st.divider()

    quiz_block(
        3,
        "Which sentence is in the Passive Voice?",
        "Select the passive sentence below:",
        ["Witnesses filmed the incident.",
         "The incident was filmed by witnesses.",
         "The witnesses ran away quickly."],
        correct_idx=1,
        fb_ok='"The incident was filmed by witnesses" is passive — "was filmed" (to be + past participle) is the giveaway. Ready for the Headline Builder!',
        fb_bad='The passive sentence is: <em>"The incident was filmed by witnesses."</em> Look for the <em>was/were + past participle</em> pattern.',
    )

# ══════════════════════════════════════════════════════════════════════════════
# SLIDE 5 – Headline Builder
# ══════════════════════════════════════════════════════════════════════════════
elif slide == 5:
    st.markdown("""
    <div class="slide-box">
      <div class="slide-num">05 / 06 — Headline Builder</div>
      <h2 class="slide-title">Writing Challenge: The Headline Maker</h2>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="newspaper">
      <div class="np-header">
        <div class="np-name">The Daily Gazette</div>
        <div class="np-tag">All the News That's Fit to Passive-ify</div>
      </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("#### Build your passive headline:")

    col1, col2, col3 = st.columns(3)
    with col1:
        obj = st.selectbox("📌 Object", ["— choose —", "A rare diamond", "The museum gates", "Security cameras"])
    with col2:
        verb = st.selectbox("🔗 Verb to be", ["— choose —", "is", "was", "were"])
    with col3:
        pp = st.selectbox("✏️ Past participle", ["— choose —", "finding", "find", "found"])

    # Live preview
    obj_val  = "" if obj  == "— choose —" else obj
    verb_val = "" if verb == "— choose —" else verb
    pp_val   = "" if pp   == "— choose —" else pp

    preview = f'{obj_val or "___"} {verb_val or "___"} {pp_val or "___"}'
    st.markdown(f"""
    <div class="newspaper">
      <div class="np-headline">{preview}</div>
    </div>
    """, unsafe_allow_html=True)

    all_selected = obj_val and verb_val and pp_val
    if st.button("Check My Headline →", disabled=not all_selected):
        st.session_state.hl_checked = True
        st.session_state.hl_obj  = obj_val
        st.session_state.hl_verb = verb_val
        st.session_state.hl_pp   = pp_val

    if st.session_state.hl_checked:
        o = st.session_state.hl_obj
        v = st.session_state.hl_verb
        p = st.session_state.hl_pp
        agree = {"A rare diamond": "was", "The museum gates": "were", "Security cameras": "were"}
        correct_pp   = (p == "found")
        correct_verb = (v == agree.get(o, ""))
        if correct_pp and correct_verb:
            st.markdown('<div class="fb ok">✅ <strong>Excellent!</strong> Perfect passive construction — object first, correct <em>to be</em>, and the right past participle. You\'re ready for Fleet Street!</div>', unsafe_allow_html=True)
        elif correct_pp and not correct_verb:
            st.markdown(f'<div class="fb mid">🟡 <strong>Almost!</strong> The past participle is right (<em>found ✓</em>), but "{o}" needs <em>{agree.get(o,"")}</em>, not <em>{v}</em>.</div>', unsafe_allow_html=True)
        else:
            st.markdown('<div class="fb bad">❌ <strong>Check the verb form.</strong> The past participle of <em>find</em> is <strong>found</strong>, not <em>finding</em> or <em>find</em>. Try again!</div>', unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
# SLIDE 6 – Write Your Own
# ══════════════════════════════════════════════════════════════════════════════
elif slide == 6:
    st.markdown("""
    <div class="slide-box">
      <div class="slide-num">06 / 06 — Your Turn</div>
      <h2 class="slide-title">Be the Reporter!</h2>
      <div class="reporter-note">
        <strong>✍️ Writing Challenge:</strong> Choose an active sentence below and rewrite it using
        <strong>passive voice</strong>. Imagine you're filing your report for the evening news.
      </div>
    </div>
    """, unsafe_allow_html=True)

    prompts = {
        "🍽️  A chef cooked the meal.":      ("the meal was cooked", "was cooked", "Think: what is the object?"),
        "🌉  Workers built the bridge.":      ("the bridge was built", "was built",  "Use were + past participle"),
        "🌪️  The storm destroyed the town.":  ("the town was destroyed", "was destroyed", "The town becomes the new subject"),
        "💊  Doctors discovered the cure.":   ("the cure was discovered", "was discovered", "Great for a formal news report"),
    }

    selected = st.radio("Choose a sentence to convert:", list(prompts.keys()), key="prompt_sel", index=None)

    if selected:
        # Show hint only after clicking
        if not st.session_state.get("hint_show", False):
            if st.button("💡 Show Hint", key="hint_btn"):
                st.session_state["hint_show"] = True
                st.rerun()
        else:
            st.markdown(f"**💡 Hint:** {prompts[selected][2]}")

        user_answer = st.text_input("Your passive sentence:", placeholder="Type your passive version here…", key="writing_ans")

        if st.button("Check My Answer", disabled=not (user_answer or "").strip()):
            st.session_state.writing_checked = True
            st.session_state["writing_ans_stored"] = user_answer
            st.session_state.writing_fb_show = False
            st.rerun()

        if st.session_state.writing_checked:
            if not st.session_state.writing_fb_show:
                if st.button("💬 Reveal Feedback", key="writing_fb_btn"):
                    st.session_state.writing_fb_show = True
                    st.rerun()
            else:
                ans = st.session_state.get("writing_ans_stored", "").lower().strip()
                correct_phrase, keyword, _ = prompts[selected]
                has_passive_verb = any(w in ans for w in ["is ", "are ", "was ", "were "])
                is_correct = correct_phrase in ans

                if is_correct:
                    st.markdown('<div class="fb ok">✅ <strong>Excellent work!</strong> Your sentence uses the passive voice correctly — the object is at the front and you\'ve used <em>was/were + past participle</em>. A real journalist\'s technique!</div>', unsafe_allow_html=True)
                    st.balloons()
                elif has_passive_verb:
                    st.markdown('<div class="fb mid">🟡 <strong>Good start!</strong> You\'ve included a passive verb (was/were) ✓ — double-check that the original <em>object</em> is now the subject and that the past participle is correct.</div>', unsafe_allow_html=True)
                else:
                    st.markdown('<div class="fb bad">❌ <strong>Keep trying!</strong> Remember: move the object to the front, add <em>was/were</em>, then the past participle. Example: "A chef cooked the meal" → <em>"The meal was cooked by a chef."</em></div>', unsafe_allow_html=True)
    else:
        st.info("👆 Select a sentence above to get started.")

# ══════════════════════════════════════════════════════════════════════════════
# Navigation bar
# ══════════════════════════════════════════════════════════════════════════════
st.markdown("---")
col_back, col_mid, col_next = st.columns([1, 2, 1])

with col_back:
    if st.button("← Back", disabled=(slide == 1), use_container_width=True):
        st.session_state.slide -= 1
        st.rerun()

with col_mid:
    # Progress dots using emoji
    dots = ""
    for i in range(1, 7):
        if i == slide:
            dots += "🔴 "
        elif i < slide:
            dots += "🔵 "
        else:
            dots += "⚪ "
    st.markdown(f"<div style='text-align:center; font-size:18px; padding-top:4px'>{dots}</div>", unsafe_allow_html=True)

with col_next:
    label = "Finish ✓" if slide == 6 else "Next →"
    if slide < 6:
        if st.button(label, use_container_width=True):
            st.session_state.slide += 1
            st.rerun()
    else:
        if st.button("🔄 Start Again", use_container_width=True):
            for key in list(st.session_state.keys()):
                del st.session_state[key]
            st.session_state.slide = 1
            st.rerun()
