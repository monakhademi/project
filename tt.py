class earthquk2:
    
    def __init__(self, data):
      self.mag=data.mag
      self.data = data
        

    def magnitude_injecction(self):
      for i in range(len(self.mag)):
        if self.data.iloc[i]['mag']< 2.0:
          self.data.iloc[i, self.data.columns.get_loc('Magnitude_Word')] ='Noticable'
        elif  self.data.iloc[i]['mag'] < 4.0:
          self.data.iloc[i, self.data.columns.get_loc('Magnitude_Word')] ='minor'
        elif  self.data.iloc[i]['mag'] < 5.0:
          self.data.iloc[i, self.data.columns.get_loc('Magnitude_Word')] ='light'
        elif  self.data.iloc[i]['mag'] < 6.0:
          self.data.iloc[i, self.data.columns.get_loc('Magnitude_Word')] ='moderate'
        elif  self.data.iloc[i]['mag'] < 7.0:
          self.data.iloc[i, self.data.columns.get_loc('Magnitude_Word')] ='strong'
        elif  self.data.iloc[i]['mag'] < 8.0: 
          self.data.iloc[i, self.data.columns.get_loc('Magnitude_Word')] ='major'
        else:
          self.data.iloc[i, self.data.columns.get_loc('Magnitude_Word')] ='epic'