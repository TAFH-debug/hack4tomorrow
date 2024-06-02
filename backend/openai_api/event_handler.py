from openai import AssistantEventHandler
import logging

class EventHandler(AssistantEventHandler):
    
    def __init__(self):
        super().__init__()
        self.answer = None

    def on_message_done(self, message) -> None:
        logging.getLogger().info("AI: " + message.content[0].text.value)
        self.answer = message.content[0].text.value
        