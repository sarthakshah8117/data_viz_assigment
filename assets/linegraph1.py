import matplotlib.pyplot as plt

years = [1920,1930,1940,1950,1960,1970,1980,1990,2000,2010]
MEN = [112, 110, 99, 125, 108, 153, 167, 201, 273, 296]
WOMEN = [6, 6, 9, 18, 39, 45, 51, 99, 208, 233]

plt.plot(years, MEN)
plt.plot(years, WOMEN)
plt.xlabel('years')
plt.ylabel('Gender')
plt.title('MEN VS WOMEN')

Gender = 'Men', 'Women'

plt.legend(Gender,
          title="Gender",
          loc="upper left")

plt.show()
