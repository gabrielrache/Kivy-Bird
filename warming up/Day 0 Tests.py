import sqlite3 as sl


con = sl.connect('BodyEvo.db')



sql = 'INSERT INTO pessoa (cd_pessoa, nm_pessoa, dt_nascimento, id_sexo) values(?, ?, ?, ?)'
data = [
    (1, 'Gabriel Carmona', '1994-01-13', 'M')
]


with con:
    con.executemany(sql, data)

with con:
    data = con.execute("SELECT * FROM pessoa")
    for row in data:
        print(row)
