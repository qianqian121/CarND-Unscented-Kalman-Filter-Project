import matplotlib.pyplot as plt
import pandas as pd

#my_cols=['px_est','py_est','vx_est','vy_est','px_meas','py_meas','px_gt','py_gt','vx_gt','vy_gt']
my_cols=['time_stamp', 'px_state', 'py_state', 'v_state', 'yaw_angle_state', 'yaw_rate_state', 'sensor_type', 'NIS', 'px_measured', 'py_measured', 'px_ground_truth', 'py_ground_truth', 'vx_ground_truth', 'vy_ground_truth']
# with open('/root/sharefolder/udacity/CarND-Unscented-Kalman-Filter-Project/build/output1.txt') as f:
with open('/Users/ssi/sharefolder/CarND-Unscented-Kalman-Filter-Project/build/output3.txt') as f:
    table_ekf_output = pd.read_table(f, sep='\t', header=1, names=my_cols, lineterminator='\n')

#table_ekf_output

x1=table_ekf_output['px_state']
y1=table_ekf_output['py_state']
x2=table_ekf_output['px_measured']
y2=table_ekf_output['py_measured']
x3=table_ekf_output['px_ground_truth']
y3=table_ekf_output['py_ground_truth']
plt.plot(x1, y1, x2, y2, x3, y3, linewidth=2.0)
plt.show()
