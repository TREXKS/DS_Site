

// Initialize data
loadData();

// FIFA world cup
var data;

// Load CSV file
function loadData() {

  d3.csv("static/data/sensorData.csv", function(data){

      data.forEach(function(d) {
        d.daysPast = parseFloat(d.daysPast);
        d.airTemp = parseFloat(d.airTemp);
      });

    var data = d3.nest()
        .sortKeys((a, b) => a - b)
        .entries(data);

        console.log(data)


		// Draw the visualization for the first time
		updateVisualization();
	});
}

// Scales
var yScale = d3.scaleLinear()
  .domain([50,
          d3.max(data, function(d) { return d.airTemp})])
  .range([ height, 0 ]);


var xScale = d3.scaleLinear()
.domain([d3.min(data, function(d) { return d.daysPast;}),
        d3.max(data, function(d) { return d.daysPast})])
.range([ padding, width]);

// Axes

var xAxis = d3.axisBottom()
	.scale(xScale);

var yAxis = d3.axisBottom()
	.scale(yScale)


// Render visualization
function updateVisualization() {


	xScale.domain([d3.min(data, function(d) { return (d.YEAR)}),
								d3.max(data, function(d) { return (d.YEAR)})]);

  yScale.domain([0, d3.max(data, function(d) { return d.GOALS })]);


	var selectBox = d3.select("#dash-type");


    svg.append("g")
 	 	.style("font-size", "15" )
 	 	.attr("transform", "translate(50,0)")
    .style("stroke", "#77A88B")
 	   .call(d3.axisLeft(yScale).ticks(3));

  var area = d3.area()
      .x(function(d) { return xScale(d.daysPast); })
      .y0(height)
      .y1(function(d) { return yScale(d.airTemp); });

// append LINE
svg.append("path")
    .datum(data)
    .style("fill","#77A88B")
    .attr("class", "area")
    .attr("d", area)

		// svg.append("g")
		// 		.attr("class", "axis x-axis")
		// 	.attr("transform", "translate(5,420)")
		// 	.call(xAxis);
    //
		// svg.append("g")
		// 		.attr("class", "axis y-axis")
		//    .call(yAxis)

	console.log(data);



// WHEN RANKING TYPE IS selected
		d3.select("#dash-type")
	    .on("change", function(d) {
	      console.log()

	      function rescale() {
        //
	      //   yScale.domain([0, d3.max(data, function(d) {
	      //     if (selectBox.property('value') == 'GOALS')
	      //       return   d.GOALS
	      //     if (selectBox.property('value') == 'AVERAGE_GOALS')
	      //       return d.AVERAGE_GOALS
				// 		if (selectBox.property('value') == 'MATCHES')
				// 			return   d.MATCHES
				// 		if (selectBox.property('value') == 'TEAMS')
				// 			return d.TEAMS
				// 		if (selectBox.property('value') == 'AVERAGE_ATTENDANCE')
				// 			return   d.AVERAGE_ATTENDANCE
				// 		})]);
        //
				// 		var line = d3.line()
				// 			.x(function(d) { return xScale(d.YEAR); })
				// 			.y(function(d) {
				// 				if (selectBox.property('value') == 'GOALS')
			  //           return   yScale(d.GOALS)
			  //         if (selectBox.property('value') == 'AVERAGE_GOALS')
			  //           return yScale(d.AVERAGE_GOALS)
				// 				if (selectBox.property('value') == 'MATCHES')
				// 					return   yScale(d.MATCHES)
				// 				if (selectBox.property('value') == 'TEAMS')
				// 					return yScale(d.TEAMS)
				// 				if (selectBox.property('value') == 'AVERAGE_ATTENDANCE')
				// 					return   yScale(d.AVERAGE_ATTENDANCE)
        //
				// 			 })
        //
				// 	 svg.select("g.axis.y-axis")
				// 	   .call(yAxis);
        //
				// 		group.selectAll("path")
				// 		  	.datum(data)
				// 				.transition()
				// 				.duration(2000)
				// 				.attr("d", line);
        //
				// 		svg.selectAll('circle')
				// 			.data(data)
				// 			.transition()
				// 			.duration(2000)
				// 			.attr("cx", function(d) { return xScale(d.YEAR)})
				// 			.attr("cy", function(d) {
				// 				if (selectBox.property('value') == 'GOALS')
				// 					return   yScale(d.GOALS)
				// 				if (selectBox.property('value') == 'AVERAGE_GOALS')
				// 					return yScale(d.AVERAGE_GOALS)
				// 				if (selectBox.property('value') == 'MATCHES')
				// 					return   yScale(d.MATCHES)
				// 				if (selectBox.property('value') == 'TEAMS')
				// 					return yScale(d.TEAMS)
				// 				if (selectBox.property('value') == 'AVERAGE_ATTENDANCE')
				// 					return   yScale(d.AVERAGE_ATTENDANCE)
				// 			})
        //
				// 			.attr("r", 6)
				// 			.attr("fill", "blue")
				// 			.on("click", function(d) {
				// 				d3.select(this)
				// 					.attr("r", 10)
				// 					.attr("fill", "red")
				// 					 showEdition(d)
				// 			})
	      // }
	      rescale();
	  });

}
