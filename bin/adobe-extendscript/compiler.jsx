#target estoolkit#dbg
var fileIn = File("/e/documents/adobe_scripts/import_v10.jsx");
fileIn.open("r");
var s = fileIn.read();
fileIn.close();
var t = app.compile(s);
var fileOut = File( fileIn.absoluteURI + "bin" ) ;
fileOut.open("w");
fileOut.write(t);