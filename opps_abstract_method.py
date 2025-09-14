from abc import ABC,abstractmethod

class car(ABC):
    @abstractmethod
    def go(self):
        pass
    @abstractmethod
    def stop(self):
        pass
    @abstractmethod
    def fm(self):
        pass

class maruthi(car):
    def go(self):
        #speed=10
        #time= speed*4
        print("car is moving forword") #time
        
    def stop(self):
        print('car is moving backword')
        
    def fm(self):
        print('the fm is on')

car1=maruthi()
car1.go()
car1.stop()
car1.fm()
