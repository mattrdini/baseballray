import csv, sys, psycopg2



# TODO: Figure out how to read parent directory and print to year var
# TODO: create function to read available years for team

# right left switch
bat_mapping = {"R":0, "L":1, "B":3}

# right left mapping
throw_mapping = {"R": True, "L": False}

# converting positions as strings to integers
pos_mapping = {"DH":0,"PH":0, "P":1, "C":2, "1B":3, "2B":4, "3B":5, "SS":6, "OF":7}

teams_by_year = {
    "BOS":range(1901,2015), #BOSTON REDSOX
    "PIT":range(1901,2015), #PITTSBURGH PIRATES
    "CHA":range(1901,2015), #CHICAGO WHITE SOX
    "PHI":range(1901,2015), #PHILADELPHIA PHILLIES
    "BRO":range(1901,1957), #BROOKLYN SUPERBAS, ROBINS, DODGERS
    "DET":range(1901,2015), #DETROIT TIGERS
    "PHA":range(1901,1954), #PHILADELPHIA ATHLETICS
    "SLN":range(1901,2015), #ST LOUIS CARDINALS
    "BLA":range(1901,1902), #BALTIMORE ORIOLES
    "BSN":range(1901,1952), #BOSTON BEANEATERS, DOVES, BEES, RUSTLERS, BRAVES
    "WS1":range(1901,1960), #WASH. SENATORS
    "CHN":range(1901,2016), #CHICAGO ORPHANS, CUBS
    "CLE":range(1901,2015), #CLEVELAND INDIANS
    "NY1":range(1901,1957), #NEW YORK GIANTS
    "CIN":range(1901,2015), #CINCINATTI REDS
    "MLA":range(1901,1901), #MILWAUKEE BREWERS
    "SLA":range(1902,1953), #ST LOUIS BROWNS
    "NYA":range(1903,1912), #NEW YORK HIGHLANDERS

##FEDERAL LEAGUES##
    "IND":range(1914,1915), #INDIANAPOLIS HOOSIERS, NEWARK PEPPER
    "BUF":range(1914,1915), #BUFFALO BUFFEDS, BLUES
    "CHF":range(1914,1915), #CHICAGO CHI-FEDS
    "KCF":range(1914,1915), #KANSAS CITY PACKERS
    "PTF":range(1914,1915), #PITTSBURGH REBELS
    "BLF":range(1914,1915), #BALTIMORE TERRAPINS
    "SLF":range(1914,1915), #ST LOUIS TERRIERS
    "SLN":
    # "ATL":range(1942,2015),
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
            sys.exit()




    # print "data/rosters/{0}/BOS{0}.ros".format(y)
    # continue
