from empl_exceptions import EmailAlreadyExistsException
class Employee:
    def __init__(self, name, salary, email):
        self.name = name
        self.salary = salary
        self.email = email
        self.validate()
        self.save_email()  # -> write email to file

    def save_email(self):
        with open('/home/vladyslav/Documents/git/ALEVEL_OOP_3/employees/emails', 'a') as f:
            f.write(self.email + '\n')

    def validate(self):
        with open('/home/vladyslav/Documents/git/ALEVEL_OOP_3/employees/emails') as f:
             for line in f:
                if self.email in line:
                    raise EmailAlreadyExistsException
                else:
                    pass
                    
                    
        """
        1. Read the file with emails.
        2. Check that self.email in file.
        3. If not: do nothing
        4. Else: raise EmailAlreadyExistsException
        :return:
        """

