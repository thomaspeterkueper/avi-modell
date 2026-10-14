"""AVI-STATE-COMPLETENESS-0001: a reproducible standard-physics counterexample.
Run: python experiments/avi-state-completeness-gate-0001.py
Requires: numpy
"""
import json
import numpy as np

def solve(h0,dt=.01,T=20):
    state=np.array([0.,0.,float(h0)])
    def f(s):
        x,v,h=s
        return np.array([v,-x-.4*v+.3*h,-h/2])
    data=[state.copy()]
    for _ in range(round(T/dt)):
        a=f(state);b=f(state+dt*a/2);c=f(state+dt*b/2);d=f(state+dt*c)
        state=state+dt*(a+2*b+2*c+d)/6
        data.append(state.copy())
    return np.asarray(data)

def measure(dt):
    A=solve(1,dt);B=solve(-1,dt);C=solve(1,dt)
    dx=np.abs(A[:,0]-B[:,0]); dv=np.abs(A[:,1]-B[:,1])
    return {"dt":dt,"max_delta_x":float(dx.max()),
            "time_max_delta_x":float(dx.argmax()*dt),
            "max_delta_v":float(dv.max()),
            "duplicate_full_state_difference":float(np.max(np.abs(A-C))),
            "final_delta_x":float(dx[-1])}

if __name__=="__main__":
    outcome={"id":"AVI-STATE-COMPLETENESS-0001","class":"BASELINE",
     "model":"dx/dt=v; dv/dt=-x-0.4v+0.3h; dh/dt=-h/2",
     "A":[0,0,1],"B":[0,0,-1],"control_A_duplicate":[0,0,1],
     "measurements":[measure(d) for d in (.04,.02,.01)]}
    with open("avi-state-completeness-gate-0001-results.json","w") as f:json.dump(outcome,f,indent=2)
    print(json.dumps(outcome,indent=2))
