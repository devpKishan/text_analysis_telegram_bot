# commands.py
from telebot import TeleBot
from analysis import analyze_message

# Define the bot instance (this should use the token from config.py)
def register_commands(bot: TeleBot):
    welcome_message = """
    Welcome to the Bot! Join Our Community Channel for Bot related Update.
    """

    # Define the start command handler
    @bot.message_handler(commands=['start'])
    def start(message):
        bot.send_message(message.chat.id, welcome_message)

    # Define the help command handler
    @bot.message_handler(commands=['help'])
    def help(message):
        help_message = """
        Available commands:
        /start - Start the bot
        /help - Display available commands
        /full_analysis - Full Analysis of text
        /word_count - Count the number of words
        /character_count - Count the number of characters
        /sentence_count - Count the number of sentences
        /syllable_count - Count the number of syllables
        /unique_word_count - Count the number of unique words
        /misspelled_words - Show misspelled words
        /repeated_words - Show repeated words
        /nouns - Extract nouns
        /verbs - Extract verbs
        /adjectives - Extract adjectives
        /adverbs - Extract adverbs
        """
        bot.send_message(message.chat.id, help_message)

    # Define handlers for each feature
    @bot.message_handler(commands=['word_count'])
    def word_count(message):
        analysis = analyze_message(message)
        bot.send_message(message.chat.id, "Word count: " + str(analysis["words"]))

    @bot.message_handler(commands=['character_count'])
    def character_count(message):
        analysis = analyze_message(message)
        bot.send_message(message.chat.id, "Character count: " + str(analysis["characters"]))

    @bot.message_handler(commands=['sentence_count'])
    def sentence_count(message):
        analysis = analyze_message(message)
        bot.send_message(message.chat.id, "Sentence count: " + str(analysis["sentences"]))

    @bot.message_handler(commands=['syllable_count'])
    def syllable_count(message):
        analysis = analyze_message(message)
        bot.send_message(message.chat.id, "Syllable count: " + str(analysis["syllables"]))

    @bot.message_handler(commands=['unique_word_count'])
    def unique_word_count(message):
        analysis = analyze_message(message)
        bot.send_message(message.chat.id, "Unique word count: " + str(analysis["unique_words"]))

    @bot.message_handler(commands=['misspelled_words'])
    def misspelled_words(message):
        analysis = analyze_message(message)
        bot.send_message(message.chat.id, "Misspelled words: " + str(analysis["misspelled_words"]))

    @bot.message_handler(commands=['repeated_words'])
    def repeated_words(message):
        analysis = analyze_message(message)
        bot.send_message(message.chat.id, "Repeated words: " + str(analysis["repeated_words"]))

    @bot.message_handler(commands=['nouns'])
    def nouns(message):
        analysis = analyze_message(message)
        bot.send_message(message.chat.id, "Nouns: " + str(analysis["nouns"]))

    @bot.message_handler(commands=['verbs'])
    def verbs(message):
        analysis = analyze_message(message)
        bot.send_message(message.chat.id, "Verbs: " + str(analysis["verbs"]))

    @bot.message_handler(commands=['adjectives'])
    def adjectives(message):
        analysis = analyze_message(message)
        bot.send_message(message.chat.id, "Adjectives: " + str(analysis["adjectives"]))

    @bot.message_handler(commands=['adverbs'])
    def adverbs(message):
        analysis = analyze_message(message)
        bot.send_message(message.chat.id, "Adverbs: " + str(analysis["adverbs"]))

    @bot.message_handler(commands=['full_analysis'])
    def full_analysis(message):
        analysis = analyze_message(message)
        bot.send_message(message.chat.id, "\n".join([
            f"WORDS: {analysis['words']}",
            f"CHARACTERS: {analysis['characters']}",
            f"SENTENCES: {analysis['sentences']}",
            f"SYLLABLES: {analysis['syllables']}",
            f"UNIQUE WORDS: {analysis['unique_words']}",
            f"MISSPELLED WORDS: {analysis['misspelled_words']}",
            f"REPEATED WORDS: {analysis['repeated_words']}",
            f"NOUNS: {analysis['nouns']}",
            f"VERBS: {analysis['verbs']}",
            f"ADJECTIVES: {analysis['adjectives']}",
            f"ADVERBS: {analysis['adverbs']}"
        ]))
