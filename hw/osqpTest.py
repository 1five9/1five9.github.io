import numpy as np
from osqp import OSQP
from scipy import sparse
from scipy.sparse import vstack
from numpy import hstack, inf, ones
import pdb

def osqp_solve_qp(P, q, G= None, h=None, A=None, b=None, initvals=None):
	""" 
	Solve a Quadratic Program defined as:
	minimize
		(1/2) * x.T * P * x + q.T * x
	subject to
		G * x <= h
		A * x == b
	using OSQP <https://github.com/oxfordcontrol/osqp>.
	"""  
	qp_A = vstack([G, A]).tocsc()
	l = -inf * ones(len(h))
	qp_l = hstack([l, b])
	qp_u = hstack([h, b])

	osqp = OSQP()
	osqp.setup(P=P, q=q, A=qp_A, l=qp_l, u=qp_u, verbose=False, polish=True)

	if initvals is not None:
		osqp.warm_start(x=initvals)

	res = osqp.solve()
	if res.info.status_val == 1:
		feasible = 1
	else:
		feasible = 0
		print("The FTOCP is not feasible at time t = ", self.time)

	Solution = res.x

	print("Solution: ", res.x)
	print("OSQP is working correctly!")


Nv = 10 # number of variables
H = sparse.csc_matrix(np.eye(Nv))
q = np.ones(Nv)

Ni = 5 # number of inequalities
G_in = sparse.csc_matrix(np.eye(Ni,Nv))
g_in = np.ones(Ni)

Ne = 2 # number of inequalities
G_eq = sparse.csc_matrix(np.ones((Ne,Nv)))
g_eq = np.ones(Ne)

osqp_solve_qp(H, q, G_in, g_in, G_eq, g_eq )

