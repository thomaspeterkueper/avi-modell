"""AVI-ROBUSTNESS-0001: dimensionless oscillator reference experiment (Python >=3.10, numpy)."""
import json
import numpy as np

def integrate(zeta, dt=0.01, horizon=30.0):
    n = round(horizon/dt)
    t = np.linspace(0, horizon, n+1)
    s = np.array([1.0, 0.0])
    points = [s.copy()]
    def f(q):
        return np.array([q[1], -2*zeta*q[1]-q[0]])
    for _ in range(n):
        a=f(s); b=f(s+dt*a/2); c=f(s+dt*b/2); d=f(s+dt*c)
        s += dt*(a+2*b+2*c+d)/6
        points.append(s.copy())
    return t, np.array(points)

def run(zeta, dt):
    t,s=integrate(zeta,dt)
    r=np.linalg.norm(s,axis=1)
    E=0.5*r**2
    ix=np.flatnonzero(r>0.05)
    recovery = float(t[ix[-1]+1]) if len(ix) and ix[-1]<len(t)-1 else None
    return {"zeta":zeta,"dt":dt,"final_state_norm":float(r[-1]),
            "final_energy":float(E[-1]),"max_state_norm":float(r.max()),
            "recovery_5pct":recovery,"max_energy_increase_per_step":float(np.diff(E).max())}

if __name__=="__main__":
    result={"experiment":"AVI-ROBUSTNESS-0001","model_class":"BASELINE",
            "solver":"RK4","time_horizon":30,"initial_state":[1,0],
            "results":[run(z,d) for z in [0,0.2,1,-0.1] for d in [.04,.02,.01]]}
    with open("avi-robustness-0001-results.json","w",encoding="utf-8") as out:
        json.dump(result,out,indent=2)
    for item in result["results"]:
        if item["dt"]==.01:print(item)
