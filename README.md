# FinanceBot

FinanceBot is a **RAG-based (Retrieval-Augmented Generation)** chatbot designed to provide personalized financial advice. It combines user input with a preloaded knowledge base of financial advice to deliver accurate and contextual responses.

---

## Project Overview

FinanceBot combines **GENERATIVE AI** to assist users in making informed financial decisions. Key features include:

- **User Input Personalization**: Tailored advice based on the user's input.
- **Knowledge Base**: A rich repository of financial advice stored as vector embeddings.
- **RAG Methodology**: Ensures the chatbot retrieves the most relevant data and provides it in an engaging conversational format.


---

### Process Flow

1. **User Information Input**  
   - Upon starting the application, users will be prompted to fill in their personal details (e.g., financial goals, preferences, or other relevant information).  
   - This information will be securely stored in the knowledge base, enhancing the chatbot's ability to provide personalized advice.

2. **Transition to Chat Interface**  
   - Once the details are saved, users will be redirected to the chat interface.  
   - They can interact with the chatbot, ask financial questions, and receive tailored advice based on their inputs and the preloaded knowledge base.


---
## Use Cases

- **Personalized Financial Advice**: Receive custom financial recommendations.
- **Financial Education**: Quickly access reliable financial knowledge.
- **Interactive Learning**: Explore financial topics through engaging conversations.
- **Decision Support**: Get actionable insights to enhance financial planning.

---

## Getting Started

### Prerequisites

Before you begin, ensure you have the following installed:

- **Python 3.10.14**
- **Git** for version control

---

### Steps to Set Up and Run

1. **Clone the Repository**
   ```bash
   git clone https://github.com/Vrushali-anil-Chaudhari/FinanceBot.git

2. **Navigate to the Source Code Directory After cloning the repository, navigate to the source code directory:**
    ```bash
    cd FinanceBot/src

3. **Install Dependencies**
    Install all required packages using the following command:
    ```bash
    pip install -r requirements.txt

4. **Configure Environment Variables**
    ```
    Create a .env file in the src directory.
    ```

5. **Add the necessary API keys, database credentials, and other configuration details.**
    Run the Application Start the chatbot interface using Streamlit:
    ```bash
    streamlit run dashboard.py

6. **Interact with FinanceBot**
    Open the URL displayed in your terminal after running Streamlit.
    
    Start asking financial questions to receive personalized advice!

--- 

### How RAG Works

FinanceBot is powered by Retrieval-Augmented Generation (RAG), a method that combines retrieval and generation to provide accurate and relevant responses. Here’s how it works:

1. User Query Input
The user enters a question or provides financial details.

2. Retrieval Phase
The chatbot queries the vector database for the most relevant information.
The knowledge base is preloaded with financial advice stored as vector embeddings, enabling efficient retrieval.

3. Augmentation Phase
Retrieved information is combined with the user's input to provide context.

4. Response Generation
A pre-trained language model processes the augmented input to generate a conversational and accurate response.

---

### Features

1. Interactive UI: Built using Streamlit for ease of use.
2. Efficient Search: Leverages vector databases for quick and relevant results.
3. Scalable Design: The architecture supports adding more financial knowledge seamlessly.
4. Beginner-Friendly Setup: Minimal prerequisites and straightforward installation.

---

### Future Enhancements

Integrating advanced NLP models for improved conversational ability.
Expanding the knowledge base with more financial insights.
Supporting voice-based interaction for better accessibility.

---

If you encounter any issues or have questions, feel free to:

Create an issue on the GitHub repository.


**Start chatting with FinanceBot and get closer to your financial goals!** 🚀 
