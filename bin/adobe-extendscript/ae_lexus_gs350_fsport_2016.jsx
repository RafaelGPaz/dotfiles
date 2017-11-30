#include "./functions.jsx";
var root = "E:/virtual_tours/gforces/manufacturers/lexus_manufacturer/ae_lexus_gs350_fsport_2016/.src/panos/ae_lexus_gs350_fsport_2016/scene_";
var doc = app.activeDocument;
main();

function main(){
    if(!documents.length) return;
    $.writeln("--------- Lexus GS350 FSPORT ----------");
    
    SavePano(7,7,"1_a");
    
    doc.layers[0].visible = true; // Gloss
    SavePano(7,2,"1_b");
    SavePano(7,3,"1_c");
    doc.layers[0].visible = false; // Gloss   
    
    SavePano(5,7,"2_a");
    doc.layers[0].visible = true; // Gloss
    doc.layers[7].visible = true; // Base 
    SavePano(5,2,"2_b");
    SavePano(5,3,"2_c");
    doc.layers[0].visible = false; // Gloss

    SavePano(6,7,"3_a");
    doc.layers[0].visible = true; // Gloss
    doc.layers[7].visible = true; // Base 
    SavePano(6,2,"3_b");
    SavePano(6,3,"3_c");
    doc.layers[0].visible = false; // Gloss
    
    doc.layers[7].visible = false; // Base    
    
    $.writeln("_EOF_");
}