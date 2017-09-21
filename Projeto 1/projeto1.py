def deltat (popT,Tc,a):
	delta = a*(popT**2)*(1 - (Tc/popT))
	return delta

def deltaA (popA,Ac,k):
	delta = k*(popA**2)*(1 - (Ac/popA))
	return delta

def deltaV (popV,Vc,l):
	delta = l*(popV**2)*(1 - (Vc/popV))
	return delta

def Tf(popA,Ap,popT):
	tubarao_fome=popA/Ap-popT
	return tubarao_fome

def Af(popV,Vp,popA):
	arraia_fome=popV/Vp-popA
	return arraia_fome

def h(popT,Ax):
	predação_arraia=popT*Ax
	return predação_arraia

def i(popA,Vx):
	predação_vieira=popA*Vx
	return predação_vieira

tempo = []
popT = [1000]
popTc = 31914893
a = -0.0000000015

popA = [15000000]    #15000000
popAc = 1659574468
k = -0.0000000000000003
 
popV = [750000000000]
popVc = 1560000000000          #delta = l*(popV**2)*(1 - (Vc/popV))
l = -0.0000000000001

Ap=52#Predação de raias fome
Vp=940#Predação de vieiras fome
Ax=52#Predação arraias
Vx=940#Predação vieiras

for t in range(0,49):
	if popT[t]<=0:
		popT.append(0)
	elif popA[t]/popT[t]<52:
		popT.append(popT[t] + deltat(popT[t],popTc,a)+Tf(popA[t],Ap,popT[t]))
	else:
		popT.append(popT[t] + deltat(popT[t],popTc,a))
	if popA[t]<=0:
		popA.append(0)
	elif popV[t]/popA[t]<940:
		popA.append(popA[t] + deltaA(popA[t],popAc,k)-h(popT[t],Ap)+Af(popV[t],Vp,popA[t]))
	else:
		popA.append(popA[t] + deltaA(popA[t],popAc,k)-h(popT[t],Ap))
	if popV[t]<=0:
		popV.append(0)
	else:
		popV.append(popV[t] + deltaV(popV[t],popVc,l)-i(popA[t],Vp))
for t in range(50):   #3000000
	tempo.append(t)

import matplotlib.pyplot as plt
plt.plot(tempo,popT)
plt.ylabel('Tubarão')
plt.xlabel('Tempo')
plt.show()

import matplotlib.pyplot as plt
plt.plot(tempo,popA)
plt.ylabel('Arraia')
plt.xlabel('Tempo')
plt.show()

import matplotlib.pyplot as plt
plt.plot(tempo,popV)
plt.ylabel('Vieira')
plt.xlabel('Tempo')
plt.show()