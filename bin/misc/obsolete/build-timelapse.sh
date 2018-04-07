#!/usr/bin/env bash

ls -1tr > files.txt
encoder -nosound -vf scale=1024:-2 -fps 1.5 -ovc lavc -lavcopts vcodec=mpeg4 -o test.avi -mf type=jpeg:fps=20 mf://@files.txt
