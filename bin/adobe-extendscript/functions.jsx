function SavePSD(saveFile){
          psdSaveOptions = new PhotoshopSaveOptions();
          psdSaveOptions.embedColorProfile = true;
         psdSaveOptions.alphaChannels = true; 
         activeDocument.saveAs(saveFile, psdSaveOptions, true, Extension.LOWERCASE);
} 

function savePSB(fileNameAndPath) 
{  
    function cTID(s) { return app.charIDToTypeID(s); };  
    function sTID(s) { return app.stringIDToTypeID(s); };  
    var desc19 = new ActionDescriptor();  
    var desc20 = new ActionDescriptor();  
    desc20.putBoolean( sTID('maximizeCompatibility'), true );  
    desc19.putObject( cTID('As  '), cTID('Pht8'), desc20 );  
    desc19.putPath( cTID('In  '), new File( fileNameAndPath ) );  
    desc19.putBoolean( cTID('LwCs'), true );  
    executeAction( cTID('save'), desc19, DialogModes.NO );  
}

function SaveJPEG(saveFile,jpegQuality) {  
     var saveOptions = new JPEGSaveOptions( );  
     saveOptions.embedColorProfile = true;   
     saveOptions.formatOptions = FormatOptions.OPTIMIZEDBASELINE;  
     saveOptions.matte = MatteType.NONE;  
     saveOptions.quality = jpegQuality;   
     activeDocument.saveAs(saveFile, saveOptions, true );  
}    

function SaveForWeb(saveFile,jpegQuality) {  
    var sfwOptions = new ExportOptionsSaveForWeb();   
    sfwOptions.format = SaveDocumentType.JPEG;   
    sfwOptions.includeProfile = false;   
    sfwOptions.interlaced = 0;   
    sfwOptions.optimized = true;   
    sfwOptions.quality = jpegQuality; //0-100   
    activeDocument.exportDocument(saveFile, ExportType.SAVEFORWEB, sfwOptions);  
}

function SavePano(a,b,c) {
    doc.layers[a].visible = true;
    doc.layers[b].visible = true;
    var saveFile = new File(root + c + ".jpg");
    $.writeln("path: ", saveFile);
    //saveJPEG( app.activeDocument, new File('~/Desktop/sample.jpg'), 10 );
    SaveJPEG(saveFile,10);
    doc.layers[a].visible = false;
    doc.layers[b].visible = false;
}

function hide_all_layers (group) {
    for (var i = 0; i < (group.length); i++) {
        group[i].visible = false;
    }
}
