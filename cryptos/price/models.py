from django.db import models
class Coin(models.Model):
    datetime = models.DateTimeField(auto_now=True)
    price = models.FloatField()
    change = models.FloatField()
    amount_bought = models.FloatField()
    def __str__(self) -> str:
        
        return f'price of {self.__name__} in {self.datetime} is {self.price} with the chnage of {self.change}'
    class Meta:
        abstract = True

class ADA(Coin):
    pass

class BTC(Coin):
    pass
class ETH(Coin):
    pass
class BNB(Coin):
    pass
class SOL(Coin):
    pass

