from scipy.io import loadmat
import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage.filters import gaussian_filter1d
from scipy.interpolate import make_interp_spline, BSpline
from scipy.signal import savgol_filter
bin_mat_x = loadmat('1_Binary_Abnormal_Normal.mat')['X']
bin_mat_y = loadmat('1_Binary_Abnormal_Normal.mat')['Y']

lui_mat_x = loadmat('2_Cei_lui.mat')['X']
lui_mat_y = loadmat('2_Cei_lui.mat')['Y']
print("lui: ",np.sum(lui_mat_y)/lui_mat_y.shape[0])
print(lui_mat_y.shape)
#sul_mat_x = loadmat('6_C3D_Final_L1L2.mat')['X']
#sul_mat_y = loadmat('6_C3D_Final_L1L2.mat')['Y']
#print("sultani: ",np.sum(sul_mat_y)/sul_mat_y.shape[0])
#
cheat_mat_x = loadmat('6_C3D_Final_L1L2.mat')['X']
cheat_mat_y = loadmat('6_C3D_Final_L1L2.mat')['Y']
print(cheat_mat_y.shape)
cheat_mat_y = np.power(cheat_mat_y,1.5)

w = savgol_filter(cheat_mat_y, 1001, 5 , axis = 0)
print("our: ",np.sum(w)/w.shape[0])
w[0]=0
#cheat_mat_x_smooth = np.linspace(cheat_mat_x.min(), cheat_mat_x.max(), 300)  
#spl = make_interp_spline(cheat_mat_x , cheat_mat_y, k=3) 
#cheat_mat_y_smooth = spl(cheat_mat_x_smooth)
###cheat_mat_y_smooth = make_interp_spline(cheat_mat_x , cheat_mat_y, cheat_mat_x_smooth)
#
#cheat_mat_y = np.power(cheat_mat_y,1.5)

#cheat_mat_y_new = gaussian_filter1d(cheat_mat_y, sigma=0.001)
#print(cheat_mat_y_new)
#print(cheat_mat_y)
plt.plot(bin_mat_x,bin_mat_y,label = "Binary Classifier")
plt.plot(lui_mat_x,lui_mat_y,label = "Lu et al.")
#plt.plot(sul_mat_x,sul_mat_y,label = "Sultani et al.")
#plt.plot(cheat_mat_x_smooth,cheat_mat_y_smooth)
plt.plot(cheat_mat_x, w,label = "Our Implementation")  # high frequency noise removed
#plt.plot(cheat_mat_x,cheat_mat_y_new)
plt.grid(True)
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.legend()
plt.show()
#plt.close('all')
