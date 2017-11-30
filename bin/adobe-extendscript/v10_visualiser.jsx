#include "./functions.jsx";
var doc = app.activeDocument;
var layer = doc.activeLayer;
var group = doc.layers;
var car_folder = doc.layers[2].name;
var root = "E:/virtual_tours/gforces/cars_visualiser/.src/panos/" + car_folder
var carfolder = Folder(root);
main();

function main(){
    $.writeln("-------------------");
    if(!documents.length) return;
    if(!carfolder.exists) carfolder.create();    
    
    hide_all_layers(group);

    //SavePano(2,2,"/scene_1_a");    
    //SavePano(2,0,"/scene_1_b");
    //SavePano(2,1,"/scene_2_a");    
    doc.layers[1].visible = true;
    //SavePano(2,0,"/scene_2_b");
    doc.layers[1].visible = false;
    
    $.writeln("_EOF_");
}