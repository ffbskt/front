__author__ = 'denis'
import random
import matplotlib.pyplot as plt
import numpy as np

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
        #print self.table.__len__(), self.table[0].__len__()
        for i in range(barriers):
            place = random.choice(self.freespace)
            Barrier(place, self)
        for i in range(victims):
            place = random.choice(self.freespace)
            Victim(place, self)
        for i in range(predators):
            place = random.choice(self.freespace)
            Predator(place, self)
    def live(self, epoch=5):
        self.epoch_stat = np.zeros([epoch, 3])
        #print self.epoch_stat
        for i in range(epoch):
            self.epoch_stat[self.epoch] = self.epoch, self.predator_count, self.victim_count

            self.epoch += 1
            #self.viuve()
            for j in self.table:
                for k in j:
                    try:
                        k.move()
                        #print k.position
                    except AttributeError:
                        pass

        #print self.freespace, self.table
    def dinamic(self):
        plt.plot(self.epoch_stat[:, 0], self.epoch_stat[:, 1])
        plt.show()


    def viuve(self):
        for i in range(self.size[0]):
            print
            for j in range(self.size[1]):
                if self.table[i][j].__class__.__name__[0] == 's':
                    print ' ',
                else:

                    print self.table[i][j].__class__.__name__[0],
                           #self.table[i][j].potential([i,j]))
        print "\n-----e", self.epoch, "------"



class OceanObject(object):
    def __init__(self, freepoint, Ocean):
        self.position = []
        self.position.append(freepoint / Ocean.size[1])
        self.position.append((freepoint - Ocean.size[1]*self.position[0]) % Ocean.size[0])
        self.Ocean = Ocean
        self.age = 0
        #print self.position
        Ocean.freespace.remove(freepoint)
        Ocean.table[self.position[0]][self.position[1]] = self

    def __getitem__(self, item):
        return self.__class__.__name__[0]

class Barrier(OceanObject):
    pass
    #def __init__(self, freepoint, Ocean):
        #Ocean.table[self.position[0]] = self

class Victim(OceanObject):
    def __init__(self, freepoint, Ocean):
        Ocean.victim_count += 1
        #print type(freepoint) == int, freepoint
        if type(freepoint) == int:
            super(Victim, self).__init__(freepoint, Ocean)
        else:
            self.Ocean = Ocean
            self.age = 0
            self.position = freepoint
            self.gorged = 10
    def move(self):
        self.age += 1
        if self.age % 3 == 0:
            #print "dddd", self.age
            self.reproduction()
        #print "potent ", self.potential(), "pos ", self.position
        self.Ocean.table[self.position[0]][self.position[1]] = ' '
        if self.potential(['B', 'V']) != []:
            self.position = random.choice(self.potential(['B', 'V']))
        privius_obj = self.Ocean.table[self.position[0]][self.position[1]]
        if privius_obj.__class__.__name__[0] == 'P':
            #print "KILL"
            Ocean.victim_count -= 1
            privius_obj.gorged = 3
        else:
            self.Ocean.table[self.position[0]][self.position[1]] = self
    def reproduction(self):
        if self.potential(['B', 'V']) != []:
            position = random.choice(self.potential(['B', 'V']))
            if self.Ocean.table[position[0]][position[1]].__class__.__name__[0] == 'P':
                self.Ocean.table[position[0]][position[1]].gorged += 5
            else:
                sun = self.__class__(position, self.Ocean)
                self.Ocean.table[sun.position[0]][sun.position[1]] = sun

    def potential(self, reserved_place):
        potential = []
        for i in [self.down(reserved_place), self.up(reserved_place),
                  self.left(reserved_place), self.right(reserved_place)]:
            if i != [[]]:
                potential.append(i)
        return potential

    def down(self, reserved_place):
        if (self.position[0] + 1 < self.Ocean.size[0] and
            self.Ocean.table[self.position[0] + 1][self.position[1]].__class__.__name__[0]
                not in reserved_place):
            return [self.position[0] + 1, self.position[1]]
        else:
            return [[]]
    def up(self, reserved_place):
        if (self.position[0] - 1 >= 0 and
            self.Ocean.table[self.position[0] - 1][self.position[1]].__class__.__name__[0]
                not in reserved_place):
           # print [self.position[0] - 1][self.position[0]]
            return [self.position[0] - 1, self.position[1]]
        else:
            #print 123
            return [[]]
    def right(self, reserved_place):
        if (self.position[1] + 1 < self.Ocean.size[1] and
            self.Ocean.table[self.position[0]][self.position[1] + 1].__class__.__name__[0]
                not in reserved_place):
            return [self.position[0], self.position[1] + 1]
        else:
            return [[]]
    def left(self, reserved_place):
        if (self.position[1] - 1 >= 0 and
            self.Ocean.table[self.position[0]][self.position[1] - 1].__class__.__name__[0]
                not in reserved_place):
            return [self.position[0], self.position[1] - 1]
        else:
            return [[]]

class Predator(Victim):
    def __init__(self, freepoint, Ocean):
        Ocean.predator_count += 1
        super(Predator, self).__init__(freepoint, Ocean)
        self.gorged = 3

    def move(self):
        self.age += 1
        if self.age % 40 == 0:
            #print "dddd", self.age
            self.reproduction()
        #print "pred", self.age
        if self.age > self.gorged:
            #print "DEATH"
            Ocean.predator_count -= 1
            self.Ocean.table[self.position[0]][self.position[1]] = ' '
        self.Ocean.table[self.position[0]][self.position[1]] = ' '
        if self.potential(['B', 'P']) != []:
            self.position = random.choice(self.potential(['B', 'P']))
        privius_obj = self.Ocean.table[self.position[0]][self.position[1]]
        if privius_obj.__class__.__name__[0] == 'V':
            self.gorged = 3
            privius_obj = ' '
        self.Ocean.table[self.position[0]][self.position[1]] = self



def main():
    Ocean1 = Ocean([20, 30], 8, 0, 10)
    Ocean1.viuve()
    #print Ocean1.table[3][0].potential() #table[3][0].down() ????????
    #Ocean1.table[3][0].move()
    #Ocean1.viuve()
    Ocean1.live(1000)
    Ocean1.dinamic()

if __name__ == '__main__':
    main()