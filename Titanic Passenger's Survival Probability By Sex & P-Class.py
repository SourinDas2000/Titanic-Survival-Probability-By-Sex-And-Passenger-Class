
# The program fetches data from a popular CSV file that contains data about all the passengers who were on the Titanic ship till the day of the catastrophic event. The motive is to plot a bar graph and a pie chart in a single figure using Matplotlib Subplots to show all the survivors, and also to compare the survival probability of a passenger based on his/her sex, age (below or under 18), and passenger class (1st, 2nd & 3rd class). The project aims to gather insights from the day of the event.


import pandas as pd
import matplotlib.pyplot as plt


# Reading the data:

data = pd.read_csv('Titanic Passenger List.csv')


# Assigning informations to a variable:

sex = data['Sex']
age = data['Age']
passenger_class = data['Pclass']
survivor_index = data['Survived']
passenger_id = data['PassengerId']


# Using matplotlib custom style -- 'Ggplot':

plt.style.use('ggplot')


# Making two plots:
    
fig1, (ax1, ax2) = plt.subplots(nrows= 1, ncols= 2, constrained_layout= True)


# Deriving data for the bar graph:

#### Total Passengers On-board:
total_passengers = passenger_id.iloc[-1]

#### Total Male Survivors:
male_survivors = data[(sex == 'male') & (age > 18) & (survivor_index > 0)]
total_male_survivors = male_survivors['Survived'].sum()

#### Total Female Survivors:
female_survivors = data[(sex == 'female') & (age > 18) & (survivor_index > 0)]
total_female_survivors = female_survivors['Survived'].sum()

#### Total Survivors Who Were Under 18 Year Old:
child_survivors = data[(age <= 18) & (data['Survived'] > 0)]
total_child_survivors = child_survivors['Survived'].sum()
    
#### Survivors Who Were In Passenger Class 1:    
first_class_survivors = data[(passenger_class == 1) & (data['Survived'] > 0)]
total_first_class_survivors = first_class_survivors['Survived'].sum()

#### Survivors Who Were In Passenger Class 2:    
second_class_survivors = data[(passenger_class == 2) & (data['Survived'] > 0)]
total_second_class_survivors = second_class_survivors['Survived'].sum()

#### Survivors Who Were In Passenger Class 3:    
third_class_survivors = data[(passenger_class == 3) & (data['Survived'] > 0)]
total_third_class_survivors = third_class_survivors['Survived'].sum()


# Plotting the bar graph:

#### Survivors By Age & Sex:   
ax1.bar( total_passengers + 0.30, total_male_survivors, 
         width= 0.20, 
         label= 'Men', 
         color= 'Red'
         )
ax1.bar( total_passengers + 0.25, total_child_survivors, 
         width= 0.20, 
         label= 'Children', 
         color= 'Orange'
         )
ax1.bar( total_passengers + 0.20, total_female_survivors, 
         width= 0.20, 
         label= 'Women', 
         color= 'Purple'
         )

#### Survivors By Passenger Class:
ax1.bar( total_passengers - 0.20, total_first_class_survivors, 
         width= 0.20, 
         label= 'First Class', 
         color= 'Gold'
         )
ax1.bar( total_passengers - 0.25, total_second_class_survivors, 
         width= 0.20, 
         label= 'Second Class', 
         color= 'Brown'
         )
ax1.bar( total_passengers - 0.30, total_third_class_survivors, 
         width= 0.20, 
         label= 'Third Class', 
         color= 'Grey'
         )


# Labeling the bar graph:

ax1.legend( fontsize= 5, 
            loc= 'upper left'
            )
ax1.set_title( 'Titanic Survivors By Sex And Passenger Class', 
                fontweight= 'bold', 
                fontsize= 8
                )
ax1.set_xlabel( f'Total Number Of Passengers ({total_passengers}) >', 
                 fontsize= 6, 
                 fontweight= 'bold'
                 )
ax1.set_ylabel( 'Survivors >', 
                 fontsize= 6, 
                 fontweight= 'bold'
                 )
ax1.tick_params( axis= 'y',
                 labelsize= 5
                 )
ax1.set_xticks([])

# Deriving data for the pie chart:

total_survivors_by_sex = [ total_male_survivors,
                           total_female_survivors,
                           total_child_survivors,
                           total_passengers
                           ]
total_survivors_by_p_class = [ total_first_class_survivors,
                               total_second_class_survivors, 
                               total_third_class_survivors,
                               total_passengers
                               ]


# Plotting the pie chart:

label_1 = ['First Class', 'Second Class', 'Third Class', 'Deaths']
colors_1= ['Gold', 'Brown', 'Yellow', 'Grey']
label_2 = ['Men', 'Women', 'Children', 'Deaths']
colors_2 = ['Red', 'Purple', 'Orange', 'White']
ax2.pie( total_survivors_by_p_class, 
         labels= label_1, 
         colors= colors_1, 
         radius= 1.2, 
         autopct= '%1.1f%%', 
         startangle= 114, 
         pctdistance= 0.80, 
         textprops= { 'fontsize': 5, 
                      'family': 'serif'
                       }
         )
ax2.pie( total_survivors_by_sex, 
         labels= label_2, 
         colors= colors_2, 
         radius= 0.65, 
         autopct= '%1.1f%%', 
         labeldistance= 1.1, 
         startangle= 55, 
         textprops= { 'fontsize': 4.7, 
                      'fontweight': 'bold', 
                      'family': 'serif'
                       }
         )


# Labeling pie chart:


ax2.set_title( 'Survival Probability By Sex And Passenger Class', 
                fontweight= 'bold', 
                fontsize= 8
                )


# Showing the two plots:

plt.show()


''' Created By Sourin Das '''