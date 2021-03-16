def borders(x1,x2,y1,y2):
    if x1<1 or y1<1 or x2<1 or y2<1:
        return False
    elif x1>8 or y1>8 or y2>8 or x2>8:
        return False
    return True

def p_allowed(cell_from,cell_to,white):
    x1, y1 = cell_from
    x2, y2 = cell_to
    return (x1 == x2 and (y1 + 1 == y2 or y1+2 ==y2 and y1==2) and y1!=1 and y2!=1 and borders(x1, x2, y1, y2) and white) or (x1 == x2 and (y1 - 1 == y2 or y1-2 ==y2 and y1==7) and y1!=8 and y2!=8 and borders(x1, x2, y1, y2) and not white)

def k_allowed(cell_from,cell_to):
    x1, y1 = cell_from
    x2, y2 = cell_to
    return borders(x1,x2,y1,y2) and max(abs(x2-x1),abs(y2-y1))==1;

def r_allowed(cell_from,cell_to):
    x1, y1 = cell_from
    x2, y2 = cell_to
    return (x2-x1)*(y2-y1)==0 and borders(x1,x2,y1,y2) and not x1==x2==y1==y2

def b_allowed(cell_from,cell_to):
    x1, y1 = cell_from
    x2, y2 = cell_to
    return abs(x2-x1)==abs(y1-y2) and borders(x1,x2,y1,y2) and abs(x2-x1)!=0

def q_allowed(cell_from,cell_to):
    return b_allowed(cell_from,cell_to) or r_allowed(cell_from,cell_to)

def n_allowed(cell_from,cell_to):
    x1, y1 = cell_from
    x2, y2 = cell_to
    if abs(x2-x1)==1:
        return abs(y2-y1)==2 and borders(x1,x2,y1,y2)
    elif abs(x2-x1)==2:
        return abs(y2-y1)==1 and borders(x1,x2,y1,y2) 
    return False

def board_move_ok(cell_from, cell_to, board):
    return True
