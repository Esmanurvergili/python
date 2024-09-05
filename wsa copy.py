import json
import os

class Users:  # Kişiler sınıfı
    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email

    def __repr__(self):
        return f"Username: {self.username}, Password: {self.password}, Email: {self.email}"
       
class UserRepository:  # Kişileri yöneten sınıf
    def __init__(self):
        self.users = []
        self.isLoggedIn = False 
        self.currentUser = {}
        self.loadUsers()
    
    def loadUsers(self):
        if os.path.exists('users.json'):
            with open('users.json', 'r', encoding='utf-8') as file:
                users = json.load(file)
                for user in users:
                    newUser = Users(username=user['username'], password=user['password'], email=user['email']) 
                    self.users.append(newUser)
            self.displayUsers()
    
    def register(self, user: Users):  # Kayıt oluşturma
        self.users.append(user)
        self.savetoFile()
        print('Kullanıcı oluşturuldu.')

    def login(self, username, password):
        for user in self.users:
            if user.username == username and user.password == password:
                self.isLoggedIn = True
                self.currentUser = user
                print('Login yapıldı.')
                break

    def logout(self):
        self.isLoggedIn = False
        self.currentUser = {}
        print('Çıkış yapıldı.')

    def identity(self):
        if self.isLoggedIn:
            print(f'Username: {self.currentUser.username}')
        else:
            print('Giriş yapılmadı.')            
    
    def savetoFile(self):  # Dosyaya kaydet
        list = [user.__dict__ for user in self.users]
        with open('users.json', 'w', encoding='utf-8') as file:
            json.dump(list, file, ensure_ascii=False, indent=4)
    
    def displayUsers(self):
        for user in self.users:
            print(user)

repository = UserRepository()

while True:
    print('Menü'.center(50, '*'))
    secim = input('1- Register\n2- Login\n3- Logout\n4- Identity\n5- Exit\nSeçiminiz: ')
    if secim == '5':
        break
    else:
        if secim == '1':  # Register
            username = input('Username: ')
            password = input('Password: ')
            email = input('Email: ')
            user = Users(username=username, password=password, email=email)
            repository.register(user)
        
        elif secim == '2':
            if repository.isLoggedIn:
                print('Zaten login oldunuz.')
            else:
                username = input('Username: ')
                password = input('Password: ')
                repository.login(username, password)
        
        elif secim == '3':
            repository.logout()
        
        elif secim == '4':
            repository.identity()
        
        else:
            print('Yanlış seçim.')
