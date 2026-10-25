"""AVI-OBSERVABILITY-0002: joint full-state reconstruction and unobservable control.
Dependencies: numpy. Run: python experiments/avi-observability-gate-0002.py
"""
import json
import numpy as np

A=np.array([[0,1,0],[-1,-.4,.3],[0,0,-.5]],float)

def evolve_matrix(M,times,dt=.01):
    assert all(t>=0 and round(t)==t for t in times)
    values={0:np.eye(3)}
    state=np.eye(3)
    for tick in range(1,round(max(times)/dt)+1):
        def f(z):return M@z
        a=f(state);b=f(state+dt*a/2);c=f(state+dt*b/2);d=f(state+dt*c)
        state=state+dt*(a+2*b+2*c+d)/6
        if tick%round(1/dt)==0:values[round(tick*dt)]=state.copy()
    return np.array([values[t][0,:] for t in times])

def assess(M,times,sigma=.01,reps=2000,seed=1729):
    H=evolve_matrix(M,times)
    sv=np.linalg.svd(H,compute_uv=False)
    rank=int(np.linalg.matrix_rank(H))
    out={"sample_times":times,"rank":rank,"singular_values":sv.tolist(),
         "condition_number":float(sv[0]/sv[-1]) if rank==3 else None}
    if rank<3:
        out["joint_reconstruction"]="not identifiable"
        return out
    truth=np.array([.7,-.2,1.])
    rng=np.random.default_rng(seed)
    data=H@truth+rng.normal(0,sigma,(reps,len(times)))
    estimated=np.linalg.lstsq(H,data.T,rcond=None)[0].T
    out["rmse"]=np.sqrt(np.mean((estimated-truth)**2,axis=0)).tolist()
    out["theoretical_sd"]=(sigma*np.sqrt(np.diag(np.linalg.inv(H.T@H)))).tolist()
    return out

if __name__=="__main__":
    control=A.copy();control[1,2]=0
    report={"id":"AVI-OBSERVABILITY-0002","type":"BASELINE","sigma":.01,"seed":1729,
    "replicates":2000,"state_truth":[.7,-.2,1.],
    "standard_short":assess(A,[0,1,2]),
    "standard_long":assess(A,list(range(11))),
    "insufficient_samples":assess(A,[1,2]),
    "decoupled_negative_control":assess(control,list(range(11)))}
    print(json.dumps(report,indent=2))
