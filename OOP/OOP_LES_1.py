class Element:
    def __init__(self, name, melting_t, boil_t):
        self.name = name
        self.melting_t = melting_t
        self.boil_t = boil_t
        
    
    def change_of_scale(self, temperature, scale):
        
        if scale == 'K':
            temperature -= 273.16
            scale = 'C'  
        elif scale == 'F':
            temperature = (temperature - 32) * 5/9
            scale = 'C'
            
        self.temperature = temperature    
        self.scale = scale
        
        return self.temperature, self.scale
        
        
    
    def state_of_aggregation(self):
        if self.temperature >= self.melting_t and self.temperature < self.boil_t:
            return f"The state of aggregation of {self.name} is: melted. The temperature is {int(self.temperature)} {self.scale},"
        elif self.temperature >= self.boil_t:
            return f"The state of aggregation of {self.name} is: boiled. The temperature is {int(self.temperature)} {self.scale}"
        else:
            return f"The state of aggregation of {self.name} is: the same. The temperature is {int(self.temperature)} {self.scale}"
    
    
  

el2 = Element('water', 100, 200)

print(el2.change_of_scale(500, 'K'))
print(el2.state_of_aggregation())