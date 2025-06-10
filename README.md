# NexusAgents: ContentCraft MVP

This is the Minimum Viable Product (MVP) for ContentCraft, the first agent in the NexusAgents marketplace. It's an AI-powered application that generates high-quality, engaging LinkedIn posts for B2B SaaS companies.

![ContentCraft Screenshot](URL_TO_YOUR_SCREENSHOT_HERE)  <!-- We will add this later -->

---

## 🚀 About The Project

ContentCraft solves a common problem for marketing managers and founders: the time-consuming task of writing compelling social media content. By providing a few simple details about a product, feature, or announcement, users can instantly generate a ready-to-publish LinkedIn post, complete with strategic hashtags and a clear call-to-action.

This project was built to demonstrate a complete end-to-end development cycle of an AI-powered application.

### Built With

*   **AI Model:** Google Gemini 1.5 Flash
*   **Web Framework:** Flask
*   **Development Environment:** GitHub Codespaces
*   **Core Libraries:** `google-generativeai`, `python-dotenv`

---

## 🏃‍♀️ Getting Started

To get a local copy up and running, follow these simple steps.

### Prerequisites

*   Python 3.9+
*   A Google AI Studio API Key

### Installation

1.  **Clone the repo:**
    ```sh
    git clone https://github.com/robert1948/NEXUSAGENTS.git
    ```
2.  **Navigate to the project directory:**
    ```sh
    cd NEXUSAGENTS
    ```
3.  **Install Python packages:**
    ```sh
    pip install -r requirements.txt
    ```
4.  **Create your environment file:**
    Create a `.env` file in the root directory and add your API key:
    ```
    GEMINI_API_KEY="YOUR_API_KEY_HERE"
    ```
5.  **Run the app:**
    ```sh
    python main.py
    ```
    The application will be available at `http://127.0.0.1:5000`.

---

##  Roadmap

See the `ROADMAP.md` file for details on the project plan and future features.