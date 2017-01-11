import gdal
import os
from PIL import Image


RASTER_PATH = 'C:\Users/blahova.m\Desktop/WGS842017-01-09_layer_14_exported_average.tif'


class GdalRasterAnalyzer(object):

    # Returns source directory from given raster file system path as string
    def get_source_dir_from_raster_path(self, raster_path):
        return os.path.dirname(raster_path)

    # returns raster data set object. If given raster path is not valid returns False and explaining console message
    def load_raster(self, raster_path):
        if os.path.exists(raster_path):
            try:
                return gdal.Open(raster_path)
            except IOError as e:
                # TODO : Change to log message added to log file
                print 'Opening raster data set failed with: ' + str(e)
                return False
        else:
            # TODO : Change to log message added to log file
            print 'Raster file path is not valid'
            return False

    # Returns list of files having exact file extension. IF given path is not valid returns False and console message
    def list_files_in_source_dir(self, source_dir_path, raster_file_extension):

        if os.path.isdir(source_dir_path):
            searched_files_list = []
            for file in os.listdir(source_dir_path):
                if file.endswith(raster_file_extension):
                    searched_files_list.append(file)

            return searched_files_list

        else:
            # TODO : Change to log message added to log file
            print 'Input path is not valid system path'
            return False

    # Returns string information about raster data sets projection
    def get_raster_file_coordinate_system(self, raster_path):
        data_source = self.load_raster(raster_path)
        return data_source.GetProjection()

    def read_raster_statistics(self, raster_file_object, raster_band_pointer, desired_statistics = str('all')):

        raster_band_object = raster_file_object.GetRasterBand(int(raster_band_pointer))
        raster_statistics_set = raster_band_object.GetStatistics(True, True)

        if desired_statistics == 'all':
            return raster_statistics_set
        elif desired_statistics == 'min':
            return raster_statistics_set[0]
        elif desired_statistics == 'max':
            return raster_statistics_set[1]
        elif desired_statistics == 'med':
            return raster_statistics_set[3]
        elif raster_statistics_set == 'mean':
            return raster_statistics_set[4]
        else:
            # TODO : Change to log message added to log file
            print 'Desired statistics pointer is not valid use one of: all, min, max, med, mean.'
            return None

    def reproject_raster_file(self, projection):
        os.sys('gdalwarp infile.tif outfile.tif -t_srs "+proj=longlat +ellps=WGS84"')

    def classify_raster_data_by_quintiles(self, raster_file_object, class_count):
        pass

    def cut_outliers(self, raster_standard_deviation, raster_file_object):
        pass

    def draw_raster_data_histogram(self, raster_data_object):
        pass

    def compare_two_histograms(self, raster_data_object_a, raster_data_object_b):
        pass



gdal_processor = GdalRasterAnalyzer()

raster_object = gdal_processor.load_raster(RASTER_PATH)
raster_source_dir = gdal_processor.get_source_dir_from_raster_path(RASTER_PATH)
raster_files_in_source_dir = gdal_processor.list_files_in_source_dir(RASTER_PATH, '.tif')
print raster_files_in_source_dir
raster_coord_system = gdal_processor.get_raster_file_coordinate_system(RASTER_PATH)
print raster_coord_system
raster_stat = gdal_processor.read_raster_statistics(raster_object, 1)
print raster_stat


