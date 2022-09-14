
@echo DOWNLOAD AND UNZIP
@echo https://gitlab.com/api/v4/projects/4207231/packages/generic/graphviz-releases/6.0.1/windows_10_msbuild_Release_graphviz-6.0.1-win32.zip

cd windows_10_msbuild_Release_graphviz-6.0.1-win32\Graphviz\bin
set %DOCS%=..\..\..
dot.exe -Tpng %DOCS%\test_dot.dot -o %DOCS%\test_dot.png

cd %DOCS%

rem https://graphviz.org/download/
rem https://gitlab.com/api/v4/projects/4207231/packages/generic/graphviz-releases/6.0.1/windows_10_msbuild_Release_graphviz-6.0.1-win32.zip
