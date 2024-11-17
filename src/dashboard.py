import streamlit as st
from PIL import Image
from utils import load_in_vectord,rag_model
# Load an icon image for the dashboard
icon_image = Image.open(r"D:\GyanInc\FinanceBot\src\static\financebot.png")  # Replace with your icon path

# Set the title and layout
st.set_page_config(page_title="FinBot: Finance Advisor Bot", layout="wide", page_icon=icon_image)

# Initialize session state to store user information and chat history
if 'user_info' not in st.session_state:
    st.session_state['user_info'] = {}



# Initialize session state for form submission and page navigation
if 'page' not in st.session_state:
    st.session_state['page'] = "Form"

# Define a custom CSS style for chat interface
st.markdown(
    """
    <style>
    .chat-bubble {
        padding: 10px;
        margin: 10px 0;
        border-radius: 10px;
        max-width: 80%;
    }
    .user-bubble {
        background-color: #DCF8C6;
        align-self: flex-end;
    }
    .bot-bubble {
        background-color: #F1F0F0;
        align-self: flex-start;
    }
    .chat-container {
        display: flex;
        flex-direction: column;
        margin-bottom: 10px;
    }
    </style>
    """, unsafe_allow_html=True
)

def form_page():
    icon_image = Image.open(r"static/financebot.png")  # Replace with your icon path
    icon_base64 = icon_image_to_base64(icon_image)

    # Center-align the image and title
    st.markdown(f"""
        <div style="display: flex; justify-content: center; align-items: center; margin-bottom: 20px;">
            <img src="data:image/png;base64,{icon_base64}" width="100" style="margin-right: 10px;"/>
            <h3 style='color: #99e5ff; margin: 0;'>FinBot: Finance Advisory Bot</h3>
        </div>
        <hr style='border: 1px solid #FFD700;'>
    """, unsafe_allow_html=True)
    st.subheader("Please fill in your information below:")

    # Collect user information
    st.session_state['user_info']['Name'] = st.text_input("Name", placeholder="Enter your full name")

    age_group = st.radio("What is your current age?", ["Select an option", "18-25", "26-35", "36 and above"])
    if age_group != "Select an option":
        st.session_state['user_info']['Age Group'] = age_group

    # Employment Status
    employment_status = st.selectbox("What is your employment status?", 
                                    ["Select an option", "Employed full-time", "Self-employed or freelancer", "Unemployed or student"])
    if employment_status != "Select an option":
        st.session_state['user_info']['Employment Status'] = employment_status

    # Annual Income
    annual_income = st.radio("What is your annual income?", 
                            ["Select an option", "Less than ₹5,00,000", "₹5,00,000 to ₹20,00,000", "More than ₹20,00,000"])
    if annual_income != "Select an option":
        st.session_state['user_info']['Annual Income'] = annual_income

    # Financial Goals
    financial_goals = st.multiselect("What are your top financial goals?",
                                    ["Saving for retirement", "Buying a house", "Paying off debt", "Others"])
    if financial_goals:
        if "Others" in financial_goals:
            other_goal = st.text_input("Please specify your other financial goal:")
            if other_goal:
                financial_goals.append(other_goal)
        st.session_state['user_info']['Financial Goals'] = financial_goals

    # Time Horizon
    time_horizon = st.selectbox("What is your time horizon for achieving these goals?", 
                                ["Select an option", "1-5 years", "6-10 years", "11 years and above"])
    if time_horizon != "Select an option":
        st.session_state['user_info']['Time Horizon'] = time_horizon

    # Risk Tolerance
    risk_tolerance = st.radio("How would you describe your risk tolerance?", 
                            ["Select an option", "Conservative (low risk)", "Moderate (medium risk)", "Aggressive (high risk)"])
    if risk_tolerance != "Select an option":
        st.session_state['user_info']['Risk Tolerance'] = risk_tolerance

    # Dependents
    dependents = st.selectbox("Do you have any dependents?", 
                            ["Select an option", "Yes, I have children", "Yes, I have other dependents", "No, I don't have any dependents"])
    if dependents != "Select an option":
        st.session_state['user_info']['Dependents'] = dependents

    # Current Debt
    current_debt = st.radio("What is your current level of debt?", 
                            ["Select an option", "No debt", "Manageable debt (less than 30% of income)", "High debt (more than 30% of income)"])
    if current_debt != "Select an option":
        st.session_state['user_info']['Current Debt'] = current_debt

    # Savings and Investments
    savings_investments = st.radio("How much do you currently have in savings and investments?", 
                                ["Select an option", "Less than ₹1,00,000", "₹1,00,000 to ₹10,00,000", "More than ₹10,00,000"])
    if savings_investments != "Select an option":
        st.session_state['user_info']['Savings and Investments'] = savings_investments

    # Financial Knowledge
    financial_knowledge = st.selectbox("How would you rate your financial knowledge?", 
                                    ["Select an option", "Beginner", "Intermediate", "Advanced"])
    if financial_knowledge != "Select an option":
        st.session_state['user_info']['Financial Knowledge'] = financial_knowledge

    if st.button("Submit"):
        st.session_state['form_submitted'] = True
        st.session_state['page'] = "Chat"
        st.rerun()


def icon_image_to_base64(image):
    import io
    import base64
    
    buffer = io.BytesIO()
    image.save(buffer, format="PNG")
    return base64.b64encode(buffer.getvalue()).decode()


def chat_page():
    # Load and prepare the icon image
    icon_image = Image.open(r"D:\GyanInc\FinanceBot\src\static\1_C_LFPy6TagD1SEN5SwmVRQ-removebg-preview.png")  # Replace with your icon path
    icon_base64 = icon_image_to_base64(icon_image)

    # Center-align the image and title
    st.markdown(f"""
        <div style="display: flex; justify-content: center; align-items: center; margin-bottom: 20px;">
            <img src="data:image/png;base64,{icon_base64}" width="100" style="margin-right: 10px;"/>
            <h3 style='color: #99e5ff; margin: 0;'>FinBot</h3>
        </div>
    """, unsafe_allow_html=True)

  

    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display previous messages
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Handle user input
    if prompt := st.chat_input("What is up?"):
        # Save user message
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # Generate assistant response
        rag_chain = rag_model()  # Assuming you have a model called `rag_model`
        
        # Concatenate user information with the user query
        user_info = dict(st.session_state['user_info'])
        prompt_user = f'''
        User Information: {user_info}
        User Query: {prompt}
        '''
        
        # Get the response from the model
        response = rag_chain.invoke(prompt_user)
        
        # Save and display the assistant's response
        st.session_state.messages.append({"role": "assistant", "content": response})
        with st.chat_message("assistant"):
            st.markdown(response)


# Navigation
if st.session_state['page'] == "Form":
    form_page()
    load_in_vectord()
elif st.session_state['page'] == "Chat":
    chat_page()
