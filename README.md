# DC_reversal_trading_strategy
This project aims to develop a trading strategy based on Directional Change intrinsic time series. It will be tested and optimised on FX ticker data downloaded from https://www.histdata.com/download-free-forex-data/.
FILES DESCRIPTION:
**"FX_Data_Import.py"** contains the the FX data import function from a local MySQL database.
**"transform_to_intrinsic_time_series.py"** file contains the function that identifies all DC events in the FX dataset based on a given "dc_threshold".
**"DC_reverersal_strategy_code.py"** file contains the logic of the strategy and records all taken positions.
**"optimisation_function.py"** file contains an optimisation function that identifies the optimal DC threshold for a given dataset.
**"DC reversal project description.pdf"** file contains full description of the process as well as step by step guide.
