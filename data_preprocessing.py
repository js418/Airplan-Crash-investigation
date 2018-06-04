# COMPSCI 590V - Data Visualization & Exploration
# Final Project
# Jie Song
# 30272759
# data cleaning

import csv
import re



def main():

    rindex = [0,1,2,3,5,6,9,10,12]
    header = ['Date','Time','City','Country','Operator','Route','Type','Manufacture','Aboard','Fatalities','Summary','Category']
    states = ["Alaska",
                  "Alabama",
                  "Arkansas",
                  "American Samoa",
                  "Arizona",
                  "California",
                  "Colorado",
                  "Connecticut",
                  "District of Columbia",
                  "Delaware",
                  "Florida",
                  "Georgia",
                  "Guam",
                  "Hawaii",
                  "Iowa",
                  "Idaho",
                  "Illinois",
                  "Indiana",
                  "Kansas",
                  "Kentucky",
                  "Louisiana",
                  "Massachusetts",
                  "Maryland",
                  "Maine",
                  "Michigan",
                  "Minnesota",
                  "Missouri",
                  "Mississippi",
                  "Montana",
                  "North Carolina",
                  "North Dakota",
                  "Nebraska",
                  "New Hampshire",
                  "New Jersey",
                  "New Mexico",
                  "Nevada",
                  "New York",
                  "Ohio",
                  "Oklahoma",
                  "Oregon",
                  "Pennsylvania",
                  "Puerto Rico",
                  "Rhode Island",
                  "South Carolina",
                  "South Dakota",
                  "Tennessee",
                  "Texas",
                  "Utah",
                  "Virginia",
                  "Virgin Islands",
                  "Vermont",
                  "Washington",
                  "Wisconsin",
                  "West Virginia",
                  "Wyoming"]

    
    with open("Airplane_Crashes_and_Fatalities_Since_1908.csv","rU") as f:
        reader = csv.reader(f,delimiter=',')
        line = list(reader)
    f.close

    with open("clean_data_1.csv","wb") as w:
        writer = csv.writer(w)
        writer.writerow(header)

        # process the attribute for each row
        for i in range(1,len(line)):
            r = []            
            for j in rindex:
                if(j == 1):
                    if(line[i][j] == ''):
                        r.append('0:00')
                    else:
                        r.append(line[i][j])
                elif(j == 2):
                    l2 = line[i][j].replace('Near','').split(',')
                    r.append(l2[0].strip())
                    x = len(l2)-1
                    if (x==0):
                        r.append(l2[0].strip())
                    elif(x>0):
                        l2[x] = l2[x].strip()
                        if (l2[x] in states):
                            r.append('United States')
                        else:
                            r.append(l2[x])
                    else:
                        r.append('unknown')
                elif(j == 3):
                    r.append(line[i][j])
                    if ('Military' in line[i][j]):
                        c = 'Military'
                    elif('Service' in line[i][j]):
                        c = 'Cargo/Service'
                    else:
                        c = 'Passeger'
                elif(j == 6):
                    if (line[i][j] == ''):
                        r.append('unknown')
                        r.append('unknown')
                    else:
                        r.append(line[i][j])
                        m = re.sub("\S*\d\S*", '', line[i][j]).strip()
                        if ('(' in m):
                            l7 = m.split('(')
                            r.append(l7[0].strip())
                        elif ('\\' in m):
                            l7 = m.split('\\')
                            r.append(l7[0].strip())
                        elif ('/' in m):
                            l7 = m.split('/')
                            r.append(l7[0].strip())                       
                        else:
                            r.append(m)
                elif(j == 9):
                    if (line[i][j] == ''):
                        r.append('0')
                    else:
                        r.append(line[i][j])
                elif(j == 10):
                    if (line[i][j] == ''):
                        r.append('0')
                    else:
                        r.append(line[i][j])
                elif(j == 12):
                    l12 = line[i][j].lower()
                    if (l12 == ''):
                        r.append('unknown')
                    else:
                        r.append(l12)
                    if ('military' in l12):
                        c = 'Military'
                    elif ('cargo plan' in l12 or 'mail plan' in l12):
                        c = 'Cargo/Service'                    
                    r.append(c)
                else:
                    if (line[i][j] == ''):
                        r.append('unknown')
                    else:
                        r.append(line[i][j])
            # print r
            writer.writerow(r)



    w.close

main()
