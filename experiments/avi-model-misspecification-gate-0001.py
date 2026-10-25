"""Missing-state bias test. pip install numpy scipy matplotlib"""
import numpy as np
from scipy.linalg import expm
from scipy.optimize import least_squares
A=np.array([[0,1,0],[-1,-.4,.3],[0,0,-.5]])
t=np.arange(0,10.01,.25)
H=np.array([expm(A*s)[0,:] for s in t])
rng=np.random.default_rng(1729)
observed=H@np.array([.7,-.2,1.])+rng.normal(0,.01,len(t))
training=t<=5

def pred(p,tt,extended):
    x,v,g,w=p[:4]
    if extended:
        a,k=p[4:]
        M=np.array([[0,1,0],[-w,-g,a],[0,0,-k]])
        init=np.array([x,v,1.])
    else:
        M=np.array([[0,1],[-w,-g]])
        init=np.array([x,v])
    return np.array([(expm(M*s)@init)[0] for s in tt])

for name,ext in [('reduced',False),('added_term',True)]:
    p0=[.7,-.2,.4,1]+([.3,.5] if ext else [])
    lb=[-3,-3,.01,.2]+([-2,.05] if ext else [])
    ub=[3,3,2,3]+([2,2] if ext else [])
    fit=least_squares(lambda p:pred(p,t[training],ext)-observed[training],p0,bounds=(lb,ub),xtol=1e-11,ftol=1e-11,gtol=1e-11)
    rmse=lambda mask:float(np.sqrt(np.mean((pred(fit.x,t[mask],ext)-observed[mask])**2)))
    print(name, 'train',rmse(training),'validation',rmse(~training), 'params',fit.x)
state=np.linalg.lstsq(H[training],observed[training],rcond=None)[0]
for label,mask in [('train',training),('validation',~training)]:
    print('complete_reference',label,float(np.sqrt(np.mean((H[mask]@state-observed[mask])**2))))
