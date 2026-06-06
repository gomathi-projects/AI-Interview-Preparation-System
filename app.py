import streamlit as st
from questions import questions
from score import calculate_score

st.title("AI Interview Preparation System")

total_score = 0

for q in questions:

    st.write(q)

    answer = st.text_area(
        "Your Answer",
        key=q
    )

    if answer:
        total_score += calculate_score(answer)

if st.button("Submit"):
    st.success(
        f"Your Score: {total_score}"
    )