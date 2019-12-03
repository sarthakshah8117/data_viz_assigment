import matplotlib.pyplot as plt

years = [1920,1930,1940,1950,1960,1970,1980,1990,2000,2010]
MEN = [22, 18, 19, 19, 18, 18, 25, 24, 48, 59]
WOMEN = [6, 6, 6, 6, 18, 19, 21, 24, 45, 62]

plt.plot(years, color  MEN)
plt.plot(years, WOMEN)
plt.xlabel('Olympic Years')
plt.ylabel('Number of Medals')
plt.title('Proportion for Skating Competition')

Gender = 'Men', 'Women'

plt.legend(Gender,
          title="Gender",
          loc="upper left")

plt.show()
