import requests
import time

headers = {
    "Authorization": input('Enter Discord Token: '),
    "X-Super-Properties": "eyJjbGllbnRfYnVpbGRfbnVtYmVyIjoyODAzNDZ9",
}

while True:
    try:
        item = requests.request(method="POST", headers=headers, url="https://discord.com/api/v9/users/@me/lootboxes/open").json()['opened_item']
        print(f"Opened a {'Right Up Down Right Up Down!' if item=='1214340999644446724' else 'Wump Shell!' if item=='1214340999644446722' else 'Power Helmet!' if item=='1214340999644446725' else 'Buster Blade!' if item=='1214340999644446720' else 'Speed Boost!' if item=='1214340999644446723' else 'Cute Plushie!' if item=='1214340999644446721' else 'Quack!!!' if item=='1214340999644446726' else 'Dream Hammer!' if item=='1214340999644446728' else 'OHHHHHH BANANA!' if item=='1214340999644446727' else 'Unknown'}") 
        time.sleep(5)
    except:
        print("An error has occurred. This is likely due to your Discord Token being invalid. Please restart the application and verify that your token is correct.")
        time.sleep(15)
        break