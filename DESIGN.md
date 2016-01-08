# UI:
- Map
- Line Chart
- Bar Chart
- Table
- Selectors/brushes


What is shown is dependant on the current 'perspective'
- "Overview / country view"
		- Map: chloropleth showing how much each country receives
		- Line chart: totals per year
		- Bar graph: same as map only on a bar chart for better comparison

	-country.click

		- line chart: how much did this country receive in the past
		- bar chart: how much does this country receive from each fund
- "Fund view" perspective from one fund
	- Map: how much does a country receive from this fund?
	- line chart: how much did this fund give in the past?
	- bar graph: same as map only on a bar chart for better comparison

	-country.click
		- line chart: how much did this country receive in the past

- "category view"
	- same as "fund view", only difference that the funds have been grouped in categores

- for each "perspective"
	- table shows a sortable overview of the first x rows of data (scrollable)
	- brushing is possible on the line and the bar
	- the selectors / brushing tab enables for further filtering (amount, fund, category, country, etc)

# Functions:

- Map:
	- drag to reposition map (mousedown, mousemove, mouseup)
	- click to select (click)
	- zoomwheel to zoom (zoom)
	- focus on mouseover (hover)

- Bar chart:
	- click to select (mousedown, mousemove, mouseup)
	- brush to select (mousedown, mousemove, mouseup)

- Line Chart:
	- focus + context via brushing (mousedown, mousemove, mouseup)

- Data modifiers:
	- dragdown box to filter (total money to countries / money to countries from funds / money to countries per category)
	- filtering by amount, country, fund, category, etc

- Data cleaning
	- delete redundant data
	- consolidate to category
	- correct for institution name changes


# Frameworks
- D3
For visualization and data modifying

- Jquery (optional)
For eventhandling / dom changes