#include "./functions.jsx";
var root = "E:/virtual_tours/gforces/manufacturers/lexus_manufacturer/ae_lexus_rx350_luxury_2016/.src/panos/ae_lexus_rx350_luxury_2016/scene_";
var doc = app.activeDocument;
main();

function main(){
    if(!documents.length) return;
    $.writeln("--------- Lexus RX350 LUXURY ----------");

    SavePano(14,14,"1_a");
    doc.layers[1].visible = true; // Gloss
    SavePano(14,6,"1_b");
    SavePano(14,8,"1_c");
    doc.layers[14].visible = true; // Base
    doc.layers[1].visible = false; // Gloss
    
    SavePano(10,10,"2_a");
    doc.layers[1].visible = true; // Gloss
    SavePano(10,5,"2_b");
    SavePano(10,6,"2_c");
    SavePano(10,7,"2_d");
    SavePano(10,8,"2_e");
    doc.layers[1].visible = false; // Gloss

    SavePano(11,11,"3_a");
    doc.layers[1].visible = true; // Gloss
    SavePano(11,5,"3_b");
    SavePano(11,6,"3_c");
    SavePano(11,7,"3_d");
    SavePano(11,8,"3_e");
    doc.layers[1].visible = false; // Gloss

    doc.layers[3].visible = true; // Gray Roof
    SavePano(12,12,"4_a");
    doc.layers[1].visible = true; // Gloss
    SavePano(12,5,"4_b");
    SavePano(12,6,"4_c");
    SavePano(12,7,"4_d");
    SavePano(12,8,"4_e");
    doc.layers[1].visible = false; // Gloss
    doc.layers[3].visible = false; // Grey Roof

    doc.layers[3].visible = true; // Gray Roof
    SavePano(13,13,"5_a");
    doc.layers[1].visible = true; // Gloss
    SavePano(13,5,"5_b");
    SavePano(13,6,"5_c");
    SavePano(13,8,"5_d"); 
    doc.layers[1].visible = false; // Gloss 
    doc.layers[3].visible = false; // Grey Roof
    
    doc.layers[14].visible = false; // Base
    
    $.writeln("_EOF_");
}