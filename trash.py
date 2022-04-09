# import tensorflow as tf
# import os 
# from argparse import Namespace


# with tf.compat.v1.gfile.Open(os.path.join("/home/trinhtuanvu/kws/model_train/ds_tc_resnet/", 'flags.txt'), 'r') as fd:
#             flags_txt = fd.read()

# flags = eval(flags_txt)
# # print(type(flags))
# # print(flags.model_name)

# from tensorflow import keras 
# base_model = keras.applications.Xception(
#     weights='imagenet',  
#     input_shape=(150, 150, 3),
#     include_top=False)  


# base_model.trainable = False


import re 
date = "hôm nay là 6/15/2017 nhé"

# print(re.search(r"^([1-9]|0[1-9]|1[0-9]|2[0-9]|3[0-1])(\.|-|/)([1-9]|0[1-9]|1[0-2])(\.|-|/)([0-9][0-9]|19[0-9][0-9]|20[0-9][0-9])$|^([0-9][0-9]|19[0-9][0-9]|20[0-9][0-9])(\.|-|/)([1-9]|0[1-9]|1[0-2])(\.|-|/)([1-9]|0[1-9]|1[0-9]|2[0-9]|3[0-1])$",date))
# print(re.search(r"^(?:(?:31(\/|-|\.)(?:0?[13578]|1[02]))\1|(?:(?:29|30)(\/|-|\.)(?:0?[13-9]|1[0-2])\2))(?:(?:1[6-9]|[2-9]\d)?\d{2})$|^(?:29(\/|-|\.)0?2\3(?:(?:(?:1[6-9]|[2-9]\d)?(?:0[48]|[2468][048]|[13579][26])|(?:(?:16|[2468][048]|[3579][26])00))))$|^(?:0?[1-9]|1\d|2[0-8])(\/|-|\.)(?:(?:0?[1-9])|(?:1[0-2]))\4(?:(?:1[6-9]|[2-9]\d)?\d{2})$",date))
# print(re.search(r"^(((0[13-9]|1[012])[-/]?(0[1-9]|[12][0-9]|30)|(0[13578]|1[02])[-/]?31|02[-/]?(0[1-9]|1[0-9]|2[0-8]))[-/]?[0-9]{4}|02[-/]?29[-/]?([0-9]{2}(([2468][048]|[02468][48])|[13579][26])|([13579][26]|[02468][048]|0[0-9]|1[0-6])00))$",date))
# print(re.search(r"^((2000|2400|2800|(19|2[0-9](0[48]|[2468][048]|[13579][26])))-02-29)$|^(((19|2[0-9])[0-9]{2})-02-(0[1-9]|1[0-9]|2[0-8]))$|^(((19|2[0-9])[0-9]{2})-(0[13578]|10|12)-(0[1-9]|[12][0-9]|3[01]))$|^(((19|2[0-9])[0-9]{2})-(0[469]|11)-(0[1-9]|[12][0-9]|30))$",date))
# print(re.search(r"^(?:(?:31(\/|-|\.)(?:0?[13578]|1[02]))\1|(?:(?:29|30)(\/|-|\.)(?:0?[13-9]|1[0-2])\2))(?:(?:1[6-9]|[2-9]\d)?\d{2})$|^(?:29(\/|-|\.)0?2\3(?:(?:(?:1[6-9]|[2-9]\d)?(?:0[48]|[2468][048]|[13579][26])|(?:(?:16|[2468][048]|[3579][26])00))))$|^(?:0?[1-9]|1\d|2[0-8])(\/|-|\.)(?:(?:0?[1-9])|(?:1[0-2]))\4(?:(?:1[6-9]|[2-9]\d)?\d{2})$",date))
# print(re.search("^(((0[13-9]|1[012])[-/]?(0[1-9]|[12][0-9]|30)|(0[13578]|1[02])[-/]?31|02[-/]?(0[1-9]|1[0-9]|2[0-8]))[-/]?[0-9]{4}|02[-/]?29[-/]?([0-9]{2}(([2468][048]|[02468][48])|[13579][26])|([13579][26]|[02468][048]|0[0-9]|1[0-6])00))$",date))
# print(re.(r"^[0-3]?[0-9].[0-3]?[0-9].(?:[0-9]{2})?[0-9]{2}$",date))
new_string = re.search(r"[0-9]{1,4}[\_|\-|\/|\|][0-9]{1,2}[\_|\-|\/|\|][0-9]{1,4}", date)
print((new_string.group(0)))
# 
reg = "^(((0[13-9]|1[012])[-/]?(0[1-9]|[12][0-9]|30)|(0[13578]|1[02])[-/]?31|02[-/]?(0[1-9]|1[0-9]|2[0-8]))[-/]?[0-9]{4}|02[-/]?29[-/]?([0-9]{2}(([2468][048]|[02468][48])|[13579][26])|([13579][26]|[02468][048]|0[0-9]|1[0-6])00))$"
new = re.search(reg,date)
# print(new)


# import datefinder

# string_with_dates = '''
#     Central design committee session Tuesday 10/22 6:30 pm
#     Th 9/19 next year LAB: Serial encoding (Section 2.2)
#     There will be another one on December 15th for those who are unable to make it today.
#     Workbook 3 (Minimum Wage): due Wednesday 9/18 11:59pm
#     He will be flying in Sept. 15th.
#     We expect to deliver this between late 2021 and early 2022.
# '''

# matches = datefinder.find_dates(string_with_dates)
# for match in matches:
#     print(match)

from dateutil import parser
datetime_object = parser.parse("8/12/1998",dayfirst=True)
print((datetime_object))
# a= "1/1/2021/abs"
# print(len(a.split("/")))

ddd = parser.parser().parse('2011', dayfirst = True,default= None)
print(ddd)