# Esse boco de código serve para gerar uma lista com todas as segundas feiras do ano a partir do periodo passado

import datetime

datas = []

start = datetime.date(2010, 1, 4)
end = datetime.date(2010, 12, 27)

current_date = start
while current_date <= end:
    datas.append(str(current_date))
    current_date += datetime.timedelta(weeks=1)

print(datas)
