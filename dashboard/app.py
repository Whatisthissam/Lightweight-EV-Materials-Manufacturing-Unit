import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="EV Manufacturing Dashboard",
    page_icon="⚡",
    layout="wide"
)

st.markdown("""
<style>
.main {
    background-color: #0E1117;
}
h1 {
    text-align:center;
}

.stMetric {
    background-color:#1E2228;
    padding:20px;
    border-radius:12px;
}
</style>
""", unsafe_allow_html=True)

def format_indian_number(num):

    if num >= 10000000:
        return f"₹{num/10000000:.2f} Cr"

    elif num >= 100000:
        return f"₹{num/100000:.2f} L"

    else:
        return f"₹{num:,.0f}"

st.title("⚡ EV Manufacturing Business Decision Dashboard")

st.sidebar.header("📊 Business Inputs")

initial_investment = st.sidebar.number_input(
    "Initial Investment (₹)",
    value=50000000
)

operational_cost = st.sidebar.number_input(
    "Annual Operational Cost (₹)",
    value=20000000
)

units = st.sidebar.number_input(
    "Units Produced",
    value=25000
)

price = st.sidebar.number_input(
    "Price per Unit (₹)",
    value=6000
)

risk_level = st.sidebar.selectbox(
    "Business Risk Preference",
    [
        "No Loss Allowed",
        "Accept Small Initial Loss",
        "High Risk High Reward"
    ]
)

revenue = units * price
profit = revenue - operational_cost - initial_investment

st.divider()

col1, col2 = st.columns(2)

with col1:
    st.metric(
        "💰 Revenue",
        format_indian_number(revenue)
    )

with col2:
    st.metric(
        "📈 Net Profit",
        format_indian_number(profit)
    )

st.divider()

data = pd.DataFrame({
    "Category": [
        "Revenue",
        "Operational Cost",
        "Initial Investment"
    ],
    "Amount": [
        revenue,
        operational_cost,
        initial_investment
    ]
})

fig = px.bar(
    data,
    x="Category",
    y="Amount",
    color="Category",
    title="Financial Breakdown"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.divider()

st.subheader("📊 Business Recommendation")

if profit > 0:

    st.success(
        f"✅ Setup the Business — Expected Profit: {format_indian_number(profit)}"
    )

else:

    if risk_level == "Accept Small Initial Loss":

        st.warning(
            "⚠️ Initial loss possible, but viable for long-term growth."
        )

    else:

        st.error(
            "❌ Not financially viable based on current inputs."
        )