
MOVEMENT_SYMBOLS = '><v^'
EMPTY_SYMBOL = '.'
TREASURE_SYMBOL = '+'
BREADCRUMB_SYMBOL = 'X'
MOVEMENT_SYMBOLS_3D = '*|'


def get_nth_row_from_map(string,n,width,height):
    '''
    (string,int,int) --> (string)
    This function takes 4 parameters to the corresponding
    arguments,namely, string, n, width, height. This function
    returns the nth row of the treasure map. If n is not a
    valid row, an empty string is returned.
    
    >> Example : get_nth_row_from_map('^..>>>..v',1, 3, 3)
                 '>>>'
    
    >> Example : get_nth_row_from_map('.>>>.X',2,2,3)
                 '.X'
    
    >> Example : get_nth_row_from_map('***>>>XX',0,4,2)
                 '***>'
    
    >> Example : get_nth_row_from_map('>>++..**',0,5,2)
                 ''
  '''
    #height means "rows" here
    #width means "columns" here
    
    val = width
    if (len(string)!=width*height)or(n>=height): #validation check for n
        return ("")
    else:
        return_string = string[(n*width) : (n*width+width)]
    return return_string



def print_treasure_map(string,width,height):
    '''
    (string,int,int) --> ()
    This funtion takes 3 parameters of a treasure map
    string and prints out the treasure map according
    to the parameters passed of the arguments, width and height.
    
    According to question, we can assume that the width and height
    inputs will always match the characters in the map string and
    we can also assume that there will be no non-negative numerals
    so we are not applying a validation check for that...
    
    >>Example :  print_treasure_map("<..vvv..^",3,3)
                 <..
                 vvv
                 ..^
    
    >>Example : print_treasure_map(">>>...<<<....^^^",4,4)
                >>>.
                ..<<
                <...
                .^^^
                
    >>Example : print_treasure_map("<..vvv..^",3,3)
                >>>..
                .<<<^
    '''
    #height means "rows" here
    #width means "columns" here
    for i in range(0,height):
        print(string[(i*width):((i+1)*width)])
        
 

def change_char_in_map(string,rowindex,columnindex,c,width,height):
    '''
    (string,int,int,string,int,int) --> (string)
    This function takes a treasure map string,row and column index ,
    a character c ,and width and height as inputs. It returns a treasure map string
    with all characters same except for the character at the rowindex
    and columnindex parameters in original string replaced by character
    corresponding to argument c. If the row index or column index are out
    of range then the string returns unchanged.
    
    >>Example : change_char_in_map('.........', 1, 1, 'X', 3, 3)
                '....X....'
    
    >>Example : change_char_in_map('..>>..XX', 1, 2, '+', 4, 2)
                '..>>..+X'
    
    >>Example : change_char_in_map('..+++.***', 3, 3, '+', 3, 3)
                '..+++.***'
    
    >>Example : change_char_in_map('>>>...^^', 0,5, '+',4,2)
                '>>>...^^'
                
    '''
    #height means number of rows here
    #width means number of columns here
    if (len(string)==width*height)and(rowindex<height)and(columnindex<width):
        index_changed = (width*rowindex) + columnindex 
        string = string[0:index_changed]+c+string[index_changed+1:len(string)]
    return string
         

def get_proportion_travelled(string):
    '''
    (string) --> (float)
    This function takes a treasure map as input and returns as float
    the percentage of the map that was travelled (the number of
    breadcrumb symbols in the map
    
    >>Example : get_proportion_travelled('.X..X.XX.')
                0.44
    >>Example : get_proportion_travelled('.X..X.XX.XXXX')
                0.62
    >>Example : get_proportion_travelled('...')
                0.0
    '''
    num_breadcrumbs = 0
    for char in string:
        if char == BREADCRUMB_SYMBOL:
            num_breadcrumbs = num_breadcrumbs + 1
   
   # Calculating ratio of breadcrumbs to all characters...
    percentage_breadcrumbs = round(num_breadcrumbs/len(string),2)
    return percentage_breadcrumbs   



def get_nth_map_from_3D_map(string,n,width,height,depth):
    '''
    (string,int,int,int) --> (string)
    This map takes 3D treasure map string and integer width,
    height and depth as inputs and returns the nth map
    of the treasure map string.
    
    If n is not a valid map, an empty string is returned.
    
    >>> Example : get_nth_map_from_3D_map('..vv.<>....vv.<>..',1,3,3,2)
                '..vv.<>..'ki
    
    >>Example : get_nth_map_from_3D_map('^|vvX.X.v^.|', 0,2,2,3)
                '^|vv'
    
    >>Example : get_nth_map_from_3D_map('^|vvX.X.',1,2,2,2)
                'X.X.'
    
    >>Example : get_nth_map_from_3D_map('^|vvX.X..|vX.X.v', 3,4,2,2)
                ''
    
    >>Example : get_nth_map_from_3D_map('^|vvX.X..|..', 17,2,2,4)
                ''
    '''          
    
    if (n>=depth) or (len(string)!=width*height*depth): # Validation Check for arguments passed
        return""
    else:
        # return_string = string[(n*height*width):(n*height*width)+(height*width)]
        # return (return_string)
        curr_index=0
        treasure_string_array=[]
        for i in range(0, depth):
            curr_string = string[curr_index:(curr_index+(height*width))]
            treasure_string_array.append(curr_string)
            curr_index += (height*width)
        return treasure_string_array[n]
# print(get_nth_map_from_3D_map('..vv.<>....vv.<>..',1,3,3,2))
# print(get_nth_map_from_3D_map('.X.XXX.X..v.vXv.v.', 0, 3, 3, 2))
# print(get_nth_map_from_3D_map('.X.XXX.X..v.vXv.v.', 1, 3, 3, 2))
# print(get_nth_map_from_3D_map('^|vvX.X..|vX.X.v', 3,4,2,2))
# print(get_nth_map_from_3D_map('^|vvX.X.',1,2,2,2))
# print(get_nth_map_from_3D_map('^|vvX.X.v^.|', 2,2,2,3))
def print_3D_treasure_map(string,width,height,depth):
    '''
    (string,int,int,int) --> ()
    This function takes a 3D map string, width,height and depth
    as arguments. Depth means the number of maps in the 3D treasure
    map,  and each map would have the number of rows and columns
    as the the parameters corresponding to height and width arguments,
    respectively.
    
    According to question, we can assume that the width, height
    and depth inputs will always match the characters in the map
    string and we can also assume that there will be no non-negative
    numerals so we are not applying a validation check for that...
    
    >>Example : print_3D_treasure_map('..vv.<>....vv.<>..',3,3,2)
                ..v
                v.<
                >..

                ..v
                v.<
                >..
    >>Example : print_3D_treasure_map('^|vv',2,1,2)
                ^|

                vv
    >>Example : print_3D_treasure_map('^|vvX.X.',2,2,2)
                ^|
                vv

                X.
                X.
    >>Example : print_3D_treasure_map('^|vvX.X.v^.|', 2,2,3)
                ^|
                vv

                X.
                X.

                v^
                .|
    
    '''
    # start = 0
    # val = width
    # for i in range(0,depth):
    #     for row in range(0,height):
    #         for column in range(start,width):
    #             print(string[column],end='')
    #         start = start+val
    #         width = width + val
    #         print()

    #     if i!= (depth-1):  #Ensuring that no blank line is left after...
    #         print()        #... the 3D treasure map has been printed    
    curr_index=0
    for i in range(0, depth):
        whole_string = (get_nth_map_from_3D_map(string,i, width, height, depth))
        for j in range(curr_index,curr_index+width):
            string_per_line = whole_string[curr_index:curr_index+width]
            print(string_per_line)
            curr_index+=width
        if(i!=depth-1):
            print()
        curr_index = 0
            
# print_3D_treasure_map('.X.XXX.X..v.vXv.v.',3,3,2)          
# print_3D_treasure_map('^|vvX.X.v^.|', 2,2,3)
# print_3D_treasure_map('^|vvX.X.',2,2,2)
# print_3D_treasure_map('..vv.<>....vv.<>..',3,3,2)
# print_3D_treasure_map('^|vv',2,1,2)
# print_3D_treasure_map('^|vvX.X.v^.|', 2,2,3)
def change_char_in_3D_map(string, row_index, column_index, depth_index, c, width, height, depth):
    '''
   
    This function takes a treasure map string ,row,column and depth index and
    width, height and depth as inputs. It returns a treasure map string
    with all characters same except for the character at the rowindex, 
    depthindex and columnindex parameters in original string replaced by character
    corresponding to argument c.
    
    If the row index or column index are out of range then the string returns unchanged.
    
    >>Example : change_char_in_3D_map('.X.XXX.X..v.vXv.v.', 0, 0, 0, '#', 3, 3, 2)
                '#X.XXX.X..v.vXv.v.'
    
    >>Example : change_char_in_3D_map('>>>>....XXXX++++',1,2,1,'<',4,2,2)
                '>>>>....XXXX++<+'
    
    >>Example : change_char_in_3D_map('>>>..XX#',3,0,1,'*',2,2,2)
                '>>>..XX#'
    
    >>Example : change_char_in_3D_map('>>>...^^^^++', 4, 2, 1, '*', 3, 2, 2)
                '>>>...^^^^++'
                
    '''
    if (len(string)!=width*height*depth or row_index>=height or column_index>=width):
        return string
    final_map_string=""
    needed_map = get_nth_map_from_3D_map(string,depth_index,width,height,depth)
    edited_map=change_char_in_map(needed_map,row_index,column_index,c,width,height)  
    for i in range(0,depth):
        if i!=depth_index:
            final_map_string += get_nth_map_from_3D_map(string,i,width,height,depth)
        elif i==depth_index:
            final_map_string+=edited_map
    return final_map_string

# print(change_char_in_3D_map('.X.XXX.X..v.vXv.v.', 0, 0, 0, '#', 3, 3, 2))
# print(change_char_in_3D_map('>>>>....XXXX++++',1,2,1,'<',4,2,2))
# print(change_char_in_3D_map('>>>..XX#',3,0,1,'*',2,2,2))
# print(change_char_in_3D_map('>>>...^^^^++', 4, 2, 1, '*', 3, 2, 2))
# print_3D_treasure_map('>>+v >v+.^ *<v.<<vv ^^|> ^v+<   vv.. ^>>^^',4,3,3)
