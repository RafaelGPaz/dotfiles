#include "./functions.jsx";
var root = "E:/virtual_tours/gforces/manufacturers/lexus_manufacturer/ae_lexus_gsf_2016/.src/panos/ae_lexus_gsf_2016/scene_";
var doc = app.activeDocument;
main();

function main(){
    if(!documents.length) return;
    $.writeln("--------- Lexus GSF 2016 ----------");
    
    SavePano(8,8,"1_a");
    doc.layers[8].visible = true; // Base
    doc.layers[1].visible = true; // Gloss
    SavePano(3,3,"1_b");
    SavePano(4,4,"1_c");
    doc.layers[1].visible = false; // Gloss   
    doc.layers[8].visible = false; // Base    
     
    doc.layers[8].visible = true; // Base
    SavePano(7,7,"2_a");
    doc.layers[1].visible = true; // Gloss
    SavePano(3,3,"2_b");
    SavePano(4,4,"2_c");
    doc.layers[1].visible = false; // Gloss
    doc.layers[8].visible = false; // Base

    doc.layers[8].visible = true; // Base
    doc.layers[7].visible = true; // Base
    SavePano(6,6,"3_a");
    doc.layers[1].visible = true; // Gloss
    SavePano(3,6,"3_b");
    SavePano(4,6,"3_c");
    doc.layers[1].visible = false; // Gloss
    doc.layers[7].visible = false; // Base
    doc.layers[8].visible = false; // Base
   
    $.writeln("_EOF_");
}