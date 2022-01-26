from item import Item
class BackstagePass(Item):
    def updateQuality(self):
        if (self.quality < 50 or self.sellIn <0):
            self.quality += 1
            self.sellIn -= 1
            if self.sellIn < 11:
                self.sellIn -= 1
                self.quality += 1
            if self.sellIn < 6:
                self.sellIn -= 1
                self.quality += 1
            if self.sellIn < 0:
                self.quality = 0
        if self.quality >= 50:
            self.quality = 50
            self.sellIn -= 1
