
import os
from lib.analysis.author.curve_fitting import generate_cl_curve_fits, generate_rt_curve_fits
from lib.analysis.thread.time_statistics import generate_time_stats_threads
from lib.analysis.thread.message_activity import generate_message_activity_heatmaps
from lib.analysis.thread.wh_table import generate_wh_table_threads
from lib.mlcatconfig.config import Config


# mailbox_list = [d for d in os.listdir('data') if os.path.isdir(os.path.join('data', d))]-fork
mailbox_list = ['lkml', 'opensuse', 'opensuse-bugs', 'opensuse-factory', 'opensuse-features', 'opensuse-kernel', 'sakai-devel']
mailbox_list = ['opensuse-kernel']


for mailbox in mailbox_list:
    # Define directories
    path=os.path.abspath("lib/mlcatconfig/mlcat.cfg")
    path_ob= Config(mailbox)
    path_ob.read(path)
    path_ob.createVariables();
    
    print("Analyzing Thread Network in Mailbox:", mailbox)
    generate_message_activity_heatmaps(clean_headers_filename=path_ob.headers_filename, foldername=path_ob.foldername)
    generate_wh_table_threads(path_ob.nodelist_filename, path_ob.edgelist_filename,path_ob.get('param_paths','foldername')+mailbox+path_ob.get('generate_wh_table_authors','wh_tables_threads_path'))
    generate_time_stats_threads(path_ob.nodelist_filename, path_ob.edgelist_filename, path_ob.headers_filename, path_ob.get('param_paths','foldername')+mailbox+path_ob.get('generate_time_stats_threads','tables_path') ,plot=True)

    # For a range of months from Jan 2010 to Sep 2016, generate CL, RT curve fits
    monthly_cl_fit_coeffs = list()
    yearly_cl_fit_coeffs = list()
    monthly_rt_fit_coeffs = list()
    yearly_rt_fit_coeffs = list()

    for year in range(2015, 2017):
        for month in ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']:
            if month in {'Jan', 'Mar', 'May', 'Jul', 'Aug', 'Oct', 'Dec'}:
                max_day = 31
            elif month == 'Feb':
                max_day = 28
            else:
                max_day = 30
            outstr = generate_time_stats_threads(path_ob.nodelist_filename, path_ob.edgelist_filename, path_ob.headers_filename,
                                        foldername=path_ob.foldername + '/curve_fit/' + month + '_' + str(year) + '/',
                                        time_lbound="01 " + month + " " + str(year) + " 00:00:00 +0000",
                                        time_ubound=str(max_day) + " " + month + " " + str(year) + " 23:59:59 +0000")
            if outstr is None:
                (a, b, c), rmsd = generate_cl_curve_fits(path_ob.foldername + '/curve_fit/' + month + '_' + str(year) + '/')
                monthly_cl_fit_coeffs.append((month, year, a, b, c, rmsd))
                (a, b, c), rmsd = generate_rt_curve_fits(path_ob.foldername + '/curve_fit/' + month + '_' + str(year) + '/')
                monthly_rt_fit_coeffs.append((month, year, a, b, c, rmsd))

        outstr = generate_time_stats_threads(path_ob.nodelist_filename, path_ob.edgelist_filename, path_ob.headers_filename,
                                    foldername=path_ob.foldername + '/curve_fit/' + 'FULL_' + str(year) + '/',
                                    time_lbound="01 Jan " + str(year) + " 00:00:00 +0000",
                                    time_ubound="31 Dec " + str(year) + " 23:59:59 +0000")
        if outstr is None:
            (a, b, c), rmsd = generate_cl_curve_fits(path_ob.foldername + '/curve_fit/' + 'FULL_' + str(year) + '/')
            yearly_cl_fit_coeffs.append((year, a, b, c, rmsd))
            (a, b, c), rmsd = generate_rt_curve_fits(path_ob.foldername + '/curve_fit/' + 'FULL_' + str(year) + '/')
            yearly_rt_fit_coeffs.append((year, a, b, c, rmsd))

    with open(path_ob.foldername + path_ob.get('cl_csv_file','cl_csv_file_path'), 'w') as csv_file:
        csv_file.write("Monthly CL Curve-fit Coefficients:\nMonth, Year, A, B, C, RMSD\n")
        for month, year, a, b, c, rmsd in monthly_cl_fit_coeffs:
            csv_file.write(str(year) + ',' + month + ',' + str(a) + ',' + str(b) + ',' + str(c) + ',' + str(rmsd) + '\n')
        csv_file.write("\nYearly CL Curve-fit Coefficients:\nMonth, Year, A, B, C, RMSD\n")
        for year, a, b, c, rmsd in yearly_cl_fit_coeffs:
            csv_file.write(str(year) + ',' + ',' + str(a) + ',' + str(b) + ',' + str(c) + ',' + str(rmsd) +'\n')
        csv_file.close()

    with open(path_ob.foldername + path_ob.get('rt_csv_file','rt_csv_file_path'), 'w') as csv_file:
        csv_file.write("Monthly RT Curve-fit Coefficients:\nMonth, Year, A, B, C, RMSD\n")
        for month, year, a, b, c, rmsd in monthly_rt_fit_coeffs:
            csv_file.write(str(year) + ',' + month + ',' + str(a) + ',' + str(b) + ',' + str(c) + ',' + str(rmsd) + '\n')
        csv_file.write("\nYearly RT Curve-fit Coefficients:\nMonth, Year, A, B, C, RMSD\n")
        for year, a, b, c, rmsd in yearly_rt_fit_coeffs:
            csv_file.write(str(year) + ',' + ',' + str(a) + ',' + str(b) + ',' + str(c) + ',' + str(rmsd) + '\n')
        csv_file.close()

    print("----------------")



