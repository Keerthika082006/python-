from abc import ABC

class foodshop(ABC):
    
    def colour(self):
        pass
    def tables(self):
        pass
    def foods(self):
        pass

class pinjabi(foodshop):
    def colour(self):
        print('colour should be blue')
        
    def tables(self):
        print('mirror tables')
        
    def foods(self):
        print('panner butter masala , naan')
        print('chicken friedrice')

class mds(foodshop):
    def colour(self):
        print('colour should be yellow')
        
    def tables(self):
        print('wood tables')
        
    def foods(self):
        print('bread ombelet')
        print('black forest')

food=pinjabi()
food.colour()
food.tables()
food.foods()
