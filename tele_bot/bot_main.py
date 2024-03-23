from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# Define bot token and username
TOKEN: Final = ""
BOT_USERNAME: Final = "@trendy_reporter_bot"

# Command to start conversation with the bot
async def start_command(update:Update, context:ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello, What can I help you with today!")

# Command to provide assistance
async def help_command(update:Update, context:ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hi, I'm trendy_reporter_bot.")

# Command to analyze user's query
async def analyze_command(update:Update, context:ContextTypes.DEFAULT_TYPE):
    # Check if there is text after the command
    if len(context.args) > 0:
        # Concatenate all arguments into a single string as the query
        query = ' '.join(context.args)
        ## TODO: Handle the AI analysis part based on the query
    else:
        await update.message.reply_text("Please provide a query after the /analyze command.")

# Function to handle responses based on user input
def handle_response(text: str) -> str:
    text = text.lower()
    match text:
        case "hello" : return f"Hello! I am awake!"
        case _ : return f"I do not understand. Please provide a valid command."

# Function to handle incoming messages
async def handle_message(update: Update, context:ContextTypes.DEFAULT_TYPE):
    # Determine the type of chat the message came from
    message_type: str = update.message.chat.type
    text: str = update.message.text
    print(f"User ({update.message.chat.id}) in {message_type}: {text}")

    # Handle bot responses based on chat type
    if message_type == 'group': 
        if BOT_USERNAME in text:
            # Extract message excluding bot username
            new_text : str = text.replace(BOT_USERNAME, '').strip()
            response: str = handle_response(new_text)
        else:
            return
    else: 
        # Handle responses for private chats
        response: str = handle_response(text=text) 
    
    print('Bot:', response)
    await update.message.reply_text(response)

# Function to handle errors
async def error(update: Update, context:ContextTypes.DEFAULT_TYPE):
    print(f"Update {update} caused error {context.error}")

if __name__ == "__main__":
    print("Starting Bot...")
    # Create the application instance
    app = Application.builder().token(TOKEN).build()

    # Register command handlers
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('analyze', analyze_command))

    # Register message handler
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    # Register error handler
    app.add_error_handler(error)

    # Start polling for updates
    app.run_polling(poll_interval=1)
