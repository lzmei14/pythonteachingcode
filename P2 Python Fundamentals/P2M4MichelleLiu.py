# [ ] create The Weather
# [ ] The Weather: import world_mean_team.csv as mean_temp.txt into the Jupyter notebook
import os
os.system("curl https://raw.githubusercontent.com/MicrosoftLearning/intropython/master/world_temp_mean.csv -o mean_temp.txt")

# [ ] Add the weather for Rio
weather_file = open('mean_temp.txt','a+')
weather_file.write("Rio de Janeiro,Brazil,30.0,18.0\n")

# [ ] Grab the column headings
weather_file.seek(0)
headings = weather_file.readline()
headings = headings.split(',')
# print(headings)

print("\nMichelle Liu")
# [ ] Read the remaining lines from the file using a while loop
city_temp = weather_file.readline()
while city_temp:
    city_temp = city_temp.split(',')
    print(headings[0].title(),"of",city_temp[0].title(),headings[2],"is",city_temp[2],"Celcius.")
    city_temp = weather_file.readline()
weather_file.close()

