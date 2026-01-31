import matplotlib.pyplot as plt
import numpy as np

t = np.linspace(0.0, 2.0, 201)
s1 = np.sin(2*np.pi*t)
s2 = np.sin(4*np.pi*t)

plt.figure(1)
plt.subplot(221, title="Wykres 1")
plt.plot(t, s1)
plt.subplot(222, title="Wykres 2")
plt.plot(t, 2*s1)
plt.subplot(223, title="Wykres 3")
plt.plot(t, s2)
plt.subplot(224, title="Wykres 4")
plt.plot(t, 2*s2)
plt.subplots_adjust(left=0.1,
                    bottom=0.1,
                    right=0.9,
                    top=0.9,
                    wspace=0.4,
                    hspace=0.4)
plt.savefig("scripts/Nazwisko_plot2_poczworny.png", dpi=1200)

plt.figure(2)
plt.plot(t, s2)
plt.grid()
plt.savefig("scripts/Nazwisko_plot2_pojedynczy.png", dpi=600)

plt.show()
