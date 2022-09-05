from functools import reduce
from mean_median_mode_variance_range import *

def kurt(user_input):
    mean_data=mean_meadian_mode(user_input,"1")
    new_list=[]
    for i in user_input:
        new_list.append((i-mean_data)**4)
    
    standar_dev=(quartile(user_input,"3")**2)
    numerator=reduce((lambda x,y:x+y),new_list)
    deno=len(user_input)*standar_dev
    return (numerator/deno)

   