users = {}
def create_user(username,age):
    if username in users:   
        print(f"Hata: {username} zaten var.")
    users[username] = {"username": username, "age": age}
    

def get_user(username):
    if username not in users:  
        print(f"Hata: {username} bulunamadı.")
    else:
     return users[username] 


def update_user(username, age):
    users[username] = {"username": username, "age": age}


def delete_user(username):
    users.pop(username)

create_user("ece", 30)
create_user("ceren", 20)
create_user("emre", 70)
create_user("bonua", 33)
update_user("ceren",23)
delete_user("emre")
get_user("aysel")
create_user("ece",22)
print(users)