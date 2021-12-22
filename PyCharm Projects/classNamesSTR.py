# Julio Claros
# 114153234
# 2018-08-11
# Exercise


class Country:
    def __init__(self, name, population, gdp):
        self.name = name
        self.population = int(population)
        self.gdp = float(gdp)

    def per_capita_gdp(self):
        return self.gdp/self.population

    def __str__(self):
        return "Country" + ": " + str(self.name)


country = Country("Xyz", 10, 20)
print(country.__str__())