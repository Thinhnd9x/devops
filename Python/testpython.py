""" a="Thinh la 1 sieu cap pro"
print(a[-3:])
b=("Linux", "Devops", "Aws", "Python")
print(b[1:4][0][3:6]) """

""" firt_tuple=("Linix", "Devops", 1999, 2001)
ans=2005 not in firt_tuple
print(ans) """

""" x=99
if x < 80:
    print("X less than 100")
else:
    print("X great than 100") """

""" a=("devops", "English", "aws", "Linux")
for i in a:
    print(f"{i} is the skill need to know") """

""" x = 0
while x <= 10:
    print("the value of x is:", x)
    x += 1
    if x == 5:
        print(f"Found my data")
        continue
    print(f"Found the Value is {x}") """

""" for i in "DevOps":
    if i == "O":
        print("Found my data")
        continue
    print(f"Value of is {i}") """

""" import random
thinh = ["dep trai", "giau co", "dieu nghe", "gioi dang", "ngau"]
random.shuffle(thinh)
print(thinh)
choice = random.choice(thinh)
for i in thinh:
    print(f"Testing {i}")
    if i == choice:
        print(f"{choice} test success")
        continue
    print("test fail") """

""" def tinhtong(s1 , s2):
    tong = s1 + s2
    return tong
print(tinhtong(40,60)) """

""" def sum(number):
    x = 0 
    for i in number:
        x += i
    return x
print(sum([2,3,5,6,8]))
 """

""" def get(msg="moning"):
    print(f"Good {msg}")

get()
get("evening") """

""" import random
def time_act(*time, **act):
    min = sum(time) + random.randint(0, 50)
    Choice = random.choice(list(act.keys()))
    print(f"You have spent {min} minus for {act[Choice]}")
time_act(10, 20 ,10, Learn="Devops", sport="Football", fun="Nimo")
 """
""" import os
path = '/home/test.py'
if os.path. isfile(path):
    print("This is a file")
elif os.path. isdir(path):
    print("This is a direction")
else:
    print("File or dir is not exists") """

""" import os
userlist=["alpha", "beta", "gamma"]
for user in userlist:
    os.system(f"useradd {user}") """

""" from fabric.api import *
def gretting(msg):
    print(f"Good {msg}")

def system_info():
    print("disk space")
    local("df -h")

    print("Memory info")
    local("free -m")

    print("Up time")
    local("uptime")

def web_setup(weburl, dir):
    sudo("yum install httpd wget unzip -y")
    sudo("systemctl start httpd")
    sudo("systemctl enable httpd")
    local("apt install zip unzip -y")
    local(f"wget -O web.zip {weburl}")
    local(f"unzip -o web.zip")

    with lcd(dir):
        local("zip -r web.zip *")
        put("web.zip", "/var/www/html", use sudo=True)
    with cd("/var/www/html"):
        sudo("unzip -o web.zip")
        sudo("systemctl restart httpd") """
try:
    number = int(input("Nhap so:"))
    kq = 10 / number
except ValueError:
    print("This is not a number")
except ZeroDivisionError:
    print("This is Zero")
else:
    print(f"The result is {kq}")
