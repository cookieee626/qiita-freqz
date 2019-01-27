# -*- coding: utf-8 -*-
import numpy as np
from matplotlib import pylab as plt

N = 256     # 正弦波1周期のサンプリング数
a1, a2 = 1.0, 0.1   # 正弦波の振幅a
f1, f2 = 5.0, 50.0  # 正弦波の周波数f
t = np.asarray([i for i in np.linspace(0.0, 1.0, N)])   # 時間領域の横軸
sin1 = a1*np.sin(2.0*np.pi*f1*t)    # 振幅a=1.0, 周波数f=5.0 の正弦波
sin2 = a2*np.sin(2.0*np.pi*f2*t)    # 振幅a=0.1, 周波数f=50.0 の正弦波
sin3 = sin1 + sin2                  # sin1 と sin2 を合成した正弦波

# FFTにより時間領域から周波数領域へ変換
fx1, fx2, fx3 = np.fft.fft((sin1, sin2, sin3))

# プロット
fig, ax = plt.subplots(nrows=2, ncols=2, figsize=(10, 10))
ax[0, 0].plot(t, sin1, 'r-', label="sin1")
ax[0, 0].plot(t, sin2, 'b-', label="sin2")
ax[1, 0].plot(t, sin3, 'g-', label="sin3(sin1 + sin2)")
# ここで周波数特性のy軸を/N*2しているためmax値が元信号の振幅になる
ax[0, 1].plot(range(N//2), np.abs(fx1[0:N//2])/N*2, 'r-', label="sin1")
ax[0, 1].plot(range(N//2), np.abs(fx2[0:N//2])/N*2, 'b-', label="sin2")
ax[1, 1].plot(range(N//2), np.abs(fx3[0:N//2])/N*2, 'g-', label="sin3")
for x in [0, 1]:
    ax[x, 0].set_title('Sin Wave')
    ax[x, 0].set_xlabel('Radian')
    ax[x, 0].set_ylabel('Signal')
    ax[x, 0].set_xticks(np.linspace(0, 1.0, 5))
    ax[x, 0].set_xticklabels(['0', '1/2$\pi$', u'$\pi$', '3/2$\pi$', u'2$\pi$'])
    ax[x, 0].grid(True)
    ax[x, 0].legend(loc="upper right")
    ax[x, 1].set_title('Frequency response')
    ax[x, 1].set_xlabel('Frequency [Hz]')
    ax[x, 1].set_ylabel('Magnitude [dB]')
    ax[x, 1].grid(True)
    ax[x, 1].legend(loc="upper right")
plt.show()
