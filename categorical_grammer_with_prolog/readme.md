I used SWI-Prolog on a Linux VM. It was pretty easy to install and start experimenting in the interactive mode.

I started by defining some "facts" about my immediate family, then expanded it to include other relatives so that I could test more complex rules likes brother-in-law and great-grandparents. At this point I switched out my family's names for dummy data, and also made up some new people and relationships. This started to get confusing, so I made a little diagram for mapping out the relationships (see [relationships.png](relationships.png)). 

With only the basic facts of gender, parents, and spouses, I was able to define all of the basic family relationships, as well as some more complicated ones. I thought it was really useful how I was able to build more complex rules using previously defined rules. For example, grandAunt(X,Y) was easy to define since aunt(X,Y) was already defined. Then with the grandAunt(X,Y) rule, I was quickly able to define secondCousin(X,Y). 

My data/rules are defined in [family.pro](family.pro). 

I included some screenshots of using these rules (see `output_*.png`).