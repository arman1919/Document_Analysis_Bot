```markdown
# Telegram Document Analysis Bot

This Telegram bot allows users to upload PDF documents and extract information from them through natural language queries. The bot utilizes OpenAI's language model for question answering and document analysis.

## Getting Started

To get started with the bot, follow these instructions:

### Prerequisites

- Python 3.10 or higher
- Telegram bot token
- OpenAI API key

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your_username/telegram-document-analysis-bot.git
   cd telegram-document-analysis-bot
   ```

2. Install the required Python packages:

   ```bash
   pip install -r requirements.txt
   ```

### Usage

1. Obtain a Telegram bot token from the BotFather and an OpenAI API key.
2. Set the `TOKEN` variable in `bot_doc_analiz_TG.py` to your Telegram bot token.
3. Set the `openai_api_key` variable in `Doc_Bot.py` to your OpenAI API key.
4. Build and run the Docker container:

   ```bash
   docker build -t telegram-doc-bot .
   docker run -d telegram-doc-bot
   ```

5. Start chatting with your bot on Telegram. You can upload PDF documents and ask questions about them.

## Bot Commands

- `/start`: Start the conversation with the bot.
- `/help`: Get help on how to use the bot.