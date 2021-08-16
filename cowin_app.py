import requests
import json
import hashlib
from configparser import ConfigParser


class Cowin():
    def __init__(self):
        self.txnId = ''

    def get_config(self,section,option):
        config = ConfigParser()
        config.read('cowin_config')
        return config.get(section=section, option=option)

    #Generate otp to verify your mobile number
    def gen_otp(self):
        url = f"{self.get_config(section='Co-win_Portal', option='base_url')}{self.get_config(section='Co-win_Portal', option='gen_otp')}"
        data = json.dumps({
            "mobile": input("enter your mobile no.:")
        })
        headers = {
            'Content-Type': 'application/json',
            'User-Agent': 'PostmanRuntime/7.28.0'
        }
        response = requests.post(url, headers=headers, data=data)
        var = response.json()
        print(var)
        txnId = response.json()
        self.txnId = txnId["txnId"]
    #Confirms the otp to complete the Authentication
    def con_otp(self):
        url = f"{self.get_config(section='Co-win_Portal', option='base_url')}{self.get_config(section='Co-win_Portal', option='con_otp')}"
        otp = input("enter the otp sent to your mobile no.\n the otp is valid only for three minutes:")
        result = hashlib.sha256(otp.encode())
        res = (result.hexdigest())
        data2 = json.dumps({
            "otp": res,
            "txnId": self.txnId
        })
        headers = {
            'Content-Type': 'application/json',
            'User-Agent': 'PostmanRuntime/7.28.0'
        }
        response = requests.post(url, headers=headers, data=data2)
        # print(response.text)
        if response.status_code == 200:
            print("mobile no. verification is completed")
            self.main()
        else:
            print('your otp is not valid please provide valid otp')
    #retrieve the all states info with state id
    def get_states(self):
        url= f"{self.get_config(section='Co-win_Portal', option='base_url')}{self.get_config(section='Co-win_Portal', option='get_states')}"
        headers = {
            'Content-Type': 'application/json',
            'User-Agent': 'PostmanRuntime/7.28.0',
            'Accept-Language':'te_IN'
        }
        response = requests.get(url, headers=headers)
        if response.status_code==200:
            output = response.json()
            data=output['states']
            for i in data:
                print(i)
                print('\n')
        else:
            print(f'Error : Status Code : {response.status_code} | Reason : {response.reason}')
    #retrieve the all districts info with district id
    def get_districts(self):
        state_id=input('enter your state id:')
        url= f"{self.get_config(section='Co-win_Portal', option='base_url')}{self.get_config(section='Co-win_Portal', option='get_districts').replace('{state_id}', state_id)}"
        headers = {
            'Content-Type': 'application/json',
            'User-Agent': 'PostmanRuntime/7.28.0',
            'Accept-Language': 'te_IN'
        }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            data = response.json()
            output = data['districts']
            for i in output:
                print(i)
                print('\n')
        else:
            print(f'Error : Status Code : {response.status_code} | Reason : {response.reason}')
    #
    def by_pin(self):
        pin=input('enter your pin:')
        date=input('enter date:')
        url = f"{self.get_config(section='Co-win_Portal', option='base_url')}{self.get_config(section='Co-win_Portal', option='by_pin').replace('{pincode}', pin).replace('{date}', date)}"
        headers = {
            'Content-Type': 'application/json',
            'User-Agent': 'PostmanRuntime/7.28.0',
            'Accept-Language': 'te_IN'
        }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            data=response.json()
            output=data['sessions']
            for i in output:
                print(i)
                print('\n')
        else:
            print(f'Error : Status Code : {response.status_code} | Reason : {response.reason}')

    def by_district(self):
        district_id=input('enter your district id:')
        date=input('enter date:')
        url= f"{self.get_config(section='Co-win_Portal', option='base_url')}{self.get_config(section='Co-win_Portal', option='by_district').replace('{district_id}', district_id).replace('{date}', date)}"
        headers = {
            'Content-Type': 'application/json',
            'User-Agent': 'PostmanRuntime/7.28.0',
            'Accept-Language': 'te_IN'
        }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            data=response.json()
            output=data['sessions']
            for i in output:
                print(i)
                print('\n')
        else:
            print(f'Error : Status Code : {response.status_code} | Reason : {response.reason}')

    def by_latlong(self):
        lat = input('enter area lattitude:')
        long = input('enter area longitude')
        url= f"{self.get_config(section='Co-win_Portal', option='base_url')}{self.get_config(section='Co-win_Portal', option='by_latlong').replace('{lat}', lat).replace('{long}', long)}"
        headers = {
            'Content-Type': 'application/json',
            'User-Agent': 'PostmanRuntime/7.28.0',
            'Accept-Language': 'te_IN'
        }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            data=response.json()
            output=data['centers']
            for i in output:
                print(i)
                print('\n')
        else:
            print(f'Error : Status Code : {response.status_code} | Reason : {response.reason}')

    def calendarby_pin(self):
        pincode=input('enter your area pincode:')
        date=input('enter a date:')
        url= f"{self.get_config(section='Co-win_Portal', option='base_url')}{self.get_config(section='Co-win_Portal', option='calendarby_pin').replace('{pincode}', pincode).replace('{date}', date)}"
        headers = {
            'Content-Type': 'application/json',
            'User-Agent': 'PostmanRuntime/7.28.0',
            'Accept-Language': 'te_IN'
        }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            data = response.json()
            output = data['centers']
            for i in output:
                print(i)
                print('\n')
        else:
            print(f'Error : Status Code : {response.status_code} | Reason : {response.reason}')

    def calendarby_district(self):
        district_id=input('enter your district id:')
        date=input('enter date:')
        url= f"{self.get_config(section='Co-win_Portal', option='base_url')}{self.get_config(section='Co-win_Portal', option='calendarby_district').replace('{id}', district_id).replace('{date}', date)}"
        headers = {
            'Content-Type': 'application/json',
            'User-Agent': 'PostmanRuntime/7.28.0',
            'Accept-Language': 'te_IN'
        }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            data = response.json()
            output = data["centers"]
            for i in output:
                print(i)
                print('\n')
        else:
            print(f'Error : Status Code : {response.status_code} | Reason : {response.reason}')

    def calendarby_center(self):
        center_id=input('enter center id:')
        date=input('enter date')
        url= f"{self.get_config(section='Co-win_Portal', option='base_url')}{self.get_config(section='Co-win_Portal', option='calendarby_center').replace('{center_id}', center_id).replace('{date}', date)}"
        headers = {
            'Content-Type': 'application/json',
            'User-Agent': 'PostmanRuntime/7.28.0',
            'Accept-Language': 'te_IN'
        }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            var=response.json()
            print(var)
        else:
            print(f'Error : Status Code : {response.status_code} | Reason : {response.reason}')

    def main(self):
        print(f'Welcome to the Cowin Portal..!')
        while True:
            print('1.States info', '2.Districts info', '3.ByPin', '4.ByDistricts', '5.ByLatLong','6.Calendar by Pin','7.Calendar by District','8.Calendar by Center', sep='\n')
            choice = input('Enter Your choice : ')
            if choice == '1':
                print('States list')
                self.get_states()
            elif choice=='2':
                print('Districts list')
                self.get_districts()
            elif choice=='3':
                print('Appointments based on Pincode')
                self.by_pin()
            elif choice=='4':
                print('Appointments based on District')
                self.by_district()
            elif choice=='5':
                print('Centers based on Lattitude&Longitude')
                self.by_latlong()
            elif choice=='6':
                print('Vaccine avalability by Pincode')
                self.calendarby_pin()
            elif choice=='7':
                print('Vaccine avalability by District')
                self.calendarby_district()
            elif choice=='8':
                print('Vaccine avalability by Cnter')
                self.calendarby_center()
            else:
                print('Invalid Selection. Please select again...!')
            decision = input('Do You Want to Continue  [y/n] : ')
            if decision == 'y' or decision == 'Y':
                continue
            else:
                decision == 'n' or decision == 'N'
                print('#stay home#stay safe')
                break

obj=Cowin()
obj.gen_otp()
obj.con_otp()
# obj.get_states()
# obj.get_districts()
# obj.by_pin()
# obj.by_district()
# obj.by_latlong()
# obj.calendarby_pin()
# obj.calendarby_district()
# obj.calendarby_center()
