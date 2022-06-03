# -*- coding: utf-8 -*-
"""Collection of functions for the manipulation of time series."""

from __future__ import absolute_import, division, print_function

import warnings

import mando
from mando.rst_text_formatter import RSTHelpFormatter

from .. import tsutils

warnings.filterwarnings("ignore")


@mando.command("stdtozrxp", formatter_class=RSTHelpFormatter, doctype="numpy")
@tsutils.doc(tsutils.docstrings)
def stdtozrxp_cli(
    input_ts="-",
    columns=None,
    start_date=None,
    end_date=None,
    dropna="no",
    skiprows=None,
    index_type="datetime",
    names=None,
    clean=False,
    round_index=None,
    source_units=None,
    target_units=None,
    rexchange=None,
):
    """Print out data to the screen in a WISKI ZRXP format.

    Parameters
    ----------
    rexchange
        [optional, default is None]

        The REXCHANGE ID to be written into the zrxp header.
    ${input_ts}
    ${columns}
    ${start_date}
    ${end_date}
    ${dropna}
    ${skiprows}
    ${index_type}
    ${names}
    ${clean}
    ${source_units}
    ${target_units}
    ${round_index}
    """
    tsutils.printiso(
        stdtozrxp(
            input_ts=input_ts,
            columns=columns,
            start_date=start_date,
            end_date=end_date,
            dropna=dropna,
            skiprows=skiprows,
            index_type=index_type,
            names=names,
            clean=clean,
            round_index=round_index,
            source_units=source_units,
            target_units=target_units,
            rexchange=rexchange,
        )
    )


@tsutils.copy_doc(stdtozrxp_cli)
def stdtozrxp(
    input_ts="-",
    columns=None,
    start_date=None,
    end_date=None,
    dropna="no",
    skiprows=None,
    index_type="datetime",
    names=None,
    clean=False,
    round_index=None,
    source_units=None,
    target_units=None,
    rexchange=None,
):
    """Print out data to the screen in a WISKI ZRXP format."""
    tsd = tsutils.common_kwds(
        input_ts,
        skiprows=skiprows,
        names=names,
        index_type=index_type,
        start_date=start_date,
        end_date=end_date,
        pick=columns,
        round_index=round_index,
        dropna=dropna,
        source_units=source_units,
        target_units=target_units,
        clean=clean,
    )
    if len(tsd.columns) != 1:
        raise ValueError(
            tsutils.error_wrapper(
                f"""
The "stdtozrxp" command can only accept a single
'time-series, instead it is seeing {len(tsd.columns)}.
"""
            )
        )

    if rexchange:
        print(f"#REXCHANGE{rexchange}|*|")
    for i in range(len(tsd)):
        print(
            (
                "{0.year:04d}{0.month:02d}{0.day:02d}{0.hour:02d}"
                "{0.minute:02d}{0.second:02d}, {1}"
            ).format(tsd.index[i], tsd[tsd.columns[0]][i])
        )
