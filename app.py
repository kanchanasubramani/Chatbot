import streamlit as st
from services.memory_service import MemoryService
from services.gemini_service import GeminiService, summarize_conversation
from services.safety_service import check_crisis, CRISIS_RESPONSE
from prompts.system_prompt import SYSTEM_PROMPT

# ------------------ Page Config ------------------ #
st.set_page_config(page_title="Mental Health Chatbot", page_icon="🧠")

st.title("🧠 Mental Health Support Chatbot")

# ------------------ Initialize Services ------------------ #
if "memory" not in st.session_state:
    st.session_state.memory = MemoryService()

if "gemini" not in st.session_state:
    st.session_state.gemini = GeminiService()

memory_service = st.session_state.memory
gemini_service = st.session_state.gemini

# ------------------ Sidebar ------------------ #
st.sidebar.title("About")
st.sidebar.write(
    "This chatbot provides emotional support and coping guidance. "
    "It is NOT a replacement for professional therapy or medical advice."
)

st.sidebar.markdown("---")
st.sidebar.subheader("🧠 Conversation Summary")

history = memory_service.get_history()

if len(history) > 3:
    summary = summarize_conversation(history)
    st.sidebar.write(summary)
else:
    st.sidebar.info("Summary will appear after a few messages.")

st.sidebar.markdown("---")

if st.sidebar.button("🔄 Clear Conversation"):
    memory_service.clear()
    st.sidebar.success("Conversation cleared.")
    st.rerun()

# ------------------ Display Chat History ------------------ #
for message in history:
    role = message["role"]
    content = message["parts"][0]

    if role == "user":
        st.chat_message("user").write(content)
    else:
        st.chat_message("assistant").write(content)

# ------------------ User Input ------------------ #
user_input = st.chat_input("How are you feeling today?")

if user_input:

    # Store user message
    memory_service.add_message("user", user_input)
    st.chat_message("user").write(user_input)

    # Safety Check
    if check_crisis(user_input):
        st.chat_message("assistant").write(CRISIS_RESPONSE)

    else:
        with st.spinner("Thinking..."):
            response = gemini_service.generate_response(
                SYSTEM_PROMPT,
                memory_service.get_history()
            )

            memory_service.add_message("assistant", response)
            st.chat_message("assistant").write(response)

    # Rerun to update summary instantly
    st.rerun()