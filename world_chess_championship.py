def carlsen(S,X):
    n_cnt = S.count("N")
    c_cnt = S.count("C")
    d_cnt = S.count("D")
    
    c_pts = 2*c_cnt + d_cnt
    n_pts = 2*n_cnt + d_cnt
    

    if c_pts>n_pts:
        return(60*X)
    elif c_pts==n_pts:
        return(55*X)
    else:
        return(40*X)
        
t = int(input())
for _ in range(0,t):
    X = int(input())
    S = str(input())
    print(carlsen(S,X))
    
