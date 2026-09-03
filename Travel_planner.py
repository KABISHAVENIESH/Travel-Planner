import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Intelligent Travel Planner",
    page_icon="✈️",
    layout="wide"
)

st.markdown("""
<style>

/* Main background */
.stApp {
    background: linear-gradient(135deg, #e0f7fa, #fce4ec);
}

/* Main title */
h1 {
    text-align: center;
    color: #6a1b9a;
    font-size: 48px;
    font-weight: bold;
}

/* Subheadings */
h2, h3 {
    color: #1565c0;
}

/* Button */
.stButton > button {
    width: 100%;
    background: linear-gradient(90deg, #7b2ff7, #f107a3);
    color: white;
    border: none;
    border-radius: 12px;
    height: 50px;
    font-size: 18px;
    font-weight: bold;
    transition: 0.3s;
}

/* Button Hover */
.stButton > button:hover {
    transform: scale(1.02);
    box-shadow: 0px 6px 18px rgba(0,0,0,0.25);
}

/* Input boxes */
div[data-baseweb="input"] {
    border-radius: 10px;
}

/* Select boxes */
div[data-baseweb="select"] {
    border-radius: 10px;
}

/* Metric Cards */
div[data-testid="stMetric"] {
    background-color: white;
    padding: 15px;
    border-radius: 15px;
    box-shadow: 0px 4px 12px rgba(0,0,0,0.12);
}

/* Expanders */
details {
    background-color: white;
    border-radius: 12px;
    padding: 10px;
}

/* Alerts */
div[data-testid="stAlert"] {
    border-radius: 12px;
}

/* Divider */
hr {
    border: 1px solid #b39ddb;
}

</style>
""", unsafe_allow_html=True)

destinations = [
    {
        "name": "Ooty",
        "interest": "Nature",
        "climate": "Cold",
        "budget": 8000,
        "days": 2,
        "description": "Beautiful hills, tea gardens, lakes and pleasant weather.",
        "image": "images/ooty.jpg"
    },
    {
        "name": "Kodaikanal",
        "interest": "Nature",
        "climate": "Cold",
        "budget": 10000,
        "days": 3,
        "description": "A peaceful hill station with lakes and beautiful scenic views.",
        "image": "images/kodaikanal.jpg"
    },
    {
        "name": "Munnar",
        "interest": "Nature",
        "climate": "Cold",
        "budget": 12000,
        "days": 3,
        "description": "Famous for tea plantations, mountains and waterfalls.",
        "image": "images/munnar.jpg"
    },
    {
        "name": "Goa",
        "interest": "Beach",
        "climate": "Hot",
        "budget": 15000,
        "days": 3,
        "description": "Popular for beaches, water activities and nightlife.",
        "image": "images/goa.jpg"
    },
    {
        "name": "Pondicherry",
        "interest": "Beach",
        "climate": "Warm",
        "budget": 9000,
        "days": 2,
        "description": "A relaxing destination with beaches and French-style architecture.",
        "image": "images/pondicherry.jpg"
    },
    {
        "name": "Jaipur",
        "interest": "Historical",
        "climate": "Hot",
        "budget": 14000,
        "days": 3,
        "description": "Known for its forts, palaces and rich cultural heritage.",
        "image": "images/jaipur.jpg"
    },
    {
        "name": "Chennai",
        "interest": "City",
        "climate": "Hot",
        "budget": 7000,
        "days": 2,
        "description": "A vibrant city known for beaches, temples and culture.",
        "image": "images/chennai.jpg"
    }
]

itineraries = {
    "Ooty": [
        "Visit Ooty Lake and enjoy boating 🚣",
        "Explore the Botanical Garden 🌿",
        "Visit Doddabetta Peak 🏔️"
    ],
    "Kodaikanal": [
        "Visit Kodaikanal Lake 🚣",
        "Explore Coaker's Walk 🌄",
        "Visit Pillar Rocks 🪨"
    ],
    "Munnar": [
        "Visit Tea Gardens 🍃",
        "Explore Eravikulam National Park 🌿",
        "Visit Mattupetty Dam 🌊"
    ],
    "Goa": [
        "Relax at Baga Beach 🏖️",
        "Try water sports 🌊",
        "Explore local markets and nightlife 🎉"
    ],
    "Pondicherry": [
        "Visit Promenade Beach 🌊",
        "Explore the French Quarter 🏘️",
        "Visit Auroville 🌿"
    ],
    "Jaipur": [
        "Visit Amber Fort 🏰",
        "Explore City Palace 👑",
        "Visit Hawa Mahal 🕌"
    ],
    "Chennai": [
        "Visit Marina Beach 🌊",
        "Explore Kapaleeshwarar Temple 🛕",
        "Visit Government Museum 🏛️"
    ]
}

def recommend_destination(budget, days, interest, climate):

    recommendations = []

    for destination in destinations:

        # Skip destinations outside budget
        if budget < destination["budget"]:
            continue

        score = 3

        if interest == destination["interest"]:
            score += 3

        if climate == destination["climate"]:
            score += 2

        if days >= destination["days"]:
            score += 2

        recommendations.append((destination, score))

    recommendations.sort(
        key=lambda x: x[1],
        reverse=True
    )

    return recommendations

def calculate_budget(total_budget):

    travel = total_budget * 0.30
    hotel = total_budget * 0.35
    food = total_budget * 0.20
    activities = total_budget * 0.15

    return travel, hotel, food, activities


st.title("✈️ Intelligent Travel Planner")

st.subheader("Discover Your Perfect Destination with AI 🤖🌍")

st.write(
    "Enter your travel preferences and our intelligent recommendation "
    "system will find the best destinations for you."
)

st.divider()


st.subheader("🧳 Plan Your Trip")

col1, col2 = st.columns(2)

with col1:

    budget = st.number_input(
        "💰 Your Budget (₹)",
        min_value=1000,
        max_value=100000,
        value=10000,
        step=1000
    )

    days = st.slider(
        "📅 Number of Days",
        min_value=1,
        max_value=10,
        value=3
    )


with col2:

    interest = st.selectbox(
        "🎯 Travel Interest",
        ["Nature", "Beach", "Historical", "City"]
    )

    climate = st.selectbox(
        "🌤️ Preferred Climate",
        ["Cold", "Warm", "Hot"]
    )


st.divider()


if st.button(
    "✨ Find My Perfect Destination",
    use_container_width=True
):

    results = recommend_destination(
        budget,
        days,
        interest,
        climate
    )

    if not results:

        st.error(
            "❌ Sorry! No destination matches your current budget. "
            "Please increase your budget."
        )

    else:

        best_destination = results[0][0]

        st.success(
            f"🎉 Based on your preferences, "
            f"**{best_destination['name']}** is our top recommendation!"
        )

        st.subheader("🏆 Top 3 AI Recommendations")

        rank_icons = ["🥇", "🥈", "🥉"]

        for index, (destination, score) in enumerate(results[:3]):

            st.markdown(
                f"## {rank_icons[index]} #{index + 1} "
                f"{destination['name']}"
            )

            image_col, info_col = st.columns([1, 2])

            with image_col:
                st.image(
                    destination["image"],
                    use_container_width=True
                )

            with info_col:

                st.write(destination["description"])

                percentage = score * 10

                st.progress(percentage / 100)

                st.metric(
                    "🤖 AI Match Score",
                    f"{score}/10 ({percentage}%)"
                )

                st.write(
                    f"🎯 **Travel Type:** "
                    f"{destination['interest']}"
                )

                st.write(
                    f"🌤️ **Climate:** "
                    f"{destination['climate']}"
                )

                st.write(
                    f"💰 **Estimated Budget:** "
                    f"₹{destination['budget']:,}"
                )

                st.write(
                    f"📅 **Recommended Days:** "
                    f"{destination['days']}"
                )

            st.divider()

        st.subheader("📊 Compare Top 3 Destinations")

        comparison_data = []

        for destination, score in results[:3]:

            comparison_data.append(
                {
                    "Destination": destination["name"],
                    "AI Match Score": f"{score}/10",
                    "Estimated Budget": f"₹{destination['budget']:,}",
                    "Recommended Days": destination["days"],
                    "Travel Type": destination["interest"],
                    "Climate": destination["climate"]
                }
            )

        comparison_df = pd.DataFrame(comparison_data)

        st.dataframe(
            comparison_df,
            use_container_width=True,
            hide_index=True
        )

        st.divider()

        st.subheader(
            f"🗓️ Suggested Itinerary for "
            f"{best_destination['name']}"
        )

        destination_itinerary = itineraries.get(
            best_destination["name"],
            []
        )

        for day, activity in enumerate(
            destination_itinerary,
            start=1
        ):

            with st.expander(f"📅 Day {day}"):
                st.write(activity)

        st.divider()

        st.subheader("💰 Suggested Budget Breakdown")

        travel, hotel, food, activities = calculate_budget(budget)

        budget_col1, budget_col2, budget_col3, budget_col4 = (
            st.columns(4)
        )

        with budget_col1:
            st.metric(
                "✈️ Travel",
                f"₹{travel:,.0f}"
            )

        with budget_col2:
            st.metric(
                "🏨 Hotel",
                f"₹{hotel:,.0f}"
            )

        with budget_col3:
            st.metric(
                "🍽️ Food",
                f"₹{food:,.0f}"
            )

        with budget_col4:
            st.metric(
                "🎯 Activities",
                f"₹{activities:,.0f}"
            )

        st.info(
            f"💡 This budget breakdown is calculated based on "
            f"your total budget of ₹{budget:,}."
        )

st.divider()

st.caption(
    "🤖 Intelligent Travel Planner | Rule-Based Artificial Intelligence Project"
)