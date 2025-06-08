class GradeTooHighException(Exception):
    pass

class GradeTooLowException(Exception):
    pass

class FormGradeTooLowException(Exception):
    pass


class Bureaucrat:
    def __init__(self, name, grade):
        if grade < 1:
            raise GradeTooHighException("You're too powerful!")
        if grade > 150:
            raise GradeTooLowException("You're not even qualified to lick envelopes!")
        self.name = name
        self.grade = grade

    def promote(self):
        if self.grade < 2:
            raise GradeTooHighException("You're too powerful!")
        self.grade = self.grade -1

    def demote(self):
        if self.grade < 150:
            raise GradeTooLowException("You're not even qualified to lick envelopes!")
        self.grade = self.grade +1

class Form:
    def __init__(self, name, sign_grade, exec_grade):
        self.name = name
        self.sign_grade = sign_grade
        self.exec_grade = exec_grade
        self.is_signed = False

    def be_signed(self, bureaucrat):
        if bureaucrat.grade > self.sign_grade:
            raise FormGradeTooLowException("Your pen sucks u broke ass")
        is_signed = True
        
class AForm:
    def __init__(self):
        

amy = Bureaucrat("Amy", 4)
tom = Bureaucrat("Tom", 8)

try:
    grade = int(input("Enter your bureaucrat grade (1-150): "))
    if grade < 1:
        raise GradeTooHighException("")
    if grade > 150:
        raise GradeTooLowException("Grade too low!")
    print("✅ Grade accepted:", grade)
except Exception as e:
    print("💥 Error:", e)

try:
    bob = Bureaucrat("Bob", 99)
    passport_form = Form("PassportApplication", 30, 25)
    passport_form.be_signed(bob)
except Exception as e:
    print("💥", e)