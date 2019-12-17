//@target photoshop
//@include "./functions.jsx"

//var files = File.openDialog("Select your files to place", "*.jpg", true);
//var sourceDir = Folder.selectDialog( 'Select the import directory.', importDir);

// 2 seat colors: 2 layers: mirrors at the bottom, then the car interior. Both mostly white.

function main(){
    $.writeln("-------------------");
    var root = "/Users/rafael/virtual-tours/gforces/cars/.src/";
    var importDir = Folder(root + "import/");
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
            // Import every layer in the car-mask.psb
            var masksDoc = app.open(maskFile);
            var masksGroup = masksDoc.layers;
            // Check number of layers in maskGroup
            if (masksGroup.length == '2') {
                // No seat colour, just 3 backgrounds
                var version = '3';
            }
            else if (masksGroup.length == '3') {
                // 2 seat colours (light and dark) and 3 backgrousds
                var version = '2';
            }
            else {
                alert('Wrong number of Layers in the mask file.')
            }
            $.writeln("[    ] Version: ", version);
            // Open template.psb
            var templateFile = File(root + "layers/template/template-v" + version + ".psb");
            var templateDoc = app.open(templateFile);
            var sourceDoc = templateDoc;
            // Select first document: maskFile
            app.activeDocument = app.documents[0];
            for (var ii = 0; ii < (masksGroup.length); ii++) {
                masksGroup[ii].duplicate(sourceDoc, ElementPlacement.PLACEATBEGINNING);
            }
            masksDoc.close(SaveOptions.DONOTSAVECHANGES);
            // Import pano.jpg
            var panoDoc = app.open(importFile);
            var panoGroup = panoDoc.layers[0];
            panoGroup.duplicate(sourceDoc, ElementPlacement.PLACEATEND);
            panoDoc.close(SaveOptions.DONOTSAVECHANGES);
            if (version == '3') {
                // Rename top 2 layers
                app.activeDocument.layers[0].name = "mirrors";
                app.activeDocument.layers[1].name = "wins";
                // $.writeln("Rename 2 layers");
            }
            if (version == '2') {
                // Rename top 3 layers
                app.activeDocument.layers[0].name = "seats";
                app.activeDocument.layers[1].name = "wins";
                app.activeDocument.layers[2].name = "mirrors";
                //$.writeln("Rename 3 layers");
            }
            var photoshopAction = "v10visualiser v" + version;
            app.doAction(photoshopAction, "photoshop_actions");
            // Rename bottom layer as the car name
            app.activeDocument.activeLayer.name = carBasename;
            var saveFile = new File(root + "layers/" + carBasename + ".psb");
            //$.writeln("path: ", saveFile);
            savePSB(saveFile);
            app.activeDocument.close(SaveOptions.DONOTSAVECHANGES);
        }
        //$.writeln(layerFile);
    }
    $.writeln("_EOF_");
}

main();
// test with gb_audi_a5-cabriolet_2016
