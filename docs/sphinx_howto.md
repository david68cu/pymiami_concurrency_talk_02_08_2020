### About Documentation used for this project(Sphinx and read the docs)

We used  Sphinx and read the docs documentation .
Read more about Sphinx [here](https://docs.readthedocs.io/en/stable/intro/getting-started-with-sphinx.html)


First created on docs/folder

To start:

    ```
       mkdir docs
       workon screencasts
       pip install sphinx
       cd docs
       ls
       sphinx-quickstart
    ```

To edit make changes to /docs/source/index.srt 
   
Then compile the html with make:

    ```
    % cd /docs/
    % ls -al
        .
        ..
        -rw-r--r--   1 davidgutierrez  staff  638 Feb 13 13:14 Makefile
        drwxr-xr-x   4 davidgutierrez  staff  128 Feb 14 20:22 build
        -rw-r--r--   1 davidgutierrez  staff  799 Feb 13 13:14 make.bat
        drwxr-xr-x   7 davidgutierrez  staff  224 Feb 14 20:22 source
    % make html
    % open index.html
    ```

This generates a conf.py file and html docs 



Workflow:

    - Inside the source folder we have the index.srt that we will edit 
    - We will make html to make the new html file with the changes by 
           cd /docs
           make html
    - If we need to change teh configuration we can do it by changing the conf.py file 
    - To see changes in browser  open  docs/build/html/index.html 


Changing theme in Sphinx:

   - You tube video  [Changing theme in Sphinx](https://www.youtube.com/watch?v=Zb_Oy5UG6Tw)
   - GitHub Sphinx themes and How To install  [GitHun Sphinx Themes](https://github.com/rtfd/sphinx_rtd_theme)


