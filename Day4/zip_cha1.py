capitals = ["Berlin", "Tokyo", "Paris", "Helsinki", "Ottawa", "Canberra"]
countries = ["Germany", "Japan", "France", "Finland", "Canada", "Australia"]

country_capitals_list = list(zip(countries, capitals))

for countries, capitals in country_capitals_list:
    print(f"The capital of {countries} is {capitals}")
