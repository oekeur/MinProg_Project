window.onload = function()
{
	Map(),
	Bar ();
	Line();
}

var EU = [40,56,100,196,203,208,233,246,250,276,300,348,191,372,380,428,440,442,470,528,616,620,642,703,705,724,752,826]
var data;
var country2007 = {"Canada": 9125257.02, "Turkmenistan": 36556.0, "Lithuania": 64362570.61, "Cambodia": 34427758.0, "Switzerland": 196712133.10999998, "Ethiopia": 5793575.85, "Argentina": 2434270.25, "Bolivia": 2519315.0, "Cameroon": 12115522.31, "Burkina Faso": 2103174.0, "Ghana": 62484.17, "Commission Department": 289660608.3899999, "Cape Verde": 1041614.57, "Slovenia": 30824996.87999999, "Guatemala": 8000.0, "Bosnia and Herzegovina": 37529611.13000001, "Germany": 996279396.3399982, "Spain": 468152398.0899996, "Netherlands": 494174608.24000007, "Pakistan": 33840141.25, "Tanzania": 335849.33, "Greenland": 42111944.0, "Gabon": 1720000.0, "Finland": 131332381.66999999, "New Zealand": 119314.88, "Yemen": 940042.39, "Jamaica": 4465000.0, "Albania": 18128612.06, "Macau": 99748.25, "United Arab Emirates": 1500.0, "India": 892136.04, "Azerbaijan": 412115.0, "Kenya": 10396793.82, "South Korea": 70395.0, "Tajikistan": 3478644.8700000006, "Congo (Democratic Republic of)": 2708449.7, "Turkey": 74003520.56000002, "Afghanistan": 39718517.88000001, "Bangladesh": 2471063.5799999996, "Solomon Islands": 400000.0, "San Marino": 3200.0, "Mongolia": 266126.82, "France": 1180186960.9600008, "Rwanda": 588436.0700000001, "Slovakia": 23657561.749999996, "Peru": 17165000.0, "Laos": 2616296.0500000003, "Norway": 64007241.029999994, "Malawi": 2438355.1500000004, "Cuba": 39369.22, "China": 29949008.569999997, "Armenia": 7415199.0, "Ukraine": 10213592.82, "Cayman Islands": 60500.0, "missing": 155584683.61999983, "Macedonia (the former Yugoslav Republic of)": 3000299.74, "Indonesia": 1523631.72, "Mauritius": 11649500.0, "Liechtenstein": 1078486.0, "Belarus": 2021313.0, "Vatican City": 48332.97, "Russia": 20031040.17, "Bulgaria": 156407592.66000003, "United States": 282032699.65, "Romania": 361010842.0300002, "Angola": 1151873.18, "Chad": 910721.18, "South Africa": 4592057.0, "Cyprus": 14955725.419999996, "Sweden": 214173965.08000004, "Malaysia": 685802.86, "Austria": 264954392.4299999, "Vietnam": 17041387.93, "Mozambique": 2853775.96, "Uganda": 134743.53, "Hungary": 56049173.96000003, "Niger": 6000002.0, "Brazil": 571608.05, "Guinea": 4800000.0, "Guyana": 4900000.0, "Costa Rica": 333249.27, "Luxembourg": 433143512.95, "Ireland": 100979450.22000003, "Nigeria": 830788.36, "Czech Republic": 46461938.139999986, "Australia": 368521.94, "Algeria": 100923.09, "El Salvador": 120000.0, "Serbia (Republic of)": 52625647.39999998, "Chile": 1504677.08, "Belgium": 836435814.8899987, "Kiribati": 478400.0, "Haiti": 1241140.92, "Belize": 2260676.63, "Hong Kong": 7322.0, "Sierra Leone": 2069677.0, "Occupied Territories - Palestine": 25195336.789999995, "Georgia": 8917394.829999998, "Montenegro (Republic of)": 72498.0, "Denmark": 208858792.74000004, "Philippines": 15180718.200000001, "Moldova": 60619826.14, "Morocco": 56555078.94, "Croatia": 6994622.49, "Micronesia": 657000.0, "Thailand": 3202706.54, "Namibia": 786072.0, "Seychelles": 4125000.0, "Portugal": 167156528.7, "Estonia": 23139902.009999998, "Uruguay": 593015.0, "Lebanon": 16118008.38, "Uzbekistan": 128578.45, "Tunisia": 67449150.0, "Colombia": 496850.0, "Burundi": 1136286.0100000002, "Taiwan": 1500.0, "Fiji": 59300.0, "Madagascar": 8180435.25, "Italy": 779794260.2499985, "Bhutan": 377562.0, "Sudan": 939845.96, "Nepal": 3023228.55, "Malta": 11075170.840000002, "Venezuela": 5088157.940000001, "Netherlands Antilles": 3945.0, "Israel": 109356717.44, "R\u00e9union": 36500.0, "Iceland": 7752557.23, "Zambia": 638794.0, "Trinidad and Tobago": 449980.0, "Zimbabwe": 4095098.0, "Jordan": 3680863.0, "Martinique": 25698.29, "Kazakhstan": 1051232.25, "Poland": 177262656.6700001, "Mauritania": 86000000.0, "Kyrgyzstan": 16053160.590000002, "Sri Lanka": 3358077.0, "Latvia": 20660003.250000004, "Sao Tome and Pr\u00edncipe": 1326000.0, "Japan": 4916978.780000001, "Syria": 684766.0, "Honduras": 2773445.0, "Mexico": 891169.54, "Egypt": 2792007.2800000003, "Nicaragua": 22979535.0, "Singapore": 3031000.0, "Botswana": 371145.01, "United Kingdom": 988205404.3500013, "Ivory coast": 473184.86, "Greece": 257091590.73999995, "Paraguay": 23025000.0, "French Guiana": 35551.66, "Comoros": 780000.0}

// Map
//////////////////////////////////////////////////////////////////////////////////////////////////////
function Map () {
	var mapwidth = $("#map").width(),
	    mapheight = mapwidth * 0.6125;
	if (mapheight > 500){
		var mapheight = 500;
	}

	var color = d3.scale.category10();

	var projection = d3.geo.mercator()
	    .center([20, 48])
	    .scale(500 )

	var path = d3.geo.path()
	    .projection(projection);

	var svgmap = d3.select("#map").append("svg")
	    .attr("width", mapwidth)
	    .attr("height", mapheight)

	d3.json("data/world-50m.json", function(error, world) {
	  if (error) throw error;
	  var countries = topojson.feature(world, world.objects.countries).features;

// reused from datamaps
	  svgmap.selectAll(".country")
	      .data(countries)
	    .enter().insert("path", ".graticule")
	    .attr("class", function(d) { 
	      if (EU.indexOf(d.id) !== -1) {
	        return "country " + "EU " + d.id;
	      }
	      else{
	        return "country " +  d.id;
	      }})
	    .attr("d", path)
	    // .on("click", console.log("Test"))

	  svgmap.insert("path", ".graticule")
	      .datum(topojson.mesh(world, world.objects.countries, function(a, b) { return a !== b; }))
	      .attr("class", "boundary")
	      .attr("d", path);
	})

}
//////////////////////////////////////////////////////////////////////////////////////////////////////

// Line chart
//////////////////////////////////////////////////////////////////////////////////////////////////////
function Line () {
// canvas size
	var linemargin = {top: 20, right: 20, bottom: 60, left: 50},
      linewidth = 400 - linemargin.left - linemargin.right,
      lineheight = 250  - linemargin.top - linemargin.bottom;

var parseDate = d3.time.format("%Y%m%d").parse,
	bisectDate = d3.bisector(function(d) { return d[0]; }).left;

// scaling
var x = d3.time.scale()
    .range([0, linewidth]);

var y = d3.scale.linear()
    .range([lineheight, 0]);

var xAxis = d3.svg.axis()
    .scale(x)
    .orient("bottom");

var yAxis = d3.svg.axis()
    .scale(y)
    .orient("left");

// line position
var pos = d3.svg.line()
    .x(function(d) { return x(d[0]); })
    .y(function(d) { return y(d[1]); });

// canvas
var svg = d3.select("#line").append("svg")
    .attr("width", linewidth + linemargin.left + linemargin.right)
    .attr("height", lineheight + linemargin.top + linemargin.bottom)
	.append("g")
    .attr("transform", "translate(" + linemargin.left + "," + linemargin.top + ")");

// import data and draw path and axis
d3.json("data/data.json", function(error, linedata) {
	if (error) throw error;

  linedata.forEach(function(d) {
    d[0] = parseDate(d[0]);
    d[1] = d[1] / 10
  });

  x.domain(d3.extent(linedata, function(d) { return d[0]; }));
  y.domain(d3.extent(linedata, function(d) { return d[1]; }));

svg.append("g")
  .attr("class", "x axis")
  .attr("transform", "translate(0," + lineheight + ")")
  .call(xAxis)
.selectAll("text")
  .attr("y", 5)
  .attr("x", 7)
  .attr("dy", ".35em")
  .attr("transform", "rotate(35)")
  .style("text-anchor", "start")


svg.append("g")
  .attr("class", "y axis")
  .call(yAxis)
.append("text")
  .attr("transform", "rotate(-90)")
  .attr("y", -35)
  .style("text-anchor", "end")
  .text("Temperature")

svg.append("path")
   .datum(linedata)
   .attr("class", "line")
   .attr("d", pos);
var focus = svg.append("g")
   .attr("class", "focus")
   .style("display", "none");


focus.append("line")
   .attr("class", "x")
   .style("stroke", "black")
   .attr("y1", 0)
   .attr("y2", lineheight);

focus.append("line")
   .attr("class", "y")
   .style("stroke", "black")
   .attr("x1", 0)
   .attr("x2", linewidth);

focus.append("text")
    .attr("class", "xt")
    .attr("dx", 8)
    .attr("dy", "-.3em");

focus.append("text")
    .attr("class", "yt")
    .attr("dx", 8)
    .attr("dy", "1em");


// svg.append("rect")
//     .attr("class", "overlay")
//     .attr("width", linewidth)
//     .attr("height", lineheight)
//     .on("mouseover", function() { focus.style("display", null); })
//     .on("mouseout", function() { focus.style("display", "none"); })
//     .on("mousemove", mousemove);


// function mousemove() {
// var x0 = x.invert(d3.mouse(this)[0]),
//     i = bisectDate(linedata, x0, 1),
//     d0 = linedata[i - 1],
//     d1 = linedata[i],
//     d = x0 - d0[0] > d1[0] - x0 ? d1 : d0;

// 	focus.select(".x")
// 	    .attr("transform","translate(" + x(d[0]) + ", 0)")
// 	               .attr("y2", lineheight);

// 	focus.select(".y")
// 	    .attr("transform","translate(0," +
// 	                         y(d[1]) + ")")
// 	               .attr("x2", linewidth);

	      
// 	focus.select("text.xt")
// 	    .attr("transform","translate( 0 ," + y(d[1]) + ")")
// 	    .text(d[1] + " C°");

// 	focus.select("text.yt")
// 	    .attr("transform","translate(" + x(d[0]) + ","+ (lineheight - 20) +")")
// 	    .text(d3.time.format("%d-%m-%Y")(d[0]));
// }
})
}
//////////////////////////////////////////////////////////////////////////////////////////////////////

// Bar chart
//////////////////////////////////////////////////////////////////////////////////////////////////////
function Bar () {
	var barmargin = {top: 20, right: 20, bottom: 30, left: 40},
	    barwidth = 400  - barmargin.left - barmargin.right,
	    barheight = 250  - barmargin.top - barmargin.bottom;

	var x = d3.scale.ordinal()
	    .rangeRoundBands([0, barwidth], .1);

	var y = d3.scale.linear()
	    .range([barheight, 0]);

	var xAxis = d3.svg.axis()
	    .scale(x)
	    .orient("bottom");

	var yAxis = d3.svg.axis()
	    .scale(y)
	    .orient("left")
	    .ticks(10, "%")

	var svg = d3.select("#bar").insert("svg")
	    .attr("width", barwidth + barmargin.left + barmargin.right)
	    .attr("height", barheight + barmargin.top + barmargin.bottom)
	  .append("g")
	    .attr("transform", "translate(" + barmargin.left + "," + barmargin.top + ")");

	d3.tsv("data/barchart.tsv", type, function(error, data) {
	  if (error) throw error;

	  x.domain(data.map(function(d) { return d.letter; }));
	  y.domain([0, d3.max(data, function(d) { return d.frequency; })]);

	  svg.append("g")
	      .attr("class", "x axis")
	      .attr("transform", "translate(0," + barheight + ")")
	      .call(xAxis);

	  svg.append("g")
	      .attr("class", "y axis")
	      .call(yAxis)
	    .append("text")
	      .attr("transform", "rotate(-90)")
	      .attr("y", 6)
	      .attr("dy", ".71em")
	      .style("text-anchor", "end")
	      .text("Frequency")
		.selectAll("text")
		  .style("text-size", "9px");

	  svg.selectAll(".bar")
	      .data(data)
	    .enter().append("rect")
	      .attr("class", "bar")
	      .attr("x", function(d) { return x(d.letter); })
	      .attr("width", x.rangeBand())
	      .attr("y", function(d) { return y(d.frequency); })
	      .attr("height", function(d) { return barheight - y(d.frequency); });
  d3.select("#sort").on("change", change);

  function change() {
    // clearTimeout(sortTimeout);

    // Copy-on-write since tweens are evaluated after a delay.
    var x0 = x.domain(data.sort(this.checked
        ? function(a, b) { return b.frequency - a.frequency; }
        : function(a, b) { return d3.ascending(a.letter, b.letter); })
        .map(function(d) { return d.letter; }))
        .copy();

    svg.selectAll(".bar")
        .sort(function(a, b) { return x0(a.letter) - x0(b.letter); });

    var transition = svg.transition().duration(750),
        delay = function(d, i) { return i * 50; };

    transition.selectAll(".bar")
        .delay(delay)
        .attr("x", function(d) { return x0(d.letter); });

    transition.select(".x.axis")
        .call(xAxis)
      .selectAll("g")
        .delay(delay);
  }
	});

	function type(d) {
	  d.frequency = +d.frequency;
	  return d;
	}


}

// // Downloadbutton
// //////////////////////////////////////////////////////////////////////////////////////////////////////
// var textFile = null,
// 		create = document.getElementById('downloadselection'),
//     textbox = document.getElementById('textbox');

// // https://stackoverflow.com/questions/21012580/is-it-possible-to-write-data-to-file-using-only-javascript
// makeTextFile = function(text) {
//       var data = new Blob([text], {
//         type: 'text/plain'
//       });

//       // If we are replacing a previously generated file we need to
//       // manually revoke the object URL to avoid memory leaks.
//       if (textFile !== null) {
//         window.URL.revokeObjectURL(textFile);
//       }

//       textFile = window.URL.createObjectURL(data);

//       return textFile;
//     };

//    create.addEventListener('click', function() {
//     create.href = makeTextFile(textbox.value);
//   }, false);
// //////////////////////////////////////////////////////////////////////////////////////////////////////
