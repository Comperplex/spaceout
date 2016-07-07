var updateCanvasSize = function(){
	$('#gameCanvas').width($(window).width());
	$('#gameCanvas').height($(window).height());
};
$(document).ready(updateCanvasSize);
$(window).resize(updateCanvasSize);


$(document).ready(function(){
	var $canvas = $('#gameCanvas');

});
