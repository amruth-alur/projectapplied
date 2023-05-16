import numpy as np

def calculate_r_squared(y_actual, y_predicted):
    ssr = np.sum((y_actual - y_predicted) ** 2)
    sst = np.sum((y_actual - np.mean(y_actual)) ** 2)
    r_squared = 1 - (ssr / sst)
    return r_squared

# Example usage
y_actual = np.array([2500, 2550, 2450, 2600, 2500, 2550, 2450, 2600, 2500, 2550, 2450, 2600,
                     2500, 2550, 2450, 2600, 2500, 2550, 2450, 2600, 2500])
y_predicted = np.array([predict_crop_yield(2000, 25, 10, 400, 60),
                        predict_crop_yield(2001, 26, 12, 380, 62),
                        predict_crop_yield(2002, 24, 11, 410, 58),
                        predict_crop_yield(2003, 27, 13, 390, 63),
                        predict_crop_yield(2004, 25, 10, 400, 60),
                        predict_crop_yield(2005, 26, 12, 380, 62),
                        predict_crop_yield(2006, 24, 11, 410, 58),
                        predict_crop_yield(2007, 27, 13, 390, 63),
                        predict_crop_yield(2008, 25, 10, 400, 60),
                        predict_crop_yield(2009, 26, 12, 380, 62),
                        predict_crop_yield(2010, 24, 11, 410, 58),
                        predict_crop_yield(2011, 27, 13, 390, 63),
                        predict_crop_yield(2012, 25, 10, 400, 60),
                        predict_crop_yield(2013, 26, 12, 380, 62),
                        predict_crop_yield(2014, 24, 11, 410, 58),
                        predict_crop_yield(2015, 27, 13, 390, 63),
                        predict_crop_yield(2016, 25, 10, 400, 60),
                        predict_crop_yield(2017, 26, 12, 380, 62),
                        predict_crop_yield(2018, 24, 11, 410, 58),
                        predict_crop_yield(2019, 27, 13, 390, 63),
                        predict_crop_yield(2020, 25, 10, 400, 60)])

r_squared = calculate_r_squared(y_actual, y_predicted)
print("R-squared:", r_squared)
