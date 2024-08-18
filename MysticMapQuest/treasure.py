
# Name : Shahmeer Sajid
# Student ID = 261073334

# Question 2 : Treasure! (85 points)


from treasure_utils import *

import random


def generate_treasure_map_row(width, boolean):
    # '''
    # (int,boolean) --> (string)
    
    # This function takes positive integer width and a
    # boolean value as inputs and returns a single row
    # of a treasure map. In the string, each character has
    # a 5/6 chance to be one the four basic movement symbols and
    # 1/6 chance to be an empty symbol.
    
    # In case of boolean value being True, there is 50%
    # chance that only one character is replaced by
    # one of the 3D movement symbols.
    
    # >> Example : random.seed(9)
    #              generate_treasure_map_row(7,False)
    #              '><∧∧vv.'
    
    # >> Example : random.seed(10)
    #              generate_treasure_map_row(12,False)
    #              'v<∧>v<>>><..'
                 
    # >> Example : random.seed(11)
    #              generate_treasure_map_row(5,True)
    #              '><>>*'
                 
    # >> Example : random.seed(15)
    #              generate_treasure_map_row(5,True)
    #              'v<<<.'
    
    # >> Example : random.seed(17)
    #              generate_treasure_map_row(6,True)
    #              '<>∧∧∧|'
    # '''
    
    # Basic_Mov=(width*5/6) # 5/6 of characters that must one of the 'Basic Movement Symbols'
    # if Basic_Mov-int(Basic_Mov)<=0.5: #Calculating Exact number of characters that belong to...
    #     Basic_Mov = int(Basic_Mov)   # ... 'Basic Movement Symbols'.
    # else:
    #     Basic_Mov = int(Basic_Mov)+1
    # BMcount=0
    # BCcount=0
    # D3count=0
    # row=""

    # while len(row)<width:
    #     n=random.randint(1,width) #generating a random number
        
    #     #As we have 4 characters in Basic Movement Symbols, so we will divide the...
    #     # ... random number generated, by 4, to see the remainder value that will...
    #     # ... determine which character should be printed.
    #     if BMcount<Basic_Mov:
    #         if n%4==0:
    #             row=row+MOVEMENT_SYMBOLS[0]
    #         if n%4==1:
    #             row=row+MOVEMENT_SYMBOLS[1]
    #         if n%4==2:
    #             row=row+MOVEMENT_SYMBOLS[2]
    #         if n%4==3:
    #             row=row+MOVEMENT_SYMBOLS[3]
    #         BMcount=BMcount+1
    #     else:
    #         remaining_char = width - Basic_Mov 
    #         row=row+(EMPTY_SYMBOL * remaining_char) # remaining 1/6 of characters belong to Empty Symbol
    
    # #Determing whether one of the characters will be replaced by a '3D Movement Symbol'? 
    # if boolean==True:
    #     #Determing a random position of the '3D Movement Symbol'
    #     num_index_changed = random.randint(0,width-1)
        
    #     #Determining a 50% chance for the character at at index calculated to be replaced by...
    #     # ... a '3D Movement Symbol'. Here we are applying two conditions to make poosibility for 50% chance...
    #     if num_index_changed % 2 == 0:
    #         row = row[0:num_index_changed] + MOVEMENT_SYMBOLS_3D[0] + row[num_index_changed+1:len(row)]
    #     elif num_index_changed>(width/2):
    #         row = row[0:num_index_changed] + MOVEMENT_SYMBOLS_3D[1] + row[num_index_changed+1:len(row)]
                
    # return row
    
    final_string=""
    new_final_string=""
    string_choices = ["MOVE", "MOVE", "MOVE", "MOVE","MOVE","EMPTY"]
    while len(final_string)<width:
        random_str = random.choice(string_choices)
        if random_str == "MOVE":
            random_num = random.randint(0,len(MOVEMENT_SYMBOLS)-1)
            final_string+=MOVEMENT_SYMBOLS[random_num]
        else:
            final_string+=EMPTY_SYMBOL
    if boolean:
        replace_decisions = [True, False]
        replace_choice = random.choice(replace_decisions)
        if replace_choice:
            char_index = random.randint(0, len(MOVEMENT_SYMBOLS_3D)-1)
            replace_char = MOVEMENT_SYMBOLS_3D[char_index]
            replacing_index = random.randint(0,len(final_string)-1)
            new_final_string = final_string[0:replacing_index] + replace_char + final_string[replacing_index:]
            final_string = new_final_string
    return final_string
# print(generate_treasure_map_row(6,True))  
# print( generate_treasure_map_row(7,False)) 

# print(generate_treasure_map_row(5, True))
    
            
def generate_treasure_map(width,height,boolean):
    '''
    (int,int,boolean) --> (string)
    This function creates and returns a treasure map of the parameter values of height and width.
    The first character of the map (row 0, column 0) must be the '>'symbol.
    The occurrence probabilities must be the same as the above function.
    
    >> Example : random.seed(52)
                 generate_treasure_map(3,3,True)
                 '><**v.*<.'
                 
    >> Example : random.seed(53)
                 generate_treasure_map(3,4,True)
                 '><*^v*v^*<<.'
    
    >> Example : random.seed(53)
                 generate_treasure_map(5,4,False)
                 '>v><.<^><.v^v^.v<^v.'
    '''
    row = ''
    for i in range(0,height):
        row = row + generate_treasure_map_row(width,boolean)
    return ('>' + row[1:len(row)]) #The first character must be the '>' symbol
    

def generate_3D_treasure_map(width,height,depth):
    '''
    (int,int,int) --> (string)
    This function creates and returns a 3D treasure map according to arguments
    corresponding to the parameters namely height,width and depth. The first character
    (row 0 column 0) must be a right pointing symbol, '>'. The occurrence
    probabilities in this 3D treasure map must be the same as in the previous
    functions.
    
    >> Example : random.seed(1)
                 generate_3D_treasure_map(5,2,2)
                 '><<|.>>>|.>>>|.*v<<.'
    
    >> Example : random.seed(10)
                 generate_3D_treasure_map(7,2,2)
                 '><>><<.*>^^v^.>>^<vv.>^*<^>.'
    
    >> Example : random.seed(15)
                 generate_3D_treasure_map(4,5,1)
                 '><<.<<v.<^*.>^^.^^v|'
    '''
    map3D = ''
    for i in range(depth):
        map3D = map3D + generate_treasure_map(width, height, True)

    return map3D


def follow_trail(map_string, start_col_index, start_row_index, start_depth_index,  width, height, depth, no_of_tiles):

    curr_map = get_nth_map_from_3D_map(map_string, start_depth_index, width, height, depth)
    curr_row_string = get_nth_row_from_map(curr_map,start_row_index, width, height)

    curr_column = start_col_index
    curr_row = start_row_index
    curr_depth = start_depth_index
    visited = 0
    num_treasures_collected = 0
    
    while visited < no_of_tiles or no_of_tiles==-1:
    
        char = curr_row_string[curr_column]
      
        if char in MOVEMENT_SYMBOLS :
            if char == ">" :
                
                visited+=1
                
                previous_char = ">"
                
                
                map_string = change_char_in_3D_map(map_string,curr_row,curr_column,curr_depth,BREADCRUMB_SYMBOL,width,height,depth)
                curr_map = get_nth_map_from_3D_map(map_string, curr_depth, width, height, depth)
                if curr_column != len(curr_row_string)-1:
                    curr_column+=1
                    
                else:
                    curr_column=0
                curr_row_string = get_nth_row_from_map(curr_map,curr_row,width,height)
                char = curr_row_string[curr_column]
                if char == BREADCRUMB_SYMBOL:
                   
                    print("Treasures collected: ",num_treasures_collected)
                    print("Symbols visited: ",visited)
                    return map_string
                if visited == no_of_tiles:
                    break
            if char == "<" :
                print("HERE")
                previous_char = "<"
                
                visited += 1
         
                
                map_string = change_char_in_3D_map(map_string,curr_row,curr_column,curr_depth,BREADCRUMB_SYMBOL,width,height,depth)
                curr_map = get_nth_map_from_3D_map(map_string, curr_depth, width, height, depth)
                
                if curr_column != 0:
                    curr_column-=1
           
                else:
                    curr_column=len(curr_row_string)-1
                curr_row_string = get_nth_row_from_map(curr_map,curr_row, width, height)
                char = curr_row_string[curr_column]
       
                if char == BREADCRUMB_SYMBOL:
                        print("Treasures collected: ",num_treasures_collected)
                        print("Symbols visited: ",visited)
                        return map_string
                if visited == no_of_tiles :
                    break
            if char == "v" :
                visited+=1
                
                previous_char = "v"
                
                map_string = change_char_in_3D_map(map_string,curr_row,curr_column,curr_depth,BREADCRUMB_SYMBOL,width,height,depth)
                curr_map = get_nth_map_from_3D_map(map_string, curr_depth, width, height, depth)
                if curr_row!=height-1:
                    curr_row+=1
                    
                else:
                    curr_row=0
                curr_row_string = get_nth_row_from_map(curr_map,curr_row,width,height)
                char = curr_row_string[curr_column]
                if char == BREADCRUMB_SYMBOL:
                        
                        print("Treasures collected: ",num_treasures_collected)
                        print("Symbols visited: ",visited)
                        return map_string
                if visited==no_of_tiles:
                    break
            
            if char == "^" :
                 
                visited+=1
                previous_char = "^"
             
                
                map_string = change_char_in_3D_map(map_string,curr_row,curr_column,curr_depth,BREADCRUMB_SYMBOL,width,height,depth)
                curr_map = get_nth_map_from_3D_map(map_string, curr_depth, width, height, depth)
                if curr_row!=0:
                    curr_row-=1
                else:
                    curr_row=height-1
                curr_row_string = get_nth_row_from_map(curr_map,curr_row,width,height)
                char = curr_row_string[curr_column]
                if char == BREADCRUMB_SYMBOL:
                       
                        print("Treasures collected: ",num_treasures_collected)
                        print("Symbols visited: ",visited)
                        return map_string
                if visited==no_of_tiles:
                    break
        if char in MOVEMENT_SYMBOLS_3D:
            if char == "*":
                
                visited+=1

                map_string = change_char_in_3D_map(map_string,curr_row,curr_column,curr_depth,BREADCRUMB_SYMBOL,width,height,depth)
                
                if curr_depth!=depth-1:
                    curr_depth+=1
                else:
                    curr_depth = 0
                curr_map = get_nth_map_from_3D_map(map_string, curr_depth, width, height, depth)
                
                curr_row_string = get_nth_row_from_map(curr_map,curr_row,width,height)
                char = curr_row_string[curr_column]
                if visited==no_of_tiles:
                    break
            if char == "|":
                visited+=1

                map_string = change_char_in_3D_map(map_string,curr_row,curr_column,curr_depth,BREADCRUMB_SYMBOL,width,height,depth)
                
                if curr_depth!=0:
                    curr_depth-=1
                else:
                    curr_depth = depth-1
                curr_map = get_nth_map_from_3D_map(map_string, curr_depth, width, height, depth)
                map_string = change_char_in_3D_map(map_string,curr_row,curr_column,curr_depth,BREADCRUMB_SYMBOL,width,height,depth)
                
                curr_row_string = get_nth_row_from_map(curr_map,curr_row,width,height)
                char = curr_row_string[curr_column]
                if visited==no_of_tiles:
                    break
            
                    
        if char in TREASURE_SYMBOL or char in EMPTY_SYMBOL:
            if char in TREASURE_SYMBOL:
                num_treasures_collected+=1
                
            visited+=1
            if previous_char == ">":
                if  curr_column!=len(curr_row_string)-1:
                    curr_column+=1
                else:
                    curr_column=0
            elif previous_char == "<":
                if  curr_column!=0:
                    curr_column-=1
                else:
                    curr_column=  len(curr_row_string)-1
            elif previous_char == "^":
                if curr_row!=0:
                    curr_row-=1
                    
                else:
                    curr_row=0
                curr_row_string = get_nth_row_from_map(curr_map,curr_row,width,height)     
            elif previous_char == "v":
                if curr_row!=height-1:
                    curr_row+=1
                    
                else:
                    curr_row=0
                    
            curr_row_string = get_nth_row_from_map(curr_map,curr_row,width,height)
            char = curr_row_string[curr_column]
            if visited==no_of_tiles:
                break
        if char in BREADCRUMB_SYMBOL:
          
            print("Treasures collected: ",num_treasures_collected)
            print("Symbols visited: ",visited)
            return map_string
    print("Treasures collected: ",num_treasures_collected)
    print("Symbols visited: ",visited)
    return map_string
                

#print(follow_trail('>>>v^..v^<<<', 2, 3, 0, 4, 3, 1, -1)) *****************************

#print(follow_trail('>>+v>v+.^*<v.<<vv^^|>^v+<vv..^>>^^', 2, 3, 2, 4, 3, 3, 100)) *************************************
# print_3D_treasure_map('>>+v>v+.^*<v.<<vv^^|>^v+<vv..^>>^^',4,3,3)
# #print(follow_trail('>>!v >v!. ^*<v     .<<v v^^| >^v!    <vv. .v>> ^^', 0, 1, 0, 4, 3, 3, 100))# **************CHECK THIS ******************

# print(len('>>!v>v!.^*<v.<<vv^^|>^v!<vv..v>>^^'))
# print(len('>X!XXX!.XXXXX.XXXv^XXXXXX!XvX..vXXX^'))