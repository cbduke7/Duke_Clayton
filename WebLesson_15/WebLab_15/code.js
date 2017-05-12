function shapes(){
	var	x = document.getElementById("canvas");
	canvas = x.getContext("2d");
	canvas.fillStyle = "blue";
	canvas.strokeStyle = "red";
	
	canvas.fillRect(10, 10, 100, 200);
	canvas.strokeRect(10, 10, 100, 200);
	canvas.clearRect(35, 35, 50, 100);
}

window.addEventListner("load", shapes, false);
