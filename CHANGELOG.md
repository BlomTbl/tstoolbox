## v103.14.9 (2021-08-01)

## v103.14.8 (2021-07-30)

### Fix

- plot input_ts, cli values

## v103.13.8 (2021-07-28)

### Fix

- units, Float64, flexible input

## v103.12.8 (2021-07-25)

### Fix

- Correctly include units.
- Correctly including units in name.

## v103.11.8 (2021-07-21)

### Fix

- Can work with "A" and "M" frequencies.
- remove pint units for calculations.

## v103.10.8 (2021-07-20)

### Fix

- Correct column names to allow for empty units.
- Added "--multi-line 3" to isort

### Refactor

- rearrange to allow "import tstoolbox"
- Reorganized to allow for "import tstoolbox"

## v103.9.8 (2021-07-07)

### Fix

- work to add units to column headers

## v103.8.8 (2021-06-29)

### Refactor

- .pre-commit-config.yaml

### Feat

- Added the beginnings of a forecast feature
style:  Added several features to .pre-commit-config.yaml
- Returned the ability to use comma separated file names.

### Fix


## v103.6.8 (2021-05-25)

### Feat

- Added the capability of using the index (usually datetimeindex) as
a `x_train_cols` in the regression.
fix: Now detect is DataFrame or Series and skip further processing in
'read_iso_ts'
- Added "min_count" keyword to `aggregate`
docs: Misc.
build: Added "extra_requires" to setup.py for development

## v103.5.8 (2021-05-07)

### Feat

- New read from xlsx, wdm files.
- rework new multiple sources read feature.
- Continue type hint tests.

### Refactor

- read_iso_ts is now part of common_kwds.

## v102.5.8 (2021-03-06)

### Fix

- Minor fixes.
- Docs, fixes because of changed memory_optimize
- memory_optimize is less aggressive
- read --columns filters output.

### Feat

- "Typical" to coerce args/kwargs.
- added butterworth filter

## v101.5.8 (2020-10-21)

### Fix

- Fixed months_across_years.

## v101.4.8 (2020-09-04)

### Fix

- Matched Paul Tor's color order.
- Needed matplotlib styles in MANIFEST.in.

## v101.4.7 (2020-09-04)

### Fix

- Incorporated SciencePlots mpl styles.

## v101.4.6 (2020-09-04)

### Fix

- Pandas implemented new tolerance approach.
- Better working with time zones.

### Feat

- Lossless compression of dataframes.
- Added plot styles, new default is "bright".

## v100.4.6 (2020-07-08)

### Fix

- Correctly uses multiple input to 'regression'

## v100.4.5 (2020-07-03)

### Feat

- Added regression sub-command.
- Added 'output_names' keyword to rename columns on output.
- Added hatch patterns to bar plots.

### Fix

- Allow for index,y to by used for "xy" type.

## v100.3.4 (2020-06-24)

### Feat

- Fix x,y plots to allow for index,y plotting
- Added autocorrelation for each column.

## v100.3.3 (2020-06-10)

### Fix

- Corrected columns selection when 0
- xy plot incorrectly inserted a column.
- Allow fit to work across multiple columns.

### Feat

- Added autocorrelation if lags==0.

## v100.2.0 (2020-06-04)

### Refactor

- Just added some vertical space.
- Improved description of r statistic.

### Feat

- Added scikit-learn scaling functions.
- Added method keyword.
- lowess and linear fit
- Added coefficient of determination to gof.

### Fix

- join_axes is deprecated.
- Added force_freq throughout.

## v100.1.0 (2020-04-25)

### Feat

- Added "groupby='all' to aggregate.

## v47.97.50.35 (2020-04-01)

## v46.96.49.34 (2020-03-06)

## v45.94.49.34 (2020-03-04)

## v43.94.47.34 (2020-02-20)

## v43.91.45.33 (2019-11-21)

## v43.89.43.31 (2019-11-01)

## v40.87.42.28 (2019-09-18)

## v40.86.42.28 (2019-09-17)

## v36.86.39.27 (2019-08-28)

## v35.86.39.27 (2019-06-21)

## v35.85.39.27 (2019-06-21)

## v34.82.39.27 (2019-05-30)