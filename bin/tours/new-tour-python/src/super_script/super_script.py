#! /usr/bin/env python

# 10/10/2011
# Loop to generate the code for the scenes tiles, asking the number of scenes. Folding marks are included'
# Required: 'tiles.xml' with a single scene code. The nome of the folder (usually pano1,etc...) is substituted by the text 'changethis'
# Need to go to same directory where the files is to run it
# 13/10/11
# Started the super-script


# Import required modules
from shutil import copyfile
import os

def base(root_folder):
    if not os.path.exists(root_folder): os.makedirs(root_folder)
    if not os.path.exists(root_folder+"/files"): os.makedirs(root_folder+"/files")
    if not os.path.exists(root_folder+"/files/images"): os.makedirs(root_folder+"/files/images")
    if not os.path.exists(root_folder+"/files/panos"): os.makedirs(root_folder+"/files/panos")

def html_files(include, root_folder):
    copyfile(include+"html/index.html", root_folder+"index.html")
    copyfile(include+"html/ipad_simulator.html", root_folder+"ipad_simulator.html")
    copyfile(include+"html/iphone_simulator.html", root_folder+"iphone_simulator.html")
    copyfile(include+"html/tablet.html", root_folder+"tablet.html")

def coord_finder(include, root_folder):
    coord_finder_path = "files/coord_finder/"
    if not os.path.exists(root_folder+coord_finder_path): os.makedirs(root_folder+coord_finder_path)
    copyfile(include+coord_finder_path+"coord_finder.xml", root_folder+coord_finder_path+"coord_finder.xml")
    if not os.path.exists(root_folder+coord_finder_path+"images"): os.makedirs(root_folder+coord_finder_path+"images")
    copyfile(include+coord_finder_path+"images/click.png", root_folder+coord_finder_path+"images/click.png")
    copyfile(include+coord_finder_path+"images/cross.png", root_folder+coord_finder_path+"images/cross.png")

def krpano(include, root_folder):
    krpano_path = "files/krpano/"
    if not os.path.exists(root_folder+krpano_path): os.makedirs(root_folder+krpano_path)
    copyfile(include+krpano_path+"krpano.swf", root_folder+krpano_path+"krpano.swf")
    copyfile(include+krpano_path+"krpanoiphone.js", root_folder+krpano_path+"krpanoiphone.js")
    copyfile(include+krpano_path+"krpanoiphone.license.js", root_folder+krpano_path+"krpanoiphone.license.js")
    copyfile(include+krpano_path+"swfaddress.js", root_folder+krpano_path+"swfaddress.js")
    copyfile(include+krpano_path+"swfkrpano.js", root_folder+krpano_path+"swfkrpano.js")
    # krpano/plugins
    krpano_plugins_path = "files/krpano/plugins/"
    if not os.path.exists(root_folder+krpano_plugins_path): os.makedirs(root_folder+krpano_plugins_path)
    copyfile(include+krpano_plugins_path+"combobox.js", root_folder+krpano_plugins_path+"combobox.js")
    copyfile(include+krpano_plugins_path+"combobox.swf", root_folder+krpano_plugins_path+"combobox.swf")
    copyfile(include+krpano_plugins_path+"editor.swf", root_folder+krpano_plugins_path+"editor.swf")
    copyfile(include+krpano_plugins_path+"options.swf", root_folder+krpano_plugins_path+"options.swf")
    copyfile(include+krpano_plugins_path+"swfaddress.js", root_folder+krpano_plugins_path+"swfaddress.js")
    copyfile(include+krpano_plugins_path+"swfaddress.swf", root_folder+krpano_plugins_path+"swfaddress.swf")
    copyfile(include+krpano_plugins_path+"textfield.swf", root_folder+krpano_plugins_path+"textfield.swf")


def main_xml(include, root_folder):
    fout=open(root_folder+"/files/main.xml","a")
    for line in open(include+"xml/main.xml"):
        fout.write(line)
    for line in open(include+"xml/instructions.xml"):
        fout.write(line)
    fout.close()

def scenes():
    scenes_no = raw_input ("How many scenes have the virtual tour? ")
    if scenes_no == '':
        print "You must specify the number of scenes"
        scenes()
    if int(scenes_no)<=0:
        print "The number of scenes needs to be at least 1"
        scenes()
    if int(scenes_no)>50:
        print "That's a lot! Are you sure? [y] [n]"
        if scenes_no == 'y':
            scenes_tiles()
        else:
            scenes()
    scenes_tiles()

def scenes_tiles():
    print 'add tiles to main.xml'

def start():

    project_name = raw_input ("Enter name for the project: ")
    root_folder = project_name+"/"
    include = "include/"

    base(root_folder)
    html_files(include, root_folder)
    coord_finder(include, root_folder)
    krpano(include, root_folder)
    main_xml(include, root_folder)
    #scenes should be the last action
    scenes()


start()

# End
print "Thank you"
