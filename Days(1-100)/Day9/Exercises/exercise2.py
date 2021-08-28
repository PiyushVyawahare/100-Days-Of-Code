travel_log = [
	{
		"country": "France",
		"visits": 12,
		"cities": ["Paris", "Lille", "Dijon"]
	},
	{
		"country": "Germany",
		"visits": 5,
		"cities": ["Berlin", "Hamburg", "Stuttgart"]
	},
]
#🚨 Do NOT change the code above

def add_new_country(country, visits, cities):
    new_dictionary = {}
    new_dictionary["country"] = country
    new_dictionary["visits"] = visits
    new_dictionary["cities"] = cities
    travel_log.append(new_dictionary)

#🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)