#include "./functions.jsx";
main();

function main(){
    $.writeln("-------------------");
    if(!documents.length) return;
    var doc = app.activeDocument;
    var layer = doc.activeLayer;
    var group = doc.layers;
    var project_folder = group[0].name;
    var car_folder = group[0].layers[0].name;
    var root = "E:/virtual_tours/gforces/manufacturers/" + project_folder + "/" + car_folder + "/" + car_folder;

    hide_all_layers(group);
    
    doc.layers[0].visible = true;
    doc.layers[group.length -1].visible = true;
    var a = 1;
    var b = 2;
    var num = 10;
    for (var i = 1; i < (group.length / 2 ); i++) {    
        doc.layers[a].visible = true;
        doc.layers[b].visible = true;
        var saveFile = new File(root + "/files/content/hs_" + num + ".jpg");
        $.writeln("    path: ", saveFile);
        SaveForWeb(saveFile,60);
        doc.layers[a].visible = false;
        doc.layers[b].visible = false;
        var num = num - 1;
        var a = a + 2;
        var b = b + 2;
    }

    hide_all_layers(group);
    doc.layers[0].visible = true;
    doc.layers[group.length -1].visible = true;
    doc.layers[group.length -2].visible = true;
    doc.layers[group.length -3].visible = true;

    $.writeln("_EOF_");
}