import random

Nouns = ["Anxiety", "Death", "Confusion", "Lonliness", "Life", "Weakness", "Hate", "Failure", "Fear","Belief", "Attention", "Pain", "Desire", "Trust", "Liberty", "Fiction", "Coldness", "Chaos"]

Verbs = ["Accept", "Accuse", "Adapt", "Apologize", "Attempt", "Fail", "Grow", "Grind", "Improve", "Insist", "Cry", "Complain", "Compare", "Burn", "Burst", "Care", "Appreciate", "Discover", "Give", "Dislike"]

Adjectives = ["Able", "Angry", "Animal", "Anxious", "Capable", "Brilliant", "Bitter", "Brave", "Best", "Competitive", "Common", "Conscious", "Crazy", "Creative", "Dramatic", "Dirty", "Drunk", "Difficult"]

Subject = ["I", "You", "He", "She", "It", "We", "You", "They"]

Articles = ["A", "An", "The"]

Prepositions = ["About", "After", "Against", "Among", "Amidst", "Before", "Below", "Under", "To", "Till", "throughout", "towards", "Inside", "Behind", "Beneath", "Past", "By", "Beyond"]

Conjunctions = ["And", "Another", "Actually", "First", "Still", "Then", "Thus", "Therefore", "Least", "Last", "Also", "Lastly", "After", "Accordingly"]

def Sentence_Generator():
  x = (random.choice(Subject), random.choice(Verbs), random.choice(Prepositions).lower(), random.choice(Articles),random.choice(Adjectives),random.choice(Conjunctions),random.choice(Adjectives),random.choice(Nouns))
  return x

print(Sentence_Generator())
