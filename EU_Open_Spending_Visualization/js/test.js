var EU = [40,56,100,196,203,208,233,246,250,276,300,348,191,372,380,428,440,442,470,528,616,620,642,703,705,724,752,826]var width = 960,
    height = 580;

var color = d3.scale.category10();

var projection = d3.geo.mercator()
    .center([18, 53])
    .scale(500 )

var path = d3.geo.path()
    .projection(projection);

var graticule = d3.geo.graticule();

var svg = d3.select("body").append("svg")
    .attr("width", width)
    .attr("height", height);

svg.append("defs").append("path")
    .datum({type: "Sphere"})
    .attr("id", "sphere")
    .attr("d", path);

d3.json("data/world-50m.json", function(error, world) {
  if (error) throw error;
  var countries = topojson.feature(world, world.objects.countries).features;

  svg.selectAll(".country")
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

  svg.insert("path", ".graticule")
      .datum(topojson.mesh(world, world.objects.countries, function(a, b) { return a !== b; }))
      .attr("class", "boundary")
      .attr("d", path);
})