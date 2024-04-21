# cf

(5x5) files and (3x3) roatnet (rn) and flow (fl) files are suffixed by 5 and 3 respectively <br>
Config file is cf3 -Can use this file for both 3x3 and 5x5 (just check contents) <br> <br>

I've also slightly modified the source (engine.h, engine.cpp, and cityflow.cpp) to accodomate for a new "get_tl_phase", which was not available in the original Data Access API, just make sure to build the project again with these changes. <br><br>

eng.py is the actual simulation/Q-learning attempt
