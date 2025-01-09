import sqlite3

# Izveido savienojumu ar SQLite datubāzi (tiks izveidota, ja tā neeksistē)
conn = sqlite3.connect('trenazieru_zale.db')
cursor = conn.cursor()

"""
cursor.execute('''
CREATE TABLE IF NOT EXISTS Sportisti (
    id_sportista INTEGER PRIMARY KEY AUTOINCREMENT,
    vards TEXT NOT NULL,
    uzvards TEXT NOT NULL,
    dzimšanas_gads INTEGER NOT NULL,
    talrunis TEXT,
    pilsēta TEXT
)
''')

# Tabula "Treneri"
cursor.execute('''
CREATE TABLE IF NOT EXISTS Treneri (
    id_trenera INTEGER PRIMARY KEY AUTOINCREMENT,
    vards TEXT NOT NULL,
    uzvards TEXT NOT NULL,
    izglītība TEXT,
    kvalifikācija TEXT
)
''')

# Tabula "Apmeklējumi"
cursor.execute('''
CREATE TABLE IF NOT EXISTS Apmekleejumi (
    id_apmekleejuma INTEGER PRIMARY KEY AUTOINCREMENT,
    id_sportista INTEGER,
    id_trenera INTEGER,
    datums TEXT NOT NULL,
    nodarbiibas_saakums TEXT,
    nodarbiibas_beigas TEXT,
    laiks INTEGER,
    FOREIGN KEY (id_sportista) REFERENCES Sportisti(id_sportista),
    FOREIGN KEY (id_trenera) REFERENCES Treneri(id_trenera)
)
''')

cursor.execute("INSERT INTO Sportisti (vards, uzvards, dzimšanas_gads, talrunis, pilsēta) VALUES (?, ?, ?, ?, ?)", 
               ("Jānis", "Bērziņš", 1990, "29123456", "Rīga"))
cursor.execute("INSERT INTO Sportisti (vards, uzvards, dzimšanas_gads, talrunis, pilsēta) VALUES (?, ?, ?, ?, ?)", 
               ("Pēteris", "Kalniņš", 1985, "29234567", "Jelgava"))

cursor.execute("INSERT INTO Treneri (vards, uzvards, izglītība, kvalifikācija) VALUES (?, ?, ?, ?)", 
               ("Aivars", "Lapiņš", "Augstākā", "Sporta skolotājs"))
cursor.execute("INSERT INTO Treneri (vards, uzvards, izglītība, kvalifikācija) VALUES (?, ?, ?, ?)", 
               ("Ilze", "Jākobsone", "Augstākā", "Fizioterapeits"))

cursor.execute("INSERT INTO Apmekleejumi (id_sportista, id_trenera, datums, nodarbiibas_saakums, nodarbiibas_beigas, laiks) VALUES (?, ?, ?, ?, ?, ?)", 
               (1, 1, "2025-01-03", "08:00", "09:00", 60))
cursor.execute("INSERT INTO Apmekleejumi (id_sportista, id_trenera, datums, nodarbiibas_saakums, nodarbiibas_beigas, laiks) VALUES (?, ?, ?, ?, ?, ?)", 
               (2, 2, "2025-01-03", "09:30", "10:30", 60))
"""

cursor.execute("SELECT * FROM Sportisti")
sportisti = cursor.fetchall()
print("Sportisti:")
for sportists in sportisti:
    print(sportists)

cursor.execute("SELECT * FROM Treneri")
treneri = cursor.fetchall()
print("\nTreneri:")
for treneris in treneri:
    print(treneris)

cursor.execute("SELECT * FROM Apmekleejumi")
apmeklejumi = cursor.fetchall()
print("\nApmeklējumi:")
for apmeklejumus in apmeklejumi:
    print(apmeklejumus)
        
conn.commit()
conn.close()