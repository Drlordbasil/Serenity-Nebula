Sure! Here's an example of what the run.bat file could look like:

```
@echo off

echo Installing required packages...
pip install -r requirements.txt

echo Running program...
python main.py

echo Program finished running.
```

Make sure that both the main.py file and the requirements.txt file are in the same directory as the run.bat file. When the user double-clicks on the run.bat file, it will install the required packages and then run the main.py program.