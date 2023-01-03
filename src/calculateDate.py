from datetime import datetime
from dateutil.relativedelta import relativedelta


def days_between_two_date(startDate, closeDate):
    startDate = datetime.strptime(str(startDate), "%Y%m%d")
    closeDate = datetime.strptime(str(closeDate), "%Y%m%d")
    daysBetweenDate = (closeDate - startDate).days

    return daysBetweenDate


def add_month_to_date(startDate, months):
    startDate = datetime.strptime(str(startDate), "%Y%m%d")
    closeDate = startDate + relativedelta(months=months, day=31)
    closeDate = closeDate.strftime("%Y%m%d")

    return closeDate


if __name__=="__main__":
    startDate = 20170228
    closeDate = 20221228
    months = 1

    print("----- Days between two dates -----")
    daysBetweenDate = days_between_two_date(startDate, closeDate)
    print(f'Days between two dates: {daysBetweenDate} days \n')

    print("----- Add month to date -----")
    closeDate2 = add_month_to_date(startDate, months)
    print(f'Close date: {closeDate2} \n')
