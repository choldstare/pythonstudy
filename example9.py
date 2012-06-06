print "I am 6'3\" tall." # escape double-quote inside string
print 'I am 6\'3" tall.' 

tabby_cat= "\tI'm tabbed in."       # \t acts as a tab
persian_cat="I'm split\non a line." # the \non split the line
backslash_cat="I'm \\ a \\ cat."    # the double \\ caused just one of them to print.\\

#the fat_cat below used """ so this allows me write indefinately and make a list 
fat_cat= """                        
I'll do a list:
\t* cat food
\t* Fishies
\t* Catnip \n\t* Grass
"""

fat_cat1= '''                     
I'll do a list:
\t* cat food\rpenis
\t* Fishies
\t* Catnip \n\t* Grass
'''

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat
print fat_cat1

#while True:
#	for i in ["/","-","|","\\","|"]:
#	print "%s\r" %i,

