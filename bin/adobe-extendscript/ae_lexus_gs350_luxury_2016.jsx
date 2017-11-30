#include "./functions.jsx";
var root = "E:/virtual_tours/gforces/manufacturers/lexus_manufacturer/ae_lexus_gs350_luxury_2016/.src/panos/ae_lexus_gs350_luxury_2016/scene_";
var doc = app.activeDocument;
main();

function main(){
    if(!documents.length) return;
    $.writeln("--------- Lexus GS350 Luxury ----------");

    SavePano(7,12,"1_a");
    doc.layers[12].visible = true; // Base
    doc.layers[0].visible = true; // Gloss
    SavePano(7,2,"1_b");
    SavePano(7,4,"1_c");
    SavePano(7,5,"1_d");
    doc.layers[0].visible = false; // Gloss
    
    SavePano(8,12,"2_a");
    doc.layers[12].visible = true; // Base
    doc.layers[0].visible = true; // Gloss
    SavePano(8,2,"2_b");
    SavePano(8,3,"2_c");
    SavePano(8,4,"2_d");
    SavePano(8,5,"2_e");
    doc.layers[0].visible = false; // Gloss

    SavePano(9,12,"3_a");
    doc.layers[12].visible = true; // Base
    doc.layers[0].visible = true; // Gloss
    SavePano(9,2,"3_b");
    SavePano(9,3,"3_c");
    SavePano(9,4,"3_d");
    SavePano(9,5,"3_e");
    doc.layers[0].visible = false; // Gloss
    
    SavePano(10,12,"4_a");
    doc.layers[12].visible = true; // Base
    doc.layers[0].visible = true; // Gloss
    SavePano(10,2,"4_b");
    SavePano(10,3,"4_c");
    SavePano(10,4,"4_d");
    SavePano(10,5,"4_e");
    doc.layers[0].visible = false; // Gloss
    
    SavePano(11,12,"5_a");
    doc.layers[12].visible = true; // Base
    doc.layers[0].visible = true; // Gloss
    SavePano(11,2,"5_b");
    SavePano(11,3,"5_c");
    SavePano(11,4,"5_d");
    SavePano(11,5,"5_e");
    doc.layers[0].visible = false; // Gloss
    
    doc.layers[12].visible = false; // Base    
    
    $.writeln("_EOF_");
}