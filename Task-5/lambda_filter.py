# Using lambda function to filter out people under 18 from a list of dictionaries
people_data = [{"name": "Bathri", "Age": 29}, {"name": "Sanjay", "Age": 28}, {"name": "Suren", "Age": 25},
        {"name": "Monish", "Age": 17}, {"name":"Naresh", "Age": 15}]
under_18 = list(filter(lambda person: person["Age"] < 18, people_data))
print("People under 18:", under_18)






