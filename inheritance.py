class Person:
    def __init__(self, firstName, lastName, idNumber):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber

    def printPerson(self):
        print("Name:", self.lastName + ",", self.firstName)
        print("ID:", self.idNumber)


class Student(Person):
    def __init__(self, firstName, lastName, idNumber, score):
        super().__init__(firstName, lastName, idNumber)
        self.score = score

    def calculate(self):
        wyniki = 0

        for score in self.score:
            wyniki += score
        srednia = wyniki/len(self.score)

        if srednia < 40:
            return 'T'
        elif srednia < 55:
            return 'D'
        elif srednia < 70:
            return 'P'
        elif srednia < 80:
            return 'A'
        elif srednia < 90:
            return 'E'
        else:
            return 'O'


line = input().split()
firstName = line[0]
lastName = line[1]
idNumber = line[2]
scores1 = int(input())
scores = list(map(int, input().split()))
s = Student(firstName, lastName, idNumber, scores)
s.printPerson()
print("Grade", s.calculate())
