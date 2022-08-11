import grequests
import time
from bs4 import BeautifulSoup
import re
import requests
import pandas as pd
import json
import cchardet


def c_oyunfor(oynfor):
    oyunforalis = []
    oyunforsatis = []
    fiyat_oynfor = oynfor.find_all(class_="button desktop sellToUsBtn")

    for l in fiyat_oynfor:
        textlm = l.text
        textlm = textlm.replace("Bize Sat ", "").replace(
            "TL", "").replace("\n", "")

        if len(oyunforalis) < 9:
            oyunforalis.append(float(textlm) * 10)
        else:
            break

    for k in oynfor.find_all(class_="flex-row mobile"):
        textlms = k.text
        textlms = textlms.replace(" ", "").replace("TL", "").replace("\n", "")

        try:
            if len(oyunforsatis) < 9:
                oyunforsatis.append(float(textlms) * 10)
            else:
                break
        except:
            pass

    print("Oyunfor Success.", oyunforalis, oyunforsatis)
    return [oyunforalis, oyunforsatis]


def c_yyg():
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'}
    yygalis = []
    yygsatis = []
    while not yygalis:        

        yyg = requests.get(
            "https://www.yesilyurtgame.com/oyun-parasi/knight-online-goldbar-gb", timeout=5, headers=header
        )
        yygsoup = BeautifulSoup(yyg.content, "lxml")

        for urunler in yygsoup.find_all("section"):
            try:
                x = urunler.text

                ya = re.findall(r"GB Alış Fiyatı :([^TL]+)", x)
                ys = re.findall(r"Satış Fiyatı :([^TL]+)", x)

                ya = "".join(ya)
                ys = "".join(ys)

                ya.strip(" \n")

                ys.strip(" \n")
                if(len(yygalis) < 9):
                    yygalis.append(float(ya)*10)
                    yygsatis.append(float(ys)*10)
                else:
                    break

            except Exception as e:
                print("Yyg_err", e)
    print("YYG Success.", yygalis, yygsatis)

    return [yygalis, yygsatis]


# *---BYNOGAME-----BYNOGAME-----BYNOGAME-----BYNOGAME-----BYNOGAME-----BYNOGAME-----BYNOGAME-----BYNOGAME-----BYNOGAME-----BYNOGAME-----BYNOGAME-----


def c_bynogame(soup):
    bynogamealis = []
    bynogamesatis = []
    tler = soup.find(
        class_="col-xl-18 col-lg-24 col-md-24 order-1 order-sm-12")

    try:
        for i in tler.find_all(class_="col"):
            i = i.text
            i = i.replace('TL', "").replace('\n', "").replace(',', ".")

            if len(bynogamealis) < 9:
                bynogamealis.append(float(i))

        for i in tler.find_all(class_="btn btn-block px-4 py-3 font-weight-bolder btn-outline-bng-black p-2"):

            i = i.text
            i = i.replace("TL'den BİZE SAT", "").replace(
                '\n', "").replace(',', ".")

            if len(bynogamesatis) < 9:
                bynogamesatis.append(float(i))
        print("BynoGame Success", bynogamealis, bynogamesatis)
        return [bynogamesatis, bynogamealis]
    except Exception as e:
        print("Bynogame_err", e)


# TODO KOPAZAR-----KOPAZAR-----KOPAZAR-----KOPAZAR-----KOPAZAR-----KOPAZAR-----KOPAZAR-----KOPAZAR-----KOPAZAR-----KOPAZAR-----KOPAZAR-----KOPAZAR-----

def c_kopazar(kopzr):
    kopazaralis = []
    kopazarsatis = []

    # *KOPAZAR ALIŞ BLOĞU BAŞ.
    try:
        for kp_af in kopzr.find_all(class_="caret-up"):
            kp_af = kp_af.string
            kp_af = kp_af.replace(" ", "").replace("₺", "")

            kp_af = float(kp_af)
            if len(kopazaralis) < 9:
                kopazaralis.append(kp_af * 10)

    except Exception as e:

        print("kopazar_af_err: ", e)

    # *KOPAZAR ALIŞ BLOĞU SON

    # ?#?#?#?#?#?#?#?#?#?#?#?#?#?#?#?#?#?

    # * KOPAZAR SATIŞ BLOĞU BAŞ.
    try:
        for kp_sf in kopzr.find_all(
            class_="col-xl-3 col-lg-6 col-sm-3 col-6 order-xl-3 order-lg-2 order-sm-3 order-2 xl-text-right text-center"
        ):

            #! String Değiştirme
            kp_sf = kp_sf.text
            kp_sf = kp_sf.replace("Satış Fiyatı", "").replace(
                "\n", "").replace(" ", "").replace("₺", "")

            #! String Değiştirme Son
            kp_sf = float(kp_sf)
            if len(kopazarsatis) < 9:
                kopazarsatis.append(kp_sf * 10)

    except Exception as e:

        print("kp_sf", e)
    print("Kopazar Success.", kopazaralis, kopazarsatis)
    return [kopazaralis, kopazarsatis]
    # * KOPAZAR SATIŞ BLOĞU SON.

# ?---KLASGAME---KLASGAME---KLASGAME---KLASGAME---KLASGAME---KLASGAME---KLASGAME---KLASGAME---KLASGAME---KLASGAME---KLASGAME---KLASGAME---KLASGAME


def c_klasgame(klsgame):
    klasgamealis = []
    klasgamesatis = []
    mmm = klsgame.find(
        class_="goldbar-table table table-borderless product-table-item"
    )
    # print("KLASGAME", mmm)
    try:
        mmm = klsgame.find(
            class_="goldbar-table table table-borderless product-table-item"
        )
        v = 2
        for kg in mmm.find_all(class_="font-weight-bold price"):
            # print(v)
            tr = kg.find("span").text
            tr = tr.replace(",", ".")
            # print(tr)
            tr = float(tr)
            if len(klasgamealis) <= 9 and len(klasgamesatis) < 9:
                if v % 2 == 0:
                    klasgamealis.append(tr*10)
                    v += 1
                elif v % 2 != 0:
                    klasgamesatis.append(tr*10)
                    v += 1
            else:
                break
    except Exception as e:

        print("klsgame_err", e)
        klasgamealis = [0 for i in range(9)]
        klasgamesatis = [0 for i in range(9)]
    return [klasgamealis, klasgamesatis]

    # * OYUNFOR-------OYUNFOR-------OYUNFOR-------OYUNFOR-------OYUNFOR-------OYUNFOR-------OYUNFOR-------OYUNFOR-------OYUNFOR-------OYUNFOR-------OYUNFOR-------


def job():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'}
    
    urls = ["https://www.bynogame.com/tr/oyunlar/knight-online/gold-bar",
            "https://www.oyunfor.com/knight-online/gb-gold-bar",          
            "https://www.kopazar.com/knight-online-gold-bar",     
            "https://www.klasgame.com/goldbar/knightonline/knight-online-gb-goldbar-premium-cash"
                    
            ]
    rs = (grequests.get(u, headers=headers) for u in urls)

    x = grequests.map(rs)
    soup = BeautifulSoup(x[0].content, "lxml")
    oynfor = BeautifulSoup(x[1].content, "lxml")
    kopzr = BeautifulSoup(x[2].content, "lxml")
    klsgame = BeautifulSoup(x[3].content, "lxml")
    # yygsoup = BeautifulSoup(x[4].content, "lxml")
    
    def control(liste):
        return (len(liste[0]) < 9 or (len(liste[0]) != len(liste[1])))
          
        
    try:
        yyg_data = c_yyg()
        if control(yyg_data):
            yyg_data[0] = ['err' for i in range(9)]
            yyg_data[1] = ['err' for i in range(9)]
    except:
        yyg_data = [[], []]
        yyg_data[0] = ['err' for i in range(9)]
        yyg_data[1] = ['err' for i in range(9)]
    try:
        bynogame_data = c_bynogame(soup)
        if control(bynogame_data):
            bynogame_data[0] = ['err' for i in range(9)]
            bynogame_data[1] = ['err' for i in range(9)]
    except:
        bynogame_data = [[], []]
        bynogame_data[0] = ['err' for i in range(9)]
        bynogame_data[1] = ['err' for i in range(9)]
    try:
        kopazar_data = c_kopazar(kopzr)
        if control(kopazar_data):
            kopazar_data[0] = ['err' for i in range(9)]
            kopazar_data[1] = ['err' for i in range(9)]
    except:
        kopazar_data = [[], []]
        kopazar_data[0] = ['err' for i in range(9)]
        kopazar_data[1] = ['err' for i in range(9)]
    try:
        klasgame_data = c_klasgame(klsgame)
        if control(klasgame_data):
            klasgame_data[0] = ['err' for i in range(9)]
            klasgame_data[1] = ['err' for i in range(9)]
    except:
        klasgame_data = [[], []]
        klasgame_data[0] = ['err' for i in range(9)]
        klasgame_data[1] = ['err' for i in range(9)]
    try:
        oyunfor_data = c_oyunfor(oynfor)
        if control(oyunfor_data):
            oyunfor_data[0] = ['err' for i in range(9)]
            oyunfor_data[1] = ['err' for i in range(9)]
    except:
        oyunfor_data = [[], []]
        oyunfor_data[0] = ['err' for i in range(9)]
        oyunfor_data[1] = ['err' for i in range(9)]

    df_kopazar = pd.DataFrame({"Sunucu": ["Altar", "Vega", "Sirius", "Ares", "Diez", "Gordion", "Rosetta", "Olympia", "Destan"],

                               "Kopazar Alış": kopazar_data[0],

                               "Kopazar Satış": kopazar_data[1],

                               })

    df_kopazar = df_kopazar.sort_values("Sunucu")

    df_bynogame = pd.DataFrame({"Sunucu": ["Sirius", "Vega", "Altar", "Destan", "Olympia", "Ares", "Diez", "Gordion", "Rosetta"],

                                "Bynogame Alış": bynogame_data[0],

                                "Bynogame Satış": bynogame_data[1],

                                })
    df_bynogame = df_bynogame.sort_values("Sunucu")
    df_yyg = pd.DataFrame({"Sunucu": ["Altar", "Sirius", "Vega", "Destan", "Rosetta", "Olympia", "Ares", "Diez", "Gordion"],

                           "Yyg Alış": yyg_data[0],

                           "Yyg Satış": yyg_data[1],

                           })
    df_yyg = df_yyg.sort_values("Sunucu")

    df_klasgame = pd.DataFrame({"Sunucu": ["Altar", "Sirius", "Vega", "Destan", "Rosetta", "Olympia", "Ares", "Diez", "Gordion"],

                                "Klasgame Alış": klasgame_data[0],

                                "Klasgame Satış": klasgame_data[1],

                                })
    df_klasgame = df_klasgame.sort_values("Sunucu")

    df_oyunfor = pd.DataFrame({"Sunucu": ["Altar", "Sirius", "Vega", "Destan", "Rosetta", "Diez", "Ares", "Olympia", "Gordion"],

                               "Oyunfor Alış": oyunfor_data[0],

                               "Oyunfor Satış": oyunfor_data[1],

                               })
    df_oyunfor = df_oyunfor.sort_values("Sunucu")

    kopazar_html = df_kopazar.to_html(
        index=False, classes='Kopazar', border='0', justify='left')
    bynogame_html = df_bynogame.to_html(
        index=False, classes='Bynogame', border='0', justify='left')
    oyunfor_html = df_oyunfor.to_html(
        index=False, classes='Oyunfor', border='0', justify='left')
    yyg_html = df_yyg.to_html(
        index=False, classes='Yyg', border='0', justify='left')
    klasgame_html = df_klasgame.to_html(
        index=False, classes='Klasgame', border='0', justify='left')

    return [kopazar_html, bynogame_html, oyunfor_html, yyg_html, klasgame_html]
