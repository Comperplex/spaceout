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
			x: obj.loc[0], y: obj.loc[1],
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
			x: 100, y: 100,
			width: 100, height: 100
		}
	}

	$canvas = $('#gameCanvas');

	$.get('/api/getMap', function(gameMapStr){
		gameMap = JSON.parse(gameMapStr);
		console.dir(gameMap);
		gameMap.forEach(function(obj){
			if (obj.objectType == 'drone'){
				$canvas.drawPath(shapes.drone);
			} else if (obj.objectType == 'beacon'){
				$canvas.drawEllipse(shapes.beacon);
			} else if (obj.objectType == 'asteroid'){
				$canvas.drawEllipse(shapes.asteroid);
			}
		});
	});
});
