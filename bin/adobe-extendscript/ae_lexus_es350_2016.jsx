#include "./functions.jsx";
var root = "E:/virtual_tours/gforces/manufacturers/lexus_manufacturer/ae_lexus_es350_2016/.src/panos/ae_lexus_es350_2016/scene_";
var doc = app.activeDocument;
main();

function main(){
    if(!documents.length) return;
    $.writeln("--------- Lexus ES350 ----------");

    SavePano(9,9,"1_a");
    SavePano(9,2,"1_b");
    SavePano(9,3,"1_c");
    SavePano(9,4,"1_d");
     
    doc.layers[9].visible = true; // Base
    SavePano(6,6,"2_a");
    SavePano(6,2,"2_b");
    SavePano(6,3,"2_c");
    SavePano(6,4,"2_d");
    doc.layers[9].visible = false; // Base
 
    doc.layers[9].visible = true; // Base
    SavePano(7,7,"3_a");
    SavePano(7,2,"3_b");
    SavePano(7,3,"3_c");
    SavePano(7,4,"3_d");
    doc.layers[9].visible = false; // Base 
 
    doc.layers[9].visible = true; // Base
    SavePano(8,8,"4_a");
    SavePano(8,2,"4_b");
    SavePano(8,3,"4_c");
    SavePano(8,4,"4_d");
    doc.layers[9].visible = false; // Base
 
    $.writeln("_EOF_");
}