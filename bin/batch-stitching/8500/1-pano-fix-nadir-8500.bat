@echo off
echo Starting...
echo.

REM Error checking for 4 images
SET /A COUNT=0
FOR %%V in (%*) DO SET /A COUNT=COUNT+1

IF NOT %COUNT% == 1 GOTO ERROR
IF "%~1" == "" GOTO ERROR

IF NOT EXIST "%~1" GOTO ERROR

REM Get filename
REM for %%a in (%~1) do (
REM     set file=%%~fa
REM     set filepath=%%~dpa
REM     set filename=%%~nxa
REM )
REM set filename="E:\_temp_\stitching_output\%filename%"

REM Copy the dropped files into the temp folder
copy "%~1" "E:\_temp_\stitching_output\pano-fix-nadir.jpg" > nul
echo [ OK ] Copy pano-fix-nadir.tif

REM path to PTGui then batch command with path to template. -x: Exit when done
"C:\Program Files\PTGui\PTGui.exe" -batch "C:\Users\Rafael\AppData\Roaming\PTGui\Templates\1-pano-fix-nadir-8500.pts" -x
echo [ OK ] Apply PTGUI template

REM Rename the file in eqr-preview to an image from the set that were copied into the temp folder.
move "E:\_temp_\stitching_output\pano-looking-down.tif" "%~dp1\_pano-looking-down.tif" > nul

REM Delete copied images from temp folder.
del "E:\_temp_\stitching_output\pano-fix-nadir.jpg"
echo [ OK ] Delete stitching_output\pano-fix-nadir.jpg

REM Rename panorama with its original name
REM move "E:\_temp_\stitching_output\pano-fix-nadir.tif" %filename% > nul
REM echo [ OK ] Move pano-looking-down.tif

GOTO DONE

:ERROR
echo.
echo Drag and drop 4 images on the droplet
echo to create and view a 360 EQUIRECTANGULAR image.
pause

:DONE
REM echo.
REM pause