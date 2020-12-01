import math

print("===================================================================")
print("Nama : Mohamad Farizal Arifin")
print("NIM : 312010231")
print("Kelas : TI.20.B1")
print("Mata Kuliah : Bahasa Pemrograman")
print("===================================================================")

def a(x):
    return x ** 2

#Lambda
def a2(x): x ** 2

print("Ubahlah kode dibawah ini menjadi fungsi menggunakan lambda \n   def a(x): \n \t   return x ** 2")
print("Lambda : def a2(x): x ** 2")


def b(x, y):
    return math.sqrt(x ** 2 + y ** 2)

#Lambda
def b2(x, y): math.sqrt(x ** 2 + y ** 2)

print("Ubahlah kode dibawah ini menjadi fungsi menggunakan lambda \n   def b(x, y): \n \t   return math.sqrt(x ** 2 + y ** 2)")
print("Lambda : def b2(x, y): math.sqrt(x ** 2 + y ** 2)")


def c(*args):
    return sum(args) / len(args)

#Lambda
def c2(*args): sum(args) / len(args)

print("Ubahlah kode dibawah ini menjadi fungsi menggunakan lambda \n   def c(*args): \n \t   return sum(args) / len(args)")
print("Lambda : def c2(*args): sum(args) / len(args)")


def d(s):
    return "".join(set(s))

#Lambda
def d2(s): "".join(set(s))

print("Ubahlah kode dibawah ini menjadi fungsi menggunakan lambda \n   def d(s): \n \t   return "".join(set(s))")
print("Lambda : def d2(s): "".join(set(s))")