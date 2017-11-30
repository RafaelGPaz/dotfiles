#include "./functions.jsx";
var root = "E:/virtual_tours/gforces/manufacturers/lexus_manufacturer/ae_lexus_rx350_2016/.src/panos/ae_lexus_rx350_2016/scene_";
var doc = app.activeDocument;
main();

function main(){
    if(!documents.length) return;
    $.writeln("--------- Lexus RX350 ----------");

    doc.layers[1].visible = true; // Gloss
    doc.layers[14].visible = true; // Base

    SavePano(9,3,"1_a");
    SavePano(9,4,"1_b");
    SavePano(9,5,"1_c");
    SavePano(9,6,"1_d");
    SavePano(9,7,"1_e");

    SavePano(10,3,"2_a");
    SavePano(10,4,"2_b");
    SavePano(10,5,"2_c");
    SavePano(10,6,"2_d");
    SavePano(10,7,"2_e");
 
    SavePano(11,3,"3_a");
    SavePano(11,4,"3_b");
    SavePano(11,5,"3_c");
    SavePano(11,7,"3_d");
    
    SavePano(12,3,"4_a");
    SavePano(12,4,"4_b");
    SavePano(12,5,"4_c");
    SavePano(12,6,"4_d");
    SavePano(12,7,"4_e");
    
    SavePano(13,3,"5_a");
    SavePano(13,5,"5_b");
    SavePano(13,5,"5_c");
    
    doc.layers[1].visible = false; // Gloss
    doc.layers[14].visible = false; // Base    
    
    $.writeln("_EOF_");
}