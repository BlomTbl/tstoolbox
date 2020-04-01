#!/usr/bin/env python
# -*- coding: utf-8 -*-

from unittest import TestCase

from pandas.testing import assert_frame_equal
from tstoolbox import tstoolbox, tsutils


class TestDescribe(TestCase):
    def setUp(self):
        self.data_0_to_1 = tstoolbox.read("tests/data_sunspot_normalized_0_to_1.csv")
        self.data_0_to_1.columns = ["Area::minmax"]
        self.data_10_to_20 = tstoolbox.read(
            "tests/data_sunspot_normalized_10_to_20.csv"
        )
        self.data_10_to_20.columns = ["Area::minmax"]
        self.data_zscore = tstoolbox.read("tests/data_sunspot_normalized_zscore.csv")
        self.data_zscore.columns = ["Area::zscore"]
        self.data_zscore = tsutils.memory_optimize(self.data_zscore)
        self.data_pct_rank = tstoolbox.read(
            "tests/data_sunspot_normalized_pct_rank.csv"
        )
        self.data_pct_rank.columns = ["Area::pct_rank"]
        self.data_pct_rank = tsutils.memory_optimize(self.data_pct_rank)

    def test_normalize_0_to_1(self):
        """Test the normalization API function from 0 to 1."""
        out = tstoolbox.normalization(input_ts="tests/data_sunspot.csv")
        assert_frame_equal(out, self.data_0_to_1)

    def test_normalize_10_to_20(self):
        """Test the normalization API function from 10 to 20."""
        out = tstoolbox.normalization(
            min_limit=10, max_limit=20, input_ts="tests/data_sunspot.csv"
        )
        assert_frame_equal(out, self.data_10_to_20)

    def test_normalize(self):
        """Test the normalization API function using the zscore method."""
        out = tstoolbox.normalization(mode="zscore", input_ts="tests/data_sunspot.csv")
        assert_frame_equal(
            out, self.data_zscore, check_less_precise=4, check_column_type=False
        )

    def test_pct_rank(self):
        """Test the normalization API function using the pct_rank method."""
        out = tstoolbox.normalization(
            mode="pct_rank", input_ts="tests/data_sunspot.csv"
        )
        assert_frame_equal(out, self.data_pct_rank)
