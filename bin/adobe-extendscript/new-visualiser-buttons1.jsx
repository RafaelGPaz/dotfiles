#include "./functions.jsx";

var doc = app.activeDocument;
var layer = doc.activeLayer;
var group = doc.layers;
var seatsGroup = doc.layers[0];
var seatColors = seatsGroup.layers;
var bgGroup = doc.layers[1];
var bgs = bgGroup.layers;
var lastlayer = group.length - 1;
var carBasename = doc.layers[lastlayer].name;

function move_btn(btn_path,btn_number){
    var originFile = new File('/c/Users/Rafael/AppData/Local/temp/btn.jpg');
    var destFile = '/e/virtual_tours/gforces/cars/' + btn_path + '/files/btn_' + btn_number + '.jpg'  
    //$.writeln(originFile);
    $.writeln("Visualiser button: ", destFile);
    originFile.copy(destFile);
    originFile.remove();
}

function main(){
    $.writeln("-------------------");
    
    if(!documents.length) return;
    
    $.writeln("[    ] " + carBasename);
    
    hide_all_layers(group);
    // Make sure 'btn' layer is hidden
    // bgGroup.artLayers.getByName("btn").visible = false;
    // Show last layer (car interior in Studio)
    doc.layers[2].visible = true;
    // Show 'Seats' layer
    seatsGroup.visible = true;
    // Hide all the seat colors
    for (var ii = 0; ii < (seatColors.length); ii = ii + 1) {
        var seat = seatColors[ii];
        seat.visible = false;
    }
    
    // Cycle through all seat colors
    var seatNo = 1;
    for (var ii = 0; ii < (seatColors.length); ii = ii + 1) {
        var seat = seatColors[ii];
        seat.visible = true;
        // Create seat colour btn
        app.doAction("v10visualiser_btn", "photoshop_actions");
        move_btn (carBasename, seatNo);
        bgGroup.visible = false;
        seat.visible = false;
        var seatNo = seatNo + 1;
    }
    app.activeDocument.close(SaveOptions.DONOTSAVECHANGES);
    $.writeln("_EOF_");
}

main();