import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Year 7 English – Passive Voice",
    page_icon="📰",
    layout="centered",
)

# Hide Streamlit chrome so only the lesson shows
st.markdown("""
<style>
#MainMenu, footer, header { visibility: hidden; }
.block-container { padding: 0 !important; max-width: 820px !important; }
.stApp { background: #2a1f14; }
</style>
""", unsafe_allow_html=True)

# ── The full lesson as a self-contained HTML string ───────────────────────────
HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700;900&family=Source+Serif+4:ital,wght@0,300;0,400;0,600;1,400&family=IBM+Plex+Mono:wght@400;600&display=swap" rel="stylesheet">
<style>
  :root {
    --ink: #1a1008; --paper: #f5f0e8; --aged: #e8dfc8;
    --accent: #c8392b; --accent2: #2563a8; --gold: #c9963a;
    --serif: 'Playfair Display', Georgia, serif;
    --body: 'Source Serif 4', Georgia, serif;
    --mono: 'IBM Plex Mono', monospace;
  }
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body {
    font-family: var(--body);
    background: #2a1f14;
    background-image:
      radial-gradient(ellipse at 20% 50%, rgba(200,57,43,0.08) 0%, transparent 60%),
      radial-gradient(ellipse at 80% 20%, rgba(37,99,168,0.08) 0%, transparent 60%);
    padding: 20px;
  }
  .lesson-wrapper { width: 100%; max-width: 780px; margin: 0 auto; }

  .lesson-header {
    display: flex; align-items: center; justify-content: space-between;
    padding: 10px 18px; background: var(--ink);
    border-radius: 6px 6px 0 0; border-bottom: 3px solid var(--gold);
  }
  .subject-tag { font-family: var(--mono); font-size: 10px; letter-spacing: 0.15em; color: var(--gold); text-transform: uppercase; }
  .lesson-title-bar { font-family: var(--serif); font-size: 13px; color: var(--paper); font-weight: 700; }

  .slide {
    display: none; background: var(--paper);
    min-height: 480px; padding: 36px 44px 28px;
    position: relative; overflow: hidden;
  }
  .slide.active { display: block; animation: slideIn 0.3s ease; }
  .slide::before {
    content: ''; position: absolute; top: 0; left: 0;
    width: 5px; height: 100%;
    background: linear-gradient(to bottom, var(--accent), var(--accent2));
  }
  @keyframes slideIn { from { opacity:0; transform:translateX(24px); } to { opacity:1; transform:translateX(0); } }
  @keyframes pulse { 0%,100%{opacity:1} 50%{opacity:0.7} }

  .slide-number { font-family: var(--mono); font-size: 11px; color: #888; letter-spacing: 0.1em; margin-bottom: 8px; }
  h1 { font-family: var(--serif); font-size: 28px; font-weight: 900; color: var(--ink); line-height: 1.15; margin-bottom: 20px; border-bottom: 2px solid var(--aged); padding-bottom: 12px; }
  h2 { font-family: var(--serif); font-size: 18px; font-weight: 700; color: var(--ink); margin: 18px 0 8px; }
  p, li { font-size: 15px; line-height: 1.65; color: #2e2010; }

  /* Slide 1 */
  .breaking-banner { background: var(--accent); color: white; font-family: var(--mono); font-size: 11px; letter-spacing: 0.12em; padding: 5px 12px; display: inline-block; margin-bottom: 16px; border-radius: 2px; animation: pulse 2s infinite; }
  .news-box { background: white; border: 2px solid var(--ink); border-radius: 4px; padding: 20px 24px; margin: 14px 0; box-shadow: 4px 4px 0 var(--ink); position: relative; }
  .news-box::after { content: '🎙️'; position: absolute; top: -12px; right: 14px; font-size: 22px; }
  .reporter-note { background: var(--aged); border-left: 4px solid var(--gold); padding: 12px 16px; margin-top: 16px; border-radius: 0 4px 4px 0; font-style: italic; font-size: 14px; }
  .term { background: rgba(201,150,58,0.18); border-radius: 2px; padding: 0 3px; font-weight: 600; }

  /* Slide 2 */
  .two-col { display: grid; grid-template-columns: 1fr 1fr; gap: 16px; margin: 12px 0; }
  .voice-card { border-radius: 6px; padding: 16px; border: 2px solid; }
  .voice-card.active-card { border-color: var(--accent2); background: #eef4ff; }
  .voice-card.passive-card { border-color: var(--accent); background: #fff2f0; }
  .voice-card h3 { font-family: var(--serif); font-size: 15px; font-weight: 700; margin-bottom: 6px; }
  .voice-card .example { font-family: var(--mono); font-size: 13px; background: white; border-radius: 3px; padding: 8px 10px; margin: 8px 0; border: 1px solid #ddd; }
  .voice-card .flow { font-size: 12px; color: #666; font-style: italic; }
  .passive-hidden { font-family: var(--mono); font-size: 12px; color: #bbb; font-style: italic; padding: 8px 10px; border: 1px dashed #ddd; border-radius: 3px; margin: 8px 0; }
  .reveal-passive-btn { margin-top: 12px; background: var(--accent2); color: white; border: none; border-radius: 4px; padding: 9px 18px; font-family: var(--serif); font-size: 13px; font-weight: 700; cursor: pointer; }
  .reveal-passive-btn:hover { background: #1a4d8a; }
  .recipe-box { background: var(--aged); border-radius: 6px; padding: 16px 20px; margin-top: 14px; }
  .recipe-box h3 { font-family: var(--serif); font-size: 15px; font-weight: 700; margin-bottom: 10px; }
  .recipe-steps { list-style: none; counter-reset: step; }
  .recipe-steps li { counter-increment: step; padding: 4px 0 4px 28px; position: relative; font-size: 14px; border-bottom: 1px dashed #c8b98a; }
  .recipe-steps li:last-child { border-bottom: none; }
  .recipe-steps li::before { content: counter(step); position: absolute; left: 0; top: 5px; width: 20px; height: 20px; background: var(--gold); color: white; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-family: var(--mono); font-size: 11px; font-weight: 600; }

  /* Slide 3 */
  .reasons-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 12px; margin: 12px 0; }
  .reason-card { background: white; border: 1.5px solid var(--aged); border-radius: 6px; padding: 12px 14px; position: relative; }
  .reason-num { font-family: var(--mono); font-size: 28px; font-weight: 600; color: var(--aged); position: absolute; top: 6px; right: 10px; line-height: 1; }
  .reason-card h3 { font-size: 13px; font-weight: 700; font-family: var(--serif); color: var(--ink); margin-bottom: 4px; }
  .reason-card p { font-size: 12.5px; color: #444; line-height: 1.5; }
  .headline-row { display: flex; align-items: stretch; border: 1.5px solid var(--ink); border-radius: 4px; overflow: hidden; margin-top: 10px; }
  .hl-content { padding: 12px 16px; flex: 1; }
  .hl-content.informal { background: #fff8f0; border-right: 2px dashed #ddd; }
  .hl-content.formal { background: #f0f8ff; }
  .hl-content .label { font-family: var(--mono); font-size: 10px; color: #888; margin-bottom: 4px; }
  .hl-content p { font-size: 14px; font-weight: 600; }

  /* Slide 4 */
  .quiz-question-label { font-family: var(--mono); font-size: 12px; color: var(--accent); letter-spacing: 0.1em; margin-bottom: 10px; }
  .sentence-display { background: var(--ink); color: var(--paper); font-family: var(--mono); font-size: 17px; padding: 16px 22px; border-radius: 6px; margin: 14px 0; border-left: 4px solid var(--gold); }
  .options { display: flex; flex-direction: column; gap: 10px; margin-top: 18px; }
  .option-btn { background: white; border: 2px solid #ddd; border-radius: 6px; padding: 13px 18px; font-family: var(--body); font-size: 15px; cursor: pointer; text-align: left; transition: all 0.18s; color: var(--ink); }
  .option-btn:hover { border-color: var(--accent2); background: #eef4ff; }
  .option-btn.correct { border-color: #1a8c4e; background: #eafaf1; color: #1a5c34; }
  .option-btn.wrong   { border-color: var(--accent); background: #fff0ee; color: #8c1a0e; }
  .feedback-box { display: none; margin-top: 14px; border-radius: 6px; padding: 12px 16px; font-size: 14px; line-height: 1.5; }
  .feedback-box.show { display: block; }
  .feedback-box.correct { background: #eafaf1; border: 1.5px solid #1a8c4e; color: #1a5c34; }
  .feedback-box.wrong   { background: #fff0ee; border: 1.5px solid #c0392b; color: #7b1a0e; }

  /* Slide 5 */
  .newspaper-mock { background: white; border: 2px solid var(--ink); border-radius: 4px; overflow: hidden; box-shadow: 4px 4px 0 var(--ink); }
  .newspaper-header { background: var(--ink); text-align: center; padding: 10px 14px 8px; border-bottom: 3px double var(--gold); }
  .newspaper-name    { font-family: var(--serif); font-size: 22px; font-weight: 900; letter-spacing: 0.04em; color: var(--paper); }
  .newspaper-tagline { font-family: var(--mono); font-size: 9px; letter-spacing: 0.12em; color: var(--gold); margin-top: 2px; }
  .headline-display  { padding: 20px 24px 14px; min-height: 72px; display: flex; align-items: center; justify-content: center; text-align: center; border-bottom: 2px solid var(--aged); }
  .headline-text     { font-family: var(--serif); font-size: 22px; font-weight: 900; color: var(--ink); line-height: 1.2; transition: all 0.3s; }
  .headline-text .blank  { color: #bbb; font-style: italic; }
  .headline-text .filled { color: var(--accent); text-decoration: underline wavy var(--gold) 1.5px; }
  .builder-area { padding: 18px 24px; }
  .builder-area h3 { font-family: var(--serif); font-size: 14px; font-weight: 700; margin-bottom: 14px; color: #555; }
  .builder-row { display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 12px; }
  .builder-group label { display: block; font-family: var(--mono); font-size: 10px; letter-spacing: 0.1em; color: #888; margin-bottom: 5px; text-transform: uppercase; }
  .builder-group select { width: 100%; padding: 9px 10px; border: 2px solid #ddd; border-radius: 4px; font-family: var(--body); font-size: 13px; background: white; color: var(--ink); cursor: pointer; }
  .builder-group select:focus { outline: none; border-color: var(--accent2); }
  .print-btn { display: block; width: 100%; margin-top: 14px; background: var(--ink); color: var(--paper); border: none; border-radius: 4px; padding: 12px; font-family: var(--serif); font-size: 15px; font-weight: 700; cursor: pointer; letter-spacing: 0.04em; transition: background 0.15s; }
  .print-btn:hover { background: var(--accent); }
  .print-btn:disabled { background: #bbb; cursor: default; }

  /* Slide 6 */
  .challenge-intro { background: linear-gradient(135deg, #1a1008 0%, #2a1f14 100%); color: var(--paper); border-radius: 8px; padding: 18px 22px; margin-bottom: 18px; position: relative; overflow: hidden; }
  .challenge-intro::after { content: '✍️'; position: absolute; right: 16px; top: 50%; transform: translateY(-50%); font-size: 36px; }
  .challenge-intro h2 { color: var(--gold); font-size: 16px; margin: 0 0 6px; }
  .challenge-intro p  { font-size: 13.5px; line-height: 1.6; color: #d0c8b8; max-width: 78%; }
  .prompts-list { display: grid; grid-template-columns: 1fr 1fr; gap: 10px; margin-bottom: 16px; }
  .prompt-card { background: white; border: 1.5px solid var(--aged); border-radius: 6px; padding: 12px 14px; cursor: pointer; transition: all 0.15s; }
  .prompt-card:hover   { border-color: var(--accent2); box-shadow: 2px 2px 0 var(--accent2); }
  .prompt-card.selected { border-color: var(--accent); background: #fff5f4; box-shadow: 2px 2px 0 var(--accent); }
  .prompt-card .active-sent { font-family: var(--mono); font-size: 11.5px; color: var(--accent); margin-bottom: 4px; font-weight: 600; }
  .prompt-card .hint { font-size: 11.5px; color: #888; }
  .write-area-wrap label { font-family: var(--mono); font-size: 10px; letter-spacing: 0.1em; color: #888; display: block; margin-bottom: 5px; text-transform: uppercase; }
  .write-area { width: 100%; min-height: 70px; padding: 12px 14px; border: 2px solid #ddd; border-radius: 6px; font-family: var(--body); font-size: 15px; resize: vertical; color: var(--ink); transition: border-color 0.15s; }
  .write-area:focus { outline: none; border-color: var(--accent2); }
  .check-btn { margin-top: 10px; background: var(--accent2); color: white; border: none; border-radius: 4px; padding: 11px 22px; font-family: var(--serif); font-size: 14px; font-weight: 700; cursor: pointer; transition: background 0.15s; }
  .check-btn:hover { background: #1a4d8a; }
  .check-btn:disabled { background: #aac0dc; cursor: default; }
  .writing-feedback { display: none; margin-top: 12px; border-radius: 6px; padding: 12px 16px; font-size: 13.5px; line-height: 1.6; }
  .writing-feedback.show    { display: block; }
  .writing-feedback.good    { background: #eafaf1; border: 1.5px solid #1a8c4e; color: #1a5c34; }
  .writing-feedback.partial { background: #fffbe8; border: 1.5px solid #c9963a; color: #6b4d0e; }
  .writing-feedback.error   { background: #fff0ee; border: 1.5px solid #c0392b; color: #7b1a0e; }

  /* Nav */
  .nav-bar { background: var(--aged); border-top: 2px solid #c8b98a; border-radius: 0 0 6px 6px; padding: 12px 20px; display: flex; align-items: center; justify-content: space-between; }
  .nav-btn { background: var(--ink); color: var(--paper); border: none; border-radius: 4px; padding: 9px 22px; font-family: var(--serif); font-size: 14px; font-weight: 700; cursor: pointer; letter-spacing: 0.03em; transition: background 0.15s; }
  .nav-btn:hover { background: var(--accent); }
  .nav-btn:disabled { background: #ccc; cursor: default; color: #999; }
  .progress-dots { display: flex; gap: 8px; align-items: center; }
  .dot { width: 10px; height: 10px; border-radius: 50%; background: #c8b98a; transition: all 0.2s; cursor: pointer; }
  .dot.active  { background: var(--accent); transform: scale(1.3); }
  .dot.visited { background: var(--accent2); }

  @media (max-width: 560px) {
    .slide { padding: 24px 20px 20px; }
    .two-col, .reasons-grid, .builder-row, .prompts-list { grid-template-columns: 1fr; }
    h1 { font-size: 22px; }
    .headline-text { font-size: 18px; }
  }
</style>
</head>
<body>
<div class="lesson-wrapper">

  <div class="lesson-header">
    <span class="subject-tag">Year 7 · English Language</span>
    <span class="lesson-title-bar">Mastering Passive Voice</span>
  </div>

  <!-- SLIDE 1 -->
  <div class="slide active" id="slide-1">
    <div class="slide-number">01 / 06 — Introduction</div>
    <h1>The Scene of the Crime</h1>
    <div class="breaking-banner">🔴 BREAKING NEWS · LIVE COVERAGE</div>
    <div class="news-box">
      <p><em>"We're coming to you live from the Royal Museum, where a priceless masterpiece vanished just minutes ago. The security guards are baffled. Someone stole the painting, but we don't know who… yet."</em></p>
    </div>
    <div class="reporter-note">
      <strong>Reporter's Note:</strong> In news reports, we often focus on <em>what happened</em> rather than <em>who did it</em>. This is where the <span class="term">Passive Voice</span> becomes our most powerful tool.
    </div>
    <p style="margin-top:16px; font-size:14px; color:#666;">Over the next six slides, you will learn how passive voice is formed, why journalists love it, and how to use it yourself. Let's begin.</p>
  </div>

  <!-- SLIDE 2 -->
  <div class="slide" id="slide-2">
    <div class="slide-number">02 / 06 — Grammar Basics</div>
    <h1>Active vs. Passive: The Basics</h1>
    <div class="two-col">
      <div class="voice-card active-card">
        <h3>🔵 Active Voice</h3>
        <p style="font-size:13px;">The subject <em>performs</em> the action.</p>
        <div class="example">"The thief stole the painting."</div>
        <div class="flow">Subject (Doer) → Action → Object</div>
      </div>
      <div class="voice-card passive-card">
        <h3>🔴 Passive Voice</h3>
        <p style="font-size:13px;">The subject is <em>acted upon</em>.</p>
        <div id="passive-example" class="passive-hidden">[ Click the button below to reveal the passive example ]</div>
        <div id="passive-flow" class="flow" style="display:none;">Object → Was/Were + Past Participle</div>
      </div>
    </div>
    <button class="reveal-passive-btn" id="reveal-btn" onclick="revealPassive()">👁️ Reveal Passive Example</button>
    <div class="recipe-box" id="recipe-box" style="display:none;">
      <h3>📋 The Recipe for Passive Voice</h3>
      <ol class="recipe-steps">
        <li><strong>Move the Object</strong> to the front of the sentence.</li>
        <li><strong>Add 'to be'</strong> (is, are, was, were) in the correct tense.</li>
        <li><strong>Change the main verb</strong> to its <span class="term">Past Participle</span> (eaten, seen, stolen…).</li>
        <li>The <strong>doer (agent)</strong> is optional — add "by [someone]" only when needed.</li>
      </ol>
    </div>
  </div>

  <!-- SLIDE 3 -->
  <div class="slide" id="slide-3">
    <div class="slide-number">03 / 06 — Why Use It?</div>
    <h1>The Journalist's Secret</h1>
    <div class="reasons-grid">
      <div class="reason-card"><span class="reason-num">1</span><h3>Focus on the Victim / Action</h3><p>When the event or victim matters more than who caused it.</p></div>
      <div class="reason-card"><span class="reason-num">2</span><h3>Objectivity</h3><p>Makes reports sound more formal, neutral, and scientific.</p></div>
      <div class="reason-card"><span class="reason-num">3</span><h3>The Doer is Unknown</h3><p>Perfect for crime stories when we don't know who acted.</p></div>
      <div class="reason-card"><span class="reason-num">4</span><h3>To Avoid Blame</h3><p>Hides responsibility — e.g., <em>"Mistakes were made."</em></p></div>
    </div>
    <h2>Compare These Headlines</h2>
    <div class="headline-row">
      <div class="hl-content informal"><div class="label">Informal / Active</div><p>"Someone smashed a window at the library!"</p></div>
      <div class="hl-content formal"><div class="label">Formal / Passive (Journalistic)</div><p>"Library window smashed in late-night incident."</p></div>
    </div>
  </div>

  <!-- SLIDE 4 -->
  <div class="slide" id="slide-4">
    <div class="slide-number">04 / 06 — Quick Practice</div>
    <h1>Practice: Reporting the Facts</h1>
    <div id="q1-section">
      <div class="quiz-question-label">QUESTION 1 OF 3</div>
      <p>Convert this <strong>Active</strong> sentence to <strong>Passive</strong>:</p>
      <div class="sentence-display">"Police arrested the suspect."</div>
      <div class="options" id="q1-options" style="display:none;">
        <button class="option-btn" onclick="checkQ1(this,false)">"The suspect arrested police."</button>
        <button class="option-btn" onclick="checkQ1(this,true)">"The suspect was arrested."</button>
        <button class="option-btn" onclick="checkQ1(this,false)">"Arrested was the suspect."</button>
      </div>
      <button id="q1-show-btn" class="reveal-passive-btn" onclick="showOptions('q1-options','q1-show-btn')" style="margin-top:12px;">👁️ Show Answer Options</button>
      <div class="feedback-box" id="q1-feedback"></div>
    </div>
    <div id="q2-section" style="display:none; margin-top:18px;">
      <div class="quiz-question-label">QUESTION 2 OF 3</div>
      <p>Convert this sentence to <strong>Passive Voice</strong>:</p>
      <div class="sentence-display">"The curator displayed the painting."</div>
      <div class="options" id="q2-options" style="display:none;">
        <button class="option-btn" onclick="checkQ2(this,false)">"The curator was displayed the painting."</button>
        <button class="option-btn" onclick="checkQ2(this,true)">"The painting was displayed by the curator."</button>
        <button class="option-btn" onclick="checkQ2(this,false)">"The painting displayed the curator."</button>
      </div>
      <button id="q2-show-btn" class="reveal-passive-btn" onclick="showOptions('q2-options','q2-show-btn')" style="margin-top:12px;">👁️ Show Answer Options</button>
      <div class="feedback-box" id="q2-feedback"></div>
    </div>
    <div id="q3-section" style="display:none; margin-top:18px;">
      <div class="quiz-question-label">QUESTION 3 OF 3</div>
      <p>Which sentence is in the <strong>Passive Voice</strong>?</p>
      <div class="sentence-display">Select the passive sentence below:</div>
      <div class="options" id="q3-options" style="display:none;">
        <button class="option-btn" onclick="checkQ3(this,false)">"Witnesses filmed the incident."</button>
        <button class="option-btn" onclick="checkQ3(this,true)">"The incident was filmed by witnesses."</button>
        <button class="option-btn" onclick="checkQ3(this,false)">"The witnesses ran away quickly."</button>
      </div>
      <button id="q3-show-btn" class="reveal-passive-btn" onclick="showOptions('q3-options','q3-show-btn')" style="margin-top:12px;">👁️ Show Answer Options</button>
      <div class="feedback-box" id="q3-feedback"></div>
    </div>
  </div>

  <!-- SLIDE 5 -->
  <div class="slide" id="slide-5">
    <div class="slide-number">05 / 06 — Headline Builder</div>
    <h1>Writing Challenge: The Headline Maker</h1>
    <div class="newspaper-mock">
      <div class="newspaper-header">
        <div class="newspaper-name">The Daily Gazette</div>
        <div class="newspaper-tagline">All the News That's Fit to Passive-ify</div>
      </div>
      <div class="headline-display">
        <div class="headline-text" id="headline-preview">
          <span class="blank" id="hl-obj">___ ___</span>&nbsp;
          <span class="blank" id="hl-verb">___</span>&nbsp;
          <span class="blank" id="hl-pp">___</span>
        </div>
      </div>
      <div class="builder-area">
        <h3>Build your passive headline by selecting each part:</h3>
        <div class="builder-row">
          <div class="builder-group">
            <label>Select object</label>
            <select id="sel-obj" onchange="buildHeadline()">
              <option value="">— choose —</option>
              <option>A rare diamond</option>
              <option>The museum gates</option>
              <option>Security cameras</option>
            </select>
          </div>
          <div class="builder-group">
            <label>Select verb to be</label>
            <select id="sel-verb" onchange="buildHeadline()">
              <option value="">— choose —</option>
              <option>is</option><option>was</option><option>were</option>
            </select>
          </div>
          <div class="builder-group">
            <label>Select past participle</label>
            <select id="sel-pp" onchange="buildHeadline()">
              <option value="">— choose —</option>
              <option>finding</option><option>find</option><option>found</option>
            </select>
          </div>
        </div>
        <button class="print-btn" id="print-btn" onclick="checkHeadline()" disabled>Check My Headline →</button>
        <div class="feedback-box" id="headline-feedback"></div>
      </div>
    </div>
  </div>

  <!-- SLIDE 6 -->
  <div class="slide" id="slide-6">
    <div class="slide-number">06 / 06 — Your Turn</div>
    <h1>Be the Reporter!</h1>
    <div class="challenge-intro">
      <h2>Writing Challenge</h2>
      <p>Choose an active sentence below and rewrite it using <strong>passive voice</strong>. Imagine you're filing your report for the evening news.</p>
    </div>
    <div class="prompts-list">
      <div class="prompt-card" id="p1" onclick="selectPrompt(1)">
        <div class="active-sent">Active: "A chef cooked the meal."</div>
        <div class="hint">💡 Think: what is the "object" here?</div>
      </div>
      <div class="prompt-card" id="p2" onclick="selectPrompt(2)">
        <div class="active-sent">Active: "Workers built the bridge."</div>
        <div class="hint">💡 Use <em>were</em> + past participle</div>
      </div>
      <div class="prompt-card" id="p3" onclick="selectPrompt(3)">
        <div class="active-sent">Active: "The storm destroyed the town."</div>
        <div class="hint">💡 The town becomes the new subject</div>
      </div>
      <div class="prompt-card" id="p4" onclick="selectPrompt(4)">
        <div class="active-sent">Active: "Doctors discovered the cure."</div>
        <div class="hint">💡 Great for a formal news report</div>
      </div>
    </div>
    <div class="write-area-wrap">
      <label>Your passive sentence:</label>
      <textarea class="write-area" id="writing-input" placeholder="Select a sentence above, then write your passive version here…" oninput="toggleCheckBtn()"></textarea>
    </div>
    <button class="check-btn" id="writing-check-btn" onclick="checkWriting()" disabled>Check My Answer</button>
    <div class="writing-feedback" id="writing-feedback"></div>
  </div>

  <!-- Navigation -->
  <div class="nav-bar">
    <button class="nav-btn" id="back-btn" onclick="goSlide(-1)" disabled>← Back</button>
    <div class="progress-dots" id="dots"></div>
    <button class="nav-btn" id="next-btn" onclick="goSlide(1)">Next →</button>
  </div>

</div>
<script>
  let current = 1;
  const total = 6;

  // Build dots
  const dotsEl = document.getElementById('dots');
  for (let i = 1; i <= total; i++) {
    const d = document.createElement('div');
    d.className = 'dot' + (i === 1 ? ' active' : '');
    d.onclick = () => jumpSlide(i);
    d.id = 'dot-' + i;
    dotsEl.appendChild(d);
  }

  function jumpSlide(n) {
    document.getElementById('slide-' + current).classList.remove('active');
    document.getElementById('dot-' + current).classList.remove('active');
    document.getElementById('dot-' + current).classList.add('visited');
    current = n;
    document.getElementById('slide-' + current).classList.add('active');
    document.getElementById('dot-' + current).classList.remove('visited');
    document.getElementById('dot-' + current).classList.add('active');
    document.getElementById('back-btn').disabled = current === 1;
    document.getElementById('next-btn').disabled = current === total;
    document.getElementById('next-btn').textContent = current === total ? 'Finish ✓' : 'Next →';
  }
  function goSlide(dir) { jumpSlide(Math.min(Math.max(1, current + dir), total)); }

  // Slide 2 – reveal passive example
  function revealPassive() {
    const ex = document.getElementById('passive-example');
    ex.className = 'example';
    ex.textContent = '"The painting was stolen (by the thief)."';
    document.getElementById('passive-flow').style.display = 'block';
    document.getElementById('reveal-btn').style.display = 'none';
    document.getElementById('recipe-box').style.display = 'block';
  }

  // Slide 4 – show options
  function showOptions(optId, btnId) {
    document.getElementById(optId).style.display = 'flex';
    document.getElementById(btnId).style.display = 'none';
  }

  let q1done = false, q2done = false, q3done = false;
  function lockButtons(sec) { document.querySelectorAll('#' + sec + ' .option-btn').forEach(b => b.disabled = true); }

  function checkQ1(btn, correct) {
    if (q1done) return; q1done = true;
    const fb = document.getElementById('q1-feedback');
    btn.classList.add(correct ? 'correct' : 'wrong');
    fb.className = 'feedback-box ' + (correct ? 'correct' : 'wrong') + ' show';
    fb.innerHTML = correct
      ? '✅ <strong>Correct!</strong> "The suspect" (the object) moves to the front, and "was arrested" (was + past participle of <em>arrest</em>) follows. Well done!'
      : '❌ <strong>Not quite.</strong> Remember the recipe: move the object to the front, then add <em>was/were</em> + past participle. The answer is: <em>"The suspect was arrested."</em>';
    lockButtons('q1-section');
    setTimeout(() => { document.getElementById('q2-section').style.display = 'block'; }, 800);
  }

  function checkQ2(btn, correct) {
    if (q2done) return; q2done = true;
    const fb = document.getElementById('q2-feedback');
    btn.classList.add(correct ? 'correct' : 'wrong');
    fb.className = 'feedback-box ' + (correct ? 'correct' : 'wrong') + ' show';
    fb.innerHTML = correct
      ? '✅ <strong>Brilliant!</strong> "The painting" moves to the front, "was displayed" is the passive verb, and "by the curator" tells us the doer.'
      : '❌ <strong>Not quite.</strong> The correct passive is: <em>"The painting was displayed by the curator."</em> The object becomes the new subject.';
    lockButtons('q2-section');
    setTimeout(() => { document.getElementById('q3-section').style.display = 'block'; }, 800);
  }

  function checkQ3(btn, correct) {
    if (q3done) return; q3done = true;
    const fb = document.getElementById('q3-feedback');
    btn.classList.add(correct ? 'correct' : 'wrong');
    fb.className = 'feedback-box ' + (correct ? 'correct' : 'wrong') + ' show';
    fb.innerHTML = correct
      ? '✅ <strong>Perfect!</strong> "The incident was filmed by witnesses" is passive — "was filmed" is the give-away (to be + past participle). Ready for the Headline Builder!'
      : '❌ The passive sentence is: <em>"The incident was filmed by witnesses."</em> Look for the <em>was/were + past participle</em> pattern.';
    lockButtons('q3-section');
  }

  // Slide 5
  function buildHeadline() {
    const obj = document.getElementById('sel-obj').value;
    const verb = document.getElementById('sel-verb').value;
    const pp = document.getElementById('sel-pp').value;
    const objEl = document.getElementById('hl-obj');
    const verbEl = document.getElementById('hl-verb');
    const ppEl = document.getElementById('hl-pp');
    objEl.textContent = obj || '___ ___'; objEl.className = obj ? 'filled' : 'blank';
    verbEl.textContent = verb || '___';   verbEl.className = verb ? 'filled' : 'blank';
    ppEl.textContent = pp || '___';       ppEl.className = pp ? 'filled' : 'blank';
    document.getElementById('print-btn').disabled = !(obj && verb && pp);
  }

  function checkHeadline() {
    const obj = document.getElementById('sel-obj').value;
    const verb = document.getElementById('sel-verb').value;
    const pp = document.getElementById('sel-pp').value;
    const fb = document.getElementById('headline-feedback');
    const agree = {'A rare diamond':'was','The museum gates':'were','Security cameras':'were'};
    const okPP = pp === 'found';
    const okVerb = verb === agree[obj];
    if (okPP && okVerb) {
      fb.className = 'feedback-box correct show';
      fb.innerHTML = '✅ <strong>Excellent headline!</strong> "' + obj + ' ' + verb + ' ' + pp + '" is a perfect passive construction. You\'re ready for Fleet Street!';
    } else if (okPP && !okVerb) {
      fb.className = 'feedback-box wrong show';
      fb.innerHTML = '🟡 <strong>Almost!</strong> The past participle is right (<em>found ✓</em>), but "' + obj + '" needs <em>' + agree[obj] + '</em>, not <em>' + verb + '</em>.';
    } else {
      fb.className = 'feedback-box wrong show';
      fb.innerHTML = '❌ <strong>Check the verb form.</strong> <em>' + pp + '</em> is not a past participle. The past participle of <em>find</em> is <strong>found</strong>. Try again!';
    }
  }

  // Slide 6
  const correctAnswers = {
    1: ['the meal was cooked','was cooked'],
    2: ['the bridge was built','was built'],
    3: ['the town was destroyed','was destroyed'],
    4: ['the cure was discovered','was discovered']
  };
  let selectedPrompt = 0;

  function selectPrompt(n) {
    document.querySelectorAll('.prompt-card').forEach(c => c.classList.remove('selected'));
    document.getElementById('p' + n).classList.add('selected');
    selectedPrompt = n;
    document.getElementById('writing-input').focus();
    document.getElementById('writing-feedback').className = 'writing-feedback';
    toggleCheckBtn();
  }

  function toggleCheckBtn() {
    const val = document.getElementById('writing-input').value.trim();
    document.getElementById('writing-check-btn').disabled = !(selectedPrompt && val.length > 3);
  }

  function checkWriting() {
    const input = document.getElementById('writing-input').value.toLowerCase().trim();
    const fb = document.getElementById('writing-feedback');
    if (!selectedPrompt) return;
    const checks = correctAnswers[selectedPrompt];
    const hasPassiveVerb = /\\b(is|are|was|were)\\b/.test(input);
    const hasCorrectContent = checks.some(c => input.includes(c));
    if (hasCorrectContent) {
      fb.className = 'writing-feedback good show';
      fb.innerHTML = '✅ <strong>Excellent work!</strong> Your sentence uses the passive voice correctly — the object has moved to the front and you\\'ve used <em>was/were + past participle</em>. A real journalist\\'s technique!';
    } else if (hasPassiveVerb) {
      fb.className = 'writing-feedback partial show';
      fb.innerHTML = '🟡 <strong>Good start!</strong> You\\'ve included a passive verb (was/were), which is great. Double-check that the original <em>object</em> is now the subject of your sentence, and that the past participle is correct.';
    } else {
      fb.className = 'writing-feedback error show';
      fb.innerHTML = '❌ <strong>Keep trying!</strong> Remember the recipe: move the object to the front, add <em>was/were</em>, then the past participle. For example, "A chef cooked the meal" → <em>"The meal was cooked by a chef."</em>';
    }
  }
</script>
</body>
</html>
"""

components.html(HTML, height=700, scrolling=True)
