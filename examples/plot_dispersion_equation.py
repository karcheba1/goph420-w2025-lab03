import numpy as np
import matplotlib.pyplot as plt


def main():
    # setup fixed parameter values
    rho1 = 1800.0  # kg/m^3
    rho2 = 2500.0
    beta1 = 1900.0  # m/s
    beta2 = 3200.0
    H = 4000.0  # m

    zeta_max = H * np.sqrt(1.0 / beta1**2 - 1.0 / beta2**2)

    # select some frequencies
    freqs = [0.1, 0.5, 1.0, 2.0]  # Hz
    nf = len(freqs)

    plt.figure()

    for j, f in enumerate(freqs):
        # define the function
        def F(z):
            return (rho2 / rho1) * np.sqrt(zeta_max**2 - z**2) / z - np.tan(
                2 * np.pi * f * z
            )

        # compute asymptotes
        atotes = [0.0]
        a = 0.0
        k = 0
        while a < zeta_max:
            a = 0.25 * (2 * k + 1) / f
            if a < zeta_max:
                atotes.append(a)
            k += 1
        atotes.append(zeta_max)
        n = len(atotes)

        # plot the function between pairs of asymptotes
        plt.subplot(nf, 1, j + 1)
        for k, ak in enumerate(atotes):
            # plot asymptote
            if k and k < n - 1:
                plt.plot([ak, ak], [-5, 5], "--r")
            # plot the function
            if k < n - 1:
                zp = np.linspace(ak + 1e-3, atotes[k + 1] - 1e-3)
                Fp = F(zp)
                plt.plot(zp, Fp, "-b")
        plt.grid()
        plt.xlabel("zeta")
        plt.ylabel("F(zeta)")
        plt.xlim((0.0, zeta_max))
        plt.ylim((-5.0, 5.0))

    plt.show()


if __name__ == "__main__":
    main()
