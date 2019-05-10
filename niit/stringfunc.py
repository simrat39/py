a = "helo"
b = "  belo   "
c = "hello to python"
len(a) # length of the string
b.rstrip() # remove trailing white space
b.lstrip() # remove leading white space
b.strip() # remove both leading and trailing white space
a.replace('he','le') # replace a part of the string
a.islower() # checks if all charecters are lowercase or not
a.isupper() # checks if all charecters are uppercase or not
a.find('elo',0,len(a)) # used to find a string from the given range
unicode(a).isnumeric() # checks if there are only numeric charecters or not , works only with unicode
a.lower() # converts string to lowercase
a.upper() # converts string to capital letters
a.capitalize() # makes first character of first word start with capital letter
a.title() # makes first charecetr of all words capital
a.istitle() # checks if the string is title case or not
c.split(' ') # splits the string according to character or set of charecters given in the paramter and returns a list
min(a) # returns lowest 
max(a) # returns highest