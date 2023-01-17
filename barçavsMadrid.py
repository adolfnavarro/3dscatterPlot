import matplotlib.pyplot as plt
# import numpy as np

plt.style.use('_mpl-gallery')

# Make data with numpy 
# np.random.seed(19680801)
# n = 100
# rng = np.random.default_rng()
# xs = rng.uniform(23, 32, n)
# ys = rng.uniform(0, 100, n)
# zs = rng.uniform(-50, -25, n)

# Make data

xs =[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

zsMadrid=[1,0,0,0,1,1,0,0,0,1,0,1,0,1,2,1,0,1,0,2]      # Titulos Madrid   copa rey + champions + liga
zsBarça=[0,0,1,2,0,0,2,1,2,0,1,0,3,2,1,2,1,0,1,0]       # Titulos Barça    copa rey + champions + liga

ysBarça=[10,40,42,-8,20,63,49,75,19,11,36,67,79,-2,94,98,8,125,-31,23]  # Barça         Balance de fichajes = Gastos en Entradas - Ingresos en Salidas 
ysMadrid=[37,16,55,50,59,89,15,164,66,44,1,58,20,67,7,-65,51,225,-39,-44]  # Madrid     Balance de fichajes = Gastos en Entradas - Ingresos en Salidas 

listaEtiquetasTemporada =["02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21"]

# Plot
fig, ax = plt.subplots(subplot_kw={"projection": "3d"},figsize=(10,7) )


ax.scatter(xs, ysMadrid, zsMadrid, c="b", marker="o" ,s=300, alpha=.7,label="Madrid")  # s Tamaño bola,  alpha= transparencia. 
ax.scatter(xs, ysBarça, zsBarça, c="r", marker="o", s=300, alpha=.7, label="Barça" )


# ax.set(xticklabels=[],
#        yticklabels=[],
#        zticklabels=[])


# Rango datos en los ejes y dato visualizado
ax.set_xticks(xs,listaEtiquetasTemporada)                                                                                   # Temporada
ax.set_yticks([-100,-75,-50,-25,0,25,50,75,100,125,150,175,200,225],[-100,-75,-50,-25,0,25,50,75,100,125,150,175,200,225])  # Balance
ax.set_zticks([0,1,2,3],["0","1","2","3"])                                                                                  # Titulos 

# Etiquetas de los ejes
ax.set_xlabel ("temporada")
ax.set_ylabel ("gastos")
ax.set_zlabel ("titulos")
 


ax.legend()  # Printar leyenda 
plt.suptitle("Balance de gastos en fichajes y num de titulos por temporada\n(champios league/Copa del rey/Liga)",size=10)  # Poner titulo

plt.show()