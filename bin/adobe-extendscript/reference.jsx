function main(){  
    if(!documents.length) return;  
    //var fileRef = File("C:/Users/Rafael/Downloads/temp/infospots_layers.tif")
    //var docRef = app.open(fileRef)
    //var root = "C:/Users/Rafael/Downloads/temp/toyota_oem"
    var root = "E:/virtual_tours/gforces/manufacturers/toyota_manufacturer"
    var doc = app.activeDocument
    var layer = doc.activeLayer;
    var group = doc.layers;

    //var doc = app.activeDocument;
    //doc.activeLayer = doc.layerSets.getByName("t1");
    //doc.activeLayer = doc.artLayers.getByName("t1");
    //app.activeDocument.activeLayer.visible

    //var layerRef = app.activeDocument.Layers.getByName("t1");
    //layerRef.allLocked = true;

    //var doc = app.activeDocument;
    //doc.activeLayer = doc.artLayers.getByName("border");

    for (var i = 2; i < (group.length - 1); i++) {
        //$.writeln(group[i]);
        doc.activeLayer = group[i]
        var car = group[i].layers;
        //$.writeln(car.length);
        var a = 0;
        var b = 1;
        var num = (car.length / 2) ;
        for (var ii = 0; ii < (car.length / 2); ii++) {
            //$.write(ii);           
            doc.activeLayer = car[a];
            doc.activeLayer = car[b];
            //save
            var saveFile = new File(root + "/toyota_" + group[i].name + "/files/content/hs_" + num + ".jpg");
            $.write(saveFile);
            SaveForWeb(saveFile,60); 
            doc.activeLayer.visible = false;
            doc.activeLayer = car[a];
            doc.activeLayer.visible = false;
            var a = a + 2;
            var b = b + 2;
            var num = num - 1;
            //$.write(num);
            //if(ii + 1 < 0  ) { break; }
        }    
        //break
    }
}

main();

function SaveForWeb(saveFile,jpegQuality) {  
    var sfwOptions = new ExportOptionsSaveForWeb();   
    sfwOptions.format = SaveDocumentType.JPEG;   
    sfwOptions.includeProfile = false;   
    sfwOptions.interlaced = 0;   
    sfwOptions.optimized = true;   
    sfwOptions.quality = jpegQuality; //0-100   
    activeDocument.exportDocument(saveFile, ExportType.SAVEFORWEB, sfwOptions);  
}  