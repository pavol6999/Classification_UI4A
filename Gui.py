import random
import time
import tkinter

class GUI:

    def __init__(self,map_size, title):
        root = tkinter.Tk()
        root.title(title)
        self.canvas = tkinter.Canvas(root,width=map_size, height=map_size)
        self.map_size = map_size

        self.canvas.pack()





    def map_pos(self,coord):
        x_arr = (5000 + coord[0]) / (10000 / self.map_size)
        y_arr = (5000 + coord[1]) / (10000 / self.map_size)
        return x_arr, y_arr



    def draw_points(self,points_dir, animate, gauss):
        self.canvas.delete("points")
        colors = {'R': ['red','brown1'],
                  'G': ['green','SpringGreen2'],
                  'B': ['blue', 'DodgerBlue2'],
                  'P': ['purple','purple1']
                  }


        random.shuffle(points_dir)
        i=0

        if animate:
            for point in points_dir:

                    x, y = self.map_pos((point[0][0],point[0][1]))
                    x1, y1 = (x - 5), (self.map_size - y -5)
                    x2, y2 = (x + 5), (self.map_size - y +5)
                    self.canvas.create_oval(x1, y1, x2, y2, fill=colors[point[1]][0], outline="black", tags='points')

                    if i%1000==0:
                        self.canvas.update_idletasks()
                        self.canvas.update()
                        time.sleep(0.02)
                    i+=1
        else:
            if gauss != 'gauss':
                for point in points_dir:
                    x,y=self.map_pos((point[0][0], point[0][1]))
                    x1,y1 =(x-10),(self.map_size - y - 10)
                    x2, y2 = (x+10) , (self.map_size -y + 10)
                    self.canvas.create_rectangle(x1,y1,x2,y2,fill=colors[point[1]][1], outline='')
            for point in points_dir:

                    x, y = self.map_pos((point[0][0],point[0][1]))
                    x1, y1 = (x - 5), (self.map_size - y -5)
                    x2, y2 = (x + 5), (self.map_size - y +5)
                    self.canvas.create_oval(x1, y1, x2, y2, fill=colors[point[1]][0], outline="black", tags='points')
        self.canvas.mainloop()



