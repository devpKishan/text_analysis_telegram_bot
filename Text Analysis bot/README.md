# Telegram Text Analysis Bot

A simple Telegram bot that analyzes text messages for various features like word count, character count, sentence count, and more. Built with Python using the `pyTelegramBotAPI` library.

## Features

- 📝 **Word Count**: Counts the total number of words in a message.
- 🔠 **Character Count**: Counts the total number of characters.
- 📄 **Sentence Count**: Identifies the number of sentences.
- 🔣 **Syllable Count**: Counts syllables based on vowel patterns.
- 🌟 **Unique Words**: Counts unique words.
- ♾️ **Repeated Words**: Detects repeated words.
- 👑 **Nouns**: Extracts nouns from the message.
- 🏃 **Verbs**: Identifies verbs based on endings like `ing`, `ed`, and `es`.
- ☁️ **Adjectives**: Extracts adjectives ending in `ous`.
- 💨 **Adverbs**: Extracts adverbs ending in `ly`.
- 🔍 **Full Analysis**: Provides a complete breakdown of the message.

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/telegram-text-analysis-bot.git
   cd telegram-text-analysis-bot
   ```

2. **Create a virtual environment (optional but recommended)**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Get your Telegram bot token**:
   - Create a bot using [BotFather](https://t.me/BotFather) and get the bot token.

5. **Configure your bot token**:
   Open the `config.py` file and paste your bot token:
   ```python
   BOT_TOKEN = "YOUR_BOT_TOKEN_HERE"
   ```

6. **Run the bot**:
   ```bash
   python bot.py
   ```

## Commands

| Command            | Description                         |
|--------------------|-------------------------------------|
| `/start`           | Start the bot and show a welcome message |
| `/help`            | Display available commands          |
| `/full_analysis`   | Get a full analysis of the message  |
| `/word_count`      | Count the number of words           |
| `/character_count` | Count the number of characters      |
| `/sentence_count`  | Count the number of sentences       |
| `/syllable_count`  | Count the number of syllables       |
| `/unique_word_count` | Count unique words                 |
| `/misspelled_words`| Show misspelled words               |
| `/repeated_words`  | Show repeated words                 |
| `/nouns`           | Extract nouns                       |
| `/verbs`           | Extract verbs                       |
| `/adjectives`      | Extract adjectives                  |
| `/adverbs`         | Extract adverbs                     |

## Project Structure

```
telegram-text-analysis-bot/
├── analysis.py        # Core logic for text analysis
├── bot.py             # Main bot implementation
├── commands.py        # Command handlers for bot
├── config.py          # Configuration file for bot token
├── requirements.txt   # Dependencies
└── README.md          # Project documentation
```

## License

This project is licensed under the MIT License.