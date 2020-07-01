def Comp_Simpsons(f, a, b, n):
    '''
    f: function to integrate over
    a: start point
    b: endpoint
    n: number of sub intervals to break domain into
    '''
    h = (b - a)/n
    
    XI_0 = f(a) + f(b)
    XI_1 = 0
    XI_2 = 0
    
    for i in np.arange(1, n):
        X = a + i*h
        
        if i % 2 == 0:
            XI_2 += f(X)
        else:
            XI_1 += f(X)
    
    XI = h*(XI_0 + 2*XI_2 + 4*XI_1)/3
    
    return XI
