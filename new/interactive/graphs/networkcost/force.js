// We load the d3.js library from the Web.
require.config({paths: {d3: "http://d3js.org/d3.v3.min"}});
require(["d3"], function(d3) {
    // The code in this block is executed when the 
    // d3.js library has been loaded.
    
    // First, we specify the size of the canvas containing
    // the visualization (size of the <div> element).
    var width = 300,
        height = 300;

    // We create a color scale.
    var color = d3.scale.category20();

    // We create a force-directed dynamic graph layout.
    var force = d3.layout.force()
        .charge(-50)
        .linkDistance(40)
        .linkStrength(0.9)
        .gravity(0.15)
        .theta(0.95)
        .size([width, height]);

    // In the <div> element, we create a <svg> graphic
    // that will contain our interactive visualization.
    var svg = d3.select("#d3-example").select("svg")
    if (svg.empty()) {
        svg = d3.select("#d3-example").append("svg")
                    .attr("width", width)
                    .attr("height", height);
    }
        
    // We load the JSON file.
    d3.json("graph.json?nocache=" + (new Date()).getTime(), function(error, graph) {
        // In this block, the file has been loaded
        // and the 'graph' object contains our graph.
        
        // We load the nodes and links in the force-directed
        // graph.
        force.nodes(graph.nodes)
            .links(graph.links)
            .start();

				// From:
				// http://logogin.blogspot.com/2013/02/d3js-arrowhead-markers.html
				svg.append("defs").append("marker")
									.attr("id", "arrowhead")
									.attr("refX", 6 + 3) /*must be smarter way to calculate shift*/
									.attr("refY", 2)
									.attr("markerWidth", 6)
									.attr("markerHeight", 4)
									.attr("orient", "auto")
									.append("path")
											.attr("d", "M 0,0 V 4 L6,2 Z"); //this is actual shape for arrowhead
			
        // We create a <line> SVG element for each link
        // in the graph.
        var link = svg.selectAll(".link")
            .data(graph.links)
            .enter().append("line")
            .attr("class", "link");
            //.style("stroke-width", function(d) { return Math.sqrt(d.value); });


        // We create a <circle> SVG element for each node
        // in the graph, and we specify a few attributes.
        var node = svg.selectAll(".node")
            .data(graph.nodes)
            .enter().append("circle")
            .attr("class", "node")
            .attr("r", function(d) { return Math.log(d.value+1)+3; })  // radius  .attr("r", 5) 
            .style("fill", function(d) {
                // The node color depends on the club.
                return color(d.group); 
            })
            .call(force.drag);

				if (graph.directed){
				  	link.attr("marker-end", "url(#arrowhead)");
					  //.attr("d", diagonal);
				}

        // The name of each node is the node number.
        node.append("title")
            .text(function(d) { return d.name; });

        // We bind the positions of the SVG elements
        // to the positions of the dynamic force-directed graph,
        // at each time step.
        force.on("tick", function() {
            link.attr("x1", function(d) { return d.source.x; })
                .attr("y1", function(d) { return d.source.y; })
                .attr("x2", function(d) { return d.target.x; })
                .attr("y2", function(d) { return d.target.y; });

            node.attr("cx", function(d) { return d.x; })
                .attr("cy", function(d) { return d.y; });
        });
    });
});
