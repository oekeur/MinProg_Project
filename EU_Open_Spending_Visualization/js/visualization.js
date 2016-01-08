window.onload = function()
{
	Map(),
	Bar ();
	Line();
}

var EU = [40,56,100,196,203,208,233,246,250,276,300,348,191,372,380,428,440,442,470,528,616,620,642,703,705,724,752,826]
var data;

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
	    .call(d3.behavior.zoom()
	    .on("zoom", redraw))

// http://techslides.com/d3-world-maps-tooltips-zooming-and-queue
function redraw() {
    svgmap.attr("transform", "translate(" + d3.event.translate + ")scale(" + d3.event.scale + ")");
}

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

	var svg = d3.select("#bar").append("svg")
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
	});

	function type(d) {
	  d.frequency = +d.frequency;
	  return d;
	}

}

