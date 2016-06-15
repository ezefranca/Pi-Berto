import serial
from threading import Thread
import facebook
from random import *

import requests

def get_fb_token(app_id, app_secret):           
    payload = {'grant_type': 'client_credentials', 'scope':'public_profile, user_friends, user_posts, publish_actions, user_tagged_places', 'client_id': app_id, 'client_secret': app_secret}
    file = requests.post('https://graph.facebook.com/oauth/access_token?', params = payload)
    #print file.text #to test what the FB api responded with    
    result = file.text.split("=")[1]
    #print file.text #to test the TOKEN
    return result

last_received = ''

# Pegar o token quando o eze entra
# token caso de merda - EAAWajIcUJAgBAKvLmCTxEEWd51gudNRwwwZC1md8nlttxrznK5knCidraWgIyibA2v3TRLSHYdJy8BKtGpuEoFZAI5E2SRTQS8C83HXZC5WhBmnBqDzZBO4HwdTzniTryvcqX47TfxxjoCbezCqloh4uRTfArNdTouNhVXv1zwZDZD
toke =  get_fb_token('1577303235896328','e46e9a642fc009965e2afb085617ccaa')
# 'EAACEdEose0cBAHP3JmtXBaOQlLeMXTWbwnyLeQYkZCZANhw5KYG90DYOOZC4ZCHUpxy93KUGZB7FjZCIvZB4k1zabXZBA0uvxGyxqVFM3XHmEpAJ5QwRSPC78fUzk3bZCQEOQZBZBxWEWws0q9PKK0s5zlDYxvYr1ViiMBTl88wn6IUBQZDZD'
graph =  facebook.GraphAPI(access_token=toke, version='2.2')

print("PASSOU")


# Checkin produto
# graph.put_object(parent_object='me', connection_name='feed',
#                  message='Humberto acaba de fazer uma compra na @AppleUS', place='298042960354301')


#graph.put_object(parent_object='me', connection_name='/137522203306294/ratings',
#                 message='Humberto acaba de fazer uma compra na @AppleUS', place='


ser = serial.Serial(port='/dev/ttyACM0', baudrate=115200)

def recieving():
    while True:
        retorno = ser.readline()
        # Esse da pra postar 

        if retorno == b'checkin\r\n':
            graph.put_object(parent_object='me', connection_name='feed', message='Postado via Raspberry Pi usando Python'  + str(randint(1, 5000)) , place='298042960354301')

            print('entrou')
            print(retorno)
            
        elif retorno == b'share\r\n':
            graph.put_object(parent_object='me', connection_name='feed', message='Humberto acaba de fazer uma compra na @AppleUS', place='298042960354301')


            print('entrou1')
            print(retorno)
        


        
        # ser.write(b'')
    ser.close()

Thread(target=recieving, args=()).start()



'''
def receiving(ser):
    global last_received
    buffer = ''

    while True:
        # last_received = ser.readline()
        buffer += ser.read(ser.inWaiting())
        if '\n' in buffer:
            last_received, buffer = buffer.split('\n')[-2:]

if __name__ ==  '__main__':
    ser = Serial(
        port='COM1',
        baudrate=115200,
        bytesize=EIGHTBITS,
        parity=PARITY_NONE,
        stopbits=STOPBITS_ONE,
        timeout=0.1,
        xonxoff=0,
        rtscts=0,
        interCharTimeout=None
    )

    Thread(target=receiving, args=(ser,)).start()
'''
