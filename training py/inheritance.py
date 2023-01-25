class land_habitat:
    def attribute(self):
        print("survives on land")
        
    

class water_habitat:
    def attribute(self):
        print("survives on water")
    
class mammals(land_habitat,water_habitat):
    def attribute(self):
        print("survives on land and water")

    
obj=mammals()
print(obj.attribute)
