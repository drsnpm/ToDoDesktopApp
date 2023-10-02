import sqlite3


class DBHandler:
    def __init__(self):
        self.con = sqlite3.connect("taskdb.db")
        try:
            self.con.execute("CREATE TABLE IF NOT EXISTS tasks(id INTEGER PRIMARY KEY AUTOINCREMENT,tasktitle TEXT, "
                         "taskdesc TEXT,taskdate TEXT,tasktime TEXT)")
            self.con.commit()
        except Exception as e:
            print(e)

    def insertTask(self, t1):
        taskTouple = [t1.title,t1.desc,t1.date,t1.time]
        try:
            self.con.execute("INSERT INTO tasks(tasktitle, taskdesc, taskdate, tasktime) values(?, ?, ?, ?)", taskTouple)
            self.con.commit()
        except Exception as e:
            print(e)

    def getTasks(self,date):
        cursor = self.con.cursor()
        rows = cursor.execute("SELECT * FROM tasks")
        return rows