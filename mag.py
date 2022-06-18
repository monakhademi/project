class earthquk():
    def __init__(self, depth):
        self.depth = depth

    def depth_to_words(self):
        if 0 < self.depth < 70:
            return "shallow"
        elif 70 < self.depth < 300:
            return "intermediate"
        elif 300 < self.depth < 700:
            return "shallow"