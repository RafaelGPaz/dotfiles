#include "./functions.jsx";
main();

function main(){
    $.writeln("-------------------");
    if(!documents.length) return;  
    var root = "E:/virtual_tours/gforces/manufacturers/toyota_manufacturer"
    var doc = app.activeDocument
    var layer = doc.activeLayer;
    var group = doc.layers;
    // Phase 1
    //for (var i = 2; i < 11; i++) {
    
    // Phase 2
    //for (var i = 11; i < 20; i++) {
    
    // All
    //for (var i = 2; i < (group.length - 1); i++) {
    
    // toyota_yaris_sedan
    //for (var i = 2; i < 3; i++) {
    // toyota_yaris_hb
    //for (var i = 3; i < 4; i++) {
    // toyota_prado
    //for (var i = 4; i < 5; i++) {
    // toyota_land_cruiser
    //for (var i = 5; i < 6; i++) {
    // toyota_hilux
    //for (var i = 6; i < 7; i++) {
    // toyota_fj
    //for (var i = 7; i < 8; i++) {
    // toyota_corola
    //for (var i = 8; i < 9; i++) {
    // toyota_camry
    //for (var i = 9; i < 10; i++) {
    // toyota_86
    //for (var i = 10; i < 11; i++) {
    
    // toyota_sequoia
    //for (var i = 11; i < 12; i++) {
    // toyota_rav4
    //for (var i = 12; i < 13; i++) {
    // toyota_prius
    //for (var i = 13; i < 14; i++) {
    // toyota_previa
    //for (var i = 14; i < 15; i++) {
    // toyota_lc
    //for (var i = 15; i < 16; i++) {
    // toyota_innova
    //for (var i = 16; i < 17; i++) {
    // toyota_fortuner
    //for (var i = 17; i < 18; i++) {
    // toyota_avanza    
    //for (var i = 18; i < 19; i++) {
    // toyota_avalon
    //for (var i = 19; i < 20; i++) {

        doc.activeLayer = group[i]
        var car = group[i].layers;
        var a = 0;
        var b = 1;
        var num = (car.length / 2);
        //$.writeln("No of layers in the document (car.length): ", car.length);
        // for each layer in the model
        for (var ii = 0; ii < (car.length - 1); ii = ii + 2) {                   
            var photo = car[ii].layers;
            var c = 1;
            //$.writeln("  No of selected layer (ii)=", ii); 
            //$.writeln("  layer id (photo): ", photo);
            //$.writeln("  No of layers inside (photo.length): ", photo.length);
            //$.writeln("  Make visible layer No: ", a);
            doc.activeLayer = car[a];
            //$.writeln("  Make visible layer No: ", b);
            doc.activeLayer = car[b];
            
            // OPTION 1: Save only the first screenshot
            doc.activeLayer = photo[0];    
            //save
            var saveFile = new File(root + "/toyota_" + group[i].name + "/files/content/hs_" + num + "_" + c + ".jpg");
            $.writeln("    path: ", saveFile);
            SaveForWeb(saveFile,60);
            // end save
            doc.activeLayer.visible = false;            
            // End option 1
            
            // OPTION 2: Loop throuh every screenshot inside the folder
            //for (var iii = 0; iii < (photo.length); iii++) {
                //$.writeln("    No of selected layer (iii)=", iii); 
            //    doc.activeLayer = photo[iii];    
                //save
            //    var saveFile = new File(root + "/toyota_" + group[i].name + "/files/content/hs_" + num + "_" + c + ".jpg");
            //    $.writeln("    path: ", saveFile);
            //    SaveForWeb(saveFile,60);
                // end save
            //    doc.activeLayer.visible = false;
            //    var c = c + 1;
            //}
            // End option 2
            
            doc.activeLayer = car[b];
            doc.activeLayer.visible = false;
            doc.activeLayer = car[a];
            doc.activeLayer.visible = false;
            var a = a + 2;
            var b = b + 2;
            var num = num - 1;    
        }
    }
    $.writeln("_EOF_");
}