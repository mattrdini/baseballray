import csv, sys, psycopg2, os

try:
   conn=psycopg2.connect("dbname='{0}' user='{1}' host='localhost'".format(os.environ['DBNAME'], os.environ['DBUSER']))
except:
   print "I am unable to connect to the database."
   sys.exit()

# TODO: Figure out how to read parent directory and print to year var
# TODO: create function to read available years for team

# right left switch
bat_mapping = {"R":0, "L":1, "B":2}

# right left mapping
throw_mapping = {"R": 0, "L": 1, "B":2}

# converting positions as strings to integers
pos_mapping = {"DH":10,"PH":11,"PR":12, "P":1, "C":2, "1B":3, "2B":4, "3B":5, "SS":6, "OF":7, "X":None}

# teams_by_year = {
#     "BOS":range(1901,2015), #BOSTON REDSOX
#     "PIT":range(1901,2015), #PITTSBURGH PIRATES
#     "CHA":range(1901,2015), #CHICAGO WHITE SOX
#     "PHI":range(1901,2015), #PHILADELPHIA PHILLIES
#     "BRO":range(1901,1957), #BROOKLYN SUPERBAS, ROBINS, DODGERS
#     "DET":range(1901,2015), #DETROIT TIGERS
#     "PHA":range(1901,1954), #PHILADELPHIA ATHLETICS
#     "SLN":range(1901,2015), #ST LOUIS CARDINALS
#     "BLA":range(1901,1902), #BALTIMORE ORIOLES
#     "BSN":range(1901,1952), #BOSTON BEANEATERS, DOVES, BEES, RUSTLERS, BRAVES
#     "WS1":range(1901,1960), #WASH. SENATORS
#     "CHN":range(1901,2016), #CHICAGO ORPHANS, CUBS
#     "CLE":range(1901,2015), #CLEVELAND INDIANS
#     "NY1":range(1901,1957), #NEW YORK GIANTS
#     "CIN":range(1901,2015), #CINCINATTI REDS
#     "MLA":range(1901,1901), #MILWAUKEE BREWERS
#     "SLA":range(1902,1953), #ST LOUIS BROWNS
#     "NYA":range(1903,1912), #NEW YORK HIGHLANDERS
#
# ##FEDERAL LEAGUES##
#     "IND":range(1914,1915), #INDIANAPOLIS HOOSIERS, NEWARK PEPPER
#     "BUF":range(1914,1915), #BUFFALO BUFFEDS, BLUES
#     "CHF":range(1914,1915), #CHICAGO CHI-FEDS
#     "KCF":range(1914,1915), #KANSAS CITY PACKERS
#     "PTF":range(1914,1915), #PITTSBURGH REBELS
#     "BLF":range(1914,1915), #BALTIMORE TERRAPINS
#     "SLF":range(1914,1915), #ST LOUIS TERRIERS
#     "SLN":
#     # "ATL":range(1942,2015),
# }


####################################
### Setting All Teams 2005-2015 ####
####################################


teams_by_year = {
    "ANA":range(2005,2016), #LA Angels
    "ARI":range(2005,2016), #Arizona Diamondbacks
    "ATL":range(2005,2016), #Atlanta BRAVES
    "BAL":range(2005,2016), #Baltimore ORIOLES
    "BOS":range(2005,2016), #Boston Red SOX
    "CHA":range(2005,2016), #Chicago White SOX
    "CHN":range(2005,2016), #Chicago CUBS
    "CIN":range(2005,2016), #Cincinatti Reds
    "CLE":range(2005,2016), #Cleveland Indians
    "COL":range(2005,2016), #Colorado Rockies
    "DET":range(2005,2016), #Detroit Tigers
    "FLO":range(2005,2012), #Florida Marlins
    "MIA":range(2012,2016), #Miami Marlins
    "HOU":range(2005,2016), #Houston Astros
    "KCA":range(2005,2016), #Kansas City Royals
    "LAN":range(2005,2016), #Los Angeles DODGERS
    "MIL":range(2005,2016), #Milwaukee Brewers
    "MIN":range(2005,2016), #Minnesotta Twins
    "NYA":range(2005,2016), #NY Yankees
    "NYN":range(2005,2016), #NY Mets
    "OAK":range(2005,2016), #Oakland Athletics
    "PHI":range(2005,2016), #Philadelphia Phillies
    "PIT":range(2005,2016), #Pittsburgh Pirates
    "SDN":range(2005,2016), #San Diego Padres
    "SEA":range(2005,2016), #Seattle Mariners
    "SFN":range(2005,2016), #San Francisco Giants
    "SLN":range(2005,2016), #St Louis Cardinals
    "TBA":range(2005,2016), #Tampa Bay Rays
    "TEX":range(2005,2016), #Texas Rangers
    "TOR":range(2005,2016), #Toronto Blue Jays
    "WAS":range(2005,2016)  #Washington Nationals
}


for team, years in teams_by_year.items():
    print team
    for y in years:
        print y
        filename = "data/rosters/{0}/{1}{0}.ros".format(y, team)
        print filename

        csv_f = csv.reader(open(filename))

        cur = conn.cursor()

        for i, row in enumerate(csv_f):
            if len(row) < 7:
                continue

            # print debugstatement
            # print row

            year = y
            id = row[0]
            fname = row[1]
            lname = row[2]
            bats = bat_mapping[row[3]]
            throws = throw_mapping[row[4]]
            team = row[5]
            pos = pos_mapping[row[6]]
            cur.execute("""INSERT INTO
                                public.rosters(id,year,first,last,bat,throw,
                                                team,position)
                            VALUES
                                (%s, %s, %s, %s, %s, %s, %s, %s)""", \
                                [id, year, fname, lname, bats, throws, team, pos])
            conn.commit()




    # print "data/rosters/{0}/BOS{0}.ros".format(y)
    # continue
