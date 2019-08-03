"""
Author: Vinay
Date: <5/10/2018>
"""

from visualise import show_vegetation_type
from visualise import show_vegetation_density
from visualise import show_wind_speed
from visualise import show_bushfire
from visualise import show_fire_risk

import csv 
import math
import random



# The following functions must return the data in the form of a
# list of lists; the choice of data type to represent the value
# in each cell, for each file type, is up to you.

def load_vegetation_type(filename):
    '''Open a csv file and return a list of lists. 
    The data type inside the lists are string.'''
    with open(filename) as file:
        reader = csv.reader(file)
        datalist=[row for row in reader]
    return datalist
    


def load_vegetation_density(filename):
    '''Open a csv file and return a list of lists. 
    The data type inside the lists is float.'''
    datalist=[]
    #count=0
    with open(filename) as file:
        reader = csv.reader(file)
        for row in reader:
            ##turn each row into a list
            listinside=[]
            for data in row:
                ## turn all the blanks to None type.
                if data=='':
                    listinside.append(None);
                    #count+=1
                else:
                    ##if it's not a blank, then turn it to float number and append it into a list
                    listinside.append(float(data))
            ## append every inner list into the outer list.
            datalist.append(listinside)
    #print(count)
    return datalist

def load_wind_speed(filename):
    '''Open a csv file and return a list of lists. 
    The data type inside the lists is float.
    (Same with the function "load_vegetation_density(filename)")'''
    datalist=[]
    #count=0
    with open(filename) as file:
        reader = csv.reader(file)
        for row in reader:
            listinside=[]
            for data in row:
                if data=='':
                    listinside.append(None);
                    #count+=1
                else:
                    listinside.append(float(data))
            datalist.append(listinside)
    #print(count)
    return datalist
                    

def load_bushfire(filename):
    '''Open a csv file and return a list of lists. '''
    with open(filename) as bushfire_csvfile:
       reader = csv.reader(bushfire_csvfile)
       # get row from table
       bushfire_list = [row for row in reader]
    return bushfire_list  


    


# The argument to this function is a wind speed map, in the
# form of a list of lists; it is the same data structure that
# is returned by your implementation of the load_wind_speed
# function.

def highest_wind_speed(wind_speed):
    '''input:a list of lists covered vegetation types mapped from the function:load_wind_speed.
       output: the highest speed in the whold map.'''
    ##initialize the highest speed:
    highest_speed=0.0
    ##go through all the list stored in the outer list:
    for list_inside in wind_speed:
        ##go through all the elements in every inner list:
        for i in range(len(list_inside)):
            ## compare each element with the highest speed: 
            if(list_inside[i]!=None and list_inside[i]>highest_speed):
                highest_speed=list_inside[i]
    return highest_speed
        
        


# The argument to this function is a vegetation type map, in the
# form of a list of lists; it is the same data structure that
# is returned by your implementation of the load_vegetation_type
# function.
    

def find_vegetation_type_dict():
    ''' Go through the biggest vegetation type file and made a specific dictionary
    which covers all the vegetation types. Since some csv files didn't include 
    all the vegetation types.
    All the numbers of vegetations are initialized to zero.'''
    ##Go through the biggest vege type file to find all the vegetations instead of making an assumption:
    all_vege_type=load_vegetation_type("data/act/vegetation_type.csv")
    newdict={}
    ##Make a new dictionary to store all the vege types:
    for list_inside in all_vege_type:
        for i in range(len(list_inside)):
            ##escape the blanks:
            if(list_inside[i]==""):
                continue
            elif (list_inside[i] not in all_vege_type):
                newdict[list_inside[i]]=0
            ##If this type has already exists, then skip it:
            elif(list_inside[i] in all_vege_type):
                continue
    return newdict


def count_cells(vegetation_type):
    '''input:a list of lists mapped from the function:load_vegetation_type, which 
       recorded the vegetation types in a specific local area.
       output: The name of vegetations and their cell numbers.If some vegetations never appear, the 
       number would be 0.'''   
    vegetable_and_cells=find_vegetation_type_dict()
     ##go through all the list stored in the outer list:
    for list_inside in vegetation_type:
         ##go through all the elements in every inner list:
         for i in range(len(list_inside)):
             ##judge whether this element appears in the dict or not, if it's a blank then it will never be inside the dict.
             if(list_inside[i] in vegetable_and_cells):
                 ## if this cell is occupied by a specific vegetation type, the cell number should add 1.
                 num_of_cells=vegetable_and_cells[list_inside[i]]
                 num_of_cells+=1
                 vegetable_and_cells[list_inside[i]]=num_of_cells
     ##print out the final solution:
    for x in vegetable_and_cells:
        print(x,": ",vegetable_and_cells[x])
        

# The arguments to this function are a vegetation type map and
# a vegetation density map, both in the form of a list of lists.
# They are the same data structure that is returned by your
# implementations of the load_vegetation_type and load_vegetation_density
# functions, respectively.

def count_area(vegetation_type, vegetation_density):
    '''input: two lists of lists.
       The first parameter: vegetation_type, which recorded the vegetation 
       types in a specific local area.
       The second parameter: vegetation density, which recorded a corresponding
       density of the vegetation appeared in the former list of lists.
       
       for example:
           
           [[Forest, Woodland],[Forest, Grassland]]
           [[0.50, 0.80],[0.40,0.10]]
          
           It means the density of Forest is 0.50 and 0.80 is for Woodland (and so on).
           
       output: The name of vegetations and the area they covered.
       
       Since one single cell's area is 100*100 sqm, the covered area should be 
       100*100*density, and the whole covered area should be the summation.
       In the upper example, the output for Forest should be "Forest :  9000.0 sq m".
       
       If some vegetations never appear, the number would be 0.'''
    vegetable_and_area=find_vegetation_type_dict()
    ## recording the length of vegetation types' lists, these two lists of lists should own the same length.
    length=len(vegetation_type)
    for density in vegetation_density:
        ##put elements in the later list into the former list, then the length of the whole list should be length*2:
        vegetation_type.append(density)
    ## go through the top half of this huge list (which means the vege type part):
    for i in range(length):
         ##judge whether this element appears in the dict or not:
         for j in range(len(vegetation_type[i])):
             if(vegetation_type[i][j] in vegetable_and_area):
                 area=vegetable_and_area[vegetation_type[i][j]]
                 ## go to the back half, find the corresponding density, and make a calculation:
                 area+=100*100*vegetation_type[i+length][j]
                 vegetable_and_area[vegetation_type[i][j]]=area
     ##print out the final solution:
    for x in vegetable_and_area:
        print(x,": ",float(vegetable_and_area[x]),"sq m")
        
                     
            
# The arguments to this function are:
# x and y - integers, representing a position in the grid;
# vegetation_type - a vegetation type map (as returned by your
#   implementation of the load_vegetation_type function);
# vegetation_density - a vegetation density map (as returned by
#   your implementation of the load_vegetation_density function);
# wind_speed - a wind speed map (as returned by your implementation
#   of the load_wind_speed function).

def fire_risk_factor_calculator(type_of_vegetation,dens):
    '''Calculate the fire risk according to the known conditions.'''
    fire_risk_factor=0.0
    if (type_of_vegetation=="Shrubland" or type_of_vegetation=="Pine Forest"):
        fire_risk_factor=math.sqrt(0.2+dens)
    elif(type_of_vegetation=="Urban Vegetation" or type_of_vegetation=="Golf Course"):
        fire_risk_factor=math.sqrt(0.05+dens)
    elif(type_of_vegetation=="Arboretum"):
        fire_risk_factor=math.sqrt(0.1+dens)
    elif(type_of_vegetation!=""):
        fire_risk_factor=math.sqrt(dens)
    return fire_risk_factor


  
def fire_risk(x, y, vegetation_type, vegetation_density, wind_speed):
    '''Calculate the fire risk factor for each cell, if needed, adding their neighbour's fire risk
    factor and return a single float number.'''
    column=x # Considering x as the column
    row=y # Considering y as the row
    coulumn_contents = []
    row_contents = []
    nearest_cell =0 # nearest cell where the fire might me impacted
    if wind_speed[row][column]!=None:
        nearest_cell = math.floor(wind_speed[row][column])
    for row_index in range(-nearest_cell, nearest_cell + 1):
        for column_index in range(-nearest_cell, nearest_cell + 1):
           
            coulumn_contents.append(column_index)
            row_contents.append(row_index)
    risk_factor = 0
    vegetationType_for_each_row=0
    vegetationDensity_for_each_row=0 
    for each_row in range(0, len(row_contents)):
        if((row + row_contents[each_row]) >= 0 and (column + coulumn_contents[each_row]) >= 0) :
            if  (row + row_contents[each_row])< len(vegetation_type) and (column + coulumn_contents[each_row]) < len(vegetation_type[row + row_contents[each_row]]):
                vegetationType_for_each_row=vegetation_type[row + row_contents[each_row]][column + coulumn_contents[each_row]]
                vegetationDensity_for_each_row=vegetation_density[row + row_contents[each_row]][column + coulumn_contents[each_row]]
                risk_factor+=fire_risk_factor_calculator(vegetationType_for_each_row,vegetationDensity_for_each_row)

    return risk_factor
               
# The arguments to this function are an initial bushfile map (a list
# of lists, as returned by your implementation of the load_bushfire
# function), a vegetation type map (as returned by your implementation
# of the load_vegetation_type function), a vegetation density map (as
# returned by your implementation of load_vegetation_density) and a
# positive integer, representing the number of steps to simulate.
    

       
def simulate_bushfire(initial_bushfire, vegetation_type, vegetation_density, steps):
    '''simulate the fire impact, if a single cell is caught on fire, then all its neighbours would
    catch fire in one step. Return the simulation result for the fire map.'''   
    bushfires=[]
    # to get all the element indexes from the array whose value is 1
    # found this idea from stackoverflow
    bushfires=[(ix,iy) for ix, row in enumerate(initial_bushfire) for iy, i in enumerate(row) if i == '1']
    print(bushfires)
    # displacement of all the nearest pixels 
    surrounding_pixels = ((-1,-1), (-1,0), (-1,1),
                          (0,-1),          (0, 1),
                          (1,-1),  (1,0),  (1,1))
    
    for each_step in range(1,steps):
        
        for each_bushfire in set(bushfires):
            
            for surrounding_pixel in surrounding_pixels:
                # new point around point(x,y)
                if((each_bushfire[0]+surrounding_pixel[0])>=0 and (each_bushfire[1]+surrounding_pixel[1])>=0):
                    if( (each_bushfire[0]+surrounding_pixel[0])<len(initial_bushfire) and (each_bushfire[1]+surrounding_pixel[1])<len(initial_bushfire)):
                        if(initial_bushfire[each_bushfire[0]+surrounding_pixel[0]][each_bushfire[1]+surrounding_pixel[1]]!=''):
                            bushfires.append((each_bushfire[0]+surrounding_pixel[0],each_bushfire[1]+surrounding_pixel[1]))

                

    for bushfire in bushfires:
        while(bushfire[0]<len(initial_bushfire)and bushfire[1]<len(initial_bushfire) and initial_bushfire[bushfire[0]][bushfire[1]]):
            initial_bushfire[bushfire[0]][bushfire[1]]='1'
            break
    return initial_bushfire
                
                    

# The arguments to this function are two bushfile maps (each a list
# of lists, i.e., same format as returned by your implementation of
# the load_bushfire function).

def compare_bushfires(bushfire_a, bushfire_b):
    '''that takes two bushfire maps (a & b) and returns the percentage
of cells that are the same '''
    # Total number of cells in both bushfire_a and bushfire_b
    total_cells = len(bushfire_a)*len(bushfire_a[0])

    # Total nuber of empty cells 
    number_of_blank_cells=sum(x.count('') for x in bushfire_a)
   
    # Total number of simialar cells in bushfire_a and busfire_b
    number_of_similar_cells =0
    for index in range(len(bushfire_a)):
        for innerindex in range(len(bushfire_a[index])):
            if(bushfire_a[index][innerindex]==bushfire_b[index][innerindex] and bushfire_a[index][innerindex]!=''):
                number_of_similar_cells = number_of_similar_cells +1
    percentage_of_similar_cells=number_of_similar_cells/(total_cells-number_of_blank_cells)
    return percentage_of_similar_cells



# The arguments to this function are:
# initial_bushfire - an initial bushfile map (a list of lists, same
#   as returned by your implementation of the load_bushfire function);
# steps - a positive integer, the number of steps to simulate;
# vegetation_type - a vegetation type map (as returned by your
#   implementation of the load_vegetation_type function);
# vegetation_density - a vegetation density map (as returned by
#   your implementation of the load_vegetation_density function);
# wind_speed - a wind speed map (as returned by your implementation
#   of the load_wind_speed function).
def simulate_bushfire_stochastic(initial_bushfire, steps,
        vegetation_type, vegetation_density,
        wind_speed):
    '''Simulate the fire  impact Stochastically with a chance of fire risk '''
    final_fire_risk=[]
    bushfires=[]
    
    # to get all the element indexes from the array whose value is 1
    # found this idea from stackoverflow
    bushfires=[(ix,iy) for ix, row in enumerate(initial_bushfire) for iy, i in enumerate(row) if i == '1']

    # displacement of all the nearest pixels 
    surrounding_pixels = ((-1,-1), (-1,0), (-1,1),
                          (0,-1),          (0, 1),
                          (1,-1),  (1,0),  (1,1))

    for y_coordinate in range(len(vegetation_type)):
        every_fire_risk = []
        for x_coordinate in range(len(vegetation_type[y_coordinate])):
            # get fire risk for   
            every_fire_risk.append(fire_risk(x_coordinate, y_coordinate, vegetation_type, vegetation_density, wind_speed))
        final_fire_risk.append(every_fire_risk)

    for each_step in range(steps):
        
        for each_bushfire in set(bushfires):
            
            for surrounding_pixel in surrounding_pixels:
            
                if 0 <= (each_bushfire[0] + surrounding_pixel[0]) < len(initial_bushfire) and 0 <= (each_bushfire[1] + surrounding_pixel[1]) < len(initial_bushfire) :
                    if ( initial_bushfire[each_bushfire[0] + surrounding_pixel[0]][each_bushfire[1] + surrounding_pixel[1]] == '0'):
                        
                      
                        bushfires.append((each_bushfire[0] + surrounding_pixel[0], each_bushfire[1] + surrounding_pixel[1]))

    for bushfire in bushfires:
        while(bushfire[0]<len(initial_bushfire)and bushfire[1]<len(initial_bushfire) and initial_bushfire[bushfire[0]][bushfire[1]]):
            initial_bushfire[bushfire[0]][bushfire[1]]='1'
            break

    return initial_bushfire
    
          



if __name__ == '__main__':
     load_density_map = load_vegetation_density("../data_and_code/data/anu/vegetation_density.csv")
#    load_type_map = load_vegetation_type("../data_and_code/data/anu/vegetation_type.csv")
#    load_wind_speed_map = load_wind_speed("../data_and_code/data/anu/wind.csv")
#    initial_bushfire=load_bushfire("../data_and_code/data/anu/initial_2003_bushfire.csv")
#    simulate1=simulate_bushfire(initial_bushfire, load_type_map, load_density_map, 16)
#    show_bushfire(simulate1)
#    bushfire_a = load_bushfire("../data_and_code/data/south/initial_2003_bushfire.csv")
#    bushfire_b = load_bushfire("../data_and_code/data/south/2003_bushfire.csv")
#    print(compare_bushfires(bushfire_a, bushfire_b))
#    initial_bushfire = load_bushfire("../data_and_code/data/anu/initial_2003_bushfire.csv")
#    initial_bushfire = load_bushfire("../data_and_code/data/south/2003_bushfire.csv")
#    vegetation_type = load_vegetation_type("../data_and_code/data/south/vegetation_type.csv")
#    vegetation_density = load_vegetation_density("../data_and_code/data/south/vegetation_density.csv")
#    wind_speed = load_wind_speed("../data_and_code/data/south/wind.csv")
#    stochastic_bush_fire =simulate_bushfire_stochastic(initial_bushfire, 80, vegetation_type, vegetation_density, wind_speed)
#    show_bushfire(stochastic_bush_fire)

    vegetation_density = load_vegetation_density("../data_and_code/data/south/vegetation_density.csv")
    vegetation_type = load_vegetation_type("../data_and_code/data/south/vegetation_type.csv")
    count_cells(vegetation_type)
#    print(initial_bushfire)
#     
#    final_bushfire =simulate_bushfire(initial_bushfire, vegetation_type, vegetation_density,26)
#    show_bushfire(final_bushfire)
