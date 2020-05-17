import time
from datetime import datetime

from application.db.people import *
from application.salary import *


if __name__ == '__main__':
    print(datetime.now())
    calculate_salary()

    time.sleep(1)

    print(datetime.now())
    get_employees()
