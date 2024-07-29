import requests
from bs4 import BeautifulSoup
import pandas as pd

url_sonu = 0
liste = []
while url_sonu <= 1600:
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 OPR/98.0.0.0"}
    url = "https://sofifa.com/?gender=1?showCol%5B0%5D=pi&showCol%5B1%5D=ae&showCol%5B2%5D=hi&showCol%5B3%5D=wi&showCol%5B4%5D=pf&showCol%5B5%5D=oa&showCol%5B6%5D=pt&showCol%5B7%5D=bo&showCol%5B8%5D=bp&showCol%5B9%5D=gu&showCol%5B10%5D=jt&showCol%5B11%5D=le&showCol%5B12%5D=vl&showCol%5B13%5D=wg&showCol%5B14%5D=rc&showCol%5B15%5D=ta&showCol%5B16%5D=cr&showCol%5B17%5D=fi&showCol%5B18%5D=he&showCol%5B19%5D=sh&showCol%5B20%5D=vo&showCol%5B21%5D=ts&showCol%5B22%5D=dr&showCol%5B23%5D=cu&showCol%5B24%5D=fr&showCol%5B25%5D=lo&showCol%5B26%5D=bl&showCol%5B27%5D=to&showCol%5B28%5D=ac&showCol%5B29%5D=sp&showCol%5B30%5D=ag&showCol%5B31%5D=re&showCol%5B32%5D=ba&showCol%5B33%5D=tp&showCol%5B34%5D=so&showCol%5B35%5D=ju&showCol%5B36%5D=st&showCol%5B37%5D=sr&showCol%5B38%5D=ln&showCol%5B39%5D=te&showCol%5B40%5D=ar&showCol%5B41%5D=in&showCol%5B42%5D=po&showCol%5B43%5D=vi&showCol%5B44%5D=pe&showCol%5B45%5D=cm&showCol%5B46%5D=td&showCol%5B47%5D=ma&showCol%5B48%5D=sa&showCol%5B49%5D=sl&showCol%5B50%5D=tg&showCol%5B51%5D=gd&showCol%5B52%5D=gh&showCol%5B53%5D=gc&showCol%5B54%5D=gp&showCol%5B55%5D=gr&showCol%5B56%5D=tt&showCol%5B57%5D=bs&showCol%5B58%5D=wk&showCol%5B59%5D=sk&showCol%5B60%5D=aw&showCol%5B61%5D=dw&showCol%5B62%5D=ir&showCol%5B63%5D=bt&showCol%5B64%5D=pac&showCol%5B65%5D=sho&showCol%5B66%5D=pas&showCol%5B67%5D=dri&showCol%5B68%5D=def&showCol%5B69%5D=phy&showCol%5B70%5D=t1&showCol%5B71%5D=t2&showCol%5B72%5D=ps1&showCol%5B73%5D=ps2&col=vl&sort=desc&offset=0" \
          + str(url_sonu)
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.content, "html.parser")

    article = soup.find("article")
    cekilen_veri = article.find("table")
    tablo1 = cekilen_veri.find_all("tr")

    for tr in tablo1[1:]:
        player_names = tr.find("a")
        player_names2 = player_names.text.strip()

        ages = tr.find("td", class_="d2")
        ages2 = ages.text.strip()

        nations_tag = tr.select_one("td:nth-of-type(2) img.flag")
        nations = nations_tag.get("title")

        positions = tr.find("span", class_="pos")
        positions2 = positions.get_text(strip=True)

        clubs = tr.select_one("td:nth-of-type(6) a")
        club_name = clubs.text.strip()

        value = tr.find("td", class_="d6 col-sort")
        value2 = value.text.strip()

        overall = tr.find("td", {"data-col": "oa"})
        overall2 = overall.find("em")["title"]

        potential = tr.find("td", {"data-col": "pt"})
        potential2 = potential.find("em")["title"]

        totalattacking = tr.find("td", {"data-col": "ta"})
        totalattacking2 = totalattacking.find("em").text.strip()

        crossing = tr.find("td", {"data-col": "cr"})
        crossing2 = crossing.find("em")["title"]

        finishing = tr.find("td", {"data-col": "fi"})
        finishing2 = finishing.find("em")["title"]

        headingaccuracy = tr.find("td", {"data-col": "he"})
        headingaccuracy2 = headingaccuracy.find("em")["title"]

        shortpassing = tr.find("td", {"data-col": "sh"})
        shortpassing2 = shortpassing.find("em")["title"]

        volleys = tr.find("td", {"data-col": "vo"})
        volleys2 = volleys.find("em")["title"]

        totalskill = tr.find("td", {"data-col": "ts"})
        totalskill2 = totalskill.find("em").text.strip()

        dribbling = tr.find("td", {"data-col": "dr"})
        dribbling2 = dribbling.find("em")["title"]

        curve = tr.find("td", {"data-col": "cu"})
        curve2 = curve.find("em")["title"]

        fkaccuracy = tr.find("td", {"data-col": "fr"})
        fkaccuracy2 = fkaccuracy.find("em")["title"]

        longpassing = tr.find("td", {"data-col": "lo"})
        longpassing2 = longpassing.find("em")["title"]

        ballcontrol = tr.find("td", {"data-col": "bl"})
        ballcontrol2 = ballcontrol.find("em")["title"]

        totalmovement = tr.find("td", {"data-col": "to"})
        totalmovement2 = totalmovement.find("em").text.strip()

        acceleration = tr.find("td", {"data-col": "ac"})
        acceleration2 = acceleration.find("em")["title"]

        sprintspeed = tr.find("td", {"data-col": "sp"})
        sprintspeed2 = sprintspeed.find("em")["title"]

        agility = tr.find("td", {"data-col": "ag"})
        agility2 = agility.find("em")["title"]

        reactions = tr.find("td", {"data-col": "re"})
        reactions2 = reactions.find("em")["title"]

        balance = tr.find("td", {"data-col": "ba"})
        balance2 = balance.find("em")["title"]

        totalpower = tr.find("td", {"data-col": "tp"})
        totalpower2 = totalpower.find("em").text.strip()

        shotpower = tr.find("td", {"data-col": "so"})
        shotpower2 = shotpower.find("em")["title"]

        jumping = tr.find("td", {"data-col": "ju"})
        jumping2 = jumping.find("em")["title"]

        stamina = tr.find("td", {"data-col": "st"})
        stamina2 = stamina.find("em")["title"]

        strength = tr.find("td", {"data-col": "sr"})
        strength2 = strength.find("em")["title"]

        longshots = tr.find("td", {"data-col": "ln"})
        longshots2 = longshots.find("em")["title"]

        totalmentality = tr.find("td", {"data-col": "te"})
        totalmentality2 = totalmentality.find("em").text.strip()

        aggression = tr.find("td", {"data-col": "ar"})
        aggression2 = aggression.find("em")["title"]

        interceptions = tr.find("td", {"data-col": "in"})
        interceptions2 = interceptions.find("em")["title"]

        positioning = tr.find("td", {"data-col": "po"})
        positioning2 = positioning.find("em")["title"]

        vision = tr.find("td", {"data-col": "vi"})
        vision2 = vision.find("em")["title"]

        penalties = tr.find("td", {"data-col": "pe"})
        penalties2 = penalties.find("em")["title"]

        composure = tr.find("td", {"data-col": "cm"})
        composure2 = composure.find("em")["title"]

        totaldefending = tr.find("td", {"data-col": "td"})
        totaldefending2 = totaldefending.find("em").text.strip()

        marking = tr.find("td", {"data-col": "ma"})
        marking2 = marking.find("em")["title"]

        standingtackle = tr.find("td", {"data-col": "sa"})
        standingtackle2 = standingtackle.find("em")["title"]

        slidingtackle = tr.find("td", {"data-col": "sl"})
        slidingtackle2 = slidingtackle.find("em")["title"]

        totalgoalkeeping = tr.find("td", {"data-col": "tg"})
        totalgoalkeeping2 = totalgoalkeeping.find("em").text.strip()

        gkdiving = tr.find("td", {"data-col": "gd"})
        gkdiving2 = gkdiving.find("em")["title"]

        gkhandling = tr.find("td", {"data-col": "gh"})
        gkhandling2 = gkhandling.find("em")["title"]

        gkkicking = tr.find("td", {"data-col": "gc"})
        gkkicking2 = gkkicking.find("em")["title"]

        gkpositioning = tr.find("td", {"data-col": "gp"})
        gkpositioning2 = gkpositioning.find("em")["title"]

        gkreflexes = tr.find("td", {"data-col": "gr"})
        gkreflexes2 = gkreflexes.find("em")["title"]

        weakfoot = tr.find("td", {"data-col": "wk"}).text.strip()
        #weakfoot2 = weakfoot.find("em")["title"]

        skillmoves = tr.find("td", {"data-col": "sk"}).text.strip()
        #skillmoves2 = skillmoves.find("em")["title"]

        internationalreputation = tr.find("td", {"data-col": "ir"}).text.strip()
        #internationalreputation2 = internationalreputation.find("em")["title"]

        liste.append([player_names2, ages2, positions2, club_name, nations,value2,overall2,potential2,totalattacking2,crossing2,finishing2,headingaccuracy2,shortpassing2,volleys2,totalskill2,dribbling2,curve2,fkaccuracy2,longpassing2,ballcontrol2,totalmovement2,acceleration2,sprintspeed2,agility2,reactions2,balance2,totalpower2,shotpower2,jumping2,stamina2,strength2,longshots2,totalmentality2,aggression2,interceptions2,positioning2,vision2,penalties2,composure2,totaldefending2,marking2,standingtackle2,slidingtackle2,totalgoalkeeping2,gkdiving2,gkhandling2,gkkicking2,gkpositioning2,gkreflexes2,weakfoot,skillmoves,internationalreputation])
        data = pd.DataFrame(liste, columns=["Name", "Age", "Position", "Club", "Nation", "Value", "Overall","Potential","Total Attacking","Crossing","Finishing","Heading Accuracy","Short Passing","Volleys","Total Skill","Dribbling","Curve","Free Kick Accuracy","Long Passing","Ball Control","Total Movement","Acceleration","Sprint Speed","Agility","Reactions","Balance","Total Power","Shot Power","Jumping","Stamina","Strength","Long Shots","Total Mentality","Aggression","Interceptions","Positioning","Vision","Penalties","Composure","Total Defending","Marking","Standing Tackle","Sliding Tackle","Total Goalkeeping","GK Diving","GK Handling","GK Kicking","GK Positioning","GK Reflexes","Weak Foot","Skill Moves","International Reputation"])

        pd.set_option('display.max_rows', None)
        pd.set_option('display.max_columns', None)
        pd.set_option('display.width', None)
        pd.set_option('display.max_colwidth', None)

        data.to_csv('men_dataset_yeni.csv')
    url_sonu += 60
