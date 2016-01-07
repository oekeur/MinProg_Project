var EU = [40,56,100,196,203,208,233,246,250,276,300,348,191,372,380,428,440,442,470,528,616,620,642,703,705,724,752,826]
var data;

// Map
//////////////////////////////////////////////////////////////////////////////////////////////////////
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

var zoom = d3.behavior.zoom()
    .translate(projection.translate())
    .scale(projection.scale())
    .scaleExtent([mapheight, 8 * mapheight])
    .on("zoom", zoomed);

var svgmap = d3.select("#map").append("svg")
    .attr("width", mapwidth)
    .attr("height", mapheight)
    .call(zoom);


d3.json("data/world-50m.json", function(error, world) {
  if (error) throw error;
  var countries = topojson.feature(world, world.objects.countries).features;

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

  svgmap.insert("path", ".graticule")
      .datum(topojson.mesh(world, world.objects.countries, function(a, b) { return a !== b; }))
      .attr("class", "boundary")
      .attr("d", path);
})

function zoomed() {
  projection.translate(d3.event.translate).scale(d3.event.scale);
  svgmap.selectAll("path").attr("d", path);
}
//////////////////////////////////////////////////////////////////////////////////////////////////////

// Line chart
//////////////////////////////////////////////////////////////////////////////////////////////////////

// // Set the dimensions of the canvas / graph
// var	linemargin = {top: 30, right: 20, bottom: 30, left: 50},
// 	linewidth = 400 - linemargin.left - linemargin.right,
// 	lineheight = 220 - linemargin.top - linemargin.bottom;

// // Parse the date / time
// var	parseDate = d3.time.format("%d-%b-%y").parse;

// // Set the ranges
// var	x = d3.time.scale().range([0, linewidth]);
// var	y = d3.scale.linear().range([lineheight, 0]);

// // Define the axes
// var	xAxis = d3.svg.axis().scale(x)
// 	.orient("bottom").ticks(5);

// var	yAxis = d3.svg.axis().scale(y)
// 	.orient("left").ticks(5);

// // Define the line
// var	valueline = d3.svg.line()
// 	.x(function(d) { return x(d.date); })
// 	.y(function(d) { return y(d.close); });
    
// // Adds the svg canvas
// var	chart1 = d3.select("#barchart")
// 	.append("svg")
// 		.attr("width", linewidth + linemargin.left + linemargin.right)
// 		.attr("height", lineheight + linemargin.top + linemargin.bottom)
// 	.append("g")
// 		.attr("transform", "translate(" + linemargin.left + "," + linemargin.top + ")");

// // Get the data
// d3.csv("data/data1.csv", function(error, data) {
// 	data.forEach(function(d) {
// 		d.date = parseDate(d.date);
// 		d.close = +d.close;
// 	});

// 	// Scale the range of the data
// 	x.domain(d3.extent(data, function(d) { return d.date; }));
// 	y.domain([0, d3.max(data, function(d) { return d.close; })]);

// 	// Add the valueline path.
// 	chart1.append("path")
// 		.attr("class", "line")
// 		.attr("d", valueline(data));

// 	// Add the X Axis
// 	chart1.append("g")
// 		.attr("class", "x axis")
// 		.attr("transform", "translate(0," + lineheight + ")")
// 		.call(xAxis);

// 	// Add the Y Axis
// 	chart1.append("g")
// 		.attr("class", "y axis")
// 		.call(yAxis);

// });

// // Adds the svg canvas
// var	chart2 = d3.select("#linechart")
// 	.append("svg")
// 		.attr("width", linewidth + linemargin.left + linemargin.right)
// 		.attr("height", lineheight + linemargin.top + linemargin.bottom)
// 	.append("g")
// 		.attr("transform", "translate(" + linemargin.left + "," + linemargin.top + ")");
		
// // Get the data
// d3.csv("data/data2.csv", function(error, data) {
// 	data.forEach(function(d) {
// 		d.date = parseDate(d.date);
// 		d.close = +d.close;
// 	});

// 	// Scale the range of the data
// 	x.domain(d3.extent(data, function(d) { return d.date; }));
// 	y.domain([0, d3.max(data, function(d) { return d.close; })]);

// 	// Add the valueline path.
// 	chart2.append("path")
// 		.attr("class", "line")
// 		.attr("d", valueline(data));

// 	// Add the X Axis
// 	chart2.append("g")
// 		.attr("class", "x axis")
// 		.attr("transform", "translate(0," + lineheight + ")")
// 		.call(xAxis);

// 	// Add the Y Axis
// 	chart2.append("g")
// 		.attr("class", "y axis")
// 		.call(yAxis);

// });
// //////////////////////////////////////////////////////////////////////////////////////////////////////
