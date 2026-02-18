# LinkedIn AI Feed Agent


A personal automation agent that scrapes your LinkedIn feed, filters AI-related posts, generates a daily summary, and suggests thoughtful comments — powered by LLaMA via Groq.

✨ Features

🔍 Scrapes your LinkedIn feed using Playwright browser automation
🧠 Filters AI-related posts from the noise
📋 Generates a daily summary of key AI themes and insights
💬 Suggests professional comments for each relevant post
⚡ Fast & free LLM inference via Groq + LLaMA 3.3


🛠️ Tech Stack
ToolPurposePlaywrightBrowser automation & LinkedIn scrapingGroqFree LLM API inferenceLLaMA 3.3 70BPost filtering, summarization & comment generationPython 3.10+Core languageJupyter NotebookDevelopment environment

⚙️ Setup
1. Clone the repo
bashgit clone https://github.com/your-username/linkedin-ai-agent.git
cd linkedin-ai-agent
2. Create a virtual environment
bashpython -m venv ai_agent_env
source ai_agent_env/bin/activate  # On Windows: ai_agent_env\Scripts\activate
3. Install dependencies
bashpip install playwright groq python-dotenv
playwright install chromium
4. Set up environment variables
Create a .env file in the root directory:
LINKEDIN_EMAIL=your-email@gmail.com
LINKEDIN_PASSWORD=your-linkedin-password
GROQ_API_KEY=gsk_your-groq-api-key

🔑 Get your free Groq API key at console.groq.com


🚀 Usage
Open and run the Jupyter notebook:
bashjupyter notebook linkedin_agent.ipynb
Or run the Python script directly:
bashpython linkedin_agent.py
The agent will:

Open a Chrome browser and log into LinkedIn
Scroll and scrape your feed
Pause for 2FA if required (you complete it manually)
Send posts to LLaMA for analysis
Print a formatted summary with suggested comments


📁 Project Structure
linkedin-ai-agent/
│
├── linkedin_agent.ipynb   # Main Jupyter notebook
├── linkedin_agent.py      # Standalone Python script
├── .env                   # Your credentials (never commit this!)
├── .gitignore
└── README.md

⚠️ Important Notes

LinkedIn ToS: This tool is intended for personal use only. Automated scraping may violate LinkedIn's Terms of Service.
Never commit your .env file — add it to .gitignore
Review AI-generated comments before posting — always add your personal touch
LinkedIn may occasionally block automated logins. If this happens, wait a few minutes and try again.


🔒 .gitignore
Make sure your .gitignore includes:
.env
ai_agent_env/
__pycache__/
*.pyc

🗺️ Roadmap

 Schedule daily runs via cron
 Email digest of AI summary
 Web dashboard to review and post comments
 Support for filtering by multiple topics


📄 License
MIT License — use freely, at your own risk.
