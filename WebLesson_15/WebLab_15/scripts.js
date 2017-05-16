/**
 * Created by dukec9804 on 5/16/2017.
 */
function shapes() {
    var x = document.getElementById("canvas");
    canvas = x.getContext("2d");
    canvas.beginPath();
    canvas.moveTo(50, 50);
    canvas.lineTo(90, 250);
    canvas.lineTo(110, 270);
    canvas.lineTo(70,60);
    canvas.lineTo(130, 270);
    canvas.lineTo(80, 7);
    canvas.lineTo(150, 255);
    canvas.closePath();
    canvas.stroke();
}
window.addEventListener("load", shapes, false);