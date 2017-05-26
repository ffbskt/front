__author__ = 'denis'
import random
import matplotlib.pyplot as plt
import numpy as np


gorg_value = 30
gorg_value_eat = 10
pred_reprod = 90
victim_reprod = 5
class Ocean:
    def __init__(self, size=[3, 3], barriers=0, victims=0, predators=0):
        self.size = size
        self.bariers = barriers
        self.victims = victims
        self.predators = predators
        self.freespace = range(size[0]*size[1])
        self.table = [[' ' for i in range(size[1])] for j in range(size[0])]
        self.epoch = 0
        self.victim_count = 0
        self.predator_count = 0
        self.Crichers = []
        for i in range(barriers):
            place = random.choice(self.freespace)
            Barrier(place, self)
        for i in range(victims):
            place = random.choice(self.freespace)
            self.Crichers.append(Victim(place, self))
        for i in range(predators):
            place = random.choice(self.freespace)
            self.Crichers.append(Predator(place, self))
    def live(self, epoch=5):
        self.epoch_stat = np.zeros([epoch, 3])
        #print self.epoch_stat
        for i in range(epoch):
            self.epoch_stat[self.epoch] = self.epoch, self.predator_count, self.victim_count
            self.epoch += 1
            #self.viuve()
            for j in self.Crichers:
                try:
                    j.move()
                except AttributeError:
                    pass # Only if I want change Criche on string

        #print self.freespace, self.table
    def dinamic(self):
        print self.Crichers.__len__()
        plt.plot(self.epoch_stat[:, 0], self.epoch_stat[:, 1])
        plt.plot(self.epoch_stat[:, 0], self.epoch_stat[:, 2])
        plt.show()


    def viuve(self):
        for i in range(self.size[0]):
            print
            for j in range(self.size[1]):
                if self.table[i][j].__class__.__name__[0] == 's':
                    print ' ',
                else:
                    print self.table[i][j].__class__.__name__[0],
        print "\n-----e", self.epoch, "------"



class OceanObject(object):
    def __init__(self, freepoint, Ocean):
        self.position = []
        self.position.append(freepoint / Ocean.size[1])
        self.position.append((freepoint - Ocean.size[1]*self.position[0]) % Ocean.size[0])
        self.Ocean = Ocean
        self.age = 0
        Ocean.freespace.remove(freepoint)
        Ocean.table[self.position[0]][self.position[1]] = self

    def __getitem__(self, item):
        return self.__class__.__name__[0]

class Barrier(OceanObject):
    pass
    #def __init__(self, freepoint, Ocean):
        #Ocean.table[self.position[0]] = self


class Cricher(OceanObject):
    def __init__(self, freespace, Ocean):
        if type(freespace) == int:
            super(Cricher, self).__init__(freespace, Ocean) # Is it correct??
        else:
            self.Ocean = Ocean
            self.age = 0
            self.position = freespace
            self.gorged = gorg_value
            self.reserved = ['B']

    def born(self):
        position = random.choice(self.potential(self.reserved, self.position))
        privius_obj = self.Ocean.table[position[0]][position[1]]
        if privius_obj == ' ':
            self.Ocean.Crichers.append(self.__class__(position, self.Ocean))
            privius_obj = self.Ocean.Crichers[-1]
            self.stat_info(1)


    def die(self):
        self.Ocean.table[self.position[0], self.position[1]] = ' ' # could kill other
        self.Ocean.Crichers.remove(self)
        self.stat_info(-1)

    def move(self):
        position = random.choice(self.potential(self.reserved, self.position))
        privius_obj = self.Ocean.table[position[0]][position[1]]
        if privius_obj == ' ':
            self.Ocean.table[self.position[0]][self.position[1]] = ' '
            privius_obj = self
        else:
            self.colision()

    def stat_info(self, add):
        pass
        #self.Ocean.predator_count += add # Example
    def colision(self, privius_obj):
        pass

    def potential(self, reserved_place, position):
        potential = []
        for i in [self.down(reserved_place, position),
                  self.up(reserved_place, position),
                  self.left(reserved_place, position),
                  self.right(reserved_place, position)]:
            if i != [[]]:
                potential.append(i)
        return potential

    def down(self, reserved_place, position):
        if (position[0] + 1 < self.Ocean.size[0] and
            self.Ocean.table[position[0] + 1][position[1]].__class__.__name__[0]
                not in reserved_place):
            return [position[0] + 1, position[1]]
        else:
            return [[]]
    def up(self, reserved_place, position):
        if (position[0] - 1 >= 0 and
            self.Ocean.table[position[0] - 1][position[1]].__class__.__name__[0]
                not in reserved_place):
            return [position[0] - 1, position[1]]
        else:
            return [[]]
    def right(self, reserved_place, position):
        if (position[1] + 1 < self.Ocean.size[1] and
            self.Ocean.table[position[0]][position[1] + 1].__class__.__name__[0]
                not in reserved_place):
            return [position[0], position[1] + 1]
        else:
            return [[]]
    def left(self, reserved_place, position):
        if (position[1] - 1 >= 0 and
            self.Ocean.table[position[0]][position[1] - 1].__class__.__name__[0]
                not in reserved_place):
            return [position[0], position[1] - 1]
        else:
            return [[]]


class Victim(Cricher):
    def stat_info(self, add):
        self.Ocean.victim_count += add
    def colision(self, privius_obj):
        if privius_obj.__class__.__name__[0] == 'P':



class Predator(Victim):
    def __init__(self, freepoint, Ocean):
        Ocean.predator_count += 1
        super(Predator, self).__init__(freepoint, Ocean)
        Ocean.victim_count -= 1 #couse init made add victim
        self.gorged = gorg_value

    def move(self):
        self.age += 1
        #print self.age, self.gorged
        if self.age % pred_reprod == 0:
            if self.age < self.gorged: # BAGGGGGGGGGG
                self.reproduction(['B', 'P'])
        #print "pred", self.age
        #print self.Ocean.predator_count
        if self.age >= self.gorged:
            self.Ocean.predator_count -= 1
            self.Ocean.table[self.position[0]][self.position[1]] = ' '
            self.Ocean.Crichers.remove(self)
            return
            #print "DEATH1", #self.Ocean.table[self.position[0]][self.position[1]].age
            #del self
        self.Ocean.table[self.position[0]][self.position[1]] = ' '
        if self.potential(['B', 'P']) != []:
            self.position = random.choice(self.potential(['B', 'P']))
        privius_obj = self.Ocean.table[self.position[0]][self.position[1]]
        if privius_obj.__class__.__name__[0] == 'V':
            self.gorged += gorg_value_eat
            self.Ocean.victim_count -= 1
            self.Ocean.Crichers.remove(privius_obj)
            #privius_obj = ' '
        self.Ocean.table[self.position[0]][self.position[1]] = self


def main():
    Ocean1 = Ocean([30, 30], 0, 10, 10)
    Ocean1.viuve()
    #print Ocean1.table[3][0].potential() #table[3][0].down() ????????
    #Ocean1.table[3][0].move()
    #Ocean1.viuve()
    Ocean1.live(1200)
    Ocean1.dinamic()

if __name__ == '__main__':
    main()