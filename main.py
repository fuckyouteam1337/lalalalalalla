import time
import requests as r
import json

list = 'FDUSD USDT USDC WNGC SNT DIA DAO' # ВПИСАТЬ КОЙН ДЛЯ ПРОПУСКА

url = 'https://api.telegram.org/bot6640569824:AAGze0uD_lv7920kTVVpsLwV0Qvb6p4LvZI/sendMessage?chat_id=-1001873297683&text='
# url = 'https://api.telegram.org/bot6640569824:AAGze0uD_lv7920kTVVpsLwV0Qvb6p4LvZI/sendMessage?chat_id=264752247&text='
next = 0
while next <= 99999999999999999:
    c = 0
    i = 0
    while i <= 999999:
        c += 1
        print('Круг: ' + str(c))
        bybit = r.get("https://api.bybit.com/spot/api/lending/v1/token/list")
        binance = r.get("https://www.binance.com/bapi/earn/v2/friendly/finance-earn/homepage/product/guaranteed?searchType=POPULAR&orderBy=APY_DESC&pageSize=100&pageIndex=1")
        gate = r.get("https://www.gate.io/apiweb/v1/lend-earn/market-list?limit=476&have_balance=0&have_award=0&is_subscribed=0&sort_type=3&page=1")

        bybit_data_get = bybit.text
        bybit_data_read = bybit_data_get
        bybit_data = json.loads(bybit_data_read)

        binance_data_get = binance.text
        binance_data_read = binance_data_get
        binance_data = json.loads(binance_data_read)

        gate_data_get = gate.text
        gate_data_read = gate_data_get
        gate_data = json.loads(gate_data_read)

        eBinanceAPR = (binance_data['data']['list'][0]['depositAsset'])
        eBinanceAPR1 = (binance_data['data']['list'][1]['depositAsset'])
        eBinanceAPR2 = (binance_data['data']['list'][2]['depositAsset'])

        eBybitAPR = (bybit_data['result'][0]['token'])
        eBybitAPR1 = (bybit_data['result'][1]['token'])
        eBybitAPR2 = (bybit_data['result'][2]['token'])

        eGateAPR = (gate_data['data']['list'][1]['asset'])
        eGateAPR1 = (gate_data['data']['list'][2]['asset'])
        eGateAPR2 = (gate_data['data']['list'][3]['asset'])
        eGateAPR3 = (gate_data['data']['list'][4]['asset'])
        eGateAPR4 = (gate_data['data']['list'][5]['asset'])
        eGateAPR5 = (gate_data['data']['list'][6]['asset'])

        aBinanceAPR = eBinanceAPR
        aBinanceAPR1 = eBinanceAPR1
        aBinanceAPR2 = eBinanceAPR2

        aBybitAPR = eBybitAPR
        aBybitAPR1 = eBybitAPR1
        aBybitAPR2 = eBybitAPR2

        aGateAPR = eGateAPR
        aGateAPR1 = eGateAPR1
        aGateAPR2 = eGateAPR2
        aGateAPR3 = eGateAPR3
        aGateAPR4 = eGateAPR4
        aGateAPR5 = eGateAPR5

        nd = 3
        aBB_n = float(binance_data['data']['list'][0]['apr'])
        aBB_n = float(aBB_n) * 100 + nd
        aBB_n = round(aBB_n)
        aBB_n = str(aBB_n)

        aBB_n1 = float(binance_data['data']['list'][1]['apr'])
        aBB_n1 = float(aBB_n1) * 100 + nd
        aBB_n1 = round(aBB_n1)
        aBB_n1 = str(aBB_n1)

        aBB_n2 = float(binance_data['data']['list'][2]['apr'])
        aBB_n2 = float(aBB_n2) * 100 + nd
        aBB_n2 = round(aBB_n2)
        aBB_n2 = str(aBB_n2)

        # ///////////////////////////////////////////////////////////////////////////////
        aBB_r = float(bybit_data['result'][0]['apy']) * 100 + nd
        aBB_r = round(aBB_r)
        aBB_r = str(aBB_r)

        aBB_r1 = float(bybit_data['result'][1]['apy']) * 100 + nd
        aBB_r1 = round(aBB_r1)
        aBB_r1 = str(aBB_r1)

        aBB_r2 = float(bybit_data['result'][2]['apy']) * 100 + nd
        aBB_r2 = round(aBB_r2)
        aBB_r2 = str(aBB_r2)
        # ///////////////////////////////////////////////////////////////////////////////
        aG_r = float(gate_data['data']['list'][1]['cryptoLoan_rate_year']) * 100 + nd
        aG_r = round(aG_r)
        aG_r = str(aG_r)

        aG_r1 = float(gate_data['data']['list'][2]['cryptoLoan_rate_year']) * 100 + nd
        aG_r1 = round(aG_r1)
        aG_r1 = str(aG_r1)

        aG_r2 = float(gate_data['data']['list'][3]['cryptoLoan_rate_year']) * 100 + nd
        aG_r2 = round(aG_r2)
        aG_r2 = str(aG_r2)

        aG_r3 = float(gate_data['data']['list'][4]['cryptoLoan_rate_year']) * 100 + nd
        aG_r3 = round(aG_r3)
        aG_r3 = str(aG_r3)

        aG_r4 = float(gate_data['data']['list'][5]['cryptoLoan_rate_year']) * 100 + nd
        aG_r4 = round(aG_r4)
        aG_r4 = str(aG_r4)

        aG_r5 = float(gate_data['data']['list'][6]['cryptoLoan_rate_year']) * 100 + nd
        aG_r5 = round(aG_r5)
        aG_r5 = str(aG_r5)

        # ///////////////////////////////////////////////////////////////////////////////
        no_actual = aBinanceAPR + ' ' + aBinanceAPR1 + ' ' + aBinanceAPR2 + ' ' + aBybitAPR + ' ' + aBybitAPR1 + ' ' + aBybitAPR2 + ' ' + aGateAPR + ' ' + aGateAPR1 + ' ' + aGateAPR2 + ' ' + aGateAPR3 + ' ' + aGateAPR4 + ' ' + aGateAPR5
  
        print('список: ' + no_actual)
        cc = 1
        x = 0
        while x <= 10:

            bybit = r.get("https://api.bybit.com/spot/api/lending/v1/token/list")
            binance = r.get("https://www.binance.com/bapi/earn/v2/friendly/finance-earn/homepage/product/guaranteed?searchType=POPULAR&orderBy=APY_DESC&pageSize=100&pageIndex=1")
            gate = r.get("https://www.gate.io/apiweb/v1/lend-earn/market-list?limit=476&have_balance=0&have_award=0&is_subscribed=0&sort_type=3&page=1")

            bybit_data_get = bybit.text
            bybit_data_read = bybit_data_get
            bybit_data = json.loads(bybit_data_read)

            binance_data_get = binance.text
            binance_data_read = binance_data_get
            binance_data = json.loads(binance_data_read)

            gate_data_get = gate.text
            gate_data_read = gate_data_get
            gate_data = json.loads(gate_data_read)

            BB_n = float(binance_data['data']['list'][0]['apr'])
            BB_n = float(BB_n) * 100 + nd
            BB_n = round(BB_n)
            BB_n = str(BB_n)

            BB_n1 = float(binance_data['data']['list'][1]['apr'])
            BB_n1 = float(BB_n1) * 100 + nd
            BB_n1 = round(BB_n1)
            BB_n1 = str(BB_n1)

            BB_n2 = float(binance_data['data']['list'][2]['apr'])
            BB_n2 = float(BB_n2) * 100 + nd
            BB_n2 = round(BB_n2)
            BB_n2 = str(BB_n2)

            BB_r = float(bybit_data['result'][0]['apy']) * 100 + nd
            BB_r = round(BB_r)
            BB_r = str(BB_r)

            BB_r1 = float(bybit_data['result'][1]['apy']) * 100 + nd
            BB_r1 = round(BB_r1)
            BB_r1 = str(BB_r1)

            BB_r2 = float(bybit_data['result'][2]['apy']) * 100 + nd
            BB_r2 = round(BB_r2)
            BB_r2 = str(BB_r2)

            G_r = float(gate_data['data']['list'][1]['cryptoLoan_rate_year']) * 100 + nd
            G_r = round(G_r)
            G_r = str(G_r)

            G_r1 = float(gate_data['data']['list'][2]['cryptoLoan_rate_year']) * 100 + nd
            G_r1 = round(G_r1)
            G_r1 = str(G_r1)

            G_r2 = float(gate_data['data']['list'][3]['cryptoLoan_rate_year']) * 100 + nd
            G_r2 = round(G_r2)
            G_r2 = str(G_r2)

            G_r3 = float(gate_data['data']['list'][4]['cryptoLoan_rate_year']) * 100 + nd
            G_r3 = round(G_r3)
            G_r3 = str(G_r3)

            G_r4 = float(gate_data['data']['list'][5]['cryptoLoan_rate_year']) * 100 + nd
            G_r4 = round(G_r4)
            G_r4 = str(G_r4)

            G_r5 = float(gate_data['data']['list'][6]['cryptoLoan_rate_year']) * 100 + nd
            G_r5 = round(G_r5)
            G_r5 = str(G_r5)

            B = (binance_data['data']['list'][0]['depositAsset'])
            B1 = (binance_data['data']['list'][1]['depositAsset'])
            B2 = (binance_data['data']['list'][2]['depositAsset'])

            BB = (bybit_data['result'][0]['token'])
            BB1 = (bybit_data['result'][1]['token'])
            BB2 = (bybit_data['result'][2]['token'])

            G = (gate_data['data']['list'][1]['asset'])
            G1 = (gate_data['data']['list'][2]['asset'])
            G2 = (gate_data['data']['list'][3]['asset'])
            G3 = (gate_data['data']['list'][4]['asset'])
            G4 = (gate_data['data']['list'][5]['asset'])
            G5 = (gate_data['data']['list'][6]['asset'])
            G6 = (gate_data['data']['list'][7]['asset'])

            all_coin = (B + ' ' + B1 + ' ' + B2 + ' ' + BB + ' ' + BB1 + ' ' + BB2 + ' ' + G + ' ' + G1 + ' ' + G2 + ' ' + G3 + ' ' + G4 + ' ' + G5)

            B = (binance_data['data']['list'][0]['depositAsset']) + ' ' + BB_n + '%'
            B1 = (binance_data['data']['list'][1]['depositAsset']) + ' ' + BB_n1 + '%'
            B2 = (binance_data['data']['list'][2]['depositAsset']) + ' ' + BB_n2 + '%'

            BB = (bybit_data['result'][0]['token']) + ' ' + BB_r + '%'
            BB1 = (bybit_data['result'][1]['token']) + ' ' + BB_r1 + '%'
            BB2 = (bybit_data['result'][2]['token']) + ' ' + BB_r2 + '%'

            G = (gate_data['data']['list'][1]['asset']) + ' ' + G_r + '%'
            G1 = (gate_data['data']['list'][2]['asset']) + ' ' + G_r1 + '%'
            G2 = (gate_data['data']['list'][3]['asset']) + ' ' + G_r2 + '%'
            G3 = (gate_data['data']['list'][4]['asset']) + ' ' + G_r3 + '%'
            G4 = (gate_data['data']['list'][5]['asset']) + ' ' + G_r4 + '%'
            G5 = (gate_data['data']['list'][6]['asset']) + ' ' + G_r5 + '%'

            cc += 1

            if cc == 6:
                print('1 = ' + no_actual)
                print('2 = ' + all_coin)
                cc += 1

            BinanceAPR = (binance_data['data']['list'][0]['depositAsset'])
            BinanceAPR1 = (binance_data['data']['list'][1]['depositAsset'])
            BinanceAPR2 = (binance_data['data']['list'][2]['depositAsset'])

            BybitAPR = (bybit_data['result'][0]['token'])
            BybitAPR1 = (bybit_data['result'][1]['token'])
            BybitAPR2 = (bybit_data['result'][2]['token'])

            GateAPR = (gate_data['data']['list'][1]['asset'])
            GateAPR1 = (gate_data['data']['list'][2]['asset'])
            GateAPR2 = (gate_data['data']['list'][3]['asset'])
            GateAPR3 = (gate_data['data']['list'][4]['asset'])
            GateAPR4 = (gate_data['data']['list'][5]['asset'])
            GateAPR5 = (gate_data['data']['list'][6]['asset'])

            aBinanceAPR = eBinanceAPR
            aBinanceAPR1 = eBinanceAPR1
            aBinanceAPR2 = eBinanceAPR2

            aBybitAPR = eBybitAPR
            aBybitAPR1 = eBybitAPR1
            aBybitAPR2 = eBybitAPR2

            aGateAPR = eGateAPR
            aGateAPR1 = eGateAPR1
            aGateAPR2 = eGateAPR2
            aGateAPR3 = eGateAPR3
            aGateAPR4 = eGateAPR4
            aGateAPR5 = eGateAPR5

            update_perc1 = ' > '
            update_perc = ' < '

            if str(aBinanceAPR) != str(BinanceAPR):
                if str(BinanceAPR) not in list:
                    if float(aBB_n) > float(BB_n):
                        str(aBB_n)
                        send = r.get(url + '🔴 ' + B + ' ' + update_perc + aBB_n + '%')
                        x = 20
                    else:
                        str(aBB_n)
                        send = r.get(url + '🟢 ' + B + ' ' + update_perc1 + aBB_n + '%')
                        x = 20
                else:
                    x = 20
            else:
                e = 1

            if str(aBinanceAPR1) != str(BinanceAPR1):
                if str(BinanceAPR1) not in list:
                    if float(aBB_n1) > float(BB_n1):
                        str(aBB_n1)
                        send = r.get(url + '🔴 ' + B1 + ' ' + update_perc + aBB_n1 + '%')
                        x = 20
                    else:
                        str(aBB_n1)
                        send = r.get(url + '🟢 ' + B1 + ' ' + update_perc1 + aBB_n1 + '%')
                        x = 20
                else:
                    x = 20
            else:
                e = 1

            if str(aBinanceAPR2) != str(BinanceAPR2):
                if str(BinanceAPR2) not in list:
                    if float(aBB_n2) > float(BB_n2):
                        str(aBB_n2)
                        send = r.get(url + '🔴 ' + B2 + ' ' + update_perc + aBB_n2 + '%')
                        x = 20
                    else:
                        str(aBB_n2)
                        send = r.get(url + '🟢 ' + B2 + ' ' + update_perc1 + aBB_n2 + '%')
                        x = 20
                else:
                    x = 20
            else:
                e = 1

            if str(aBybitAPR) != str(BybitAPR):
                if str(BybitAPR) not in list:
                    if float(aBB_r) > float(BB_r):
                        str(aBB_r)
                        send = r.get(url + '🔴 ' + BB + ' ' + update_perc + aBB_r + '%')
                        x = 20
                    else:
                        str(aBB_r)
                        send = r.get(url + '🟢 ' + BB + ' ' + update_perc1 + aBB_r + '%')
                        x = 20
                else:
                    x = 20
            else:
                e = 1

            if str(aBybitAPR1) != str(BybitAPR1):
                if str(BybitAPR1) not in list:
                    if float(aBB_r1) > float(BB_r1):
                        str(aBB_r1), str(BB_n)
                        send = r.get(url + '🔴 ' + BB1 + ' ' + update_perc + aBB_r1 + '%')
                        x = 20
                    else:
                        str(aBB_r1), str(BB_n)
                        send = r.get(url + '🟢 ' + BB1 + ' ' + update_perc1 + aBB_r1 + '%')
                        x = 20
                else:
                    x = 20
            else:
                e = 1

            if str(aBybitAPR2) != str(BybitAPR2):
                if str(BybitAPR2) not in list:
                    if float(aBB_r2) > float(BB_r2):
                        str(aBB_r2)
                        send = r.get(url + '🔴 ' + BB2 + ' ' + update_perc + aBB_r2 + '%')
                        x = 20
                    else:
                        str(aBB_r2)
                        send = r.get(url + '🟢 ' + BB2 + ' ' + update_perc1 + aBB_r2 + '%')
                        x = 20
                else:
                    x = 20
            else:
                e = 1

            if str(aGateAPR) != str(GateAPR):
                if str(GateAPR) not in list:
                    if float(aG_r) > float(G_r):
                        str(aG_r)
                        send = r.get(url + '🔴 ' + G + ' ' + update_perc + aG_r + '%')
                        x = 20
                    else:
                        str(aG_r)
                        send = r.get(url + '🟢 ' + G + ' ' + update_perc1 + aG_r + '%')
                        x = 20
                else:
                    x = 20
            else:
                e = 1

            if str(aGateAPR1) != str(GateAPR1):
                if str(GateAPR1) not in list:
                    if float(aG_r1) > float(G_r1):
                        str(aG_r1)
                        send = r.get(url + '🔴 ' + G1 + ' ' + update_perc + aG_r1 + '%')
                        x = 20
                    else:
                        str(aG_r1)
                        send = r.get(url + '🟢 ' + G1 + ' ' + update_perc1 + aG_r1 + '%')
                        x = 20
                else:
                    x = 20
            else:
                e = 1

            if str(aGateAPR2) != str(GateAPR2):
                if str(GateAPR2) not in list:
                    if float(aG_r2) > float(G_r2):
                        str(aG_r2)
                        send = r.get(url + '🔴 ' + G2 + ' ' + update_perc + aG_r2 + '%')
                        x = 20
                    else:
                        str(aG_r2)
                        send = r.get(url + '🟢 ' + G2 + ' ' + update_perc1 + aG_r2 + '%')
                        x = 20
                else:
                    x = 20
            else:
                e = 1

            if str(aGateAPR3) != str(GateAPR3):
                if str(GateAPR3) not in list:
                    if float(aG_r3) > float(G_r3):
                        str(aG_r3)
                        send = r.get(url + '🔴 ' + G3 + ' ' + update_perc + aG_r3 + '%')
                        x = 20
                    else:
                        str(aG_r3)
                        send = r.get(url + '🟢 ' + G3 + ' ' + update_perc1 + aG_r3 + '%')
                        x = 20
                else:
                    x = 20
            else:
                e = 1

            if str(aGateAPR4) != str(GateAPR4):
                if str(GateAPR4) not in list:
                    if float(aG_r4) > float(G_r4):
                        str(aG_r4)
                        send = r.get(url + '🔴 ' + G4 + ' ' + update_perc + aG_r4 + '%')
                        x = 20
                    else:
                        str(aG_r4)
                        send = r.get(url + '🟢 ' + G4 + ' ' + update_perc1 + aG_r4 + '%')
                        x = 20
                else:
                    x = 20
            else:
                e = 1

            if str(aGateAPR5) != str(GateAPR5):
                if str(GateAPR5) not in list:
                    if float(aG_r5) > float(G_r5):
                        str(aG_r5)
                        send = r.get(url + '🔴 ' + G5 + ' ' + update_perc + aG_r5 + '%')
                        x = 20
                    else:
                        str(aG_r5)
                        send = r.get(url + '🟢 ' + G5 + ' ' + update_perc1 + aG_r5 + '%')
                        x = 20
                else:
                    x = 20
            else:
                e = 1

            print('search ' + str(x))
            x += 1
            time.sleep(3)
    time.sleep(1)
    i += 1
next += 1


