import requests
import os

def main():
    os.system("clear")
    print("""\033[1;32m 
    
    
        ｙＨａｐｅｒ - ＩＰ                           


""")

    ip_input = input("\033[1;32m IP \033[m\033[0;37m ==> \033[m ")

    request = requests.get('http://ip-api.com/json/{}'.format(ip_input))

    address_data = request.json()

    if 'erro' not in address_data:
        print()
        print('\033[1;32m>\033[1;37m>\033[1;32m> \033[1;37mＩＰ   ｅｎｃｏｎｔｒａｄｏ \033[1;32m<\033[1;37m<\033[1;32m<')
        print()
        print('\033[1;36mSTATUS: {}'.format(address_data['status']))
        print('\033[1;36mPAIS: {}'.format(address_data['country']))
        print('\033[1;36mPAIS SIGLA: {}'.format(address_data['countryCode']))
        print('\033[1;36mESTADO: {}'.format(address_data['regionName']))
        print('\033[1;36mESTADO SIGLA: {}'.format(address_data['region']))
        print('\033[1;36mCIDADE: {}'.format(address_data['city']))
        print('\033[1;36mZIP: {}'.format(address_data['zip']))
        print('\033[1;36mLATITUDE: {}'.format(address_data['lat']))
        print('\033[1;36mLONGITUDE: {}'.format(address_data['lon']))
        print('\033[1;36mTIMEZONE: {}'.format(address_data['timezone']))
        print('\033[1;36mISP: {}'.format(address_data['isp']))
        print('\033[1;36mORG: {}'.format(address_data['org']))
        print('\033[1;36mAS: {}'.format(address_data['as']))
        print('\033[1;36mIP: {}'.format(address_data['query']))
        print()
    
    opt = input('\033[1;37mDeseja realizar uma nova busca? \033[1;32ms\033[1;37m/\033[1;32mn\033[1;37m:\033[1;36m ')
    if opt == 's':
        main()

    if opt == 'S':
        main()

    if opt == 'n':
        print("\033[1;32mAté mais seu burro")
    
    if opt == 'N':
        print("\033[1;32mAté mais seu burro")

if __name__== '__main__':
    main()
