
# The program fetches data from a popular CSV file that contains data and information about all the passengers who were on the Titanic ship right on the day of the catastrophic event. The motive of this program is to plot a bar graph and a piechart in a single figure using matplotlib in order to show all the survivors among the deaths and also to compare the surviving likelihood of a survivor based on his/her sex, age (below or under 18) and passenger class. The program aims to gather insights from the day of the event.

# Note: The probability is out of the total survivors and not the total strength of the ship. As the death toll is very high.


import pandas as pd

import matplotlib.pyplot as plt


plt.style.use('ggplot')


# Reading data:

data = pd.read_csv('Titanic Passenger List.csv')


# Assigning data to a variable:

sex = data['Sex']

age = data['Age']

passenger_id = data['PassengerId']

passenger_class = data['Pclass']

survivor_index = data['Survived']


# Making two plots:
    
fig1, (ax1, ax2) = plt.subplots(nrows= 1, ncols= 2)


# Fetching data for the bar graph:

total_passengers = passenger_id.iloc[-1]

male_survivors = data[(sex == 'male') & (age > 18) & (survivor_index > 0)]

total_male_survivors = male_survivors['Survived'].sum()

female_survivors = data[(sex == 'female') & (age > 18) & (survivor_index > 0)]

total_female_survivors = female_survivors['Survived'].sum()

child_survivors = data[(age <= 18) & (data['Survived'] > 0)]

total_child_survivors = child_survivors['Survived'].sum()
    
    
first_class_survivors = data[(passenger_class == 1) & (data['Survived'] > 0)]

total_first_class_survivors = first_class_survivors['Survived'].sum()

second_class_survivors = data[(passenger_class == 2) & (data['Survived'] > 0)]

total_second_class_survivors = second_class_survivors['Survived'].sum()

third_class_survivors = data[(passenger_class == 3) & (data['Survived'] > 0)]

total_third_class_survivors = third_class_survivors['Survived'].sum()


# Plotting bar graph:
    
ax1.bar(total_passengers + 0.30, total_male_survivors, width= 0.20, label= 'Men', color= 'Red')

ax1.bar(total_passengers + 0.25, total_child_survivors, width= 0.20, label= 'Children', color= 'Orange')

ax1.bar(total_passengers + 0.20, total_female_survivors, width= 0.20, label= 'Women', color= 'Purple')


ax1.bar(total_passengers - 0.20, total_first_class_survivors, width= 0.20, label= 'First Class', color= 'Gold')

ax1.bar(total_passengers - 0.25, total_second_class_survivors, width= 0.20, label= 'Second Class', color= 'Brown')

ax1.bar(total_passengers - 0.30, total_third_class_survivors, width= 0.20, label= 'Third Class', color= 'Grey')


# Labeling the bar graph:

ax1.legend(fontsize= 5, loc= 'upper left')

ax1.set_title('Titanic Survivors By Sex And Passenger Class', fontweight= 'bold', fontsize= 8)

ax1.set_xlabel('Total Number Of Passengers >>> \n', fontsize= 6, fontweight= 'bold')

ax1.set_ylabel('Survivors >>>', fontsize= 6, fontweight= 'bold')


# Fetching data for pie chart:

total_survivors_by_sex = [

                          total_male_survivors,
                          total_female_survivors,
                          total_child_survivors
                          
                                                    ]

total_survivors_by_passenger_class = [

                      total_first_class_survivors,
                      total_second_class_survivors, 
                      total_third_class_survivors
                      
                                                      ]


# Plotting the pie chart:

label_1 = ['First Class', 'Second Class', 'Third Class']

colors_1= ['Gold', 'Brown', 'Grey']

label_2 = ['Men', 'Women', 'Children']

colors_2 = ['Red', 'Purple', 'Orange']


ax2.pie( total_survivors_by_passenger_class, 
         labels= label_1, 
         colors= colors_1, 
         radius= 1.2, 
         autopct= '%1.1f%%', 
         startangle= 90, 
         pctdistance=0.80, 
         textprops= {
                       'fontsize': 6, 
                       'family': 'serif'
                       }
                         )

ax2.pie( total_survivors_by_sex, 
         labels= label_2, 
         colors= colors_2, 
         radius= 0.60, 
         autopct= '%1.1f%%', 
         labeldistance= 1.1, 
         startangle= 130, 
         textprops= {
                      'fontsize': 6, 
                      'fontweight': 'bold', 
                      'family': 'serif'
                      }
                        )


# Labeling second plot:

ax2.legend(loc= 'lower left', fontsize= 5)

ax2.set_title('Surviving Probability By Sex And Passenger Class', fontweight= 'bold', fontsize=8)


# Showing the two plots:
    
plt.tight_layout()

plt.show()


''' Created By Sourin Das '''