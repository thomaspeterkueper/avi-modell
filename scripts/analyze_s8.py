#!/usr/bin/env python3
"""AVI H0 oscillator analysis of author-exported FigS8 FRA frequency sweep.
No artificial data. CSV/TXT columns must be explicitly assigned.
Example:
 python analyze_s8.py --input vertical_with_magnet.txt --freq-col 0 --amp-col 1 --unit nm --output s8_result.json
"""
import argparse, json, numpy as np
from scipy.optimize import least_squares

def main():
 p=argparse.ArgumentParser()
 p.add_argument('--input',required=True);p.add_argument('--freq-col',type=int,required=True)
 p.add_argument('--amp-col',type=int,required=True);p.add_argument('--unit',choices=['m','nm','um','V'],required=True)
 p.add_argument('--delimiter',default=None);p.add_argument('--skiprows',type=int,default=0)
 p.add_argument('--output',default='s8_result.json')
 a=p.parse_args()
 x=np.loadtxt(a.input,delimiter=a.delimiter,skiprows=a.skiprows)
 f=x[:,a.freq_col]; amp=x[:,a.amp_col]
 good=np.isfinite(f)&np.isfinite(amp)&(f>0)&(amp>=0)
 f,amp=f[good],amp[good]
 if len(f)<8: raise ValueError('Need at least 8 valid data points')
 # Magnitude with nonnegative baseline and common transfer function;
 # amplitude B arbitrary unless instrument is calibrated.
 def predict(theta):
  f0,Q,B,c=theta
  r=f/f0
  return B/np.sqrt((1-r*r)**2+(r/Q)**2)+c
 bounds=([0.2*min(f),1.,0.,0.],[5*max(f),1e5,np.inf,np.inf])
 start=[f[np.argmax(amp)],40.,max(amp.max()/40,1e-15),max(0,float(np.percentile(amp,5)))]
 fit=least_squares(lambda t:predict(t)-amp,start,bounds=bounds,max_nfev=20000)
 f0,Q,B,c=map(float,fit.x)
 out={'source':a.input,'unit':a.unit,'n':len(f),'model':'amplitude |chi(f)| plus positive offset','f0_Hz':f0,'Q':Q,'B_unscaled':B,'offset':c,'rms_residual':float(np.sqrt(np.mean((predict(fit.x)-amp)**2))),'converged':bool(fit.success),'notes':['Unweighted fit; no confidence bounds until measurement uncertainties available','Requires explicit instrument scaling and independent thermal/optical backgrounds','Not an AVI-anomaly test']}
 if a.unit != 'V':
  fac={'m':1.,'nm':1e-9,'um':1e-6}[a.unit]
  out['resonant_amplitude_m_excluding_offset']=float(B*Q*fac)
  out['force_first_harmonic_N_if_M128mg']=float(1.28e-4*(2*np.pi*f0)**2*B*fac)
 with open(a.output,'w') as h:json.dump(out,h,indent=2)
 print(json.dumps(out,indent=2))
if __name__=='__main__': main()
