#include "./functions.jsx";
var root = "E:/virtual_tours/gforces/manufacturers/lexus_manufacturer/ae_lexus_rxf350_2016/.src/panos/ae_lexus_rxf350_2016/scene_";
var doc = app.activeDocument;
main();

function main(){
    if(!documents.length) return;
    $.writeln("--------- Lexus RX F 350 ----------");
    doc.layers[8].visible = true;

    SavePano(5,2,"1_a");
    SavePano(5,3,"1_b");
    SavePano(6,2,"2_a");
    SavePano(6,3,"2_b");
    SavePano(7,2,"3_a");
    SavePano(7,3,"3_b");
    
    doc.layers[8].visible = false;
    $.writeln("_EOF_");
}