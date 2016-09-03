# -*- coding: UTF-8 -*
from datetime import date
import calendar
from dagatal import d
#header = 
#body =


manudir_skel = ((2016,8,('Ágúst').decode('utf-8')),
                (2016,9,('September').decode('utf-8')),
                (2016,10,('Október').decode('utf-8')),
                (2016,11,('Nóvember').decode('utf-8')),
                (2016,12,('Desember').decode('utf-8')),
                (2017,1,('Janúar').decode('utf-8')),
                (2017,2,('Febrúar').decode('utf-8')),
                (2017,3,('Mars').decode('utf-8')),
                (2017,4,('Apríl').decode('utf-8')),
                (2017,5,('Maí').decode('utf-8')))
months = []
skoladagatal = calendar.Calendar(0)

for manudur in manudir_skel:
    m = {'name': manudur[2],'year': manudur[0],'serial': manudur[1],'weeks': [], 'left_margin': float(0), 'right_margin': float(0)}
    it = list(skoladagatal.itermonthdays(m['year'],m['serial']))
    week_n = len(it)/7
    for i in range(week_n):
        m['weeks'].append(it[i*7:(i+1)*7])
        
    week0 = m['weeks'][0]
    count_zeros = float(0)
    for day in week0:
        if day == 0:
           count_zeros += 1
    m['left_margin'] = 100*count_zeros/float(7)

    week_last = m['weeks'][-1]
    count_zeros = float(0)
    for day in week_last:
        if day == 0:
           count_zeros += 1
           
    m['right_margin'] = 100*count_zeros/float(7)


    months.append(m)

weeksStart = 'var w%s = ['
weekStart = '{marginLeft: %s,marginRight: %s,days:['
weekEnd = ']}'
dayTemplate = '{tegund:%s,specials:%s,day:%s, month:%s}'
weeksEnd = "];"

output_file = open('gogn.js', 'w')

    
specialTemplate = '{title: "%s",logo: "%s"}'

for month in months:
    output =''
    output += weeksStart % month['serial']
    mon = month['serial']
    week_len = len(month['weeks'])
    i = 0
    for week in month['weeks']:
        if i==0:
           output += weekStart % ('"'+str(month['left_margin']) + '%"',0)
        elif i== week_len-1:
             output += weekStart % (0,'"'+str(month['right_margin']) + '%"')
        else:
            output += weekStart % (0,0)
        for day in week:
            if day != 0:
               dayJSON = d[str(mon) + '-' + str(day)]
               
               if len(dayJSON['specials'])== 0:
                  spec = 'null'
               else:
                   spec = '['
                   for special in dayJSON['specials']:
                       
                       spec += specialTemplate % (special[0],special[1])
                       spec += ','
                   spec = spec[:-1]
                   spec += ']'
               output += dayTemplate % ('"' + dayJSON['tegund'] + '"',spec,day,month['serial'])
               output += ','

        output=output[:-1]
        output += weekEnd
        output += ','
        i += 1
    output += weeksEnd
    output_file.write(output)
    
output_file.close()
