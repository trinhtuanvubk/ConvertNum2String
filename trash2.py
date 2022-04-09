import re 
import datetime 
from datetime import date, datetime
from dateutil import parser
# datestring = 'hôm nay thật đẹp là ngày 12/98 và ngày 10/88'
# import dateutil.parser

# new_string = re.search(r"[0-9]{1,4}[\_|\-|\/|\|][0-9]{1,2}[\_|\-|\/|\|][0-9]{1,4}", datestring)
# new_string = re.findall(r"[0-9]{1,2}[\_|\-|\/|\|][0-9]{1,4}", datestring)
# # date = new_string.group(0)
# # print(new_string.group(0))
# print(new_string)
# # yourdate = dateutil.parser.parse(datestring)
# my_date = datetime.strptime(date, "%m/%y")
# print(my_date.year)
# print(my_date.month)


def replace_(datetime:str):
    datetime_object = parser.parse(datetime,dayfirst=True)
    print(datetime_object)
    year = datetime_object.year
    month = datetime_object.month
    day = datetime_object.day
    print(len(datetime.split("/")))
    if len(datetime.split("/")) > 2 : 
        return "ngày {} tháng {} năm {}".format(day,month,year)
    else : 
        return "tháng {} năm {}".format(month,year)

def date_to_string(paragraph:str): 
    # text = paragraph
    paragraph = paragraph.lower()
    d_m_y_re = r"[0-9]{1,4}[\_|\-|\/|\||\.][0-9]{1,2}[\_|\-|\/|\||\.][0-9]{1,4}"
    d_m_y_all = re.findall(d_m_y_re,paragraph)
    for date in  d_m_y_all :
        print(date)
        try:
            new_date = replace_(date)
            paragraph = paragraph.replace(date,new_date)
        except:
            pass
    # return paragraph
    m_y_re = r"[0-9]{1,2}[\_|\-|\/|\|][0-9]{1,4}"
    m_y_all = re.findall(m_y_re,paragraph)
    for date in m_y_all :
        print(date)
        try:
            new_date = replace_(date)
            paragraph = paragraph.replace(date,new_date)
        except:
            pass
    d_m_re =  r"[0-9]{1,4}[\_|\-|\/|\|][0-9]{1,2}"
    d_m_all = re.findall(d_m_re,paragraph)
    for date in d_m_all :
        print(date)
        try:
            new_date = replace_(date)
            paragraph = paragraph.replace(date,new_date)
        except:
            pass
    return paragraph

if __name__ == "__main__": 
    datestring = 'ngày hôm nay là 8/12/98 và 2021, chúng tôi sẽ đến vào 8-10'
    paragraph = date_to_string(datestring) 
    print(paragraph)
    
