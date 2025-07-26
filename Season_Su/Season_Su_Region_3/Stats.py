#!/usr/bin/python3
import pandas as pd
import os
import re
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as colors
from matplotlib.ticker import PercentFormatter

def extract_number(filename):
    match = re.search(r'(\d+)\.txt$', filename)
    if match:
        return int(match.group(1))
    else:
        raise ValueError(f"Filename does not match expected pattern: {filename}")

# Get the full path of the current working directory
current_directory_path = os.getcwd()

# Extract the base name (the last component) of the path
Season = os.path.basename(current_directory_path)

# Process x files
paths_x = []
for path_to_result in os.listdir(Season+'_Results'):
    if path_to_result[:8] == 'r3E2gs_x':
        paths_x.append(Season+'_Results/'+path_to_result)
paths_x = sorted(paths_x, key = extract_number)
matrix_x = [np.loadtxt(f) for f in paths_x]
matrix_x = np.stack(matrix_x)
mean_x = np.sum(matrix_x, axis=0)/len(paths_x)
var_x = (matrix_x-mean_x)**2
sample_var_x = np.sum(var_x, axis=0)/(len(paths_x)-1)
mean_var_x = np.mean(sample_var_x)
s_mean_var_x = np.sqrt(mean_var_x)
L2_dist_x = np.sqrt(np.sum(var_x, axis=1))
rms_dist_x = np.sqrt(np.sum(var_x, axis=1)/len(matrix_x[1,:]))

# Process p files
paths_p = []
for path_to_result in os.listdir(Season+'_Results'):
    if path_to_result[:8] == 'r3E2gs_p':
        paths_p.append(Season+'_Results/'+path_to_result)
paths_p = sorted(paths_p, key = extract_number)
matrix_p = [np.loadtxt(f) for f in paths_p]
matrix_p = np.stack(matrix_p)
mean_p = np.sum(matrix_p, axis=0)/len(paths_p)
var_p = (matrix_p-mean_p)**2
sample_var_p = np.sum(var_p, axis=0)/(len(paths_p)-1)
mean_var_p = np.mean(sample_var_p)
s_mean_var_p = np.sqrt(mean_var_p)
L2_dist_p = np.sqrt(np.sum(var_p, axis=1))
rms_dist_p = np.sqrt(np.mean(var_p, axis=1))

# Process e files
paths_e = []
for path_to_result in os.listdir(Season+'_Results'):
    if path_to_result[:8] == 'r3E2gs_e':
        paths_e.append(Season+'_Results/'+path_to_result)
paths_e = sorted(paths_e, key = extract_number)
matrix_e = [np.loadtxt(f) for f in paths_e]
matrix_e = np.stack(matrix_e)
mean_e = np.sum(matrix_e, axis=0)/len(paths_e)
var_e = (matrix_e-mean_e)**2
sample_var_e = np.sum(var_e, axis=0)/(len(paths_e)-1)
mean_var_e = np.mean(sample_var_e)
s_mean_var_e = np.sqrt(mean_var_e)
L2_dist_e = np.sqrt(np.sum(var_e, axis=1))
rms_dist_e = np.sqrt(np.mean(var_e, axis=1))

# Create and save each plot individually
n_bins = 15
output_dir = Season + '_Results'

# L2 Distance (x)
plt.figure(figsize=(6, 4))
plt.hist(L2_dist_x, bins=n_bins, color='skyblue', edgecolor='black')
plt.title('L2 Distance (x)')
plt.grid(True, linestyle='--', alpha=0.7)
plt.text(0.95, 0.95, f'mean_var: {mean_var_x:.2e}\ns_mean_var: {s_mean_var_x:.2e}',
         transform=plt.gca().transAxes, ha='right', va='top',
         bbox=dict(facecolor='white', alpha=0.8))
plt.tight_layout()
plt.savefig(os.path.join(output_dir, f'{Season}_L2_x.png'))
plt.close()

# L2 Distance (p)
plt.figure(figsize=(6, 4))
plt.hist(L2_dist_p, bins=n_bins, color='salmon', edgecolor='black')
plt.title('L2 Distance (p)')
plt.grid(True, linestyle='--', alpha=0.7)
plt.text(0.95, 0.95, f'mean_var: {mean_var_p:.2e}\ns_mean_var: {s_mean_var_p:.2e}',
         transform=plt.gca().transAxes, ha='right', va='top',
         bbox=dict(facecolor='white', alpha=0.8))
plt.tight_layout()
plt.savefig(os.path.join(output_dir, f'{Season}_L2_p.png'))
plt.close()

# L2 Distance (e)
plt.figure(figsize=(6, 4))
plt.hist(L2_dist_e, bins=n_bins, color='lightgreen', edgecolor='black')
plt.title('L2 Distance (e)')
plt.grid(True, linestyle='--', alpha=0.7)
plt.text(0.95, 0.95, f'mean_var: {mean_var_e:.2e}\ns_mean_var: {s_mean_var_e:.2e}',
         transform=plt.gca().transAxes, ha='right', va='top',
         bbox=dict(facecolor='white', alpha=0.8))
plt.tight_layout()
plt.savefig(os.path.join(output_dir, f'{Season}_L2_e.png'))
plt.close()

# RMS Distance (x)
plt.figure(figsize=(6, 4))
plt.hist(rms_dist_x, bins=n_bins, color='skyblue', edgecolor='black')
plt.title('RMS Distance (x)')
plt.grid(True, linestyle='--', alpha=0.7)
plt.text(0.95, 0.95, f'mean_var: {mean_var_x:.2e}\ns_mean_var: {s_mean_var_x:.2e}',
         transform=plt.gca().transAxes, ha='right', va='top',
         bbox=dict(facecolor='white', alpha=0.8))
plt.tight_layout()
plt.savefig(os.path.join(output_dir, f'{Season}_RMS_x.png'))
plt.close()

# RMS Distance (p)
plt.figure(figsize=(6, 4))
plt.hist(rms_dist_p, bins=n_bins, color='salmon', edgecolor='black')
plt.title('RMS Distance (p)')
plt.grid(True, linestyle='--', alpha=0.7)
plt.text(0.95, 0.95, f'mean_var: {mean_var_p:.2e}\ns_mean_var: {s_mean_var_p:.2e}',
         transform=plt.gca().transAxes, ha='right', va='top',
         bbox=dict(facecolor='white', alpha=0.8))
plt.tight_layout()
plt.savefig(os.path.join(output_dir, f'{Season}_RMS_p.png'))
plt.close()

# RMS Distance (e)
plt.figure(figsize=(6, 4))
plt.hist(rms_dist_e, bins=n_bins, color='lightgreen', edgecolor='black')
plt.title('RMS Distance (e)')
plt.grid(True, linestyle='--', alpha=0.7)
plt.text(0.95, 0.95, f'mean_var: {mean_var_e:.2e}\ns_mean_var: {s_mean_var_e:.2e}',
         transform=plt.gca().transAxes, ha='right', va='top',
         bbox=dict(facecolor='white', alpha=0.8))
plt.tight_layout()
plt.savefig(os.path.join(output_dir, f'{Season}_RMS_e.png'))
plt.close()

# #!/usr/bin/python3
# import pandas as pd
# import os
# import re
# import numpy as np
# import matplotlib.pyplot as plt
# import matplotlib.colors as colors
# from matplotlib.ticker import PercentFormatter
# def extract_number(filename):
#     match = re.search(r'(\d+)\.txt$', filename)
#     if match:
#         return int(match.group(1))
#     else:
#         raise ValueError(f"Filename does not match expected pattern: {filename}")

# # Get the full path of the current working directory
# current_directory_path = os.getcwd()

# # Extract the base name (the last component) of the path
# Season = os.path.basename(current_directory_path)

# paths_x = []
# paths_p = []
# paths_e = []
# for path_to_result in os.listdir(Season+'_Results'):
#     if path_to_result[:8] == 'r1E2gs_x':
#         paths_x.append(Season+'_Results/'+path_to_result)
#     elif path_to_result[:8] == 'r1E2gs_p':
#         paths_p.append(Season+'_Results/'+path_to_result)
#     elif path_to_result[:8] == 'r1E2gs_e':
#         paths_e.append(Season+'_Results/'+path_to_result)
# paths_x = sorted(paths_x, key = extract_number)
# matrix_x = [np.loadtxt(f) for f in paths_x]
# matrix_x = np.stack(matrix_x)
# mean_x = np.sum(matrix_x, axis=0)/len(paths_x)
# var_x = (matrix_x-mean_x)**2
# sample_var_x =np.sum(matrix_x, axis=0)/(len(paths_x)-1)
# mean_var_x = np.mean(sample_var_x)
# s_mean_var_x = np.sqrt(mean_var_x)
# L2_dist_x = np.sqrt(np.sum(var_x , axis = 1))
# rms_dist_x = np.sqrt(np.mean(var_x, axis = 1))

# paths_p = sorted(paths_p, key = extract_number)
# matrix_p = [np.loadtxt(f) for f in paths_p]
# matrix_p = np.stack(matrix_p)
# mean_p = np.sum(matrix_p, axis=0)/len(paths_p)
# var_p = (matrix_p-mean_p)**2
# sample_var_p = np.sum(matrix_p, axis=0)/(len(paths_x)-1)
# mean_var_p = np.mean(sample_var_p)
# s_mean_var_p = np.sqrt(mean_var_p)
# L2_dist_p = np.sqrt(np.sum(var_p , axis = 1))
# rms_dist_p = np.sqrt(np.mean(var_p, axis = 1))

# paths_e = sorted(paths_e, key = extract_number)
# matrix_e = [np.loadtxt(f) for f in paths_e]
# matrix_e = np.stack(matrix_e)
# mean_e = np.sum(matrix_e, axis=0)/len(paths_e)
# var_e = (matrix_e-mean_e)**2
# sample_var_e =np.sum(matrix_e, axis=0)/(len(paths_x)-1)
# mean_var_e = np.mean(sample_var_e)
# s_mean_var_e = np.sqrt(mean_var_e)
# L2_dist_e = np.sqrt(np.sum(var_e , axis = 1))
# rms_dist_e = np.sqrt(np.mean(var_e, axis = 1))


# n_bins = 5
# legend = ['distribution']

# # Creating histogram
# fig, axs = plt.subplots(1, 1, figsize=(10, 7), tight_layout=True)

# # Remove axes splines
# for s in ['top', 'bottom', 'left', 'right']:
#     axs.spines[s].set_visible(False)

# # Remove x, y ticks
# axs.xaxis.set_ticks_position('none')
# axs.yaxis.set_ticks_position('none')

# # Add padding between axes and labels
# axs.xaxis.set_tick_params(pad=5)
# axs.yaxis.set_tick_params(pad=10)

# # Add x, y gridlines
# axs.grid(visible=True, color='grey',
#          linestyle='-.', linewidth=0.5,
#          alpha=0.6)

# # Add Text watermark
# fig.text(0.9, 0.15, 'Jeeteshgavande30',
#          fontsize=12,
#          color='red',
#          ha='right',
#          va='bottom',
#          alpha=0.7)

# # Creating histogram
# N, bins, patches = axs.hist(L2_dist_x, bins=n_bins)

# # Setting color
# fracs = np.zeros_like(N, dtype=float)
# nonzero = N > 0
# fracs[nonzero] = (N[nonzero] ** (1 / 5)) / N.max()
# norm = colors.Normalize(fracs.min(), fracs.max())

# for thisfrac, thispatch in zip(fracs, patches):
#     color = plt.cm.viridis(norm(thisfrac))
#     thispatch.set_facecolor(color)

# # Adding extra features    
# axs.set_xlabel("X-axis")
# axs.set_ylabel("y-axis")
# axs.legend(legend)
# axs.set_title('Customized histogram')

# # Show plot
# plt.show()
