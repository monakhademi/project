class density():
    def __init__(self, time, data):
        self.time = time
        self.data = data
        
    def expdensity(self):    
        duration = self.time.max() - self.time.min()
        density = len(self.data) / float(duration.days)
        return density