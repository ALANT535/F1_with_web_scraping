try:
    
    from bs4 import BeautifulSoup as bs
    import time
    import random
    import requests
    drivers=[]
    teams1=[]
    a=input("Enter a year and i'll tell you about it:")

    page= requests.get("https://www.formula1.com/en/results.html/"+a+"/drivers.html")
    soup=bs(page.content,features="html.parser")


    l=soup.find_all(class_="dark bold ArchiveLink")

    for i in range(len(l)):
        drivertemp=l[i].text.split()
        l1=" ".join(drivertemp[0:len(drivertemp)-1])
        drivers.append(l1)
    


    print(len(drivers)," total drivers.")
    l=soup.find_all(class_="grey semi-bold uppercase ArchiveLink")    
    for i in range(len(l)):
        # teamtemp=soup.find_all(class_="grey semi-bold uppercase ArchiveLink")[i].text
        teams1.append(l[i].text)
   
    teams=[]       #create unique list of teams
    for i in teams1:
        if i not in teams:
            teams.append(i)
        else:
            continue
    print(len(teams)," total teams")
        
    print("WDC: ",drivers[0])
    print("WCC: ",teams[0])

except:
    pass



