import mysql.connector
import matplotlib.pyplot as plt
import numpy as np

db = mysql.connector.connect(
    host="localhost",
    user="django",
    password="pypy",
    database="database"
)

conn = db.cursor()
conn.execute(
    "select nome,sum(total) total from tabela where group by nome limit 0,10")
result = conn.fetchall()

dadosx = []
dadosy = []
i = 0

for x in result:
    i += 1
    dadosx.insert(i, list(x)[0])
    dadosy.insert(i, list(x)[3])

x = np.array(dadosx)
y = np.array(dadosy)

plt.xlabel("Clientes")
plt.ylabel("Valores")
plt.title('Rank 10 Clientes')
plt.grid(True)

plt.plot(x, y)
plt.show()
