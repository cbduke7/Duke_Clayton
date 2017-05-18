var canvas = document.getElementById("canvasMaze");
context = canvas.getContext("2d");
var currRectX = 425;
var currrRecty = 3;
var mazeWidth = 400;
var mazeHeight = 400;
var intervalvar;
function drawMazeAndRectangle(rectX, rectY) {
    makeWhite(0, 0, canvas.width, canvas.height);
    var mazeImg =new Image();
    maze.Img.onLoad = function() {
        context.drawImage(mazeImg, 0, 0);
    }
}