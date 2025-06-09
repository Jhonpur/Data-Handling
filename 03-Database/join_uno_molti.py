'''Esercizio #8: Eseguire una join uno-a-molti
Modificate il codice mostrato nella sezione precedente in modo che la query sia una join
della tabella emps con la tabella orders. È possibile mantenere la condizione che empno sia
maggiore di 9001. Adattate la chiamata print() per produrre le righe della join modificata.'''
import mysql.connector

try:
    cnx = mysql.connector.connect(user = 'root', password = '''ciaone''',
                                  host='127.0.0.1',
                                  database = 'sampledb')
    cursor = cnx.cursor()
    query = ("""SELECT e.empno, e.empname, e.job, o.pono 
                FROM emps e JOIN orders o ON e.empno = o.empno
                WHERE e.empno > %s""")
    empno = 9001
    cursor.execute(query, (empno,))
    for (empno, empname, job, orders) in cursor:
        print("{}, {}, {}, {}".format(empno, empname, job, orders))
except mysql.connector.Error as err:
    print("Error-Code:", err.errno)
    print("Error-Message: {}".format(err.msg))
#La clausola finally viene eseguita in ogni caso . In questa clausola, si chiude esplicitamente il cursore e quindi la connessione
finally:
    cursor.close()
    cnx.close()