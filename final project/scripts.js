var canvas = document.getElementById("canvasMaze");
context = canvas.getContext("2d");
var currRectX = 728.5;
var currrRecty = 3;
var mazeWidth = 1457;
var mazeHeight = 1453;
var intervalvar;
function drawMazeAndRectangle(rectX, rectY) {
    makeWhite(0, 0, canvas.width, canvas.height);
    var mazeImg =new Image();
    maze.Img.onLoad = function() {
        context.drawImage(mazeImg, 0, 0);
        drawRectangle(rectX, rectY, "#FF0000", false, true);
        context.beginPath();
        context.closePath();
        context.fillStyle = '#00ff00';
        context.fill();
    };
    mazeIMg.src = "mazeLevel1.gif"
}
function drawRectangle(x, y, style){
    makeWhite(currRectX, currrRecty, 15, 15);
    currRectX = x;
    currRectY = y;
    context.beginPath();
    context.rect(x, y, 15, 15);
    context.closePath();
    context.fillStyle = style;
    context.fill();
}

drawMazeAndRectangle(728.5, 3);