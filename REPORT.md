# Final Report 
<sub>Oscar Keur, 11122102</sub>

## Description of application
The visualization made in this project revolves around public spending in the EU in general. The specific data that is shown is the set of
grants that the European Commission gave between 2007 and 2013. The main aim is to give insights into the spending of the EU. Secondly the idea was to aid discussions about the EU.
I think this visualization can indeed accomplish this at current stage, but with some more development more information could be made available and thus the insights could be even more usefull.


At the time of writing this report I found that the EU did indeed make such an application. Main differences: 
- My visualization shows the development from 2007 untill 2013.
- FTS doesn't have any means of comparing countries
- FTS only has low-level data, I added an aggregate component to the data
http://ec.europa.eu/budget/fts/index_en.htm

-----
## Technical design
Big part of the project was to structure the data into something usefull. So a lot of prepocessing in Python has been done. A interactive visualization is produced, I would however have liked to have a bit more time to make more interactive elements.

### Pre-processing
The files could have been merged some more, maybe something for a rainy sunday.

#### Countrycodes 
Make a dictionary to map between country names and country codes

#### Datacleaning
Remove all redudant data from the datafiles and correct / flag missing values

#### Dataprocessing
Process the data files into files containing the data for a country or institution for one year

#### Countrytotal / institutiontotal
Merge the data per year into one json object (dictionary) with the country / category as the key

### Visualization
- First initialize some data
- Draw the map, with the total amount received as the input for a chloropleth
- Draw a barchart showing the total of categories
- Draw a line graph, which initially shows the sum of all the amounts
- Fill the table with the sum per country

For the map and data: on(hover) the line graph changes according to the where the mouse is.

-----
## Challenges
The main challenge, as appeared, was to preprocess the data. The data is very low-level and so the structuring of data had to be completely done. Furthermore the data contained some strange encodings and weird practices.
Lots of time lost correcting this and structuring the data into something usefull. Main problem here is that from 2009 onwards when one grants had multiple subsidiaries the data was all put into one row in excel separated by newlines. This means that processing this data gets alot more complicated. Trade-off that has been made here was to group this data into missing values, because I did no succeed in separating the values without new errors.

### Possible improvements (in chronological order)
 - onclick draw extra line and show categories per country
 - more datasources (EDF, ESF, GDP)
 - deeper data (make the level available at a lower lovel (include the specific grants for example))
 - search function