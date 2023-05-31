/***************************************************************************************
*    Title: Double Histogram
*    Author: Yan Holtz
*    Date: 2018
*    Code version: 4.0
*    Availability: https://d3-graph-gallery.com/graph/histogram_double.html
*    Updated by: Eduardo Morales
*
***************************************************************************************/

// get the data
d3.csv("Data/Samoyed/all_features.csv", function(data) {

    // set the dimensions and margins of the graph
    var margin = {top: 10, right: 30, bottom: 30, left: 40},
    width = 560 - margin.left - margin.right,
    height = 500 - margin.top - margin.bottom;

    // append the svg object to the body of the page
    var svg = d3.select("#chart-histogram-samoyed")
    .append("svg")
    .attr("width", width + margin.left + margin.right)
    .attr("height", height + margin.top + margin.bottom)
    .append("g")
    .attr("transform",
        "translate(" + margin.left + "," + margin.top + ")");

  // X axis
  var x = d3.scaleLinear()
      .domain([0,9])    
      .range([0, width]);
  svg.append("g")
      .attr("transform", "translate(0," + height + ")")
      .call(d3.axisBottom(x));

  // set the parameters for the histogram
  var histogram = d3.histogram()
      .value(function(d) { return +d.value; })   
      .domain(x.domain())  // domain of the graphic
      .thresholds(x.ticks(40)); // numbers of bins

  // get the bins.
  var bins1 = histogram(data.filter( function(d){return d.color == 'reds'} ));
  var bins2 = histogram(data.filter( function(d){return d.color == 'greens'} ));
  var bins3 = histogram(data.filter( function(d){return d.color == 'blues'} ));
  var bins4 = histogram(data.filter( function(d){return d.color == 'whites'} ));
  var bins5 = histogram(data.filter( function(d){return d.color == 'blacks'} ));
  var bins6 = histogram(data.filter( function(d){return d.color == 'browns'} ));

  // Y axis
  var y = d3.scaleLinear()
      .range([height, 0]);
      y.domain([0, d3.max(bins1, function(d) { return d.length; })]); 
  svg.append("g")
      .call(d3.axisLeft(y));

  // append the bars for series 1
  svg.selectAll("rect")
      .data(bins1)
      .enter()
      .append("rect")
        .attr("x", 1)
        .attr("transform", function(d) { return "translate(" + x(d.x0) + "," + y(d.length) + ")"; })
        .attr("width", function(d) { return x(d.x1) - x(d.x0) -1 ; })
        .attr("height", function(d) { return height - y(d.length); })
        .style("fill", "red")
        .style("opacity", 0.4)

  // append the bars for series 2
  svg.selectAll("rect2")
      .data(bins2)
      .enter()
      .append("rect")
        .attr("x", 1)
        .attr("transform", function(d) { return "translate(" + x(d.x0) + "," + y(d.length) + ")"; })
        .attr("width", function(d) { return x(d.x1) - x(d.x0) -1 ; })
        .attr("height", function(d) { return height - y(d.length); })
        .style("fill", "green")
        .style("opacity", 0.4)

    // append the bars for series 3
    svg.selectAll("rect3")
    .data(bins3)
    .enter()
    .append("rect")
        .attr("x", 1)
        .attr("transform", function(d) { return "translate(" + x(d.x0) + "," + y(d.length) + ")"; })
        .attr("width", function(d) { return x(d.x1) - x(d.x0) -1 ; })
        .attr("height", function(d) { return height - y(d.length); })
        .style("fill", "blue")
        .style("opacity", 0.4)

    // append the bars for series 4
    svg.selectAll("rect4")
        .data(bins4)
        .enter()
        .append("rect")
            .attr("x", 1)
            .attr("transform", function(d) { return "translate(" + x(d.x0) + "," + y(d.length) + ")"; })
            .attr("width", function(d) { return x(d.x1) - x(d.x0) -1 ; })
            .attr("height", function(d) { return height - y(d.length); })
            .style("fill", "gray")
            .style("opacity", 0.4)

    // append the bars for series 5
    svg.selectAll("rect5")
    .data(bins5)
    .enter()
    .append("rect")
        .attr("x", 1)
        .attr("transform", function(d) { return "translate(" + x(d.x0) + "," + y(d.length) + ")"; })
        .attr("width", function(d) { return x(d.x1) - x(d.x0) -1 ; })
        .attr("height", function(d) { return height - y(d.length); })
        .style("fill", "black")
        .style("opacity", 0.4)

    // append the bars for series 6
    svg.selectAll("rect6")
        .data(bins6)
        .enter()
        .append("rect")
            .attr("x", 1)
            .attr("transform", function(d) { return "translate(" + x(d.x0) + "," + y(d.length) + ")"; })
            .attr("width", function(d) { return x(d.x1) - x(d.x0) -1 ; })
            .attr("height", function(d) { return height - y(d.length); })
            .style("fill", "brown")
            .style("opacity", 0.4)

  // legend
  svg.append("circle").attr("cx",10).attr("cy",30).attr("r", 6).style("fill", "red")
  svg.append("circle").attr("cx",10).attr("cy",60).attr("r", 6).style("fill", "green")
  svg.append("circle").attr("cx",10).attr("cy",90).attr("r", 6).style("fill", "blue")
  svg.append("circle").attr("cx",10).attr("cy",120).attr("r", 6).style("fill", "gray")
  svg.append("circle").attr("cx",10).attr("cy",150).attr("r", 6).style("fill", "black")
  svg.append("circle").attr("cx",10).attr("cy",180).attr("r", 6).style("fill", "brown")
  svg.append("text").attr("x", 20).attr("y", 30).text("Reds").style("font-size", "15px").attr("alignment-baseline","middle")
  svg.append("text").attr("x", 20).attr("y", 60).text("Greens").style("font-size", "15px").attr("alignment-baseline","middle")
  svg.append("text").attr("x", 20).attr("y", 90).text("Blues").style("font-size", "15px").attr("alignment-baseline","middle")
  svg.append("text").attr("x", 20).attr("y", 120).text("Whites").style("font-size", "15px").attr("alignment-baseline","middle")
  svg.append("text").attr("x", 20).attr("y", 150).text("Blacks").style("font-size", "15px").attr("alignment-baseline","middle")
  svg.append("text").attr("x", 20).attr("y", 180).text("Browns").style("font-size", "15px").attr("alignment-baseline","middle")

});

// get the data
d3.csv("Data/Xoloitzquintle/all_features.csv", function(data) {

    // set the dimensions and margins of the graph
    var margin = {top: 10, right: 30, bottom: 30, left: 40},
        width = 560 - margin.left - margin.right,
        height = 500 - margin.top - margin.bottom;
    
    // append the svg object to the body of the page
    var svg = d3.select("#chart-histogram-xolo")
        .append("svg")
        .attr("width", width + margin.left + margin.right)
        .attr("height", height + margin.top + margin.bottom)
        .append("g")
        .attr("transform",
            "translate(" + margin.left + "," + margin.top + ")");

    // X axis
    var x = d3.scaleLinear()
        .domain([0,9])    
        .range([0, width]);
    svg.append("g")
        .attr("transform", "translate(0," + height + ")")
        .call(d3.axisBottom(x));
  
    // set the parameters for the histogram
    var histogram = d3.histogram()
        .value(function(d) { return +d.value; }) 
        .domain(x.domain())  // domain of the graphic
        .thresholds(x.ticks(40)); // numbers of bins
  
    // get the bins.
    var bins1 = histogram(data.filter( function(d){return d.color == 'reds'} ));
    var bins2 = histogram(data.filter( function(d){return d.color == 'greens'} ));
    var bins3 = histogram(data.filter( function(d){return d.color == 'blues'} ));
    var bins4 = histogram(data.filter( function(d){return d.color == 'whites'} ));
    var bins5 = histogram(data.filter( function(d){return d.color == 'blacks'} ));
    var bins6 = histogram(data.filter( function(d){return d.color == 'browns'} ));
  
    // Y axis
    var y = d3.scaleLinear()
        .range([height, 0]);
        y.domain([0, 80]);  
    svg.append("g")
        .call(d3.axisLeft(y));
  
    // append the bars for series 1
    svg.selectAll("rect")
        .data(bins1)
        .enter()
        .append("rect")
          .attr("x", 1)
          .attr("transform", function(d) { return "translate(" + x(d.x0) + "," + y(d.length) + ")"; })
          .attr("width", function(d) { return x(d.x1) - x(d.x0) -1 ; })
          .attr("height", function(d) { return height - y(d.length); })
          .style("fill", "red")
          .style("opacity", 0.4)
  
    // append the bars for series 2
    svg.selectAll("rect2")
        .data(bins2)
        .enter()
        .append("rect")
          .attr("x", 1)
          .attr("transform", function(d) { return "translate(" + x(d.x0) + "," + y(d.length) + ")"; })
          .attr("width", function(d) { return x(d.x1) - x(d.x0) -1 ; })
          .attr("height", function(d) { return height - y(d.length); })
          .style("fill", "green")
          .style("opacity", 0.4)
  
      // append the bars for series 3
      svg.selectAll("rect3")
      .data(bins3)
      .enter()
      .append("rect")
          .attr("x", 1)
          .attr("transform", function(d) { return "translate(" + x(d.x0) + "," + y(d.length) + ")"; })
          .attr("width", function(d) { return x(d.x1) - x(d.x0) -1 ; })
          .attr("height", function(d) { return height - y(d.length); })
          .style("fill", "blue")
          .style("opacity", 0.4)
  
      // append the bars for series 4
      svg.selectAll("rect4")
          .data(bins4)
          .enter()
          .append("rect")
              .attr("x", 1)
              .attr("transform", function(d) { return "translate(" + x(d.x0) + "," + y(d.length) + ")"; })
              .attr("width", function(d) { return x(d.x1) - x(d.x0) -1 ; })
              .attr("height", function(d) { return height - y(d.length); })
              .style("fill", "gray")
              .style("opacity", 0.4)
  
      // append the bars for series 5
      svg.selectAll("rect5")
      .data(bins5)
      .enter()
      .append("rect")
          .attr("x", 1)
          .attr("transform", function(d) { return "translate(" + x(d.x0) + "," + y(d.length) + ")"; })
          .attr("width", function(d) { return x(d.x1) - x(d.x0) -1 ; })
          .attr("height", function(d) { return height - y(d.length); })
          .style("fill", "black")
          .style("opacity", 0.4)
  
      // append the bars for series 6
      svg.selectAll("rect6")
          .data(bins6)
          .enter()
          .append("rect")
              .attr("x", 1)
              .attr("transform", function(d) { return "translate(" + x(d.x0) + "," + y(d.length) + ")"; })
              .attr("width", function(d) { return x(d.x1) - x(d.x0) -1 ; })
              .attr("height", function(d) { return height - y(d.length); })
              .style("fill", "brown")
              .style("opacity", 0.4)
  
    // legend
    svg.append("circle").attr("cx",10).attr("cy",30).attr("r", 6).style("fill", "red")
    svg.append("circle").attr("cx",10).attr("cy",60).attr("r", 6).style("fill", "green")
    svg.append("circle").attr("cx",10).attr("cy",90).attr("r", 6).style("fill", "blue")
    svg.append("circle").attr("cx",10).attr("cy",120).attr("r", 6).style("fill", "gray")
    svg.append("circle").attr("cx",10).attr("cy",150).attr("r", 6).style("fill", "black")
    svg.append("circle").attr("cx",10).attr("cy",180).attr("r", 6).style("fill", "brown")
    svg.append("text").attr("x", 20).attr("y", 30).text("Reds").style("font-size", "15px").attr("alignment-baseline","middle")
    svg.append("text").attr("x", 20).attr("y", 60).text("Greens").style("font-size", "15px").attr("alignment-baseline","middle")
    svg.append("text").attr("x", 20).attr("y", 90).text("Blues").style("font-size", "15px").attr("alignment-baseline","middle")
    svg.append("text").attr("x", 20).attr("y", 120).text("Whites").style("font-size", "15px").attr("alignment-baseline","middle")
    svg.append("text").attr("x", 20).attr("y", 150).text("Blacks").style("font-size", "15px").attr("alignment-baseline","middle")
    svg.append("text").attr("x", 20).attr("y", 180).text("Browns").style("font-size", "15px").attr("alignment-baseline","middle")
  
  });

  // get the data
d3.csv("Data/Pomeranian/all_features.csv", function(data) {

    // set the dimensions and margins of the graph
    var margin = {top: 10, right: 30, bottom: 30, left: 40},
        width = 560 - margin.left - margin.right,
        height = 500 - margin.top - margin.bottom;

    // append the svg object to the body of the page
    var svg = d3.select("#chart-histogram-pomeranian")
        .append("svg")
        .attr("width", width + margin.left + margin.right)
        .attr("height", height + margin.top + margin.bottom)
        .append("g")
        .attr("transform",
            "translate(" + margin.left + "," + margin.top + ")");

    // X axis
    var x = d3.scaleLinear()
        .domain([0,9])    
        .range([0, width]);
    svg.append("g")
        .attr("transform", "translate(0," + height + ")")
        .call(d3.axisBottom(x));
  
    // set the parameters for the histogram
    var histogram = d3.histogram()
        .value(function(d) { return +d.value; }) 
        .domain(x.domain())  // domain of the graphic
        .thresholds(x.ticks(40)); // numbers of bins
  
    // get the bins.
    var bins1 = histogram(data.filter( function(d){return d.color == 'reds'} ));
    var bins2 = histogram(data.filter( function(d){return d.color == 'greens'} ));
    var bins3 = histogram(data.filter( function(d){return d.color == 'blues'} ));
    var bins4 = histogram(data.filter( function(d){return d.color == 'whites'} ));
    var bins5 = histogram(data.filter( function(d){return d.color == 'blacks'} ));
    var bins6 = histogram(data.filter( function(d){return d.color == 'browns'} ));
  
    // Y axis
    var y = d3.scaleLinear()
        .range([height, 0]);
        y.domain([0, 1500]);   
    svg.append("g")
        .call(d3.axisLeft(y));
  
    // append the bars for series 1
    svg.selectAll("rect")
        .data(bins1)
        .enter()
        .append("rect")
          .attr("x", 1)
          .attr("transform", function(d) { return "translate(" + x(d.x0) + "," + y(d.length) + ")"; })
          .attr("width", function(d) { return x(d.x1) - x(d.x0) -1 ; })
          .attr("height", function(d) { return height - y(d.length); })
          .style("fill", "red")
          .style("opacity", 0.4)
  
    // append the bars for series 2
    svg.selectAll("rect2")
        .data(bins2)
        .enter()
        .append("rect")
          .attr("x", 1)
          .attr("transform", function(d) { return "translate(" + x(d.x0) + "," + y(d.length) + ")"; })
          .attr("width", function(d) { return x(d.x1) - x(d.x0) -1 ; })
          .attr("height", function(d) { return height - y(d.length); })
          .style("fill", "green")
          .style("opacity", 0.4)
  
      // append the bars for series 3
      svg.selectAll("rect3")
      .data(bins3)
      .enter()
      .append("rect")
          .attr("x", 1)
          .attr("transform", function(d) { return "translate(" + x(d.x0) + "," + y(d.length) + ")"; })
          .attr("width", function(d) { return x(d.x1) - x(d.x0) -1 ; })
          .attr("height", function(d) { return height - y(d.length); })
          .style("fill", "blue")
          .style("opacity", 0.4)
  
      // append the bars for series 4
      svg.selectAll("rect4")
          .data(bins4)
          .enter()
          .append("rect")
              .attr("x", 1)
              .attr("transform", function(d) { return "translate(" + x(d.x0) + "," + y(d.length) + ")"; })
              .attr("width", function(d) { return x(d.x1) - x(d.x0) -1 ; })
              .attr("height", function(d) { return height - y(d.length); })
              .style("fill", "gray")
              .style("opacity", 0.4)
  
      // append the bars for series 5
      svg.selectAll("rect5")
      .data(bins5)
      .enter()
      .append("rect")
          .attr("x", 1)
          .attr("transform", function(d) { return "translate(" + x(d.x0) + "," + y(d.length) + ")"; })
          .attr("width", function(d) { return x(d.x1) - x(d.x0) -1 ; })
          .attr("height", function(d) { return height - y(d.length); })
          .style("fill", "black")
          .style("opacity", 0.4)
  
      // append the bars for series 6
      svg.selectAll("rect6")
          .data(bins6)
          .enter()
          .append("rect")
              .attr("x", 1)
              .attr("transform", function(d) { return "translate(" + x(d.x0) + "," + y(d.length) + ")"; })
              .attr("width", function(d) { return x(d.x1) - x(d.x0) -1 ; })
              .attr("height", function(d) { return height - y(d.length); })
              .style("fill", "brown")
              .style("opacity", 0.4)
  
    // legend
    svg.append("circle").attr("cx",10).attr("cy",30).attr("r", 6).style("fill", "red")
    svg.append("circle").attr("cx",10).attr("cy",60).attr("r", 6).style("fill", "green")
    svg.append("circle").attr("cx",10).attr("cy",90).attr("r", 6).style("fill", "blue")
    svg.append("circle").attr("cx",10).attr("cy",120).attr("r", 6).style("fill", "gray")
    svg.append("circle").attr("cx",10).attr("cy",150).attr("r", 6).style("fill", "black")
    svg.append("circle").attr("cx",10).attr("cy",180).attr("r", 6).style("fill", "brown")
    svg.append("text").attr("x", 20).attr("y", 30).text("Reds").style("font-size", "15px").attr("alignment-baseline","middle")
    svg.append("text").attr("x", 20).attr("y", 60).text("Greens").style("font-size", "15px").attr("alignment-baseline","middle")
    svg.append("text").attr("x", 20).attr("y", 90).text("Blues").style("font-size", "15px").attr("alignment-baseline","middle")
    svg.append("text").attr("x", 20).attr("y", 120).text("Whites").style("font-size", "15px").attr("alignment-baseline","middle")
    svg.append("text").attr("x", 20).attr("y", 150).text("Blacks").style("font-size", "15px").attr("alignment-baseline","middle")
    svg.append("text").attr("x", 20).attr("y", 180).text("Browns").style("font-size", "15px").attr("alignment-baseline","middle")
  
  });