﻿#include "./functions.jsx";var root = "/Users/rafael/virtual-tours/gforces/manufacturers/lexus_manufacturer/v3/.src/panos/ae_lexus_es_2019/scene_";var doc = app.activeDocument;main();function main(){    if(!documents.length) return;    $.writeln("--------- Lexus ES 2019 ----------");    SavePano(8,4,"3_a_e");    doc.layers[4].visible = true;    SavePano(8,3,"3_a_f");    doc.layers[4].visible = false;    SavePano(8,2,"3_a_g");    SavePano(7,4,"3_b_e");    doc.layers[4].visible = true;    SavePano(7,3,"3_b_f");    doc.layers[4].visible = false;    SavePano(7,2,"3_b_g");    SavePano(6,4,"3_c_e");    doc.layers[4].visible = true;    SavePano(6,3,"3_c_f");    doc.layers[4].visible = false;    SavePano(6,2,"3_c_g");    SavePano(5,4,"3_d_e");    doc.layers[4].visible = true;    SavePano(5,3,"3_d_f");    doc.layers[4].visible = false;    SavePano(5,2,"3_d_g");        doc.layers[4].visible = true; // Base    doc.layers[8].visible = true; // Base    $.writeln("_EOF_");}