
x=c(0.9, 1.3, 1.9, 2.1, 2.6, 3, 3.9, 4.4, 4.7, 5, 6, 7, 8, 9.2, 10.5, 11.3, 11.6, 12, 12.6, 13,13.3,      10.7, 10, 8.5, 8,  7, 6, 4.75, 5.1, 5.48, 5.6, 4.2, 3.5, 2.55, 2.1, 1.3,0.9)
y=c(1.3, 1.5, 1.85, 2.1, 2.6, 2.7, 2.4, 2.15, 2.05, 2.1, 2.25, 2.3, 2.25, 1.95, 1.4, 0.9, 0.7, 0.6, 0.5, 0.4, 0.25,     0, 0.25, -0.5, -2, -4, -4.8, -5.1, -4, -2, 0.1, 1.01, 1.01, 1.05, 1.2, 1,1.3)


plot(x,y, pch=20, cex=1, col = "blue", asp=1,xlab="X", ylab="Y", main="pato")

vx1 = c(x[1:21])
vy1 = c(y[1:21])
splines = splinefun(vx1, vy1, method = "fmm")
curve(splines(x), add = TRUE, col=1, from= vx1[1], to=vx1[length(vx1)] )

vx2 = c(x[21:23])
vy2 = c(y[21:23])
splines = splinefun(vx2, vy2, method = "fmm")
curve(splines(x), add = TRUE, col=1, from= vx2[1], to=vx2[length(vx2)] )

vx3 = c(x[23:24])
vy3 = c(y[23:24])
splines = splinefun(vx3, vy3, method = "fmm")
curve(splines(x), add = TRUE, col=1, from= vx3[1], to=vx3[length(vx3)] )

vx4 = c(x[24:28])
vy4 = c(y[24:28])
splines = splinefun(vx4, vy4, ,method = "fmm")
curve(splines(x), add = TRUE, col=1, from= vx4[1], to=vx4[length(vx4)] )

vx5 = c(x[28:31])
vy5 = c(y[28:31])
splines = splinefun(vx5, vy5, method = "fmm")
curve(splines(x), add = TRUE, col=1, from= vx5[1], to=vx5[length(vx5)] )

vx6 = c(x[31:32])
vy6 = c(y[31:32])
splines = splinefun(vx6, vy6, method = "fmm")
curve(splines(x), add = TRUE, col=1, from= vx6[1], to=vx6[length(vx6)] )

vx7 = c(x[32:36])
vy7 = c(y[32:36])
splines = splinefun(vx7, vy7, method = "fmm")
curve(splines(x), add = TRUE, col=1, from= vx7[1], to=vx7[length(vx7)] )

vx8 = c(x[36:37])
vy8 = c(y[36:37])
splines = splinefun(vx8, vy8, method = "fmm")
curve(splines(x), add = TRUE, col=1, from= vx8[1], to=vx8[length(vx8)] )
