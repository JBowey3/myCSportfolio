
#3/17/25
#AP CREATE Project

#initialize
from PIL import Image   #image import algorithm (for opening/viewing images in python)--source at bottom of file
import requests
from io import BytesIO

#full lists of NFL team names, logo images, cities of residence, and adjectives--sources at bottom of file
teams = ["BuffaloBills","MiamiDolphins","NewEnglandPatriots","NewYorkJets","BaltimoreRavens","CincinnatiBengals","ClevelandBrowns","PittsburghSteelers","HoustonTexans","IndianapolisColts",
         "JacksonvilleJaguars","TennesseeTitans","DenverBroncos","KansasCityChiefs","LasVegasRaiders","LosAngelesChargers","DallasCowboys","NewYorkGiants","PhiladelphiaEagles",
         "WashingtonCommanders","ChicagoBears","DetroitLions","GreenBayPackers","MinnesotaVikings","AtlantaFalcons","CarolinaPanthers","NewOrleansSaints","TampaBayBuccaneers","ArizonaCardinals",
         "LosAngelesRams","SanFrancisco49ers","SeattleSeahawks"]
teamPics = ["https://cdn.ssref.net/req/202504041/tlogo/pfr/buf.png","https://upload.wikimedia.org/wikipedia/en/thumb/3/37/Miami_Dolphins_logo.svg/100px-Miami_Dolphins_logo.svg.png","https://upload.wikimedia.org/wikipedia/en/thumb/b/b9/New_England_Patriots_logo.svg/100px-New_England_Patriots_logo.svg.png","https://upload.wikimedia.org/wikipedia/en/thumb/6/6b/New_York_Jets_logo.svg/100px-New_York_Jets_logo.svg.png","https://upload.wikimedia.org/wikipedia/en/thumb/1/16/Baltimore_Ravens_logo.svg/100px-Baltimore_Ravens_logo.svg.png","https://upload.wikimedia.org/wikipedia/commons/thumb/8/81/Cincinnati_Bengals_logo.svg/100px-Cincinnati_Bengals_logo.svg.png","https://upload.wikimedia.org/wikipedia/en/thumb/d/d9/Cleveland_Browns_logo.svg/100px-Cleveland_Browns_logo.svg.png","https://upload.wikimedia.org/wikipedia/commons/thumb/d/de/Pittsburgh_Steelers_logo.svg/100px-Pittsburgh_Steelers_logo.svg.png","https://upload.wikimedia.org/wikipedia/en/thumb/2/28/Houston_Texans_logo.svg/100px-Houston_Texans_logo.svg.png","https://upload.wikimedia.org/wikipedia/commons/thumb/0/00/Indianapolis_Colts_logo.svg/100px-Indianapolis_Colts_logo.svg.png","https://upload.wikimedia.org/wikipedia/en/thumb/7/74/Jacksonville_Jaguars_logo.svg/100px-Jacksonville_Jaguars_logo.svg.png","https://upload.wikimedia.org/wikipedia/en/thumb/c/c1/Tennessee_Titans_logo.svg/100px-Tennessee_Titans_logo.svg.png","https://upload.wikimedia.org/wikipedia/en/thumb/4/44/Denver_Broncos_logo.svg/100px-Denver_Broncos_logo.svg.png","https://upload.wikimedia.org/wikipedia/en/thumb/e/e1/Kansas_City_Chiefs_logo.svg/100px-Kansas_City_Chiefs_logo.svg.png","https://upload.wikimedia.org/wikipedia/en/thumb/4/48/Las_Vegas_Raiders_logo.svg/100px-Las_Vegas_Raiders_logo.svg.png","https://upload.wikimedia.org/wikipedia/en/thumb/a/a6/Los_Angeles_Chargers_logo.svg/100px-Los_Angeles_Chargers_logo.svg.png","https://upload.wikimedia.org/wikipedia/commons/thumb/1/15/Dallas_Cowboys.svg/100px-Dallas_Cowboys.svg.png","https://upload.wikimedia.org/wikipedia/commons/thumb/6/60/New_York_Giants_logo.svg/100px-New_York_Giants_logo.svg.png","https://upload.wikimedia.org/wikipedia/en/thumb/8/8e/Philadelphia_Eagles_logo.svg/100px-Philadelphia_Eagles_logo.svg.png","https://upload.wikimedia.org/wikipedia/commons/thumb/0/0c/Washington_Commanders_logo.svg/2560px-Washington_Commanders_logo.svg.png","https://upload.wikimedia.org/wikipedia/commons/thumb/5/5c/Chicago_Bears_logo.svg/100px-Chicago_Bears_logo.svg.png","https://upload.wikimedia.org/wikipedia/en/thumb/7/71/Detroit_Lions_logo.svg/100px-Detroit_Lions_logo.svg.png","https://upload.wikimedia.org/wikipedia/commons/thumb/5/50/Green_Bay_Packers_logo.svg/100px-Green_Bay_Packers_logo.svg.png","https://upload.wikimedia.org/wikipedia/en/thumb/4/48/Minnesota_Vikings_logo.svg/98px-Minnesota_Vikings_logo.svg.png","https://upload.wikimedia.org/wikipedia/en/thumb/c/c5/Atlanta_Falcons_logo.svg/100px-Atlanta_Falcons_logo.svg.png","https://upload.wikimedia.org/wikipedia/en/thumb/1/1c/Carolina_Panthers_logo.svg/100px-Carolina_Panthers_logo.svg.png","https://upload.wikimedia.org/wikipedia/commons/thumb/5/50/New_Orleans_Saints_logo.svg/98px-New_Orleans_Saints_logo.svg.png","https://upload.wikimedia.org/wikipedia/en/thumb/a/a2/Tampa_Bay_Buccaneers_logo.svg/100px-Tampa_Bay_Buccaneers_logo.svg.png","https://upload.wikimedia.org/wikipedia/en/thumb/7/72/Arizona_Cardinals_logo.svg/100px-Arizona_Cardinals_logo.svg.png","https://upload.wikimedia.org/wikipedia/en/thumb/8/8a/Los_Angeles_Rams_logo.svg/100px-Los_Angeles_Rams_logo.svg.png","https://upload.wikimedia.org/wikipedia/commons/thumb/3/3a/San_Francisco_49ers_logo.svg/100px-San_Francisco_49ers_logo.svg.png","https://upload.wikimedia.org/wikipedia/en/thumb/8/8e/Seattle_Seahawks_logo.svg/100px-Seattle_Seahawks_logo.svg.png"]
teamCity = ["Buffalo","Miami","Boston","New York","Baltimore","Cincinnati","Cleveland","Pittsburgh","Houston","Indianapolis","Jacksonville","Nashville","Denver","Kansas City","Las Vegas","Los Angeles","Dallas","New York","Philadelphia","Washington DC","Chicago","Detroit","Green Bay","Minneapolis","Atlanta","Charlotte","New Orleans","Tampa Bay","Phoenix","Los Angeles","San Francisco","Seattle"]
team_word = ["Patriotic","Resilient","Innovative","Tough","Steely","Dominant","Powerful","Electric","Hard-nosed","Underdog","Innovative","Iconic","Relentless","Historic","Mile-High","Hard-hitting","America","Championship","Defiant","Prideful","Adaptable","Classic","Legendary","Explosive","Faithful","Fearsome","Elite","Dynamic","Noble"]
filtered_list = []

#functions
def open_image(url):   #short parameter function for executing the open image algorithm based on a given URL
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    img.show()

#function that receives a team name from the user and locates it's index on a list to supply the user with general info about them
def random_team(team):
    print("Want to know more about your recommended NFL team?")
    x = teams.index(team)
    print("here is the team's logo and a word associated with them!: ")
    print(team_word[x])
    open_image(teamPics[x])

#function that receives a favorite city from the user and outputs a possible team to root for by locating it in a team list
def favcity_team(city):                                                #parameter
    for i in range(len(teamCity)):                                    #loop
        if city in teamCity[i]:                                       #if statement
            filtered_list.append(teams[i])
    print("You could root for this NFL team!:")
    print(filtered_list)

def all_teams():    #function that prints all the NFL team names for unfamiliar users
    print("here is a list of all NFL teams, feel free to explore intriguing ones!")
    print(teams)

def team_rec(): #function that provides the user with an interface to execute all other functions in one place
    print("Welcome to the NFL team recommender program, where all uncertain new fans can find a team to support!")
    print("what do you want to do?:")
    print("""1. Be recommended an NFL team"
2. Learn more about an NFL team of your choice"
3. View a list of all the NFL teams"
4. Quit""")
    while True:
        option = int(input("(1-5) select option: "))
        if option == 1:
            favcity_team(input("what is your favorite major US city?: "))
        if option == 2:
            random_team(input("what NFL team would you like to know about?: "))
        if option == 3:
            all_teams()
        if option == 4:
            break  #loop end/user quit

#main
team_rec()  #one call

#data source for all list(s) (teams, cities, logos, descriptions): Sports Reference®. 2025. Accessed via: https://www.pro-football-reference.com/teams/
#image importation code derived from: Tarun Singh. July 2023. Accessed via: https://www.tutorialspoint.com/how-to-open-an-image-from-the-url-in-pil
