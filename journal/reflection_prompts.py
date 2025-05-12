import random
import os

class ReflectionPrompts:
    def __init__(self):
        self.default_prompts = [
            "What did you learn from today's experience?",
            "How did this situation make you feel?",
            "Is there a different way you could have approached this?",
            "What are you grateful for today?",
            "What can you improve tomorrow?"
        ]
        self.mood_based_prompts = {
            "happy": ["What made you feel this way?", "How can you keep this positivity going?"],
            "sad": ["What is causing your sadness?", "How can you cope with these feelings?"],
            "anxious": ["What is making you feel anxious?", "What can you do to feel more in control?"]
        }

    def generate_prompt(self, mood=None, tags=None):
        if mood and mood in self.mood_based_prompts:
            return random.choice(self.mood_based_prompts[mood])
        elif tags and "work" in tags:
            return "What was the most challenging part of your work today?"
        else:
            return random.choice(self.default_prompts)