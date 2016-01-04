# MinProg_Project

## Project proposal
My project centers upon public spending in the EU. Using data from the Directorate General for Budget a visualization is made showing where the money goes. This will be done from different perspectives;

1. Country perspective: showing what funds gives money to a country (select country > see the different funds)
2. Funds perspective: select a fund and see where the money goes to (both on a bar chart and map)

The aim is to clarify some common misconceptions about EU spending. Therefore it is not only possible to explore the data, but also a set of stories will be shown. ie. "The EU is costing a lot of money" after which a comparison a shown between GDP and contribution to the EU.

1. Features
	* Minimum Viable Product
	* Map showing where money goes (choloropleth)
	* Barchart showing the amount of € per category
	* Choosing if you want to use countries or funds as categories

* Optional
	* Selecting different categories for comparison (search/click)
	* Some premade stories about EU spending
	* Linechart showing historical data
	* Integrating data from the big EU investment funds
	* Table for data exploration
	* Integrating other data (such as GDP?)

2. Problem Solving

The problem being solved is aiding to transparancy about spending in the EU. This project could therefore possibly be seen among other Open Spending iniatives.
There will be some stories told about common misconceptions about spending in the EU. Don't see this project however as a pro EU iniative, nor as a counter EU iniative. The idea is to make it possible to form an opinion based on the data. The stories included are merely included as a guidance or starting point.


3. Sketch
![Designsketch](/doc/mockup1.png)

4. Data sets and sources

Directorate General for Budget: https://open-data.europa.eu/en/data/dataset/FTS

European Development Funds: https://open-data.europa.eu/en/data/dataset/FTS

European Social Fund: http://ec.europa.eu/esf/main.jsp?catId=31&langId=en

Missing: Farming Fund



5. Decompose problem
 * Data gathering
 	* Multiple sources (DGB / EDF / ESF / ...)
 * Data restructuring
 * Chloropleth map
 * Bar chart
 * Storytelling
 	* Arguments


6. What external components?
	* D3
	* D3 Maps
	* (JQuery)
	* (Bootstrap)
	* (Typeahead /similar)


7. Potential problems and solutions
	* Too much data: preprocess data to narrow down the dataset, possibly aggregate to fund (now EVERY grant is stored)
	* Incomplete data sets: Probably not, because the EU are bureaucrats, but it's possible..

8. Similar
Openspending.org has a similar dataset. This is however só big that it is almost unusable. Very lowlevel data is making finding data very hard
https://openspending.org/eu-commission-fts?_view=default