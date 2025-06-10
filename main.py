import os
import google.generativeai as genai
from dotenv import load_dotenv
from flask import Flask, request, render_template_string

# --- SETUP AND CONFIGURATION ---
load_dotenv()
try:
    genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
except AttributeError:
    print("Error: The GEMINI_API_KEY was not found. Please check your .env file.")
    exit()

# --- FLASK APP INITIALIZATION ---
app = Flask(__name__)

# --- THE AI'S "BRAIN" (Same as before) ---
system_instruction = "You are \"ContentCraft,\" an expert content creation agent specializing in generating engaging LinkedIn posts for marketing managers at B2B SaaS companies.\n\nYour Goal: To create high-quality, professional, and effective LinkedIn posts that drive engagement and achieve the user's specific goals.\n\nYour Personality: Professional yet approachable, with a tone of authority and enthusiasm. You are data-aware and results-oriented.\n\nRules of Operation:\n1. Analyze the user's input carefully: identify the product, target audience, and primary goal.\n2. The output must be a single, ready-to-publish LinkedIn post.\n3. The post should be concise, ideally around 150 characters.\n4. Incorporate a clear Call-to-Action (CTA).\n5. Include 3-4 relevant and strategic hashtags.\n6. If the user provides a customer success story or a specific data point, feature it prominently.\n7. Embody the \"ContentCraft\" persona."
chat_history = [
    {
        "role": "user", "parts": [ "Product: \"FlowState,\" a project management SaaS tool.\nAudience: Tech startups, project managers, CTOs.\nGoal: Drive traffic to our new landing page.\nDetails: Mention that our client, TechTrend Innovations, cut project delays by 40%." ]
    },
    {
        "role": "model", "parts": [ "🚀 Struggling to keep your projects on track? Our SaaS tool, FlowState, transforms chaos into clarity for tech startups! One client, TechTrend Innovations, cut project delays by 40% using our intuitive platform. Ready to streamline your workflow? Check it out: [link to landing page]\n\n#ProjectManagement #SaaS #Productivity #Tech" ]
    },
    {
        "role": "user", "parts": [ "Product: \"Insightify\", a business intelligence dashboard.\nAudience: Marketing analysts and data scientists.\nGoal: Announce our new integration with Salesforce.\nDetails: Users can now visualize their Salesforce data instantly." ]
    },
    {
        "role": "model", "parts": [ "📈 Your Salesforce data, visualized instantly. Our new Insightify + Salesforce integration is now live!\n\nStop spending hours exporting data. Connect your account and see your marketing and sales dashboards come to life in seconds.\n\n➡️ Try it now: [Link to Insightify Integration Page]\n\n#BusinessIntelligence #Salesforce #DataAnalytics #DataViz" ]
    }
]
model = genai.GenerativeModel(
    model_name="gemini-1.5-flash-latest",
    system_instruction=system_instruction
)
chat = model.start_chat(history=chat_history)

# --- WEB INTERFACE (HTML TEMPLATE) ---
# For our simple MVP, we'll keep the HTML right inside our Python script.
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>NexusAgents: ContentCraft</title>
    <style>
        body { font-family: sans-serif; background-color: #121212; color: #e0e0e0; max-width: 700px; margin: 2rem auto; padding: 1rem; }
        h1, h2 { color: #bb86fc; }
        textarea { width: 100%; min-height: 150px; background-color: #333; color: #e0e0e0; border: 1px solid #444; border-radius: 5px; padding: 10px; font-size: 1rem; }
        input[type="submit"] { background-color: #03dac6; color: #121212; border: none; padding: 10px 20px; border-radius: 5px; font-size: 1rem; cursor: pointer; margin-top: 1rem; }
        .result { background-color: #2a2a2a; padding: 1rem; border-radius: 5px; margin-top: 2rem; white-space: pre-wrap; }
    </style>
</head>
<body>
    <h1>NexusAgents: ContentCraft</h1>
    <h2>Your AI LinkedIn Post Generator</h2>
    <form method="post">
        <label for="prompt">Enter your post details below:</label><br><br>
        <textarea name="prompt" id="prompt" required>{{ user_prompt }}</textarea><br>
        <input type="submit" value="Generate Post">
    </form>
    {% if result %}
    <div class="result">
        <h2>ContentCraft's Response:</h2>
        <p>{{ result }}</p>
    </div>
    {% endif %}
</body>
</html>
"""

# --- FLASK ROUTES (The Web Server Logic) ---
# --- FLASK ROUTES (The Web Server Logic) ---
@app.route("/", methods=["GET", "POST"])
def index():
    user_prompt = ""
    result = ""
    if request.method == "POST":
        user_prompt = request.form["prompt"]
        if user_prompt:
            try:
                # TRY to send the user's prompt to the Gemini chat
                response = chat.send_message(user_prompt)
                result = response.text
            except Exception as e:
                # If an error occurs, catch it and display a friendly message
                result = f"An error occurred: {e}"
                
    # Render the HTML page, passing in any variables we need
    return render_template_string(HTML_TEMPLATE, user_prompt=user_prompt, result=result)
# --- RUN THE APP ---
if __name__ == "__main__":
    # Note: 'debug=True' is for development. We'll turn it off for production.
    app.run(host="0.0.0.0", port=5000, debug=True)