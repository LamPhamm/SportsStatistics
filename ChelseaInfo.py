
from bs4 import BeautifulSoup
import requests
import re

#Chelsea Player Stats link
playersUrl="https://www.premierleague.com/clubs/4/Chelsea/squad"
seasonUrl="https://fbref.com/en/squads/cff3d9bb/Chelsea-Stats"
trophiesUrl="https://www.chelseafc.com/en/history/trophy-cabinet"

#Get the text of the url into an html doc
page=requests.get(playersUrl).text
doc=BeautifulSoup(page,"html.parser")

page2=requests.get(seasonUrl).text
doc2=BeautifulSoup(page2,"html.parser")

page3=requests.get(trophiesUrl).text
doc3=BeautifulSoup(page3,"html.parser")

#This function gets the nationality for any player
def getNationality(player_name):
    tag=doc.find(text=re.compile(player_name))

    #Get the ultimate parent of the tag in order to get the stats
    parent=tag.parent.parent.parent.parent

    #Get the nationality of the player
    nationality=parent.find(class_="squadPlayerStats").find(class_="playerCountry").string
    return nationality

#This function gets the appearances for any player
def getAppearances(player_name):
    tag=doc.find(text=re.compile(player_name))

    #Get the ultimate parent of the tag in order to get the stats
    parent=tag.parent.parent.parent.parent

    #Get the appearances of the player
    appearances=list(parent.find(class_="squadPlayerStats").find_all(class_="info"))[1].string
    return appearances

#This function gets the clean sheets for any defender
def getCleanSheets(player_name):
    tag=doc.find(text=re.compile(player_name))

    #Get the ultimate parent of the tag in order to get the stats
    parent=tag.parent.parent.parent.parent

    #Get the clean sheets of the player
    clean_sheets=list(parent.find(class_="squadPlayerStats").find_all(class_="info"))[2].string
    return clean_sheets

#This function gets the number of goals for any defender
def getGoalsForDefender(player_name):
    tag=doc.find(text=re.compile(player_name))

    #Get the ultimate parent of the tag in order to get the stats
    parent=tag.parent.parent.parent.parent

    #Get the number of goals of the player
    goals=list(parent.find(class_="squadPlayerStats").find_all(class_="info"))[3].string
    return goals

#This function gets the number of goals for any attacker
def getGoalsForAttacker(player_name):
    tag=doc.find(text=re.compile(player_name))

    #Get the ultimate parent of the tag in order to get the stats
    parent=tag.parent.parent.parent.parent

    #Get the number of goals of the player
    goals=list(parent.find(class_="squadPlayerStats").find_all(class_="info"))[2].string
    return goals

#This function gets the number of assists for any attacker
def getAssists(player_name):
    tag=doc.find(text=re.compile(player_name))

    #Get the ultimate parent of the tag in order to get the stats
    parent=tag.parent.parent.parent.parent

    #Get the number of assists of the player
    assists=list(parent.find(class_="squadPlayerStats").find_all(class_="info"))[3].string
    return assists
        
#TROPHY STATISTICS
#Gets the number of league titles and what years
def getLeagueTitles():
    
    titles=list(doc3.find(text=re.compile("LEAGUE TITLES")).parent.parent.children)[1].string
    titlesYears=list(doc3.find(text=re.compile("LEAGUE TITLES")).parent.parent.children)[2].string
    return titles,titlesYears

#Gets the number of champions league titles and what years
def getChampionsLeagueTitles():
    titles=list(doc3.find(text=re.compile("CHAMPIONS LEAGUE")).parent.parent.children)[1].string
    titlesYears=list(doc3.find(text=re.compile("CHAMPIONS LEAGUE")).parent.parent.children)[2].string
    return titles,titlesYears

#Gets the number of club world cups and what years
def getClubWorldCups():
    titles=list(doc3.find(text=re.compile("CLUB WORLD CUP")).parent.parent.children)[1].string
    titlesYears=list(doc3.find(text=re.compile("CLUB WORLD CUP")).parent.parent.children)[2].string
    return titles,titlesYears

#Gets the number of europa leagues and what years
def getEuropaLeagues():
    titles=list(doc3.find(text=re.compile("EUROPA")).parent.parent.children)[1].string
    titlesYears=list(doc3.find(text=re.compile("EUROPA")).parent.parent.children)[2].string
    return titles,titlesYears

#Gets the number of FA cups and what years
def getFACups():
    titles=list(doc3.find(text=re.compile("FA CUP")).parent.parent.children)[1].string
    titlesYears=list(doc3.find(text=re.compile("FA CUP")).parent.parent.children)[2].string
    return titles,titlesYears

#Gets the number of league cups and what years
def getLeagueCups():
    titles=list(doc3.find(text=re.compile("LEAGUE CUP")).parent.parent.children)[1].string
    titlesYears=list(doc3.find(text=re.compile("LEAGUE CUP")).parent.parent.children)[2].string
    return titles,titlesYears

#Gets the number of SUPER cups and what years
def getSuperCups():
    titles=list(doc3.find(text=re.compile("SUPER")).parent.parent.children)[1].string
    titlesYears=list(doc3.find(text=re.compile("SUPER")).parent.parent.children)[2].string
    return titles,titlesYears

#Gets the number of club world cups and what years
def getCommunityShields():
    titles=list(doc3.find(text=re.compile("COMMUNITY")).parent.parent.children)[1].string
    titlesYears=list(doc3.find(text=re.compile("COMMUNITY")).parent.parent.children)[2].string
    return titles,titlesYears

#SEASON STATISTICS
#Gets the league position of Chelsea
def getRecord():
    infoList=list(doc2.find(text=re.compile("Record")).parent.parent.children)[2]
    record=infoList.split(",")[0].strip()
    return record

#Gets the points of Chelsea
def getPoints():
    infoList=list(doc2.find(text=re.compile("Record")).parent.parent.children)[2]
    points=infoList.split(",")[1].strip()[:9]
    return points

#Gets the league position of Chelsea
def getPosition():
    infoList=list(doc2.find(text=re.compile("Record")).parent.parent.children)[2]
    position=infoList.split(",")[2].strip()[:3]
    return position

#Gets the goals for the season for Chelsea
def getGoals():
    infoList=list(doc2.find(text=re.compile("Goals")).parent.parent.children)
    goals=infoList[1].split()[0]
    return goals

#Gets the goals concded for the season for Chelsea
def getGoalsConceded():
    infoList=list(doc2.find(text=re.compile("Goals")).parent.parent.children)
    goalsConceded=infoList[3].split()[0]
    return goalsConceded
