Notes and Tools
======================================

This is a page that contains tools, links and notes used through the course.    

## Notes

Notes from chapter 2 (Py Ingredients) has been uploaded.  


## Python Virtual Environment

We are having jupyter setup in a virtual environment so that it will be easy to 
get all dependencies for the system installed without having to have potential
issues with other libraries that your system might have installed, for this purpose
the class will have all code created in a virtual environment.   

### Mac / Linux

If you are running on a mac or a linux system make sure that you have both python
installed (3.5) and that you have the venv module by running the below command.  

        python -m venv
        
If you get an error such as `no command named python` or `module venv not found` 
then there is an issue with your installation that needs to be resolved.   

Once the issue with your installation is resolved you can run the below command
from the root of your repo, to get the virtual environment setup.  

        bin/setup_venv
        
This creates a virtual environment for your class repo, however you will need
to activate it for each terminal (bash shell) that you open.  You can do so
by running the below command.  

**NOTE: You will need to run this everytime.**   

        source .env/bin/activate
        
If all has been completed successfully you should see a new entry on the left of 
your terminal (at the prompt) that should be `(.env)`.  If that is not found 
there may have been an error in the previous step, so try the step again and
if that fails contact me with detail on the error.   

Now you should be in an environment that will allow for jupyter and ipython
to be run successfully which you can test by running either of the below 
commands.  

        # Start up the notebook
        jupyter notebook
        
        # Start up the interpreter (REPL)
        ipython

### Windows

For windows I am assuming that you are using windows 7 or greater and that you
are not using ubuntu for windows or any other vm.    

First you will want to make sure that you have python 3.5 installed on your system
and that you can access it from the command prompt.  So start by opening a new 
`command prompt (cmd.exe)` and running the below command.  

**NOTE: This is not the git bash, it is the windows built-in command prompt**   

        python -m venv
        
If that command return an error that either `no command named python` or 
`module venv not found` you likely have a bad installation of python.  Go through
the process of uninstalling (if one exists) and then reinstalling python, and be
sure to select the checkbox `Add Python 3.5 to PATH` as found in this image

![windows python installer]("https://docs.python.org/3/_images/win_installer.png")   


## Tools

* [Code Formatter for Slides](http://markup.su/highlighter/)    

