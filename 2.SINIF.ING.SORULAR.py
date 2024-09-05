import random

class Question:
    def __init__(self, text, choices, answer):
        self.text = text  
        self.choices = choices  # seçenekler listesi
        self.answer = answer

    def checkAnswer(self, answer):
        return self.answer == answer  # kullanıcının cevabını doğru cevapla karşılaştır

class Quiz:
    def __init__(self, questions):
        self.questions = questions   # sorular listesi
        random.shuffle(self.questions)  # Soruları rastgele karıştır
        self.score = 0
        self.questionindex = 0

    def getQuestion(self):
        return self.questions[self.questionindex] 

    def displayQuestion(self):  # mevcut soruyu ve seçenekleri ekrana yazdır
        question = self.getQuestion()
        print(f'Soru {self.questionindex + 1}: {question.text}')

        for choice in question.choices:
            print('- ' + choice)

        answer = input('Cevap: ')
        self.guess(answer)  # cevabı işle
        self.loadQuestion() # sonraki soruya geç

    def guess(self, answer):  # kullanıcının cevabını kontrol et ve skoru güncelle
        question = self.getQuestion()
        if question.checkAnswer(answer):
            self.score += 1   # doğruysa skoru bir arttır
        self.questionindex += 1   # sonraki soruya geç

    def loadQuestion(self):   # sorular bitti mi kontrol et sonucu göster
        if self.questionindex >= len(self.questions):
            self.showScore()
        else:
            self.displayProgress()
            self.displayQuestion()

    def showScore(self):  # sonuçları ekrana yazdır
        print('Skor: ', self.score)

    def displayProgress(self):  # kullanıcının ilerlemesini göster
        totalQuestions = len(self.questions)
        questionNumber = self.questionindex + 1
        if questionNumber > totalQuestions:
            print('Quiz bitti.')
        else:
            print(f'Soru {questionNumber} / {totalQuestions}'.center(100, '*'))

# Soruları oluştur
s1 = Question('jacket ne demek?', ['ceket', 'etek', 'bluz', 'hırka'], 'ceket')
s2 = Question('stop ne demek?', ['devam et', 'dur', 'sola dön', 'sağa dön'], 'dur')
s3 = Question('cold ne demek?', ['sıcak', 'yağmur', 'buz gibi', 'soğuk'], 'soğuk')
s4 = Question('good afternoon ne demek?', ['günaydın', 'iyi akşamlar', 'tünaydın', 'iyi geceler'], 'tünaydın')
s5 = Question('good evening ne demek?', ['günaydın', 'iyi akşamlar', 'tünaydın', 'iyi geceler'], 'iyi akşamlar')
s6 = Question('nasılsın ne demek?', ['I am fine', 'how are you', 'nice to meet you', 'see you later'], 'how are you')
s7 = Question('nice to meet you ne demek?', ['iyiyim', 'sizinle tanıştığıma memnun oldum', 'nasılsın', 'daha sonra görüşürüz'], 'sizinle tanıştığıma memnun oldum')
s8 = Question('daha sonra görüşürüz ingilizcede ne demek?', ['see you later', 'nice to meet you', 'how are you', 'I am fine'], 'see you later')
s9 = Question('stand ...! kalkınız demek için boşluğa ne gelmeli?', ['close', 'up', 'open', 'down'], 'up')
s10 = Question('... the door! kapıyı açınız demek için boşluğa ne gelmeli?', ['down', 'up', 'open', 'close'], 'close')
s11 = Question('sola dönünüz ne demek?', ['stop', 'turn right', 'turn left'], 'turn left')
s12 = Question('kol ne demek?', ['arm', 'ear', 'eye', 'hand'], 'arm')
s13 = Question('kesmek ne demek?', ['read', 'write', 'stick', 'cut'], 'cut')
s14 = Question('read ne demek?', ['oku', 'yaz', 'yapıştır', 'kes'], 'oku')
s15 = Question('yapıştırmak ne demek?', ['write', 'stick', 'read', 'cut'], 'stick')
s16 = Question('match ne demek?', ['eşleştir', 'write', 'altını çiz', 'yaz'], 'eşleştir')
s17 = Question('sıra ne demek?', ['ruler', 'desk', 'chair', 'table'], 'desk')
s18 = Question('hangisi okul eşyası değildir?', ['chair', 'eraser', 'draw', 'sharpener'], 'draw')
s19 = Question('chair ne demek?', ['sandalye', 'cetvel', 'silgi', 'tahta'], 'sandalye')
s20 = Question('umbrella ne demek?', ['şemsiye', 'masa', 'yağmur', 'kulaklık'], 'şemsiye')
s21 = Question('muz ne demek?', ['orange', 'stawberry', 'cherry', 'banana'], 'banana')
s22 = Question('desk ne anlama gelir?', ['masa', 'sıra', 'sandalye', 'tahta'], 'sıra')
s23 = Question('senin telefon numaran ne? inglizcede ne demek?', ['how are you', 'how old are you', 'what is your telephone number', 'what is your name'], 'what is your telephone number')
s24 = Question('yeşil ne demek?', ['yellow', 'green', 'purple', 'grey'], 'green')
s25 = Question('black ne demek?', ['sarı', 'kahverengi', 'siyah', 'pembe'], 'siyah')
s26 = Question('dislike ne demek?', ['beğenmek', 'sevmek', 'sevmemek', 'hoşuna gitmek'], 'sevmemek')
s27 = Question('head ne demek?', ['göz', 'baş', 'el', 'ayak'], 'baş')
s28 = Question('kulak ne demek?', ['ear', 'nose', 'eye', 'finger'], 'ear')
s29 = Question('point to my ...! ağzımı göster demek için boşluğa ne gelmeli?', ['mouth', 'knee', 'toe', 'feet'], 'mouth')
s30 = Question('ayak ne demek?', ['feet', 'toe', 'knee', 'teet'], 'feet')
s31 = Question('look at my...! gözlerime bak demek için boşluğa ne gelmeli?', ['nose', 'eyes', 'teeth', 'toes'], 'eyes')
s32 = Question('toes ne demek?', ['ayak', 'diz', 'ayak parmağı', 'diş'], 'ayak parmağı')
s33 = Question('teeth ne demek?', ['el', 'diş', 'ağız', 'kol'], 'diş')
s34 = Question('count your...! parmaklarını say demek için boşluğa ne gelmeli?', ['ears', 'teeth', 'fingers', 'toes'], 'fingers')
s35 = Question('cherry ne demek?', ['çilek', 'elma', 'kiraz', 'şeftali'], 'kiraz')
s36 = Question('kayısı ne demek?', ['orange', 'plum', 'melon', 'apricot'], 'apricot')
s37 = Question('pineapple ne demek?', ['çilek', 'ananas', 'karpuz', 'üzüm'], 'ananas')
s38 = Question('watermelon ne demek?', ['karpuz', 'kavun', 'greyfurt', 'erik'], 'karpuz')
s39 = Question('kavun ne demek?', ['plum', 'grapes', 'peach', 'melon'], 'melon')
s40 = Question('duck ne demek?', ['kanguru', 'aslan', 'civciv', 'ördek'], 'ördek')
s41 = Question('zürafa ne demek?', ['sheep', 'chicken', 'snake', 'giraffe'], 'giraffe')
s42 = Question('cow ne demek?', ['keçi', 'koyun', 'inek', 'maymun'], 'inek')
s43 = Question('timsah ne demek?', ['horse', 'crocodile', 'tiger', 'rabbit'], 'crocodile')
s44 = Question('snake ne demek?', ['yılan', 'maymun', 'zebra', 'at'], 'yılan')
s45 = Question('that is an ... o bir fil demek için boşluğa ne gelmeli?', ['monkey', 'rabbit', 'elephant', 'donkey'], 'elephant')
s46 = Question('walk ne demek?', ['koşmak', 'yürümek', 'atlamak', 'yüzmek'], 'yürümek')
s47 = Question('sing ne demek?', ['şarkı söylemek', 'oynamak', 'koşmak', 'yüzmek'], 'şarkı söylemek')

questions = [s1, s2, s3, s4, s5, s6, s7, s8, s9, s10, s11, s12, s13, s14, s15, s16, s17, s18, s19, s20, s21, s22, s23, s24, s25, s26, s27, s28, s29, s30, s31, s32, s33, s34, s35, s36, s37, s38, s39, s40, s41, s42, s43, s44, s45, s46, s47]

# Quiz'i başlat
quiz = Quiz(questions)
quiz.loadQuestion()
