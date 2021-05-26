a = ['a','hello',173,2222,'mike']
b = ('a','b','c',5,9)
print(len(a))
try:
    print(b.insert(2,"hello"))
except:
    print("Cannot edit a tuple")
dict ={
    "brand":"nissan",
    "model":"sentra",
    "year":"2017"
}
print(dict["brand"])
set = {"hi","hello","greetings"}
print(type(set))
c = ['c','c','c','d''e']
for x in c:
    if (x == "d"):
        break;

