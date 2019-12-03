from matplotlib import pyplot as plt

Gender = 'Men', 'Women'
average_medal_ratio = [43.690,56.310]  
explode = (0,0.1)  # it "explode" the 1st slice   
  
fig1, ax1 = plt.subplots()  
ax1.pie(average_medal_ratio, explode=explode, labels=Gender, autopct='%1.1f%%',  
        shadow=True, startangle=90)  
ax1.axis('equal')
ax1.set_title("Ratio Of Gold Medals Won \n(Using %, Of Total_Records)")  # Equal aspect ratio ensures that pie is drawn as a circle.  

ax1.legend(Gender,
          title="Gender",
          loc="upper right",
          bbox_to_anchor=(1, 0, 0.1, 1))
  
plt.show() 