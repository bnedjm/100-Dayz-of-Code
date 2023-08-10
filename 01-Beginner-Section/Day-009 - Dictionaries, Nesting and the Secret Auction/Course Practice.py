programming_dictionary = {
  "Bug": "An error in a program that prevents the program from running as expected.",
  "Function": "A piece of code that you can easily call over and over again.",
  "Loop": "The action of doing something over and over again",
}

#retrieving items from dictionary.
print(programming_dictionary["Bug"])

#Adding new items to dictionary.
programming_dictionary["Test"] = "Sample info"
print(programming_dictionary)

#Create an empty dictionary
empty_dict = {}

#Wipe an exsisting dictionary.
programming_dictionary = {}
print(programming_dictionary)

#Edit an item in a disctionary.
programming_dictionary["Bug"] = "A moth in your computer"
print(programming_dictionary["Bug"])

#Loop through a dictionary.
for key in programming_dictionary:
  print(key)
  print(programming_dictionary[key])

#Nesting.
capitals = {
  "France" : "Paris",
  "Germany" : "Berlin"
}

#Nesting a list in a dictionary.
travel_log = {
  "France" : ["Paris", "Lille", "Dijon"],
  "Germany" : ["Berlin", "Hamburg", "Stuttgart"],
}

#Nesting a dictionary in a dictionary.
cities_visited = {
  "France" : {"cities_visited" : ["Paris", "Lille", "Dijon"], "total_visits" : 12},
  "Germany" : {"cities_visited" : ["Berlin", "Hamburg", "Stuttgart"], "total_visits" : 14},
}
cities_visited_count = {
  "France" : {
    "Paris" : 2,
    "Lille" : 3,
    "Dijon" : 1,
  },
  "Germany" : {
    "Berlin" : 3,
    "Hamburg" : 1,
    "Stuttgart" : 5,
  }
}

#Nesting a dictionary in a list.
travel_log = [
  {
    "country" : "France",
    "cities_visited" : ["Paris", "Lille", "Dijon"],
    "tatl_visits" : 12,
  },
  {
    "country" : "Germany",
    "cities_visited" : ["Berlin", "Hamburg", "Stuttgart"],
    "tatl_visits" : 14,
  }
]
