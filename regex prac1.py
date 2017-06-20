# -*- coding: iso-8859-15 -*-
import re

f=open("german_postcodes.txt","r")

cities='''
1.  Berlin          3.382.169 Berlin
2.  Hamburg         1.715.392 Hamburg
3.  München         1.210.223 Bayern
4.  Köln              962.884 Nordrhein-Westfalen
5.  Frankfurt am Main 646.550 Hessen
6.  Essen             595.243 Nordrhein-Westfalen
7.  Dortmund          588.994 Nordrhein-Westfalen
8.  Stuttgart         583.874 Baden-Württemberg
9.  Düsseldorf        569.364 Nordrhein-Westfalen
10. Bremen            539.403 Bremen
11. Hannover          515.001 Niedersachsen
12. Duisburg          514.915 Nordrhein-Westfalen
13. Leipzig           493.208 Sachsen
14. Nürnberg          488.400 Bayern
15. Dresden           477.807 Sachsen
16. Bochum            391.147 Nordrhein-Westfalen
17. Wuppertal         366.434 Nordrhein-Westfalen
18. Bielefeld         321.758 Nordrhein-Westfalen
19. Mannheim          306.729 Baden-Württemberg
'''
cities=cities.decode("iso-8859-15")
top_cities_pc=''
c=cities.split("\n")
d={}
for s in c:
    state=re.search(r"\.\s+([A-Za-zwÄÖÜäöüß]*).*\d\s(.*)",s)
    if state:
        d[state.group(1)]=[state.group(2)]
print d

x=''
for l in f:
    for i in d:
        pcode=re.search(r'''^(\d*),"%s"'''%(d[i][0]),l)
        if pcode:
            x+=pcode.group(0)
    print x
            #top_cities_pc
f.close()


