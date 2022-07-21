from Dndboard import Dndboard
from time import sleep

board = Dndboard()
board.setBrightness(1.0)
for _ in range(10):
    board.fillRow(0,(0,0,255))
    sleep(0.1)
    board.fillRow(1,(0,255,255))
    sleep(0.1)
    board.fillRow(2,(255,255,255))
    sleep(0.1)
    board.fillRow(3,(255,0,255))
    sleep(0.1)
    board.fillRow(4,(200,0,255))
    sleep(0.1)
    board.fillRow(5,(255,100,100))
    sleep(0.1)
    board.fillRow(6,(100,100,100))
    sleep(0.1)
    board.fillRow(7,(200,120,100))
    sleep(0.1)
    board.fillRow(8,(50,200,100))
    sleep(0.1)
    board.fillRow(9,(170,200,255))
    sleep(0.1)
    board._pixels.fill((0,0,0))
    board._pixels.show()
