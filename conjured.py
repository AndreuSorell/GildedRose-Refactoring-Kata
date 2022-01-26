from item import Item
class Conjured(Item):
    def updateQuality(self):
        if self.quality > 0:
            self.sellIn -= 1
            self.quality -= 2
        if self.quality < 0:
            self.quality = 0
