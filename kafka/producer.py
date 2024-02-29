# import requests
# import csv
# import time
# from datetime import datetime
#
# # Function to retrieve data from the API
# def get_cat_fact():
#     response = requests.get('https://catfact.ninja/fact')
#     data = response.json()
#     return data['fact']
#
# # Function to write data to a CSV file
# def write_to_csv(fact):
#     with open('cat_facts.csv', 'a', newline='') as csvfile:
#         writer = csv.writer(csvfile)
#         writer.writerow([datetime.now().strftime("%Y-%m-%d %H:%M:%S"), fact])
#
#
# # Main function to run the program
# def main():
#     # Write CSV header
#     with open('cat_facts.csv', 'w', newline='') as csvfile:
#         writer = csv.writer(csvfile)
#         writer.writerow(['Timestamp', 'Fact'])
#
#     # Loop for 1 minute
#     end_time = time.time() + 60
#     while time.time() < end_time:
#         fact = get_cat_fact()
#         write_to_csv(fact)
#         time.sleep(1)  # Sleep for 1 second between each API call
#
# if __name__ == "__main__":
#     main()


import requests
import  csv




response=requests.get(url='https://catfact.ninja/fact')
data = response.json()

with open(file='new.csv',mode='w',newline='') as csvfile:
    writer=csvfile.read()




