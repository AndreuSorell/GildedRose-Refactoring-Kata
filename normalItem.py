from item import Item
class NormalItem(Item):
    def __init__(self, name, sellIn, quality):
        Item.__init__(self, name, sellIn, quality)

    def updateQuality(self):
        if self.quality > 0:
            if self.sellIn < 0:
                self.sellIn -= 1
                self.quality -= 2
            else:
                self.sellIn -= 1
                self.quality -= 1
        if self.quality < 0:
            self.quality = 0

if __name__ == '__main__':
    NormalItem(name="+5 Dexterity Vest", sellIn=10, quality=20).updateQuality()