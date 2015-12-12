#!/usr/bin/env python

import fileinput
import glob
import os
import pprint

def main():
    file_list = []
    for tour in os.listdir(os.getcwd()):
        dir_list = ['plugins', 'content', 'include', 'scenes']
        for d in dir_list:
            # print(d)
            if d == 'include':
                xml_files = glob.glob(tour + "/files/" + d + "/*/*.xml")
            else:
                xml_files = glob.glob(tour + "/files/" + d + "/*.xml")
            for xml_file in xml_files:
                file_list.append(xml_file)
        for line in file_list:
            print("[ DONE ] " + line) 

        with open(tour + '/files/tour.xml', 'w') as file:
            input_lines = fileinput.input(file_list, mode="rU")
            file.writelines('<krpano version="1.18">')
            file.writelines(input_lines)
            # pprint.pprint(file_list)

        pass

    print("_EOF_")

if __name__ == '__main__':
    main()
