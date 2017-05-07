# From Fig. 1 of Bocquet 2010 "Beyond Gaussian Statistical Modeling
# in Geophysical Data Assimilation".
from common import *

from mods.Lorenz95 import core

t = Chronology(0.05,dkObs=1,T=4**3,BurnIn=20)

m = 10
f = {
    'm'    : m,
    'model': core.step,
    'noise': 0
    }

X0 = GaussRV(m=m, C=0.001)

jj = arange(0,m,2)
h = partial_direct_obs_setup(m,jj)
h['noise'] = 1.5
 
other = {'name': os.path.relpath(__file__,'mods/')}

setup = TwinSetup(f,h,t,X0,**other)

####################
# Suggested tuning
####################
#                                                 Expected RMSE_a:
#cfgs += EnKF('Sqrt',N=24,rot=True,infl=1.02)            # 0.32
#cfgs += PartFilt(N=50 ,NER=0.3,reg=1.7)                 # 1.0
#cfgs += OptPF(   N=50,NER=0.25,reg=1.4,Qs=0.4)          # 0.61
#cfgs += PartFilt(N=100,NER=0.2,reg=1.3)                 # 0.35
#cfgs += OptPF(   N=100,NER=0.2,reg=1.0,Qs=0.3)          # 0.37
#cfgs += PartFilt(N=800,NER=0.2,reg=0.8)                 # 0.25
#cfgs += OptPF(   N=800,NER=0.2,reg=0.6,Qs=0.1)          # 0.25

# Note: contrary to the article, we use, in the EnKF,
# - inflation instead of additive noise ?
# - Sqrt      instead of perturbed obs
# - random orthogonal rotations.
# The PartFilt is also perhaps better tuned?
# This explains why the above benchmarks are superior to article.

#cfgs += PFxN     (N=30, NER=0.4,reg=0.6,Qs=1.0,xN=1000) # 0.48
#cfgs += PFxN     (N=50, NER=0.3,reg=0.8,Qs=1.1,xN=100 ) # 0.43
#cfgs += PFxN     (N=100,NER=0.3,reg=0.5,Qs=1.0,xN=100 ) # 0.38
#cfgs += PFxN     (N=300,NER=0.3,reg=0.3,Qs=0.8,xN=100 ) # 0.29
#cfgs += PFxN_EnKF(N=25 ,NER=0.4 ,       Qs=1.5,xN=100)  # 0.49
#cfgs += PFxN_EnKF(N=50 ,NER=0.25,       Qs=1.5,xN=100)  # 0.36
#cfgs += PFxN_EnKF(N=100,NER=0.20,       Qs=1.0,xN=100)  # 0.31
#cfgs += PFxN_EnKF(N=300,NER=0.10,       Qs=1.0,xN=100)  # 0.28
# PFxN worse than PartFilt (bootstrap) with N>100. Potential causes:
# - Tuning
# - 'reg' is better (less bias coz 'no-uniq-jitter') than 'Qs'
