# XlogADIF2SOTAactivator.py #
----------

## About ##
**XlogADIF2SOTAactivator.py** is a Python application that converts an Xlog
ADIF export file into a SOTA Activator Log (CSV) that can be uploaded to the
SOTA Data website.

## Dependencies ##
Python 2.6+?

## Requirements ##
1. This application requires a log exported from Xlog using the ADIF format.
   At a minimum, the log must contain a date, timestamp, band, mode and callsign
   of each QSO using the appropriate ADIF format tags.
2. This application will ask the user to provide the callsign they used during
   the activation.
3. This application will ask the user to provide the summit reference of the
   summit that was activated.

## Assumptions ##

## Limitations ##
1. This application can only process one summit activation at a time.  You will
   need to generate a log specific to each summit reference.

## Functionality ##
1. The application will ask the user to provide:
   * The callsign used during the activation
   * The summit reference of the activating summit
   * The path/filename of the ADIF log exported from Xlog
   * The path/filename of the output file to be written
2. The application will attempt to open the input file specified by the user.
   * If this file does not exist, the application will display an error stating
   such and exit.
   * If this file does exist, the application will continue to Step 3.
3. The application will attempt to open the output file specified by the user.
   * If the application is unable to create the file (incorrect path/filename
   provided or disk write error received), the application will display an
   error stating such and exit.
   * If the file can be created/written to, the application will do so and exit.
