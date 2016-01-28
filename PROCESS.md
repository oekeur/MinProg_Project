# Processbook
A processbook to document day-to-day the challenges, decisions and emotionsl breakdowns.

## Day 1
- Voorstel schrijven, eerste te moeilijk ideeën, na wat lezen het FTS (Financial Transparancy System) van de EC gevonden.
- Dit biedt een goede basis die uitbreidbaar is. Eerst "droog" geldstromen mappen en exploration maken. Als er tijd over is koppelen aan andere bronnen. (EDF, ESF, EuroStat)
- 'S avonds ingelezen in Bootstrap lijkt een goede basis voor een mooi ontwerp.

## Day 2
Begonnen met designschets uitwerken in html met Bootstrap tot een prototype. Voorlopig 3 tabs, een landingpage met uitleg over het project, een tab met interactieve exploration en een tab met premade stories.

## Day 3
- Standupmeeting met voornamelijk globale uitleg over ieders project en globale problemen.
- 13:00 D3 Datamaps ingeplaatst + centered op europe + europese kleuren
- Jquery ingelezen (eventhandlers) voor interactie
- Geprobeerd meerdere eventhandlers in datamaps te koppelen, lukt vooralsnog niet.

## Day 4
- Besloten om te proberen datamaps weg te halen en zelf met d3 en topojson een kaart te maken (want met d3 lukte het wel meerdere eventhandlers te gebruiken)
- 12:00: worldmap ingetekdn met enkel d3, nu id's op de landen plaatsen, kijken hoe dat in datamaps gaat 
- 15:00 adhv topojson met d3 kaart werkend ingevoegd in project

## Day 5
Bar + line chart ingevoegd, volledig d3 dashboard dus.
Zooming aan map toegevoegd, trnaslate laat m uit beeld vliegen..
met brushing bezig geweest, nog niet ingevoegd.
designdocument geschreven, prototype compleet door design en invoegen d3 visualisaties:
wat mist er nog in prototype? tabel + selectors + filters

## Day 6
Wat Ui interdace toegevoegd (bar chart sorteren, downloadknop voor de data),
bezig geweest met datacleaning: als meerdere entiteiten onder 1 subsidie vallen, is de subsidietitel alleen in de eerste rij vermeld,
in 1 jaar stond er ook alleen een totaalbedrag in de eerste rij van een subsidie en in de andere rijen niks.
iets met while row[0] == empty: row[0] =row-1[0]. alles naar csv, xls met meerdere tabbladen tot 1 csv gemerged
tevens zitten er soms separatortekens in de naam van een entiteit.. RegEx?

## Day 7
Voornamelijk bezig geweest met datacleaning.
Basisscript voor verwijderen van redundant data is af.
Missing values worden gemarkeerd. in de data zitten newline karakters, lukt nog niet deze te verwijderen...
Nagedacht over apart overzicht bestand met totalen, nog niet gemaakt.
Git doet het niet

## Day 8
Datacleaning: probleem met de newline nu "grof" opgelost. Newlines worden vervangen door slashes. Nadeel: als er meerdere begunstigden zijn, kan je ze niet los benaderen. Voor alpha ok, voor final moet dat, vind ik, wel anders.
Dus nieuwe entries als er newlines worden gevonden.

## Day 9
Unicodeencoding heeft me veel tijd gekost. python is in utf-8, in de data zitten latin-1 karakters.
Wel basis voor een sum over landen af. Bij runnen bleek er een fout in de datacleaning te zitten als er meerdere recipients voor een project zijn.
Zorgen dat ie alle amounts in dezelfde column zet. Moet zo gefixt zijn.

## Day 10
Dus niet zo gefixt.. Rottig om zelf de data te moeten structureren. List of dicts is niet handig blijkbaar, want dan moet je loopen en daarna keys uitlezen.
Alles in dicts zetten

## Day 11
Bezig met de data van de landen per jaar in 1 dict te zetten. Ondertussen ook bezig om instituties te sommen op categorieën.

## Day 12
Data per land per jaar werkt. Choropleth wil niet aan de praat met colorbrewer. Gesettled voor een linearscale. Quantize zou ook nog kunnen

## Day 13
Choropleth werkt, verder gaan met categoriën werkend krijgen voor de barchart. linechart werkt wel voor de countrydata.

## Day 14
Categorieën geven in de loop wel de juiste respons maar buiten de loop niet, ligt niet aan de scope (getest..)

## Day 15
Categoriën 's avonds werkend gekregen. Doet wat t moet doen, werkt ook meteen in linechart, SCORE.
Probleem is dat door de manier van assignen de complete dictionary aan de laatste waarde uit de loop werd toegewezen. De manier van countrydata als basis om beter te assignen.

## Day 16
Deze week heel weinig tijd ivm tentamens in Delft.

## Day 17
Deze week heel weinig tijd ivm tentamens in Delft.

## Day 18
Deze week heel weinig tijd ivm tentamens in Delft.
Vandaag code opgeschoond.
Vriend naar code laten kijken, die opmerkte dat bepaalde landen geen data hadden. Door verkeerd gebruik van try/except werden niet alle landen werden opgenomen in de data (als voor 1 jaar data miste bouncete de hele reeks)
Nu per jaar checken of er een value is, zo nee 0, anders assign.

## Day 19
Laatste tentamen gehad. Beetje getweakt aan UI, Lorem ipsums door zinnige teksten vervangen. Het stories-tabblad is verwijderd wegens gebrek aan tijd. Voor de rest de deliverables maken.