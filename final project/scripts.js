var canvas = document.getElementById("canvasMaze");
context = canvas.getContext("2d");
var currRectX = 728.5;
var currrRecty = 3;
var mazeWidth = 1457;
var mazeHeight = 1453;
var intervalvar;
function drawMazeAndRectangle(rectX, rectY) {
    makeWhite(0, 0, canvas.width, canvas.height);
    var mazeImg = new Image();
    mazeImg.onLoad = function() {
        context.drawImage(mazeImg, 0, 0);
        drawRectangle(rectX, rectY, "#FF0000", false, true);
        context.beginPath();
        context.closePath();
        context.fillStyle = '#00ff00';
        context.fill();
    };
    mazeImg.src = "mazeLevel1.gif"
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

function MoveRect(e) {
    var newX;
    var newY;
    var canMove;
    e = e || window.event;
    switch(e.keyCode) {
        case 38: //arrow up key
        case 87: // W ley
            newX = currRectX;
            newY = currRectY - 3;
            break;
        case 37: // arrow left key
        case 65: // A key
            newX = currRectX - 3;
            newY = currRectY;
            break;
        case 40: //arrow down key
        case 83: // S ley
            newX = currRectX;
            newY = currRectY + 3;
            break;
        case 39: // arrow right key
        case 68: // D key
            newX = currRectX + 3;
            newY = currRectY;
            break;
        default: return;
    }
    movingAllowed = canMoveTo(newX, newY);
    if (movingAllowed === 1) {      // 1 means 'the rectangle can move'
        drawRectangle(newX, newY, "#FF0000", false, true);
        currRectX = newX;
        currRectY = newY;
    }
    else if (movingAllowed === 2) { // 2 means 'the rectangle reached the end poimt'
        clearInterval(intervalVar); // set timer later
        makeWhite(0, 0, canvas.width, canvas.height);
        context.font = "40px arial";
        context.fillStyle = "blue";
        context.textAlign = " center";
        context.textBaseline = "middle";
        context.fillText("Congradulations!", canvas.width / 2, canvas.height / 2);
        window.reomoveEventListener("keydown", moveRect, true);
    }

}


drawMazeAndRectangle(728.5, 3);
window.addEventListener("keydown", moveRect, true);