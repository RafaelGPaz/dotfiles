#include "./functions.jsx";

//var files = File.openDialog("Select your files to place", "*.jpg", true);
//var sourceDir = Folder.selectDialog( 'Select the import directory.', importDir);

function main(){
    $.writeln("-------------------");
    var root = "E:/virtual_tours/gforces/cars/.src/"
    var templateFile = File(root + "layers/template/template.psb")
    var importDir = Folder(root + "import/")
    var panoFile = importDir.getFiles("*.jpg");
    
    if(panoFile.length == 0){  
        alert("No files to import");
    }
    $.writeln("Processing...");
    // $.writeln(panoFile);
    // For each jpg car in the 'import' directory
    for (var i = 0; i < (panoFile.length); i++) {
        //$.writeln(i);
        var car = panoFile[i].name;
        var carBasename = car.match(/(.*)\.[^\.]+$/)[1];
        var layerFile =  File(root + "layers/" + carBasename + ".psb");
        var importFile = File(root + "import/" + carBasename + ".jpg");
        var maskFile = File(root + "masks/" + carBasename + ".psb");
        
        // Check if there is a PSB file in 'layers'. If not then make it
        if (File(layerFile).exists == false) {
            $.writeln("[    ] " + carBasename);
            // Open template.psb
            var templateDoc = app.open(templateFile);
            // Import every layer in the car-mask.psb
            var masksDoc = app.open(maskFile);
            var sourceDoc = templateDoc;
            var masksGroup = masksDoc.layers;
            for (var ii = 0; ii < (masksGroup.length); ii++) {
                masksGroup[ii].duplicate(sourceDoc, ElementPlacement.PLACEATBEGINNING);
            }
            masksDoc.close(SaveOptions.DONOTSAVECHANGES);
            // Import pano.jpg
            var panoDoc = app.open(importFile);
            var panoGroup = panoDoc.layers[0];
            panoGroup.duplicate(sourceDoc, ElementPlacement.PLACEATEND); 
            panoDoc.close(SaveOptions.DONOTSAVECHANGES);
            // Rename top 3 layers
            app.activeDocument.layers[0].name = "seats";
            app.activeDocument.layers[1].name = "wins";
            app.activeDocument.layers[2].name = "mirrors";
            app.doAction("v10visualiser", "photoshop_actions");
            // Rename bottom layer as the car name
            app.activeDocument.activeLayer.name = carBasename;
            var saveFile = new File(root + "layers/" + carBasename + ".psb");
            //$.writeln("path: ", saveFile);
            savePSB(saveFile);
            app.activeDocument.close(SaveOptions.DONOTSAVECHANGES);
        }
        //$.writeln(layerFile);
        //break;
    }
    $.writeln("_EOF_");
}

main();