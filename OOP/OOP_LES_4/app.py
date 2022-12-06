from empl_exceptions import EmailAlreadyExistsException
from employee import Employee

from datetime import datetime
import logging


def main():
    emp1 = Employee('Vlad', 25, 'vlmed@gmail.com')

if __name__ == '__main__':
    try:
        main()
    except EmailAlreadyExistsException:
        print('This email is already exist!')
        
        Log_Format = " %(asctime)s - %(message)s"
        logging.basicConfig(filename = "/home/vladyslav/Documents/git/ALEVEL_OOP_3/employees/logs",
                filemode = "a",
                format = Log_Format, 
                level = logging.ERROR)
        logger = logging.getLogger()
        logger.error(EmailAlreadyExistsException)
        
        # write traceback to the logs txt
        # 1. with open...
        # 2. message = f"{datetime.date.today()}
        # {datetime.datetime.now().hour}:
        # {datetime.datetime.now().minute} {traceback.format_exc}"
        # 3. log a message in the file
        # 3*. implement with logging https://docs.python.org/3/library/logging.html
