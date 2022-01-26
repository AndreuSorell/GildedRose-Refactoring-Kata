from item import Item
class AgedBrie(Item):
    def updateQuality(self):
        if self.quality < 50:
            if self.sellIn < 0:
                self.sellIn -= 1
                self.quality += 2
            else:
                self.sellIn -= 1
                self.quality += 1
        if self.quality > 50:
            self.quality = 50
