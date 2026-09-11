# The chat bot application was set up to accept user messages on a web endpoint, and to use a cloud adapter to process conversations. 
# Error handling was added to provide feedback on processing error and return the proper response during the message processing.

# Importing required libraries
import sys
import traceback
from datetime import datetime
from aiohttp import web
from aiohttp.web import Request, Response
from botbuilder.core import TurnContext
from botbuilder.core.integration import aiohttp_error_middleware
from botbuilder.integration.aiohttp import (
    CloudAdapter,
    ConfigurationBotFrameworkAuthentication,
)
from botbuilder.schema import Activity, ActivityTypes

from bots.echo_bot import EchoBot
from config import DefaultConfig


# Loading application configuration
application_settings = DefaultConfig()


# Creating authentication and adapter
authentication = ConfigurationBotFrameworkAuthentication(application_settings)
bot_adapter = CloudAdapter(authentication)


# Handling unexpected errors during conversation
async def handle_error(turn_context: TurnContext, exception: Exception):

    # Displaying error details
    print(f"\nUnexpected Error: {exception}", file=sys.stderr)
    traceback.print_exc()

    # Sending error message
    await turn_context.send_activity(
        "An unexpected error occurred while processing the request."
    )

    # Sending restart message
    await turn_context.send_activity(
        "Please correct the issue and restart the chatbot."
    )

    # Sending trace information
    if turn_context.activity.channel_id == "emulator":

        error_trace = Activity(
            type=ActivityTypes.trace,
            timestamp=datetime.utcnow(),
            label="Error Trace",
            name="Conversation Error",
            value=str(exception),
            value_type="https://www.botframework.com/schemas/error",
        )

        await turn_context.send_activity(error_trace)


# Assigning error handler
bot_adapter.on_turn_error = handle_error


# Creating chatbot object
chatbot = EchoBot()


# Receiving incoming requests
async def process_messages(request: Request) -> Response:

    return await bot_adapter.process(request, chatbot)


# Creating web application
web_application = web.Application(
    middlewares=[aiohttp_error_middleware]
)


# Registering message endpoint
web_application.router.add_post(
    "/api/messages",
    process_messages,
)


# Starting application
if __name__ == "__main__":

    web.run_app(
        web_application,
        host="localhost",
        port=application_settings.PORT,
    )