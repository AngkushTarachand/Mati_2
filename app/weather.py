import json

import requests

base_url = "http://api.weatherapi.com/v1/forecast.json?"
base_url_2 = 'key=4a7e42ecf0464c25add141136220210&q='
city = "Mauritius"

url = base_url + base_url_2 + "&q=" + city + "&days=10&aqi=yes&alerts=yes"
# print(url)
response = requests.get(url).json()

# for key in response:
#     print(key)

# print(response['location'])
# print(response['forecast'])
p = json.dumps(response, indent=4)
# print(p)


class TodayCondition:
    @staticmethod
    def get_date():
        return response['forecast']['forecastday'][0]["date"]

    @staticmethod
    def average_temp():
        return response['forecast']['forecastday'][0]["day"]["avgtemp_c"]

    @staticmethod
    def amount_precipitation():
        return response['forecast']['forecastday'][0]["day"]["totalprecip_mm"]

    @staticmethod
    def condition_weather():
        return response['forecast']['forecastday'][0]["hour"][0]['condition']["text"]


date_list = []
temp_list = []


# class Temperature:
#     @staticmethod
#     def get_temp_graph():
#         for each in range(len(response['forecast']['forecastday'])):
#             print(response['forecast']['forecastday'][each]["date"][-4:],
#                   response['forecast']['forecastday'][each]["day"]["avgtemp_c"])
#
#             date_list.append(response['forecast']['forecastday'][each]["date"][-5:])
#             temp_list.append(response['forecast']['forecastday'][each]["day"]["avgtemp_c"])
#             # print(date_list)
#         print("Graph")
#         x = date_list
#         y = temp_list
#
#         plt.plot(x, y)
#         plt.xlabel("date")
#         plt.ylabel("temperature")
#         plt.title("Graph")
#         # plt.show()
#         print("Ongoing")
#         # print(plt.show())
#         print("saved")
#         plt.savefig('static/p1.png')
#         plt.close()
#
#         return plt.savefig('static/p1.png')

