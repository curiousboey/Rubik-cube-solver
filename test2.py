import matplotlib.pyplot as plt


x=[1,2,3,4]
y=[5,6,3,7]
fig = plt.figure(figsize=(8, 6))
ax1 = plt.subplot2grid((2, 2), (0, 0), colspan=2, rowspan=1)
ax1.plot(x, y)
ax2 = plt.subplot2grid((2, 2), (1, 0), colspan=1, rowspan=1)
ax2.plot(y, x)
ax3 = plt.subplot2grid((2, 2), (1, 1), colspan=1, rowspan=1)
ax3.plot(y, x)

# fig, ax1.plot([1, 2], [1, 2])
