# Tech_Assessment_Ease_Solutions
Challenge solutions to python developer tech assessment.
Este codigo, recorre una matriz de nxn, y buca el camino mas largo y con mayor altura, suponiendo que la matriz es el mapa de una montaña. Para correrlo hace un Clone del repositorio, y en la carpeta resultante, se abre una consola y se corre el archivo main.py (Por defecto tiene un map de 1000x100)
```
python3 main.py
```
![resultado](https://user-images.githubusercontent.com/88687007/145681746-3452c299-dd74-43f3-a192-1f6f6d08d044.png)

Si se desea evaluar una matriz diferente, permite meter la ruta como un parametro de entrada
```
python3 main.py skirsesort.kitzbuehel/4x4.txt 
```
![resultado1](https://user-images.githubusercontent.com/88687007/145681896-451480af-30ac-41d7-9131-a3b320729479.png)

El algoritmo retorna como resultado:

- La cantidad de pasos mas larga contada
- La diferencia de altura mas alta
- El vectoc con las posiciones por las que baja
