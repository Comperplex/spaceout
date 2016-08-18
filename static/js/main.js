$(document).ready(function(){
	var $map = $('#gameArea');

	function pm(input, margin=1){ // plus or minus a random number by a specified margin
		return input + (Math.random() * (margin * 2)) - margin;
	}

	function getAngle(v){ // get the angle given an x,y vector
		return (Math.atan2(v[1], v[0]) * (180 / Math.PI)) + 90;
	}

	function addDrone(obj){
		var $drone = $("<svg id=\""+obj.ID+"\" width=\"20px\" height=\"20px\" viewBox=\"0 0 10 10\">\n<polygon fill=\"#33f\" stroke=\"#00c\" stroke-width=\"1\" stroke-linejoin=\"round\" points=\"5,0.5 0.5,9.5 5,8 9.5,9.5 5,0.5\"></polygon>\n</svg>");
		$drone.css({
			left: obj.loc[0]+'px',
			top: obj.loc[1]+'px',
			transform: 'rotate('+getAngle(obj.velocity)+'deg)'
		});
		return $drone;
	}

	function addBeacon(obj){
		var beacon = $("<svg width=\"400px\" height=\"400px\" viewBox=\"0 0 10 10\">\n<circle cx=\"5\" cy=\"5\" r=\"4.75\" stroke=\"#667\" stroke-width=\"0.5\" fill=\"#99a\" stroke-linejoin=\"round\" />\n</svg>";)
		$beacon.css({
			left: obj.loc[0]+'px',
			top: obj.loc[1]+'px'
		});
		return $beacon;
	}

	function addAsteroid(loc, id){
		var points = pm(10)+","+pm(1)+" "+pm(16)+","+pm(4)+" "+pm(19)+","+pm(10)+" "+pm(16)+","+pm(16)+" "+pm(10)+","+pm(19)+" "+pm(4)+","+pm(16)+" "+pm(1)+","+pm(10)+" "+pm(4)+","+pm(4);
		var $asteroid = $("<svg width=\"10px\" height=\"10px\" viewBox=\"0 0 20 20\">\n<polygon fill=\"#f33\" stroke=\"#c00\" stroke-width=\"4\" stroke-linejoin=\"round\" points=\""+points+"\"></polygon>\n</svg>");
		$asteroid.css({
			left: obj.loc[0]+'px',
			top: obj.loc[1]+'px'
		});
		return $asteroid;
	}

	function writeMsg(msg){
		$.get('/api/writeMsg', {'msg':msg});
	}

	function drawMap(){
		$.get('/api/getMap', function(gameMapStr){
			gameMap = JSON.parse(gameMapStr);
			gameMap.forEach(function(obj){
				writeMsg($('#'+obj.ID).length);
				if ($('#'+obj.ID).length){
					$('#'+obj.ID).css({
						'left':obj.loc[0]+'px',
						'top':obj.loc[1]+'px',
						'transform':'rotate('+getAngle(obj.velocity)+'deg)'
					});
				} else {
					switch (obj.objectType){
						case 'drone':
							$map.append(addDrone(obj));
							break;
						case 'beacon':
							$map.append(addBeacon(obj));
							break;
						case 'asteroid':
							$map.append(addAsteroid([50,50], 'asteroid 1'))
							break;
					}
				}
			});
		});
	};

	function runGame(tickFreq=1){
		var tickCount = 0;

		window.gameLoop = window.setInterval(function(){
			drawMap();
			tickCount += 1;
		}, tickFreq*5000);
	}

	runGame();
});
