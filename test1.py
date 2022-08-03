


def solution(text, num):
    if len(text) < num:
        return text
    else:
        new_text = text[:num]
        ls1 = text.split(' ')
        ls2 = new_text.split(' ')
        for sent1, sent2 in zip(ls1, ls2):
            if sent2 != sent1:
                ls2.remove(sent2)
                break
        output = ' '.join(ls2)
        print(output)

a = ['aabbb', 'ba', 'aaa', 'b', 'abba']
def solution2(S):
    if len(S) > 0:
        if 'ba' in S:
            return False
        else:
            for char in range(len(S)):
                if S[char] == 'a' or S[char] == 'b':
                    return True
print(solution2(a[0]))
print(solution2(a[1]))
print(solution2(a[2]))
print(solution2(a[3]))
print(solution2(a[4]))


def solution3(N=-5000):
    N = str(N)
    possibles = []
    fives = []
    for i in range(len(N)):
        if str(N)[i] == "5":
            fives.append(i)
    for k in fives:
        chars = list(N)
        chars[k] = ''
        possibles.append(int("".join(chars)))
    return max(possibles)

class Animal:
    animal1 = 'Goose'
    animal2 = 'Duck'
    animal3 = 'Dog'
    animal4 = 'Fish'

    def __init__(self, name):
        self.name = name

    def make_sound(self):
        if self.name == Animal.animal1 or self.name == Animal.animal2:
            return '~~ sound= GA GA ~~'
        elif self.name == Animal.animal3:
            return '~~ sound= HUF HUF ~~'
        else:
            print('This Animal Has not this methods')

    def walking(self):
        if self.name == Animal.animal1 or self.name == Animal.animal3:
            return ' ~~ WALKING ~~'
        else:
            print('This Animal Has not this methods')

    def swimming(self):
        if self.name == Animal.animal1 or self.name == Animal.animal2 or self.name == Animal.animal4:
            return '~~ SWIMMING ~~'
        else:
            print('This Animal Has not this methods')


goose = Animal('Goose')
duck = Animal('Duck')
dog = Animal('Dog')
fish = Animal('Fish')
