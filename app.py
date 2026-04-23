import streamlit as st
from predictor import *

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="AI Health Assistant", layout="wide")

# ---------------- PREMIUM UI (CSS) ----------------

def divider():
    st.markdown("<div class='divider'></div>", unsafe_allow_html=True)

def space(h=20):
    st.markdown(f"<div style='height:{h}px'></div>", unsafe_allow_html=True) 
    
st.markdown("""
<style>

/* GLOBAL */
.stApp {
    background: #0b1220;
    color: #e2e8f0;
    font-family: 'Inter', sans-serif;
}

/* CONTAINER */
.block-container {
    padding: 1.5rem 3rem;
}

/* SIDEBAR */
[data-testid="stSidebar"] {
    background: #0f172a;
    border-right: 1px solid rgba(255,255,255,0.05);
}

/* CARD (UPGRADED) */
.card {
    background: #111827;
    padding: 18px;
    border-radius: 16px;
    border: 1px solid rgba(255,255,255,0.06);
    transition: 0.2s ease;
}

.card:hover {
    transform: translateY(-3px);
    border: 1px solid rgba(99,102,241,0.3);
}

/* KPI CARD */
.kpi-card {
    padding: 14px;
}

.kpi-title {
    font-size: 12px;
    color: #94a3b8;
}

.kpi-value {
    font-size: 24px;
    font-weight: 600;
    margin-top: 5px;
}

/* SECTION SPACING */
.section {
    margin-top: 20px;
}

/* SUMMARY TEXT */
.summary {
    font-size: 14px;
    color: #cbd5f5;
}

/* BUTTON (UPGRADED) */
.stButton>button {
    background: #4f46e5;
    border-radius: 8px;
    padding: 6px 14px;
    font-size: 13px;
    transition: 0.2s;
}

.stButton>button:hover {
    background: #6366f1;
}

/* DIVIDER */
.divider {
    border-top: 1px solid rgba(255,255,255,0.08);
    margin: 20px 0;
}

/* TEXT IMPROVEMENTS */
h1, h2, h3 {
    font-weight: 600;
}

p {
    color: #cbd5f5;
}
/* SIDEBAR CONTAINER */
[data-testid="stSidebar"] {
    background: #0f172a;
    border-right: 1px solid rgba(255,255,255,0.05);
    padding-top: 10px;
}

/* RADIO GROUP */
div[role="radiogroup"] {
    gap: 4px;
}

/* MENU ITEM */
div[role="radiogroup"] > label {
    display: flex;
    align-items: center;
    padding: 10px 14px;
    border-radius: 10px;
    margin-bottom: 4px;
    border: 1px solid transparent;
    transition: all 0.2s ease;
    font-size: 14px;
}

/* HOVER */
div[role="radiogroup"] > label:hover {
    background: rgba(255,255,255,0.04);
}

/* ACTIVE */
div[role="radiogroup"] > label[data-checked="true"] {
    background: rgba(99,102,241,0.12);
    border: 1px solid rgba(99,102,241,0.35);
}

/* REMOVE RADIO DOT */
div[role="radiogroup"] input {
    display: none;
}
</style>
""", unsafe_allow_html=True)

if "page" not in st.session_state:
    st.session_state.page = "🏠 Home"

# if "analyze_clicked" not in st.session_state:
#     st.session_state.analyze_clicked = False

# ---------------- SIDEBAR ----------------
st.sidebar.markdown("""
<div style="padding-bottom:10px;">
    <h2 style="margin-bottom:2px;">🧠 Health AI</h2>
    <p style="color:#64748b; font-size:12px; margin-top:0;">
        Healthcare Dashboard
    </p>
</div>

<hr style="border:1px solid rgba(255,255,255,0.06)">
<p style="color:#64748b; font-size:11px; margin-bottom:8px;">
MENU
</p>
""", unsafe_allow_html=True)


page = st.sidebar.radio(
    "",
    ["🏠 Home", "🩺 Analyze","📊 Analytics","📜History" ,"ℹ️ About"],
    index=["🏠 Home", "🩺 Analyze", "📊 Analytics", "ℹ️ About"].index(st.session_state.page)
)

# ---------------- HOME PAGE ----------------
if page == "🏠 Home":

    # -------- HERO SECTION --------
    st.markdown("""
    <div style="
        padding: 30px 0;
        border-bottom: 1px solid rgba(255,255,255,0.08);
        margin-bottom: 25px;
    ">
        <h1 style="font-size:42px; margin-bottom:10px;">
            🧠 AI Health Assistant
        </h1>
        <p style="font-size:18px; color:#94a3b8; max-width:600px;">
            Intelligent symptom analysis, real-time predictions, and
            explainable health insights — all in one place.
        </p>
    </div>
    """, unsafe_allow_html=True)

    # -------- CTA BUTTONS --------
    col1, col2 = st.columns(2)

    with col1:
        if st.button("🚀 Start Analysis", key="home_analyze"):
            st.session_state.page = "🩺 Analyze"
            st.rerun()

    with col2:
        if st.button("📊 View Analytics", key="home_analytics"):
            st.session_state.page = "📊 Analytics"
            st.rerun()

    st.markdown("<div style='height:25px'></div>", unsafe_allow_html=True)

    # -------- KPI STATS --------
    col1, col2, col3, col4 = st.columns(4)

    col1.markdown("""
    <div class="card kpi-card">
        <div class="kpi-title">Predictions Made</div>
        <div class="kpi-value">120+</div>
    </div>
    """, unsafe_allow_html=True)

    col2.markdown("""
    <div class="card kpi-card">
        <div class="kpi-title">Accuracy</div>
        <div class="kpi-value">92%</div>
    </div>
    """, unsafe_allow_html=True)

    col3.markdown("""
    <div class="card kpi-card">
        <div class="kpi-title">Conditions Covered</div>
        <div class="kpi-value">25+</div>
    </div>
    """, unsafe_allow_html=True)

    col4.markdown("""
    <div class="card kpi-card">
        <div class="kpi-title">Users Helped</div>
        <div class="kpi-value">300+</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<div style='height:30px'></div>", unsafe_allow_html=True)

    # -------- FEATURES --------
    st.markdown("""
    <h2 style="font-weight:600; margin-bottom:5px;">Core Features</h2>
    <p style="color:#64748b; font-size:14px; margin-bottom:20px;">
    Key capabilities of the system
    </p>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        <div class="card">
            <p style="color:#94a3b8; font-size:12px;">01</p>
            <h4 style="margin-top:5px;">Disease Prediction</h4>
            <p style="color:#cbd5f5; font-size:14px;">
            Predicts possible conditions using symptom similarity logic.
            </p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("<div style='height:15px'></div>", unsafe_allow_html=True)

        st.markdown("""
        <div class="card">
            <p style="color:#94a3b8; font-size:12px;">02</p>
            <h4 style="margin-top:5px;">Drug Interaction Check</h4>
            <p style="color:#cbd5f5; font-size:14px;">
            Identifies risky combinations between medicines and habits.
            </p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("<div style='height:15px'></div>", unsafe_allow_html=True)

        st.markdown("""
        <div class="card">
            <p style="color:#94a3b8; font-size:12px;">03</p>
            <h4 style="margin-top:5px;">Explainable Results</h4>
            <p style="color:#cbd5f5; font-size:14px;">
            Provides reasoning and confidence behind predictions.
            </p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="card">
            <p style="color:#94a3b8; font-size:12px;">04</p>
            <h4 style="margin-top:5px;">Health Analytics</h4>
            <p style="color:#cbd5f5; font-size:14px;">
            Visual insights into your health trends over time.
            </p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("<div style='height:15px'></div>", unsafe_allow_html=True)

        st.markdown("""
        <div class="card">
            <p style="color:#94a3b8; font-size:12px;">05</p>
            <h4 style="margin-top:5px;">Report Generation</h4>
            <p style="color:#cbd5f5; font-size:14px;">
            Generates structured, medical-style reports.
            </p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("<div style='height:15px'></div>", unsafe_allow_html=True)

        st.markdown("""
        <div class="card">
            <p style="color:#94a3b8; font-size:12px;">06</p>
            <h4 style="margin-top:5px;">Real-Time Processing</h4>
            <p style="color:#cbd5f5; font-size:14px;">
            Fast predictions with minimal delay.
            </p>
        </div>
        """, unsafe_allow_html=True)

    # -------- WHY SECTION --------
    st.markdown("## 🚀 Why This App?")

    st.markdown("""
    <div class="card">
        <p style="font-size:16px; line-height:1.8;">
        Unlike basic symptom checkers, this system provides explainable results,
        tracks your health history, and helps you make better decisions through
        data-driven insights.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<div style='height:30px'></div>", unsafe_allow_html=True)

    # -------- FINAL CTA --------
    st.markdown("""
    <div class="card" style="text-align:center;">
        <h3>🚀 Ready to analyze your health?</h3>
        <p style="color:#94a3b8;">Start your AI-powered diagnosis now</p>
    </div>
    """, unsafe_allow_html=True)

# ---------------- ANALYZE PAGE ----------------
# ---------------- ANALYZE PAGE ----------------
elif page == "🩺 Analyze":

    st.title("🩺 Health Analysis")

    # -------- STATE INIT --------
    if "analyze_clicked" not in st.session_state:
        st.session_state.analyze_clicked = False
    
    if "result_clicked" not in st.session_state:
        st.session_state.result_clicked = False

    # -------- INPUTS --------
    user_text = st.text_area("Describe your symptoms", key="symptom_input")
    age = st.number_input("Enter Age", min_value=1, max_value=100, key="age_input")
    ongoing_meds = st.text_input("Ongoing Medications (optional)")
    
    duration = st.selectbox(
        "Symptom Duration",
        ["1-2 days", "3-5 days", "1 week+", "Chronic"]
    )
    
    severity = st.slider("Symptom Severity", 1, 10, 5)

    # -------- BUTTON --------
    if st.button("Analyze", key="analyze_btn1"):
        st.session_state.analyze_clicked = True

    # -------- AFTER CLICK --------
    if st.session_state.analyze_clicked:

        extracted = extract_symptoms(user_text)
        normalized = normalize_symptoms(extracted)

        habits = st.multiselect(
            "Habits / Medicines",
            ["Alcohol", "BP_Medicine", "Sugar_Medicine"],
            key="habits_select"
        )

        # 👉 RESULT BUTTON INSIDE FLOW
        if st.button("Get Results", key="result_btn3"):

            results = predict_category(normalized, age)

            if results and len(results) > 0:
                # create columns (max 3)
                cols = st.columns(min(len(results), 3))

                for i, (col, res) in enumerate(zip(cols, results), 1):

                    with col:
                        interactions = check_interaction(res['medicines'], habits)

                        # Label
                        if i == 1:
                            st.success("🟢 Most Likely")
                        elif i == 2:
                            st.warning("🟡 Possible")
                        else:
                            st.info("🔵 Less Likely")

                        # Card UI
                        st.markdown(f"""
                        <div class="card">
                            <p style="color:#94a3b8;">Option {i}</p>
                            <h4>{res['disease']}</h4>
                            <p>Confidence: {res['confidence']}%</p>
                        </div>
                        """, unsafe_allow_html=True)

                        # Expandable full report
                        with st.expander("View Full Report"):
                            report = generate_report(
                                res,
                                interactions,
                                age,
                                normalized,
                                habits
                            )

                            st.markdown(report)

                            import uuid
                            st.download_button(
                                label="📄 Download Report",
                                data=report,
                                file_name=f"health_report_{i}.txt",
                                mime="text/plain",
                                key=f"download_{i}_{uuid.uuid4()}"
                            )
# ---------------- ANALYTICS ----------------
elif page == "📊 Analytics":

    st.markdown("""
    <div style="padding-bottom:20px;">
        <h1 style="font-size:38px;">📊 Health Analytics</h1>
        <p style="color:#aaa;">Clean insights about your health trends</p>
    </div>
    """, unsafe_allow_html=True)

    tab1, tab2, tab3 = st.tabs(["📈 Trends", "🧠 Insights", "📊 Distribution"])

    # -------- TAB 1 --------
    with tab1:

        st.markdown("""
        <div style="margin-bottom:15px;">
            <h2 style="margin-bottom:5px;">📈 Health Trends</h2>
            <p style="color:#94a3b8; font-size:14px;">
            Track how your health predictions and recovery patterns change over time.
            </p>
        </div>
        """, unsafe_allow_html=True)

        col1, col2 = st.columns(2)

    # -------- CONFIDENCE GRAPH --------
        with col1:
            fig1 = plot_confidence_graph()
            if fig1:
                st.markdown('<div class="card">', unsafe_allow_html=True)

                st.markdown("""
                <h4 style="margin-bottom:5px;">Prediction Confidence</h4>
                <p style="color:#94a3b8; font-size:13px;">
                Shows how confident the AI has been in its predictions over time.
                Higher values indicate stronger matches with symptoms.
                </p>
                """, unsafe_allow_html=True)

                st.plotly_chart(fig1, use_container_width=True)

                st.markdown('</div>', unsafe_allow_html=True)

    # -------- HEALTH IMPROVEMENT GRAPH --------
        with col2:
            fig2 = plot_health_improvement()
            if fig2:
                st.markdown('<div class="card">', unsafe_allow_html=True)

                st.markdown("""
                <h4 style="margin-bottom:5px;">Health Improvement Trend</h4>
                <p style="color:#94a3b8; font-size:13px;">
                Indicates whether your health condition is improving or worsening
                based on recent analyses and confidence trends.
                </p>
                """, unsafe_allow_html=True)

                st.plotly_chart(fig2, use_container_width=True)

                st.markdown('</div>', unsafe_allow_html=True)

    # -------- EXTRA SPACING --------
        st.markdown("<div style='height:20px'></div>", unsafe_allow_html=True)

        # -------- INSIGHT  --------
        st.markdown("""
        <div class="card">
            <h4>🧠 Insight</h4>
            <p style="color:#cbd5f5; font-size:14px;">
            Consistently high confidence scores usually indicate stable symptom patterns,
            while fluctuations may suggest changing conditions or incomplete inputs.
            </p>
        </div>
        """, unsafe_allow_html=True)

    # -------- TAB 2 --------
    with tab2:

        st.markdown("""
        <div style="margin-bottom:15px;">
            <h2 style="margin-bottom:5px;">🧠 Health Insights</h2>
            <p style="color:#94a3b8; font-size:14px;">
            AI-generated insights based on your past health analyses and trends.
            </p>
        </div>
        """, unsafe_allow_html=True)

        history = load_history()

        if history:

            confidences = [h['confidence'] for h in history]
            avg_conf = sum(confidences) / len(confidences)
            max_conf = max(confidences)
            min_conf = min(confidences)

            diseases = [h['disease'] for h in history]
            most_common = max(set(diseases), key=diseases.count)

            # -------- KPI ROW --------
            col1, col2, col3, col4 = st.columns(4)

            col1.markdown(f"""
            <div class="card kpi-card">
                <div class="kpi-title">Average Confidence</div>
                <div class="kpi-value">{round(avg_conf,1)}%</div>
            </div>
            """, unsafe_allow_html=True)

            col2.markdown(f"""
            <div class="card kpi-card">
                <div class="kpi-title">Highest Confidence</div>
                <div class="kpi-value">{round(max_conf,1)}%</div>
            </div>
            """, unsafe_allow_html=True)

            col3.markdown(f"""
            <div class="card kpi-card">
                <div class="kpi-title">Lowest Confidence</div>
                <div class="kpi-value">{round(min_conf,1)}%</div>
            </div>
            """, unsafe_allow_html=True)

            col4.markdown(f"""
            <div class="card kpi-card">
                <div class="kpi-title">Total Analyses</div>
                <div class="kpi-value">{len(history)}</div>
            </div>
            """, unsafe_allow_html=True)

            # -------- SPACING --------
            st.markdown("<div style='height:25px'></div>", unsafe_allow_html=True)

            # -------- MAIN INSIGHT SECTION --------
            col1, col2 = st.columns([2,1])

            with col1:
                st.markdown(f"""
                <div class="card">
                    <h3 style="margin-bottom:10px;">📊 AI Summary</h3>
                    <p class="summary">
                    Your most frequently detected condition is <b>{most_common}</b>.
                    The system shows an average confidence of <b>{round(avg_conf)}%</b>,
                    indicating {"stable" if avg_conf > 70 else "moderate"} prediction patterns.
                    </p>
                </div>
                """, unsafe_allow_html=True)

            with col2:
                st.markdown('<div class="card">', unsafe_allow_html=True)
                st.markdown("""
                <h4 style="margin-bottom:8px;">Health Score</h4>
                <p style="color:#94a3b8; font-size:13px;">
                Overall health confidence score based on your history
                </p>
                """, unsafe_allow_html=True)

                st.progress(avg_conf / 100)
                st.write(f"**{round(avg_conf)}%**")

                st.markdown('</div>', unsafe_allow_html=True)

            # -------- SPACING --------
            st.markdown("<div style='height:20px'></div>", unsafe_allow_html=True)

            # -------- HIGHLIGHT CARD --------
            st.markdown(f"""
            <div style="
                background: linear-gradient(135deg, rgba(99,102,241,0.08), rgba(59,130,246,0.04));
                padding: 18px;
                border-radius: 16px;
                border: 1px solid rgba(255,255,255,0.05);
            ">
                <div style="font-size:13px; color:#94a3b8;">
                    Most Frequent Condition
                </div>
                <div style="font-size:26px; font-weight:600; margin-top:6px;">
                    {most_common}
                </div>
                <div style="font-size:13px; color:#64748b; margin-top:4px;">
                    Based on your recent health patterns
                </div>
            </div>
            """, unsafe_allow_html=True)

            # -------- SPACING --------
            st.markdown("<div style='height:20px'></div>", unsafe_allow_html=True)

            # -------- RECOMMENDATIONS --------
            st.markdown("""
            <h4 style="margin-bottom:10px;">💡 Recommendations</h4>
            """, unsafe_allow_html=True)

            col1, col2, col3 = st.columns(3)

            col1.markdown("<div class='card'>💧 Stay hydrated</div>", unsafe_allow_html=True)
            col2.markdown("<div class='card'>😴 Maintain sleep cycle</div>", unsafe_allow_html=True)
            col3.markdown("<div class='card'>🧠 Monitor symptoms regularly</div>", unsafe_allow_html=True)

        else:
            st.info("No data available yet. Start analyzing to generate insights.")

    # -------- TAB 3 --------
    with tab3:

        st.markdown("""
        <div style="margin-bottom:15px;">
            <h2 style="margin-bottom:5px;">📊 Data Distribution</h2>
            <p style="color:#94a3b8; font-size:14px;">
            Understand how your symptoms and predicted conditions are distributed
            across your health history.
            </p>
        </div>
        """, unsafe_allow_html=True)

        col1, col2 = st.columns(2)

        # -------- SYMPTOM FREQUENCY --------
        with col1:
            fig3 = plot_symptom_frequency()
            if fig3:
                st.markdown('<div class="card">', unsafe_allow_html=True)

                st.markdown("""
                <h4 style="margin-bottom:5px;">Symptom Frequency</h4>
                <p style="color:#94a3b8; font-size:13px;">
                Displays how often specific symptoms appear in your past analyses.
                Helps identify recurring health patterns.
                </p>
                """, unsafe_allow_html=True)

                st.plotly_chart(fig3, use_container_width=True)

                st.markdown('</div>', unsafe_allow_html=True)

        # -------- DISEASE DISTRIBUTION --------
        with col2:
            fig4 = plot_disease_frequency()
            if fig4:
                st.markdown('<div class="card">', unsafe_allow_html=True)

                st.markdown("""
                <h4 style="margin-bottom:5px;">Condition Distribution</h4>
                <p style="color:#94a3b8; font-size:13px;">
                Shows how frequently different conditions have been predicted.
                Useful for identifying dominant or repeated diagnoses.
                </p>
                """, unsafe_allow_html=True)

                st.plotly_chart(fig4, use_container_width=True)

                st.markdown('</div>', unsafe_allow_html=True)

        # -------- SPACING --------
        st.markdown("<div style='height:20px'></div>", unsafe_allow_html=True)

        # -------- INSIGHT BOX --------
        st.markdown("""
        <div class="card">
            <h4>🧠 Insight</h4>
            <p style="color:#cbd5f5; font-size:14px;">
            Frequent symptoms may indicate underlying chronic conditions,
            while repeated predictions of the same disease suggest a need
            for closer monitoring or medical consultation.
            </p>
        </div>
        """, unsafe_allow_html=True)

        # -------- EXTRA RECOMMENDATION ROW --------
        st.markdown("<div style='height:15px'></div>", unsafe_allow_html=True)

        col1, col2, col3 = st.columns(3)

        col1.markdown("<div class='card'>📌 Track recurring symptoms</div>", unsafe_allow_html=True)
        col2.markdown("<div class='card'>🧾 Compare past reports</div>", unsafe_allow_html=True)
        col3.markdown("<div class='card'>👨‍⚕️ Consult doctor if patterns repeat</div>", unsafe_allow_html=True)



# ---------------- ABOUT ----------------
elif page == "ℹ️ About":

    # 🔥 Minimal Elegant Header
    st.markdown("""
    <div style="
        padding: 20px 0;
        border-bottom: 1px solid rgba(255,255,255,0.08);
        margin-bottom: 20px;
    ">
        <h1 style="margin-bottom:5px;">🧠 AI Health Assistant</h1>
        <p style="color:#94a3b8; margin:0;">
            Smart • Predictive • Explainable Healthcare System
        </p>
    </div>
    """, unsafe_allow_html=True)

    # -------- OVERVIEW --------
    st.markdown("""
    <div class="card">
        <h3> Project Overview</h3>
        <p style="line-height:1.8; color:#cbd5f5;">
        AI Health Assistant is a modern AI-powered system that analyzes user symptoms,
        predicts possible conditions, and generates structured medical-style reports.
        It focuses on clarity, explainability, and real-time insights.
        </p>
    </div>
    """, unsafe_allow_html=True)

    space()
    divider()
    space()
    # -------- FEATURES --------
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        <div class="card">
            <h3>✨ Key Features</h3>
            <ul style="line-height:2; color:#cbd5f5;">
                <li>🩺 Smart Disease Prediction</li>
                <li>🧠 Explainable AI Output</li>
                <li>💊 Drug Interaction Detection</li>
                <li>📊 Interactive Analytics</li>
                <li>📄 Report Generation</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="card">
            <h3>⚙️ How It Works</h3>
            <ul style="line-height:2; color:#cbd5f5;">
                <li>🔍 Symptom extraction</li>
                <li>🔁 Similarity matching</li>
                <li>📈 Confidence scoring</li>
                <li>⚠️ Risk detection</li>
                <li>🧾 Report generation</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    space()
    divider()
    space()
    # -------- TECH + HIGHLIGHTS --------
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        <div class="card">
            <h3>🛠️ Tech Stack</h3>
            <p style="line-height:1.8; color:#cbd5f5;">
            Python • Streamlit • Plotly • Matplotlib <br>
            Custom AI Logic
            </p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="card">
            <h3>🌟 Highlights</h3>
            <ul style="line-height:2; color:#cbd5f5;">
                <li>⚡ Fast predictions</li>
                <li>🎯 Confidence-based results</li>
                <li>🧾 Clean medical reports</li>
                <li>📊 Visual insights</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    space()
    divider()
    space()
    # -------- FUTURE --------
    st.markdown("""
    <div class="card">
        <h3>🚀 Future Enhancements</h3>
        <ul style="line-height:2; color:#cbd5f5;">
            <li>🤖 Chatbot interaction</li>
            <li>📄 PDF reports</li>
            <li>🔊 Voice input</li>
            <li>🌐 Real medical data integration</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

    space()
    divider()
    space()
    # -------- DISCLAIMER --------
    st.markdown("""
    <div style="
        padding: 16px;
        border-radius: 12px;
        border: 1px solid rgba(255,255,255,0.08);
        background: rgba(255,255,255,0.02);
    ">
        <h4 style="color:#f87171; margin-bottom:5px;">⚠️ Disclaimer</h4>
        <p style="color:#94a3b8; font-size:14px;">
        This app is for educational purposes only and does not replace professional medical advice.
        Always consult a doctor for medical concerns.
        </p>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("""
<div style="
    text-align:center;
    margin-top:30px;
    color:#64748b;
    font-size:13px;
">
Built with ❤️ using AI • Your Name
</div>
""", unsafe_allow_html=True)
    
# ---------------- HISTORY PAGE ----------------
elif page == "📜 History":

    st.markdown("""
    <div style="padding-bottom:20px;">
        <h1 style="font-size:38px;">📜 Health History</h1>
        <p style="color:#aaa;">Track your past analyses and results</p>
    </div>
    """, unsafe_allow_html=True)

    history = load_history()

    if history:

        # -------- CLEAR BUTTON --------
        col1, col2 = st.columns([3,1])
        with col2:
            if st.button("🗑️ Clear History"):
                save_history([])
                st.success("History cleared!")
                st.rerun()

        st.markdown("<div style='height:15px'></div>", unsafe_allow_html=True)

        # -------- SHOW HISTORY --------
        for i, h in enumerate(reversed(history), 1):

            st.markdown(f"""
            <div class="card" style="margin-bottom:12px;">
                <p style="color:#94a3b8;">Record {i}</p>
                <b>Symptoms:</b> {", ".join(h['symptoms'])}<br>
                <b>Condition:</b> {h['disease']}<br>
                <b>Confidence:</b> {h['confidence']}%
            </div>
            """, unsafe_allow_html=True)

    else:
        st.info("No history available yet. Start analyzing to generate data.")