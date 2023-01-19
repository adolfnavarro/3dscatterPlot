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

# Eje x  Valores
xs=[i for i in range (1,21)]  #  20 temporadas. Cada una de 1 año [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]   Se ha usado una declaración por comprehnsion
listaEtiquetasTemporada =["02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21"]   # Etiquetas del eje x . Representa temporadas de futbol.  

# Eje  z  Valores
zsMadrid=[1,0,0,0,1,1,0,0,0,1,0,1,0,1,2,1,0,1,0,2]      # Titulos Madrid   copa rey + champions + liga      rango: 0 - 3
zsBarça=[0,0,1,2,0,0,2,1,2,0,1,0,3,2,1,2,1,0,1,0]       # Titulos Barça    copa rey + champions + liga      rango: 0 - 3

# Eje y Valores 
ysBarça=[10,40,42,-8,20,63,49,75,19,11,36,67,79,-2,94,98,8,125,-31,23]  # Gastos Barça         Balance de fichajes = Gastos en Entradas - Ingresos en Salidas    en Millones de euros
ysMadrid=[37,16,55,50,59,89,15,164,66,44,1,58,20,67,7,-65,51,225,-39,-44]  # Gastos Madrid     Balance de fichajes = Gastos en Entradas - Ingresos en Salidas     en Millones de euros




# Plot
fig, ax = plt.subplots(subplot_kw={"projection": "3d"},figsize=(10,7) )   

ax.scatter(xs, ysMadrid, zsMadrid, c="b", marker="o" ,s=300, alpha=.7,label="Madrid")  # Para definir los plots del Madrid    s Tamaño bola,  alpha= transparencia. 
ax.scatter(xs, ysBarça, zsBarça, c="r", marker="o", s=300, alpha=.7, label="Barça" )   # Para definir los plots del Barça 


# ax.set(xticklabels=[],       # Sugerido en el codigo base de matplotlitb. Se sustituye por las funciones set_xticks    
#        yticklabels=[],       # Razón Matplotlib doc official : This method should only be used after fixing the tick positions using Axes.set_xticks. Otherwise, the labels may end up in unexpected positions.
#        zticklabels=[])


# Hacer las divisiones de los ejes y la etiqueta por valor que mostraran. 
ax.set_xticks(xs,listaEtiquetasTemporada)
ax.set_yticks([-100,-75,-50,-25,0,25,50,75,100,125,150,175,200,225],[-100,-75,-50,-25,0,25,50,75,100,125,150,175,200,225])
ax.set_zticks([0,1,2,3],["0","1","2","3"])



# Titulos de los ejes
ax.set_xlabel ("Temporada")
ax.set_ylabel ("Gastos")
ax.set_zlabel ("Títulos")
 


ax.legend()  # Printar leyenda 
plt.suptitle("Balance de gastos en fichajes y num de titulos por temporada\n(champios league/Copa del rey/Liga)",size=10)  # Poner titulo general grafico

plt.show()