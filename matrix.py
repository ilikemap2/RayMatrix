import sys
import numpy as np

print("Make space between values.")

n = map(float, input("Reflactive Index>> ").split())
r = map(float, input("Curvature>> ").split())
d = map(float, input("Thickness>> ").split())

n = list(n)
n.insert(0, 1.0)
r = list(r)
d = list(d)

print(n)

all_matrix = []
        
def calculate_matrix():
    
    i = len(r)
    
    matrix_list = []
    
    l_n = n[i]
    l_n_1 = n[i-1]
    l_r = r[i-1]
    l_d = d[i-1]
    
    last_matrix = np.array([[1,0],[(-(l_n-l_n_1)/(l_r*l_n)),(l_n_1/l_n)]])
    
    matrix_list.append(last_matrix)
    
    i -= 1
        
    while i >= 1:
        
        i -= 1
        X = i
        
        n_n = n[X+1]
        n_n_1 = n[X]
        n_r = r[X]
        n_d = d[X]
        
        id_matrix = np.array([[1,n_d],[0,1]])
        
        matrix_list.append(id_matrix)
        
        X_matrix = np.array([[1,0],[(-(n_n-n_n_1)/(n_r*n_n)),(n_n_1/n_n)]])
        
        matrix_list.append(X_matrix)
        
    all_matrix = matrix_list
    
    return matrix_list
        
if len(n)==(len(r)+1):
    if len(n)==(len(d)+1):
        if len(n)>=3:
            All = calculate_matrix()
            
            N = 2
            
            seki = All[0] @ All[1]
            
            while N <= (len(All) - 1):
                
                seki = seki @ All[N]
                
                N += 1
                
            f = -1/seki[1,0]
            print(f)
        