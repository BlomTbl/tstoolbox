#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_peak_detect
----------------------------------

Tests for `tstoolbox` module.
"""

from pandas.util.testing import TestCase
from pandas.util.testing import assert_frame_equal
import sys
import shlex
import subprocess
try:
    from cStringIO import StringIO
except:
    from io import StringIO

import pandas as pd

from tstoolbox import tstoolbox


def capture(func, *args, **kwds):
    sys.stdout = StringIO()      # capture output
    out = func(*args, **kwds)
    out = sys.stdout.getvalue()  # release output
    return out


output_peak_detection=b'Datetime,0,0_peak,0_valley\n2000-01-01 00:00:00,0,,\n2000-01-01 01:00:00,0.258819,,\n2000-01-01 02:00:00,0.5,,\n2000-01-01 03:00:00,0.707107,,\n2000-01-01 04:00:00,0.866025,,\n2000-01-01 05:00:00,0.965926,,\n2000-01-01 06:00:00,1,1,\n2000-01-01 07:00:00,0.965926,,\n2000-01-01 08:00:00,0.866025,,\n2000-01-01 09:00:00,0.707107,,\n2000-01-01 10:00:00,0.5,,\n2000-01-01 11:00:00,0.258819,,\n2000-01-01 12:00:00,1.22465e-16,,\n2000-01-01 13:00:00,-0.258819,,\n2000-01-01 14:00:00,-0.5,,\n2000-01-01 15:00:00,-0.707107,,\n2000-01-01 16:00:00,-0.866025,,\n2000-01-01 17:00:00,-0.965926,,\n2000-01-01 18:00:00,-1,,-1\n2000-01-01 19:00:00,-0.965926,,\n2000-01-01 20:00:00,-0.866025,,\n2000-01-01 21:00:00,-0.707107,,\n2000-01-01 22:00:00,-0.5,,\n2000-01-01 23:00:00,-0.258819,,\n'
input_peak_detection = b'Datetime,0\n2000-01-01 00:00:00,0.0\n2000-01-01 01:00:00,0.258819\n2000-01-01 02:00:00,0.5\n2000-01-01 03:00:00,0.707107\n2000-01-01 04:00:00,0.866025\n2000-01-01 05:00:00,0.965926\n2000-01-01 06:00:00,1.0\n2000-01-01 07:00:00,0.965926\n2000-01-01 08:00:00,0.866025\n2000-01-01 09:00:00,0.707107\n2000-01-01 10:00:00,0.5\n2000-01-01 11:00:00,0.258819\n2000-01-01 12:00:00,1.22465e-16\n2000-01-01 13:00:00,-0.258819\n2000-01-01 14:00:00,-0.5\n2000-01-01 15:00:00,-0.707107\n2000-01-01 16:00:00,-0.866025\n2000-01-01 17:00:00,-0.965926\n2000-01-01 18:00:00,-1.0\n2000-01-01 19:00:00,-0.965926\n2000-01-01 20:00:00,-0.866025\n2000-01-01 21:00:00,-0.707107\n2000-01-01 22:00:00,-0.5\n2000-01-01 23:00:00,-0.258819\n'

class TestPeakDetect(TestCase):
    def setUp(self):
        dindex = pd.date_range('2000-01-01T00:00:00', periods=24, freq='H')
        self.ats = pd.np.arange(0, 360, 15)
        self.ats = pd.np.sin(2*pd.np.pi*self.ats/360)
        self.ats = pd.DataFrame(self.ats, index=dindex)

        self.compare = self.ats.copy()
        self.compare = self.compare.join(pd.Series(pd.np.zeros(len(self.ats)).astype('f'), index=self.ats.index, name='0_peak'))
        self.compare = self.compare.join(pd.Series(pd.np.zeros(len(self.ats)).astype('f'), index=self.ats.index, name='0_valley'))
        self.compare.index.name = 'Datetime'
        self.compare['0_peak'] = pd.np.nan
        self.compare['0_peak'][self.compare[0] == 1.0] = 1.0
        self.compare['0_valley'] = pd.np.nan
        self.compare['0_valley'][self.compare[0] == -1.0] = -1.0

    def test_peak_rel_direct(self):
        out = tstoolbox.peak_detection(input_ts=self.ats, print_input=True, type='both')
        self.maxDiff = None
        assert_frame_equal(out, self.compare)

    def test_peak_minmax_direct(self):
        out = tstoolbox.peak_detection(method='minmax', window=3, input_ts=self.ats, print_input=True, type='both')
        self.maxDiff = None
        assert_frame_equal(out, self.compare)

    def test_peak_zero_crossing_direct(self):
        out = tstoolbox.peak_detection(method='zero_crossing', window=3, input_ts=self.ats, print_input=True, type='both')
        self.maxDiff = None
        fp = open('/tmp/tslog3.txt', 'w')
        fp.write('{0}'.format(out))
        fp.write('\n')
        fp.write('{0}'.format(self.compare))
        fp.close()
        assert_frame_equal(out, self.compare)

#    def test_peak_parabola_direct(self):
#        out = tstoolbox.peak_detection(method='parabola', input_ts=self.ats, print_input=True, type='both')
#        self.maxDiff = None
#        assert_frame_equal(out, self.compare)

    def test_peak_sine_direct(self):
        out = tstoolbox.peak_detection(method='sine', points=9, input_ts=self.ats, print_input=True, type='both')
        self.maxDiff = None
        assert_frame_equal(out, self.compare)

    # CLI...
    def test_peak_rel_cli(self):
        args = 'tstoolbox peak_detection --type="both" --print_input=True'
        args = shlex.split(args)
        out = subprocess.Popen(args, stdout=subprocess.PIPE, stdin=subprocess.PIPE).communicate(input=input_peak_detection)[0]
        self.maxDiff = None
        self.assertEqual(out, output_peak_detection)

    def test_peak_minmax_cli(self):
        args = 'tstoolbox peak_detection --window=3 --method="minmax" --type="both" --print_input=True'
        args = shlex.split(args)
        out = subprocess.Popen(args, stdout=subprocess.PIPE, stdin=subprocess.PIPE).communicate(input=input_peak_detection)[0]
        self.maxDiff = None
        self.assertEqual(out, output_peak_detection)

    def test_peak_zero_crossing_cli(self):
        args = 'tstoolbox peak_detection --method="zero_crossing" --type="both" --window=3 --print_input=True'
        args = shlex.split(args)
        out = subprocess.Popen(args, stdout=subprocess.PIPE, stdin=subprocess.PIPE).communicate(input=input_peak_detection)[0]
        self.maxDiff = None
        self.assertEqual(out, output_peak_detection)

    #def test_peak_parabola_cli(self):
    #    args = 'tstoolbox peak_detection --method="parabola" --type="both" --print_input=True'
    #    args = shlex.split(args)
    #    out = subprocess.Popen(args, stdout=subprocess.PIPE, stdin=subprocess.PIPE).communicate(input=input_peak_detection)[0]
    #    self.maxDiff = None
    #    self.assertEqual(out, output_peak_detection)

    def test_peak_sine_cli(self):
        args = 'tstoolbox peak_detection --method="sine" --type="both" --points=9 --print_input=True'
        args = shlex.split(args)
        out = subprocess.Popen(args, stdout=subprocess.PIPE, stdin=subprocess.PIPE).communicate(input=input_peak_detection)[0]
        self.maxDiff = None
        self.assertEqual(out, output_peak_detection)
