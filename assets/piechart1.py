from matplotlib import pyplot as plt
Men =[]
Women =[]
Gender = 'Men', 'Women'
Average_medal_ratio = [68.35, 31.65]
explode = (0, 0.1) # explode 1 pie piece

fig1, ax1 = plt.subplots()  
ax1.pie(Average_medal_ratio, explode=explode, labels=Gender, autopct='%1.1f%%',
	shadow=True, startangle=90)
ax1.axis('equal')
ax1.set_title("Medals Won By Men And Women\n(using %, medals category)")

ax1.legend(
	title="Medals",
    loc="upper right",
    bbox_to_anchor=(1, 0, 0.1, 1))

plt.show() 