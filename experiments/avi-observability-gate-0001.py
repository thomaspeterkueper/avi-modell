"""AVI-OBSERVABILITY-0001: recover hidden h0 using noisy measurements of x(t).
Standard linear dynamics, synthetic measurements; no AVI-specific prediction.
No third-party dependencies. Run: python experiments/avi-observability-gate-0001.py
"""
import json, math, random

def evolve(h0, step=0.01, duration=10.0):
    s=[0.0,0.0,float(h0)]
    def f(z): return [z[1],-z[0]-0.4*z[1]+0.3*z[2],-0.5*z[2]]
    def add(a,b,factor): return [x+factor*y for x,y in zip(a,b)]
    out={0: s[0]}
    n=round(duration/step)
    for i in range(1,n+1):
        a=f(s);b=f(add(s,a,step/2));c=f(add(s,b,step/2));d=f(add(s,c,step))
        s=[x+step*(p+2*q+2*r+w)/6 for x,p,q,r,w in zip(s,a,b,c,d)]
        if i%100==0:out[i//100]=s[0]
    return out

def estimate(noise, windows, reps=200, seed=1729):
    # x0 and v0 are known; estimate ONLY h0 by weighted least squares.
    rng=random.Random(seed)
    k=evolve(1.0)
    gain=[k[i] for i in windows]
    gram=sum(g*g for g in gain)
    if gram<1e-14:return {"identified":False,"gramian":gram}
    estimates=[]
    for _ in range(reps):
        measured=[g+rng.gauss(0,noise) for g in gain]
        estimates.append(sum(g*y for g,y in zip(gain,measured))/gram)
    rmse=math.sqrt(sum((h-1.0)**2 for h in estimates)/reps)
    return {"identified":True,"gramian":gram,"rmse_h0":rmse,
            "theoretical_sd":noise/math.sqrt(gram),"mean_h0":sum(estimates)/reps}

def run():
    cases={}
    for window, times in {"initial_only":[0],"early":[1,2],"long":[1,2,3,4,5,6,7,8,9,10]}.items():
        cases[window]={str(s):estimate(s,times) for s in (0.0,0.01,0.1)}
    return {"id":"AVI-OBSERVABILITY-0001","class":"BASELINE",
            "seed":1729,"repetitions":200,"state":"(x,v,h)",
            "dynamics":"x'=v; v'=-x-0.4v+0.3h; h'=-0.5h",
            "truth":{"x0":0,"v0":0,"h0":1},
            "measurement":"y=x+Gaussian(0,sigma), sampled integer t",
            "assumptions":"x0 and v0 known; noise independent Gaussian",
            "cases":cases}

if __name__=="__main__":
    print(json.dumps(run(),indent=2,sort_keys=True))
