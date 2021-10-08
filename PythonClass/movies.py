movie = dict()


movie['Ant-Man'] = dict()
movie['Ant-Man']['year'] = dict()
movie['Ant-Man']['year'] = 2015
movie['Ant-Man']['stars'] = dict()
movie['Ant-Man']['stars'] = ['Paul Rudd', 'Evangeline Lilly', "Michael Douglas", "Michelle Pfeiffer"]


movie["Ava"] = dict()
movie['Ava']['year'] = dict()
movie['Ava']['year'] = 2020
movie['Ava']['stars'] = dict()
movie['Ava']['stars'] = ['Jessica Chastain', 'Colin Farrell', "John Malkovich"]


movie["The Hangover"] = dict()
movie['The Hangover']['year'] = dict()
movie['The Hangover']['year'] = 2009
movie['The Hangover']['stars'] = dict()
movie['The Hangover']['stars'] = ['Zach Galifianakis', 'Bradley Cooper', "Ed Helms", "Ken Jeong", "Justin Bartha"]


movie["Lion"] = dict()
movie['Lion']['year'] = dict()
movie['Lion']['year'] = 2016
movie['Lion']['stars'] = dict()
movie['Lion']['stars'] = ['Dev Patel', 'Nicole Kidman', "Sunny Pawar"]


movie["Deadpool"] = dict()
movie['Deadpool']['year'] = dict()
movie['Deadpool']['year'] = 2016
movie['Deadpool']['stars'] = dict()
movie['Deadpool']['stars'] = ['Ryan Reynolds', 'Morena Baccarin', "T.J. Miller"]


for k, v in movie.items():
    print(k, "[", v['year'], "] stars",  v['stars'])


