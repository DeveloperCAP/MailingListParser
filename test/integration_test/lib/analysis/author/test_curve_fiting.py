from lib.analysis.author.curve_fitting import *
import unittest
import mock


def test_inv_func():

    x = 5
    a = 10
    b = 25
    c = 7
    assert inv_func(x, a, b, c) == 10

def test_generate_crt_dist():

    csv_filename = './test/integration_test/data/conversation_refresh_times.csv'
    req_re_times = ([106.01, 272.03000000000003, 438.05000000000007, 604.07, 770.09, 936.1100000000001, 1102.13, 1268.15, 1434.17, 1600.19, 1766.21, 1932.23, 2098.25, 2264.2700000000004, 2430.29, 2596.3100000000004, 2762.33, 2928.3500000000004, 3094.37, 3260.3900000000003, 3426.41, 3592.4300000000003, 3758.45, 3924.4700000000003, 4090.4900000000002, 4256.51, 4422.530000000001, 4588.55, 4754.57, 4920.59, 5086.610000000001, 5252.63, 5418.650000000001, 5584.67, 5750.6900000000005, 5916.710000000001, 6082.7300000000005, 6248.75, 6414.77, 6580.790000000001, 6746.81, 6912.83, 7078.85, 7244.870000000001, 7410.89, 7576.91, 7742.93, 7908.950000000001, 8074.970000000001, 8240.99], [0.375, 0.0, 0.0, 0.0, 0.125, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.125, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.125, 0.0, 0.0, 0.0, 0.0, 0.0, 0.125, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.125])
    generate_crt_dist(csv_filename) == req_re_times


@mock.patch("matplotlib.pyplot.figure")
@mock.patch("matplotlib.pyplot.plot")
@mock.patch("matplotlib.pyplot.legend")
@mock.patch("matplotlib.pyplot.ylabel")
@mock.patch("matplotlib.pyplot.xlabel")
@mock.patch("matplotlib.pyplot.savefig")
def test_generate_crt_curve_fits(mock_figure, mock_plot, mock_legend, mock_ylabel, mock_xlabel, mock_savefig):
    
    foldername = './test/integration_test/data/curve_fitting/'

    generate_crt_curve_fits(foldername)


def test_generate_cl_dist():

    csv_filename = './test/integration_test/data/conversation_length.csv'
    req_lengths = ([7861.65, 22400.949999999997, 36940.25, 51479.549999999996, 66018.85, 80558.15, 95097.44999999998, 109636.75, 124176.05, 138715.35, 153254.65, 167793.94999999998, 182333.25, 196872.55, 211411.84999999998, 225951.15, 240490.44999999998, 255029.75, 269569.05000000005, 284108.35, 298647.65, 313186.94999999995, 327726.25, 342265.54999999993, 356804.85, 371344.15, 385883.44999999995, 400422.75, 414962.04999999993, 429501.35, 444040.65, 458579.94999999995, 473119.25, 487658.54999999993, 502197.85, 516737.15, 531276.45, 545815.75, 560355.05, 574894.35, 589433.6499999999, 603972.95, 618512.25, 633051.55, 647590.85, 662130.1499999999,676669.45, 691208.75, 705748.0499999999, 720287.35], [0.4444444444444444, 0.0, 0.0, 0.2222222222222222, 0.0, 0.0, 0.1111111111111111, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.1111111111111111, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.1111111111111111])
    assert generate_cl_dist(csv_filename) == req_lengths


@mock.patch("matplotlib.pyplot.figure")
@mock.patch("matplotlib.pyplot.plot")
@mock.patch("matplotlib.pyplot.legend")
@mock.patch("matplotlib.pyplot.ylabel")
@mock.patch("matplotlib.pyplot.xlabel")
@mock.patch("matplotlib.pyplot.savefig")
def test_generate_cl_curve_fits(mock_figure, mock_plot, mock_legend, mock_ylabel, mock_xlabel, mock_savefig):
    
    foldername = './test/integration_test/data/curve_fitting/'

    generate_cl_curve_fits(foldername)


def test_generate_rt_dist():

    csv_filename = './test/integration_test/data/response_time.csv'
    req_times = ([783.76, 1441.28, 2098.8, 2756.3199999999997, 3413.84, 4071.3599999999997, 4728.879999999999, 5386.4, 6043.92, 6701.4400000000005, 7358.959999999999, 8016.48, 8674.0, 9331.52, 9989.039999999999, 10646.56, 11304.08, 11961.6, 12619.119999999999, 13276.64, 13934.16, 14591.68, 15249.199999999999, 15906.72, 16564.239999999998, 17221.760000000002, 17879.28, 18536.8, 19194.32, 19851.839999999997, 20509.36, 21166.879999999997, 21824.4, 22481.92, 23139.440000000002, 23796.96, 24454.48, 25112.0, 25769.519999999997, 26427.04, 27084.559999999998, 27742.08, 28399.6, 29057.12, 29714.64, 30372.159999999996, 31029.68, 31687.199999999997, 32344.72, 33002.24], [0.1111111111111111, 0.2222222222222222, 0.2222222222222222, 0.0, 0.1111111111111111, 0.2222222222222222, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.1111111111111111])
    assert generate_rt_dist(csv_filename) == req_times


@mock.patch("matplotlib.pyplot.figure")
@mock.patch("matplotlib.pyplot.plot")
@mock.patch("matplotlib.pyplot.legend")
@mock.patch("matplotlib.pyplot.ylabel")
@mock.patch("matplotlib.pyplot.xlabel")
@mock.patch("matplotlib.pyplot.savefig")
def test_generate_rt_curve_fits(mock_figure, mock_plot, mock_legend, mock_ylabel, mock_xlabel, mock_savefig):
    
    foldername = './test/integration_test/data/curve_fitting/'

    generate_rt_curve_fits(foldername)
