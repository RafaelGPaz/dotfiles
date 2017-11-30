#include "./functions.jsx";

// ACTION: new_btn
//   Load 'btn' layer selection
//   Copy merged
//   Deselect
//   New document
//   Paste
//   Resize to 62 x 35
//   Add 1px white border
//   Save for Web in folder 'c:/Users/Rafael/AppData/Local/temp/btn.jgp'
// Then the script will move 'btn.jpg' to the corresponding folder and rename as 'btn_1.jpg' and 'btn_2.jpg'

function move_btn(btn_path,btn_number){
    var originFile = new File('/c/Users/Rafael/AppData/Local/temp/btn.jpg');
    var destFile = '/e/virtual_tours/gforces/cars/' + btn_path + '/files/btn_' + btn_number + '.jpg'  
    //$.writeln(originFile);
    //$.writeln("Visualiser button: ", destFile);
    originFile.copy(destFile);
    originFile.remove();
}
function main(){
    $.writeln("Processing...");
    var root = "E:/virtual_tours/gforces/cars/.src/";
    var root2 = "E:/virtual_tours/gforces/cars/";
    var panosDir = Folder(root + "panos/");
    var layersDir = Folder(root + "layers/");
    var psbFile = layersDir.getFiles("*.psb");
    
    if(psbFile.length == 0){  
        alert("No files to import");
    }
    //$.writeln(psbFile);
    // For each psb file in 'layers' directory
    for (var i = 0; i < (psbFile.length); i++) {
        //$.writeln(i);
        var car = psbFile[i].name;
        var carBasename = car.match(/(.*)\.[^\.]+$/)[1];
        var layerFile =  File(root + "layers/" + carBasename + ".psb");
        var panoFolderPath = panosDir + "/" + carBasename;
        var panoFolder = new Folder(panoFolderPath);
        
        // Check if there is a folder in 'panos'with the same name as the PSB file
        // If there isn't create it and export all panos
        if (panoFolder.exists == false) {
            $.writeln("[    ] " + carBasename);
            var doc = app.open(layerFile);
            var layer = doc.activeLayer;
            var group = doc.layers;
            var seatsGroup = doc.layers[0];
            var seatColors = seatsGroup.layers;
            var bgGroup = doc.layers[1];
            var bgs = bgGroup.layers; 
            //$.writeln(seatColors);
            //$.writeln(bgs);
           
            // Create folder
            var carFolder = Folder(root + "panos/" + carBasename);
            //$.writeln(carFolder);
            carFolder.create();

            // I need to create 2 folders to move the colour seats buttons inside them
            var tourFolderPath = new Folder (root2 + "/" + carBasename);
            var filesFolderPath = new Folder (root2 + "/" + carBasename + "/files");
            tourFolderPath.create();
            filesFolderPath.create();
            
            hide_all_layers(group);
            // Make sure 'btn' layer is hidden
            // bgGroup.artLayers.getByName("btn").visible = false;
            // Show last layer (car interior in Studio)
            doc.layers[2].visible = true;
            // Show 'Seats' layer
            seatsGroup.visible = true;
            // Hide all the seat colors
            for (var ii = 0; ii < (seatColors.length); ii = ii + 1) {
                var seat = seatColors[ii];
                seat.visible = false;
            }
            // Cycle through all seat colors
            var seatNo = 1;
            for (var ii = 0; ii < (seatColors.length); ii = ii + 1) {
                var seat = seatColors[ii];
                seat.visible = true;
                // Create seat colour btn
                app.doAction("v10visualiser_btn", "photoshop_actions");
                move_btn (carBasename, seatNo);
                // Hide all the backgrounds
                for (var iii = 0; iii < (bgs.length); iii = iii + 1) {
                    var bg = bgs[iii];
                    bg.visible = false;
                }
                // Create mirror reflection
                app.doAction("v10visualiser_mirror", "photoshop_actions");
                // Save
                var saveFile = new File(carFolder + "/" + "scene_" + [seatNo] + "_a.jpg");
                SaveJPEG(saveFile,10);
                //$.writeln("path: ", saveFile);
                // Delete first layer at the top (mirror reflection)
                doc.layers[0].remove();
                // Cicle through all the backgrounds
                bgGroup.visible = true;
                for (var iii = 0; iii < (bgs.length); iii = iii + 1) {
                    if (iii == 0) { var bgLet = "b"; }
                    if (iii == 1) { var bgLet = "c"; }
                    var bg = bgs[iii];
                    //$.writeln(bg);
                    bg.visible = true;
                    // Create mirror reflection
                    app.doAction("v10visualiser_mirror", "photoshop_actions");
                    // Save
                    var saveFile = new File(carFolder + "/" + "scene_" + [seatNo] + "_" + bgLet + ".jpg");
                    //$.writeln("path: ", saveFile);                
                    SaveJPEG(saveFile,10);
                    bg.visible = false;
                    // Delete first layer at the top (mirror reflection)
                    doc.layers[0].remove();
                }
                bgGroup.visible = false;
                seat.visible = false;
                var seatNo = seatNo + 1;
            }
            hide_all_layers(group);
            app.activeDocument.close(SaveOptions.DONOTSAVECHANGES);
        }
    }
    
    $.writeln("_EOF_");
}

main();