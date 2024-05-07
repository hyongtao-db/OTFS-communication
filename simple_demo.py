import numpy as np
from numpy import sqrt
from numpy.fft import fft, ifft

M = 8; # subcarrier
N = 4; # timeslot
QPSKconstel = [-0.7071-0.7071j, 
            -0.7071+0.7071j, 
            0.7071-0.7071j, 
            0.7071+0.7071j];

# X_DD
np.random.seed(199)
xDD_idx = np.random.randint(4, size=(M*N));
xDD = np.take(QPSKconstel, xDD_idx);
X_DD = np.reshape(xDD, (N, M));
# print("X_DD = ", X_DD)

# modulate
X_DD = np.asarray(X_DD);
s_mat = ifft(X_DD, axis=-2)*sqrt(N);
s = np.reshape(s_mat, M*N);

# pass an ideal channel
r = s 

# demodulate
r_mat = np.reshape(r, (M, N), order='F');
Y_DD = fft(np.moveaxis(r_mat, -1, -2), axis=-2)/sqrt(N);
# print("Y_DD = ", Y_DD)