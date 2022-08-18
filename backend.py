import grequests
import time
from bs4 import BeautifulSoup
import re
import cchardet
import requests
import pandas as pd
import json


def c_oyunfor(oyunfor_request_data):
    """
    This functions simply takes the response from requests function, arranges it so that we only get price information.

    Args:
        oyunfor_request_data (object): requests response from oyunfor gb price page

    Returns:
        list: returns list which contains two seperate list 
        oyunforalis:list = buy price list which contains scraped float variables.
        oyunforsatis:list = sell price list which contains scraped float variables..

        returns #* list [  [oyunforalis],[oyunforsatis]  ] 

    """

    oyunforalis = []
    oyunforsatis = []
    raw_txt_oyunfor = oyunfor_request_data.find_all(
        class_="button desktop sellToUsBtn")

    for i in raw_txt_oyunfor:
        raw_txt_oyunfor_buy = i.text
        raw_txt_oyunfor_buy = raw_txt_oyunfor_buy.replace("Bize Sat ", "").replace(
            "TL", "").replace("\n", "")

        if len(oyunforalis) < 9:
            oyunforalis.append(float(raw_txt_oyunfor_buy) * 10)
        else:
            break

    for i in oyunfor_request_data.find_all(class_="flex-row mobile"):
        try:
            raw_txt_oyunfor_sell = i.text
            raw_txt_oyunfor_sell = raw_txt_oyunfor_sell.replace(
            " ", "").replace("TL", "").replace("\n", "")

            if len(oyunforsatis) < 9:
                oyunforsatis.append(float(raw_txt_oyunfor_sell) * 10)
            else:
                break
        except: #* For eliminating unconvertable strings.
            pass
    print("Oyunfor Success.", oyunforalis, oyunforsatis)
    return [oyunforalis, oyunforsatis]



def c_yyg():
    """
    This functions creates its own response due to technical conditions, then arranges it so that we only get price information.
    
    No Args
    
    Returns:
        list: returns list which contains two seperate list 
        yygalis = buy price list which contains scraped float variables.
        yygsatis = buy price list which contains scraped float variables..

        returns #* list [  [yygalis],[yygsatis]  ] 

    """
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'}
    yygalis = []
    yygsatis = []
    while not yygalis:        

        yyg = requests.get(
            "https://www.yesilyurtgame.com/oyun-parasi/knight-online-goldbar-gb", timeout=5, headers=header
        )
        yygsoup = BeautifulSoup(yyg.content, "lxml")

        for i in yygsoup.find_all("section"):
            try:
                raw_txt_yyg_data = i.text

                raw_txt_yyg_buy = re.findall(r"GB Alış Fiyatı :([^TL]+)", raw_txt_yyg_data)
                raw_txt_yyg_sell = re.findall(r"Satış Fiyatı :([^TL]+)", raw_txt_yyg_data)

                raw_txt_yyg_buy = "".join(raw_txt_yyg_buy)
                raw_txt_yyg_sell = "".join(raw_txt_yyg_sell)

                raw_txt_yyg_buy.strip(" \n")
                raw_txt_yyg_sell.strip(" \n")
                
                if(len(yygalis) < 9):
                    yygalis.append(float(raw_txt_yyg_buy)*10)
                    yygsatis.append(float(raw_txt_yyg_sell)*10)
                else:
                    break

            except Exception as e:
                print("Yyg_err", e)
                
    print("YYG Success.", yygalis, yygsatis)
    return [yygalis, yygsatis]



def c_bynogame(bynogame_request_data):
    
    """
    This functions simply takes the response from requests function, arranges it so that we only get price information.
    
    Args:
        bynogame_request_data (object): requests response from oyunfor gb price pag
    
    Returns:
        list: returns list which contains two seperate list 
        bynogamealis = buy price list which contains scraped float variables.
        bynogamesatis = buy price list which contains scraped float variables..

        returns #* list [  [bynogamesatis],[bynogamealis]  ] 

    """
    
    bynogamealis = []
    bynogamesatis = []
    raw_txt_bynogame = bynogame_request_data.find(
        class_="col-xl-18 col-lg-24 col-md-24 order-1 order-sm-12")

    try:
        for i in raw_txt_bynogame.find_all(class_="col"):
            raw_txt_bynogame_buy = i.text
            raw_txt_bynogame_buy = raw_txt_bynogame_buy.replace('TL', "").replace('\n', "").replace(',', ".")

            if len(bynogamealis) < 9:
                bynogamealis.append(float(raw_txt_bynogame_buy))

        for i in raw_txt_bynogame.find_all(class_="btn btn-block px-4 py-3 font-weight-bolder btn-outline-bng-black p-2"):

            raw_txt_bynogame_sell = i.text
            raw_txt_bynogame_sell = raw_txt_bynogame_sell.replace("TL'den BİZE SAT", "").replace(
                '\n', "").replace(',', ".")

            if len(bynogamesatis) < 9:
                bynogamesatis.append(float(raw_txt_bynogame_sell))
        print("BynoGame Success", bynogamealis, bynogamesatis)
        return [bynogamesatis, bynogamealis]
    except Exception as e:
        print("Bynogame_err", e)



def c_kopazar(kopazar_request_data):
    
    """
    This functions simply takes the response from requests function, arranges it so that we only get price information.
    
    Args:
        kopazar_request_data (object): requests response from oyunfor gb price pag
    
    Returns:
        list: returns list which contains two seperate list 
        kopazaralis = buy price list which contains scraped float variables.
        kopazarsatis = buy price list which contains scraped float variables.

        returns #* list [  [kopazaralis],[kopazarsatis]  ] 

    """
    kopazaralis = []
    kopazarsatis = []

    
    try:
        for raw_txt_kopazar_buy in kopazar_request_data.find_all(class_="caret-up"):
            raw_txt_kopazar_buy = raw_txt_kopazar_buy.string
            raw_txt_kopazar_buy = raw_txt_kopazar_buy.replace(" ", "").replace("₺", "")

            raw_txt_kopazar_buy = float(raw_txt_kopazar_buy)
            if len(kopazaralis) < 9:
                kopazaralis.append(raw_txt_kopazar_buy * 10)

    except Exception as e:

        print("raw_txt_kopazar_buy:", e)   
    

    
    try:
        for raw_txt_kopazar_sell in kopazar_request_data.find_all(
            class_="col-xl-3 col-lg-6 col-sm-3 col-6 order-xl-3 order-lg-2 order-sm-3 order-2 xl-text-right text-center"
        ):

            #! String Değiştirme
            raw_txt_kopazar_sell = raw_txt_kopazar_sell.text
            raw_txt_kopazar_sell = raw_txt_kopazar_sell.replace("Satış Fiyatı", "").replace(
                "\n", "").replace(" ", "").replace("₺", "")


            raw_txt_kopazar_sell = float(raw_txt_kopazar_sell)
            if len(kopazarsatis) < 9:
                kopazarsatis.append(raw_txt_kopazar_sell * 10)

    except Exception as e:
        print("raw_txt_kopazar_sell:", e)
        
    print("Kopazar Success.", kopazaralis, kopazarsatis)
    return [kopazaralis, kopazarsatis]



def c_klasgame(klasgame_request_data):
    """
    This functions simply takes the response from requests function, arranges it so that we only get price information.
    
    Args:
        bynogame_request_data (object): requests response from oyunfor gb price pag
    
    Returns:
        list: returns list which contains two seperate list 
        klasgamealis = buy price list which contains scraped float variables.
        klasgamesatis = buy price list which contains scraped float variables..

        returns #* list [  [klasgamealis],[klasgamesatis]  ] 

    """
    klasgamealis = []
    klasgamesatis = []    
    try:
        raw_txt_klasgame_data = klasgame_request_data.find(
            class_="goldbar-table table table-borderless product-table-item"
        )
        v = 2
        for i in raw_txt_klasgame_data.find_all(class_="font-weight-bold price"):
            
            raw_txt_klasgame_buy_sell_data = i.find("span").text
            raw_txt_klasgame_buy_sell_data = raw_txt_klasgame_buy_sell_data.replace(",", ".")
            
            raw_txt_klasgame_buy_sell_data = float(raw_txt_klasgame_buy_sell_data)
            
            if len(klasgamealis) <= 9 and len(klasgamesatis) < 9:
                if v % 2 == 0: #* Buy Data Block
                    klasgamealis.append(raw_txt_klasgame_buy_sell_data*10)
                    v += 1
                elif v % 2 != 0: #* Sell Data Block
                    klasgamesatis.append(raw_txt_klasgame_buy_sell_data*10)
                    v += 1
            else:
                break
    except Exception as e:

        print("klsgame_err", e)
        # klasgamealis = [0 for i in range(9)]
        # klasgamesatis = [0 for i in range(9)]
    print("Klasgame Sucsess",klasgamealis,klasgamesatis)
    return [klasgamealis, klasgamesatis]


async def job():
    
    urls = ["https://www.bynogame.com/tr/oyunlar/knight-online/gold-bar",
            "https://www.oyunfor.com/knight-online/gb-gold-bar",
            "https://www.kopazar.com/knight-online-gold-bar",
            "https://www.klasgame.com/goldbar/knightonline/knight-online-gb-goldbar-premium-cash",
            ]
    rs = (grequests.get(u) for u in urls)

    x = grequests.map(rs)
    soup = BeautifulSoup(x[0].content, "lxml")
    oynfor = BeautifulSoup(x[1].content, "lxml")
    kopzr = BeautifulSoup(x[2].content, "lxml")
    klsgame = BeautifulSoup(x[3].content, "lxml")
    
    def control(liste=None):
        """Checks if list is empty or checks length of list[0] and list[1] equal.
            
            
            returns the same list if there is no error. 
            if there is, returns liste filled with err.
             
            
            
        Args:
            liste (list):  Defaults to None.
        """
        
        def listpr():
            err_list = [[], []]
            err_list[0] = ['err' for i in range(9)]
            err_list[1] = ['err' for i in range(9)]
            return err_list
            
        if not liste or not liste[0] or not liste[1]:
            return listpr()
        elif (len(liste[0]) < 9 or (len(liste[0]) != len(liste[1]))):        
            return listpr()
        else:
            return liste
          
        
    try:
        yyg_data = c_yyg()
        yyg_data=control(yyg_data)
        
    except:
        yyg_data=control()
        
        
    try:
        bynogame_data = c_bynogame(soup)
        bynogame_data=control(bynogame_data)
    except:
        bynogame_data=control()
    
    
    try:
        kopazar_data = c_kopazar(kopzr)
        kopazar_data=control(kopazar_data)
    except:
        kopazar_data=control()
        
        
    try:
        klasgame_data = c_klasgame(klsgame)
        klasgame_data=control(klasgame_data)
        
    except:
        klasgame_data=control()
    try:
        oyunfor_data = c_oyunfor(oynfor)
        oyunfor_data = control(oyunfor_data)
    except:        
        oyunfor_data = control()

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
