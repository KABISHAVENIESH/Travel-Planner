# ✈️ Intelligent Travel Planner 🤖

An intelligent travel recommendation web application built using **Python** and **Streamlit**. The application recommends suitable travel destinations based on the user's preferences, including **budget, travel interest, preferred climate, and trip duration**.

## 🌟 Features

- 🤖 Rule-Based AI Recommendation System
- 💰 Budget-Based Destination Filtering
- 🎯 Travel Interest Matching
- 🌤️ Climate Preference Matching
- 📅 Trip Duration Matching
- 🏆 Top 3 Destination Recommendations
- 📊 AI Match Score and Ranking
- 📋 Destination Comparison
- 🗓️ Day-Wise Travel Itinerary
- 💰 Travel Budget Breakdown
- 🖼️ Destination Images
- 🎨 Interactive and User-Friendly Streamlit Interface

## 🧠 How the Recommendation System Works

The application uses a **rule-based Artificial Intelligence approach** to recommend destinations.

The system evaluates the user's preferences:

- 💰 Budget
- 📅 Number of travel days
- 🎯 Travel interest
- 🌤️ Preferred climate

Each destination receives a score based on how well it matches the user's preferences.

### Scoring Logic

| Criteria | Score |
|----------|-------|
| Budget Match | +3 |
| Travel Interest Match | +3 |
| Climate Match | +2 |
| Trip Duration Match | +2 |

The destinations are then ranked based on their total score.

## 🔄 Application Workflow

User Preferences -> Destination Knowledge Base -> Rule-Based AI Engine -> Destination Filtering -> Score Calculation -> Destination Ranking -> Top 3 Recommendations -> Itinerary + Comparison + Budget Breakdown
