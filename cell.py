from graphics import Window, Line, Point


class Cell:
    def __init__(self, win: Window):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self._win = win

    def draw(self, x1, y1, x2, y2):
        if self._win is None:
            return
        
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        
        if self.has_left_wall:
            line = Line(Point(x1, y1), Point(x1, y2))
            self._win.draw_line(line)
        
        if self.has_top_wall:
            line = Line(Point(x1, y1), Point(x2, y1))
            self._win.draw_line(line)
        
        if self.has_right_wall:
            line = Line(Point(x2, y1), Point(x2, y2))
            self._win.draw_line(line)
            
        if self.has_bottom_wall:
            line = Line(Point(x1, y2), Point(x2, y2))
            self._win.draw_line(line)
            
    def draw_move(self, to_cell, undo = False):
        half_length1 = abs(self._x1 - self._x2) // 2
        x_center1 = self._x1 + half_length1
        y_center1 = self._y1 + half_length1
        
        half_length2 = abs(self._x1 - self._x2) // 2
        x_center2 = to_cell._x1 + half_length2
        y_center2 = to_cell._x1 + half_length2
        
        line_color = "red"
        if undo:
            line_color = "gray"
            
        line = Line(Point(x_center1, y_center1), Point(x_center2, y_center2))
        self._win.draw_line(line, fill_color=line_color)
        