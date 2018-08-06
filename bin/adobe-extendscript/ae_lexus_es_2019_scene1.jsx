
#include "./functions.jsx";

var root = "/Users/rafael/virtual-tours/gforces/manufacturers/lexus_manufacturer/v3/.src/panos/ae_lexus_es_2019/scene_";
var doc = app.activeDocument;
main();

function main(){
    if(!documents.length) return;
    $.writeln("--------- Lexus ES 2019 ----------");

    SavePano(8,4,"1_a_e");
    doc.layers[4].visible = true;
    SavePano(8,3,"1_a_f");
    doc.layers[4].visible = false;
    SavePano(8,2,"1_a_g");

    SavePano(7,4,"1_b_e");
    doc.layers[4].visible = true;
    SavePano(7,3,"1_b_f");
    doc.layers[4].visible = false;
    SavePano(7,2,"1_b_g");

    SavePano(6,4,"1_c_e");
    doc.layers[4].visible = true;
    SavePano(6,3,"1_c_f");
    doc.layers[4].visible = false;
    SavePano(6,2,"1_c_g");

    SavePano(5,4,"1_d_e");
    doc.layers[4].visible = true;
    SavePano(5,3,"1_d_f");
    doc.layers[4].visible = false;
    SavePano(5,2,"1_d_g");

    doc.layers[4].visible = true; // Base
    doc.layers[8].visible = true; // Base

    $.writeln("_EOF_");
}