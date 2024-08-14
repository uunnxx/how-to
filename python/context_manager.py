# https://scribe.rip/@chuanwuliu/pythons-with-statement-737deed906f0


class DatabaseConnection():

    def __enter__(self):
        # make a database connection and return it
        # ...
        return self.dbconn

    def __exit__(self, exc_type, exc_val, exc_tb):
        # make sure the dbconnection gets closed
        self.dbconn.close()
        # ...


with DatabaseConnection() as mydbconn:
    # do stuff
    ...


# -----------------------------------------------------------------------------


fp = open(r"C:\Users\SharpEl\Desktop\myfile.txt")
try:
    for line in fp:
        print(line)
finally:
    fp.close()


with open(r"C:\Users\SharpEl\Desktop\myfile.txt") as fp:
    for line in fp:
        print(line)


# -----------------------------------------------------------------------------


 class Log:
    def __init__(self,filename):
        self.filename=filename
        self.fp=None
    def logging(self,text):
        self.fp.write(text+'\n')
    def __enter__(self):
        print("__enter__")
        self.fp=open(self.filename,"a+")
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("__exit__")
        self.fp.close()

with Log(r"C:\Users\SharpEl\Desktop\myfile.txt") as logfile:
    print("Main")
    logfile.logging("Test1")
    logfile.logging("Test2")


# -----------------------------------------------------------------------------


class ManagedFile:
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        self.file = open(self.name, 'w')
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()


with ManagedFile('hello.txt') as f:
    f.write('hello, world!')
    f.write('bye now')`enter code here`
