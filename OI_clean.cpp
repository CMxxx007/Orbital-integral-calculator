#include <numeric>
#include <bits/stdc++.h>
#include <complex>
#include <vector>
#include <iostream>
#include <fstream>
#include <boost/python.hpp>
#include <pyconfig.h>
using namespace std;
#define NUM_NODES 5000
const double pie = 3.141592654;
const double hbarc = 1.973*pow(10,-13);
const double n_a = 6.23 * pow(10,23);
//const double pi = 3.141592654 ;
const double fm = pow(10,-15);
const double e =  1.6*pow(10,-19);
const double barn = pow(10,-28);
const double nA = pow(10,-9);
const double hour = 3600;
const double alpha = 1.44;
const double u = 931.494;

const double omeg_min = -100; //omega_min
const double omeg_max = -omeg_min; //omega_max

const complex<double> i(0.0,1.0);

double ang_degrees(double angle) {
           double deg;
           deg = (180/pie)*angle;
           return (deg);
}

//beam velocity (c)
double vl(double m_p, double beamenergy_lab){
return(sqrt((2 * beamenergy_lab) / (u * m_p)));
}
//nuclear radius (fm)
double r_o(double ap){
return(1.2*pow(ap,1/3));
}
//reduced mass
double red_mass(double mp, double mt)
{
return(u*mt*mp/( mt + mp));
}
//half distance of closest approach (fm)
double a(int zp,int zt,double mp, double mt, double beamenergy_lab)
{
//cm frame kinetic energy (MeV)
double vv = vl(mp,beamenergy_lab);
return(zp*zt*alpha)/(red_mass(mp,mt)*pow(vv,2)); 
}

//eccentricity
double eccent(double vvv){
double uuu = 1/sin(0.5*vvv);
return(uuu); 
}

//adiabaticity parameter
double xi_if(double de, int zp,int zt,double mp, double mt, double beamenergy_lab)
{
double bb = a(zp,zt,mp,mt,beamenergy_lab)*fm/vl(mp,beamenergy_lab);
return((de/hbarc)*bb);
}

////////functions to compute collision function///////////////////
double c1(double eps, double omeg){
double jj0 = cosh(omeg) + eps;
 return(jj0);
 }

double c2(double eps, double omeg){
 double jj1 = eps*cosh(omeg) + 1;
 return(jj1);
 }
 
double c3(double eps, double omeg){
 double jj2 = sqrt(pow(eps,2)-1)*sinh(omeg);
 return(jj2);
 }
 
double c4(double eps, double omeg){
 double jj3 = eps*sinh(omeg)+omeg;
 return(jj3);
 }
/////////function to select collision function based on lambda and mu value
complex<double> colfselec(int lam, int mu, double eps, double omeg)
 {
  complex<double> colf;
  colf = pow(c1(eps,omeg) + i*c3(eps,omeg),mu)/pow(c2(eps,omeg),mu+lam);
       return(colf);
  }
//////integrand of orbital integral 
complex<double> func0(int lam, int mu, double eps, double adia, double omeg)
{
complex<double> f0 = exp(i*adia*c4(eps,omeg))*colfselec(lam,mu,eps,omeg); 
return(f0);
}

//////function to compute orbital integral numerically using Gauss-Legendre quadrature
complex<double> glf(int l, int m, double thtt,double addd, double omin, double omax,int steps)
{
 vector<double> weights(steps);
 vector<double> nodes(steps);
 complex<double> nn = 10.0;

  // Generate Gauss-Legendre nodes and weights
  for (int i = 0; i < steps; i++) {
    double x = cos(M_PI * (i + 0.5) / steps);
    nodes[i] = (omax + omin) / 2 + (omax - omin) / 2 * x;
    weights[i] = M_PI / steps * sin(M_PI * (i + 0.5) / steps);
  }
    
  complex<double> res = 0;
  for (int i = 0; i < steps; i++) {
    res += weights[i] * func0(l, m,1/sin(0.5*thtt) , addd, nodes[i]);
  }
  return(nn*res);
  }
  
double oival(int lamm,int mu, double vtht,double adia_param)
{
  double oi_val = real(glf(lamm,mu,vtht,adia_param,omeg_min,omeg_max,NUM_NODES));
   return(oi_val);
}

BOOST_PYTHON_MODULE(oi_cal)
{
 boost::python::def("get_oi", oival);
 }

