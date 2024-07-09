import curses
from curses import wrapper
import queue
import time


MAZE = [
    ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
    ["#", "O", " ", " ", "#", " ", "#", " ", " ", " ", " ", "#", " ", "#", " ", " ", " ", "#", " ", " ", " ", " ", "#", " ", "#", " ", " ", " ", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", "#", "#", "#", " ", "#", " ", "#", "#", "#", "#", " ", " ", "#", " ", "#", " ", " ", " ", "#", " ", "#", "#", "#"],
    ["#", " ", "#", " ", " ", " ", " ", " ", " ", "#", " ", " ", " ", " ", " ", " ", "#", " ", "#", "#", " ", "#", "#", " ", "#", " ", "#", " ", " ", "#"],
    ["#", "#", "#", "#", "#", "#", "#", "#", " ", "#", " ", "#", "#", "#", " ", "#", "#", " ", "#", "#", " ", " ", "#", " ", "#", " ", "#", "#", " ", "#"],
    ["#", " ", " ", " ", " ", " ", " ", "#", " ", "#", " ", "#", " ", "#", " ", "#", " ", " ", " ", " ", " ", " ", "#", " ", " ", " ", " ", " ", " ", "#"],
    ["#", " ", "#", "#", "#", "#", " ", "#", " ", "#", "#", "#", " ", "#", " ", "#", "#", "#", "#", " ", " ", "#", "#", " ", "#", "#", "#", "#", " ", "#"],
    ["#", " ", " ", " ", "#", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "#", " ", "#", " ", " ", "#", " ", " ", " ", " ", " ", "#", " ", "#", "#"],
    ["#", "#", "#", " ", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", " ", "#", "#", "#", "#", " ", "#", "#", "#", "#", "#", "#", " ", "#"],
    ["#", " ", " ", " ", "#", " ", " ", " ", "#", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "#", " ", "#", " ", " ", " ", " ", " ", " ", "#"],
    ["#", " ", "#", "#", "#", "#", "#", " ", "#", " ", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", " ", "#", " ", "#", "#", "#", "#", "#", "#"],
    ["#", " ", " ", " ", " ", " ", "#", " ", " ", " ", "#", " ", " ", " ", " ", " ", " ", " ", " ", "#", " ", " ", "#", " ", " ", " ", " ", " ", " ", "#"],
    ["#", "#", "#", "#", "#", " ", "#", "#", "#", "#", "#", " ", "#", "#", "#", "#", " ", "#", " ", "#", " ", "#", "#", "#", "#", "#", "#", "#", " ", "#"],
    ["#", " ", " ", " ", "#", " ", " ", " ", " ", " ", " ", " ", "#", " ", " ", "#", " ", "#", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", " ", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", " ", "#", "#", " ", "#", "#", "#", "#", " ", "#", "#", "#", "#", "#", "#", "#", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "#", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "#"], 
    ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "X", "#"],
]


def show_maze(MAZE,stdscr,path=[]):
    yellow_ = curses.color_pair(1)
    red = curses.color_pair(2)
    for i,row in enumerate(MAZE):
        for j,value in enumerate(row):
            if (i,j) in path:
                stdscr.addstr( i , j*2 ,"X", red)
            else:
                stdscr.addstr( i , j*2 , value,yellow_)
            stdscr.refresh()
    time.sleep(0.3)
    
def find_start(MAZE,stdscr,start):
    for i,row in enumerate(MAZE):
        for j,value in enumerate(row):
            if value==start:
                return i,j

def find_path(MAZE,stdscr):
    start="O"
    end="X"
    start_pos=find_start(MAZE,stdscr,start)
    q=queue.Queue()
    q.put((start_pos,[start_pos]))

    visited=set( )
    
    while not q.empty():
        current_pos,path = q.get()
        
        row,col = current_pos
        show_maze(MAZE,stdscr,path)
        stdscr.clear()
        stdscr.refresh()
        if MAZE[row][col] == end:
            return path
        
        neighbours=find_neighbour(MAZE,row,col)
        for neighbour in neighbours:
            if neighbour in visited:
                continue
            r,c = neighbour
            if MAZE[r][c]=="#":
                continue
            
            new_path=path+[neighbour]
            q.put((neighbour, new_path))
            visited.add(neighbour)

def find_neighbour(MAZE,row,col):
    neighbors=[]
    if row > 0: #up
        neighbors.append((row-1,col))
    if row +1<len(MAZE):#down
        neighbors.append((row+1,col))
    if col > 0:#left
        neighbors.append((row,col-1)) 
    if col+1<len(MAZE[0]):#right
        neighbors.append((row,col+1))
    return neighbors
        
    
            
def main(stdscr):
    curses.init_pair(1,curses.COLOR_YELLOW,curses.COLOR_BLACK)
    curses.init_pair(2,curses.COLOR_RED,curses.COLOR_BLACK)
    curses.init_pair(3,curses.COLOR_GREEN,curses.COLOR_BLACK)
    
    find_path(MAZE,stdscr)
    
    stdscr.getkey()
    
wrapper(main)
