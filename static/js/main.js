updateCanvasSize = function(){
	var canvas = document.getElementById('gameCanvas');
	canvas.width = $(window).width();
	canvas.height = $(window).height();
};

$(document).ready(function(){
	$(window).resize(updateCanvasSize);
	updateCanvasSize();

	shapes = {
		'drone': {
			strokeStyle: '#00c',
			strokeWidth: 2,
			fillStyle: '#33f',
			radius: 10,
			sides: 3,
			p1: {
				type: 'line',
				x1:0,  y1:-10,
				x2:-10,y2:10,
				x3:0,  y3:8,
				x4:10, y4:10,
				x5:0,  y5:-10
			}
		},
		'beacon': {
			strokeStyle: '#667',
			strokeWidth: 4,
			fillStyle: '#99a',
			width: 100, height: 100
		}
	}

	function drawMap(){
		$.get('/api/getMap', function(gameMapStr){
			gameMap = JSON.parse(gameMapStr);
			console.dir(gameMap);
			gameMap.forEach(function(obj){
				if (obj.objectType == 'drone'){
					drone = shapes.drone;
					drone.x = obj.loc[0];
					drone.y = obj.loc[1];
					$canvas.drawPath(drone);
				} else if (obj.objectType == 'beacon'){
					beacon = shapes.beacon;
					beacon.x = obj.loc[0];
					beacon.y = obj.loc[1];
					$canvas.drawEllipse(shapes.beacon);
				} else if (obj.objectType == 'asteroid'){
					asteroid = shapes.asteroid;
					asteroid.x = obj.loc[0];
					asteroid.y = obj.loc[1];
					$canvas.drawEllipse(shapes.asteroid);
				}
			});
		});
	};

	$canvas = $('#gameCanvas');
	drawMap();
	$.get('/api/addObj');

	
});
