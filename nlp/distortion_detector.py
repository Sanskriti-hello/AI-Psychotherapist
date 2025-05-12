DISTORTION_PATTERNS = {
    "black_and_white": ["always", "never", "every time", "completely", "nothing", "everything"],
    "catastrophizing": ["ruined", "disaster", "worst ever", "hopeless", "unbearable", "end of the world", "irreparable"],
    "mind_reading": ["they think", "they must believe", "i know they", "they’re judging", "they’re disappointed", "they must hate me"],
    "personalization": ["it's all my fault", "I caused this", "they’re upset because of me", "if I had done something differently"],
    "overgeneralization": ["always", "never", "every", "none", "all", "everyone", "no one", "nothing will ever change"],
    "emotional_reasoning": ["I feel like", "it feels like", "I must be", "I'm worthless because I feel this way"],
    "should_statements": ["I should", "I must", "I have to", "I ought to", "I need to"],
    "labeling": ["I'm a failure", "I'm stupid", "I'm worthless", "I'm unlovable", "I'm a loser"],
    "discounting_the_positive": ["that doesn't count", "I'm just lucky", "it’s not that big of a deal"],
    "external_attribution": ["it's their fault", "they made me do this", "I couldn’t help it", "it’s because of them"],
    "control_fallacy": ["I must control everything", "I can't control anything", "I am responsible for how others feel"],
    "focusing_on_the_negative": ["nothing good happens", "everything is bad", "I always mess things up", "no one ever notices the good things"],
    "blaming": ["it's their fault", "they're responsible", "I'm just a victim", "if only they hadn't"],
    "heaven's reward fallacy": ["I’ll be rewarded if I just sacrifice", "if I’m good enough, good things will come to me"],
    "fortune_telling": ["I know it will go wrong", "this will never work", "there's no way this can succeed"],
    "magnification": ["this is the worst", "I can’t handle this", "this is a catastrophe", "I’ll never recover from this"],
    "minimization": ["it’s not a big deal", "it doesn’t matter", "it’s just a small thing"],
    "emotional_blackmail": ["if you loved me, you would", "I need to do this for them", "they’ll be angry if I don't"],
}

def detect_distortions(text: str) -> list:
    """
    Detects cognitive distortions based on keyword matching.
    Returns a list like ['black_and_white', 'catastrophizing']
    """
    distortions = []
    lower_text = text.lower()
    for distortion, patterns in DISTORTION_PATTERNS.items():
        for phrase in patterns:
            if phrase in lower_text:
                distortions.append(distortion)
                break
    return distortions
