@echo off
echo Starting...
echo.

REM Error checking for 4 images
SET /A COUNT=0
FOR %%V in (%*) DO SET /A COUNT=COUNT+1

IF NOT %COUNT% == 1 GOTO ERROR
IF "%~1" == "" GOTO ERROR

IF NOT EXIST "%~1" GOTO ERROR

REM Copy the dropped files into the temp folder
copy "%~1" "E:\_temp_\stitching_output\pano-looking-down.tif" > nul
echo [ OK ] Copy pano-looking-down.tif

REM path to PTGui then batch command with path to template. -x: Exit when done
"C:\Program Files\PTGui\PTGui.exe" -batch "C:\Users\Rafael\AppData\Roaming\PTGui\Templates\3-nadir-fixed-8500.pts" -x
echo [ OK ] Apply PTGUI template

:: REM Rename the file in eqr-preview to an image from the set that were copied into the temp folder.
copy "E:\_temp_\stitching_output\nadir-fixed.tif" "%~dp1\_nadir-fixed.tif" > nul
echo [ OK ] Copy nadir-fixed.tif

REM Delete copied images from temp folder.
del "E:\_temp_\stitching_output\pano-looking-down.tif"
echo [ OK ] Delete stitching_output\pano-looking-down.tif
del "E:\_temp_\stitching_output\nadir-fixed.tif"
echo [ OK ] Delete stitching_output\nadir-fixed.tif

GOTO DONE

:ERROR
echo.
echo Drag and drop 4 images on the droplet
echo to create and view a 360 EQUIRECTANGULAR image.
pause

:DONE
REM echo.
REM pause