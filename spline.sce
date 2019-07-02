
//x  = [2,3,4,5,7,8,9]; 
//y = [1.05,2.0,2.1,2.3,3.1,3.5,3.6];

x= [2,4,5,12,19,25,34,43,47,50,55,60];
y=[3,10,11,14.5,19.5,20,19.5,15,11,10,9,3];
//x = [1.02, 1.05, 1.15, 2.0, 3.0, 4.42, 5.42, 6.3, 7.42, 8.7, 9.5, 9.6];
//y = [1.95, 2.4, 2.9, 3.3, 4.1, 4.5, 4.5, 4.15, 3.36, 3.0, 2.5, 1.9];

xi = linspace(1,60,60);

yk = interp(xi, x, y, splin(x,y,"not_a_knot"));
//yf = interp(xi, x, y, splin(x,y,"fast"));
//ym = interp(xi, x, y, splin(x,y,"monotone"));
xt=[3,6,9];
yt=[0,0,0];
xk = interp(xi, xt, yt, splin(xt,yt,"not_a_knot"));
plot(xt,yt,'o',xi,xk,'-');
plot(x,y,'o',xi,yk,'-') 
//plot(x,y,'X',xi,yf,'-r') 
//plot(x,y,'+',xi,yf,'-b') 

xlabel('x')
ylabel('y') 
legend(['','Not a knot','','Fast','','Monotone'])
