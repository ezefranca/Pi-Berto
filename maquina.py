import serial
from threading import Thread
import facebook

last_received = ''

# Pegar o token quando o eze entra
# token caso de merda - EAAWajIcUJAgBAKvLmCTxEEWd51gudNRwwwZC1md8nlttxrznK5knCidraWgIyibA2v3TRLSHYdJy8BKtGpuEoFZAI5E2SRTQS8C83HXZC5WhBmnBqDzZBO4HwdTzniTryvcqX47TfxxjoCbezCqloh4uRTfArNdTouNhVXv1zwZDZD
graph = facebook.GraphAPI(access_token='EAACEdEose0cBAO7q9BKxPCBqWFrlQLZBEFr6coz0hQZCOZCLEeSo7DRX4fvIDTmmUFuvZCoofVkTgTpUjguNHTCMFOa0lF4iJjUfZChSyQzTXwS6ZAh5R5NVZAfyPQhLbBfyGeckMemUaph4XsfPOSZAiKqjNKqSThC5KTFJ79hCiwZDZD', version='2.2')

# Esse da pra postar 
graph.put_object(parent_object='me', connection_name='feed',
                 message='Muito legal!', place='298042960354301')

# Checkin produto
# graph.put_object(parent_object='me', connection_name='feed',
#                  message='Humberto acaba de fazer uma compra na @AppleUS', place='298042960354301')


#graph.put_object(parent_object='me', connection_name='/137522203306294/ratings',
#                 message='Humberto acaba de fazer uma compra na @AppleUS', place='298042960354301')




ser = serial.Serial(port='/dev/ttyACM1', baudrate=115200)

def recieving():
    while True:
        print('legal')
        print(ser.readline())
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
