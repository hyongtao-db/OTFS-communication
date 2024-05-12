import numpy as np
from numpy import sqrt
from numpy.fft import fft, ifft

# OFDM simple demo
M = 8; # subcarrier
N = 4; # No. of OFDM symbols
QPSKconstel = [-0.7071-0.7071j, 
            -0.7071+0.7071j, 
            0.7071-0.7071j, 
            0.7071+0.7071j];

np.random.seed(199)
X_idx = np.random.randint(4, size=(M*N));
X = np.take(QPSKconstel, X_idx);
X = np.reshape(X, (N, M));
# print("X = ", X);

# OFDM modulate
X = np.asarray(X);
s_mat = ifft(X, axis=-1);
s = np.reshape(s_mat, M*N);

# pass an ideal channel
r = s

# OFDM demodulate
r_mat = np.reshape(r, (N, M));
Y = fft(r_mat);
# print("Y = ", Y);
