#include "./functions.jsx";
var root = "E:/virtual_tours/gforces/manufacturers/lexus_manufacturer/ae_lexus_is_fsport_2017/.src/panos/ae_lexus_is_fsport_2017/scene_";
var doc = app.activeDocument;
main();

function main(){
    if(!documents.length) return;
    $.writeln("--------- Lexus IS FSPORT ----------");
    
    SavePano(5,5,"1_a");
    
    doc.layers[0].visible = true; // Gloss
    SavePano(5,2,"1_b");
    doc.layers[0].visible = false; // Gloss   
    
    SavePano(4,5,"2_a");
    doc.layers[0].visible = true; // Gloss
    doc.layers[5].visible = true; // Base 
    SavePano(4,2,"2_b");
    doc.layers[0].visible = false; // Gloss
    
    doc.layers[5].visible = false; // Base    
    
    $.writeln("_EOF_");
}