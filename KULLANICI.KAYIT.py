import json
import os

class Users:  # kişiler sınıfı
    def __init__(self, username, password, email):
       self.username = username
       self.password =password
       self.email = email
       
class UserRepository:  # kişileri yöneten sınıf
    def __init__(self):
        self.users =[]
        self.isLoggedIn = False 
        self.currentUser = {}
    
    # kullanıcı bilgilerinin json  dosyaları içine aktar.
        self.loadUsers()
    
    def loadUsers(self):
        if os.path.exists('user.json'):
         with open ('users.json','r',encoding='utf-8')as file:
             users = json.load(file)
             for user in users:
              user = json.loads(user)
              newUser = user(username = user['username'],password = user['password'],email = user['email']) 
              self.users.append(newUser)
         print(self.users)
    
    def register(self, user: Users):  # kayıt oluşturma
        self.users.append(user)
        self.savetoFile()
        print('kullanıcı oluşturuldu.')

    def login(self,username, password):
        for user in self.users:
            if user.username == username and user.password == password:
                self.isLoggedIn = True
                self.currentUser = user
                print('login yapıldı.')
                break

    def logout(self):
        self.isLoggedIn = False
        self.currentUser = {}
        print('çıkış yapıldı.')

    def identity(self):
        if self.isLoggedIn:
         print(f'username: {self.currentUser.username}')
        else :
            print('giriş yapılmadı.')            
    
    def savetoFile(self):  # dosyaya kaydet
        list = []

        for user in self.users:
            list.append(json.dumps(user.__dict__))
        with open('users.json','w') as file:
            json.dump(list, file)

repository = UserRepository()

while True:
    print('menü'.center(50,'*'))
    secim = input('1- register\n2- login\n3- logout\n4- identity\n5- exit\nseçiminiz: ')  # identity= kimlik bilgileri
    if secim == '5':
        break
    else:
        if secim == '1': # register
            username = input('username: ')
            password = input('password: ')
            email = input('email: ')
            user = Users(username = username, password = password, email = email)
            repository.register(user)
        
        elif secim == '2':
            if repository.isLoggedIn:
                print('zaten login oldunuz')
            else:
                username = input('username: ')
                password = input('password: ')
                repository.login(username, password)
        
        elif secim == '3':
            repository.logout()
        
        elif secim == '4':
            repository.identity()
        
        else:
            print('yanlış seçim')


            