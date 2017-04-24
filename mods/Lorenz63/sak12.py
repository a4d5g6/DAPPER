# Reproduce results from
# table1 of sakov et al "iEnKF" (2012)

from common import *

from mods.Lorenz63.core import step, dfdx
from aux.utils import Id_op, Id_mat

m = 3
p = m

t = Chronology(0.01,dkObs=25,T=4**5,BurnIn=4)

m = 3
f = {
    'm'    : m,
    'model': step,
    'jacob': dfdx,
    'noise': 0
    }

mu0 = array([1.509, -1.531, 25.46])
X0 = GaussRV(C=2,mu=mu0)

h = {
    'm'    : p,
    'model': Id_op(),
    'jacob': Id_mat(m),
    'noise': GaussRV(C=2,m=p)
    }

other = {'name': os.path.relpath(__file__,'mods/')}

setup = OSSE(f,h,t,X0,**other)


####################
# Suggested tuning
####################
#config = Climatology()  # note no tuning required          # 8.5
#config = D3Var()        # tuning not stirctly required     # 1.26
#config = ExtKF(infl=90) # some inflation tuning needed     # 0.87
#config = EnKF('Sqrt',   N=3 ,  infl=1.30)                  # Very variable
#config = EnKF('Sqrt',   N=10,  infl=1.02,rot=True)         # 0.63 (sak: 0.65)
#config = EnKF('PertObs',N=500, infl=0.95,rot=False)        # 0.56
#config = EnKF_N(        N=10,            rot=True)         # 0.54
#config = iEnKF('Sqrt',  N=10,  infl=1.02,rot=True,iMax=10) # 0.31
#config = PartFilt(      N=100 ,reg=2.4,NER=0.3)            # 0.38
#config = PartFilt(      N=800 ,reg=0.9,NER=0.2)            # 0.28
#config = PartFilt(      N=4000,reg=0.7,NER=0.05)           # 0.27
#config = PFD(xN=1000,   N=30  ,reg=0.7,NER=0.2,Qs=2)       # 0.56

