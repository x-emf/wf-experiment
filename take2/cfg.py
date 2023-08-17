N_CLASSES = 5

desired_websites = "opensecrets.org amazon.com"

websites = "adafruit.com reddit.com discord.com opensecrets.org amazon.com".split()
DESIRED_CLASS_INDICES = [ websites.index(i) for i in desired_websites.split() ]

TRAIN_TEST_SPLIT = 0.8 # Amount for training
