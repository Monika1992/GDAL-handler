import gdal
import os
import Image


RASTER_PATH = ''


class GdalRasterAnalyzer(object):

    def prepare_local_variables(self, raster_path):
        self.raster_path = raster_path

    def get_source_dir_from_raster_path(self, raster_path):
        pass

    def list_raster_in_source_dir(self, source_dir_path):
        pass

    def load_raster(self, raster_path):
        pass

    def read_raster_statistics(self, raster_file_object, raster_statistics = None):

        raster_statistics_set = None

        if raster_statistics == 0:
            pass
        elif raster_statistics == 1:
            pass
        elif raster_statistics == 2:
            pass
        elif raster_statistics == 3:
            pass
        else:
            return raster_statistics_set

    def classify_raster_data_by_quantiles(self, raster_file_object, class_count):
        pass

    def cut_outliers(self, raster_standard_deviation, raster_file_object):
        pass

    def draw_raster_data_histogram(self, raster_data_object):
        pass

    def compare_two_histograms(self, raster_data_object_a, raster_data_object_b):
        pass





