Write out the analysis for the centered difference approximation for the
first derivative (as defined in the lecture) in a Taylor series
expansions. Show that the approximation is second order.

The equation for the central difference approximation is a as follows:
\[\lim_{h\to 0}\frac{f(a+h) - f(a-h)}{2h} = f'(a)\] This is equivalent
to change of \(y\) value divided by the change of \(x\).We have \(2h\)
on the bottom because \(h - -h = 2h\). This is important to recognize
because the general form of the Taylor series is
\(f(a)+\frac {f'(a)}{1!} (x-a)+ \frac{f''(a)}{2!} (x-a)^2+\frac{f'''(a)}{3!}(x-a)^3+ \cdots\),
and in the case of the central difference approximation \(x-a\) is the
\(h\) value.  
Using the Taylor series in the central difference approximation it
appears as: \[\begin{aligned}
  f'(a)= \lim_{h\to0} \frac{1}{2h} [ (f(a)+\frac {f'(a)}{1} (h)+ \frac{f''(a)}{2} (h)^2+\frac{f'''(a)}{6}(h)^3+ \cdots)  -   \\
(f(a)+\frac {f'(a)}{1} (-h)+ \frac{f''(a)}{2} (-h)^2+\frac{f'''(a)}{6}(-h)^3+ \cdots)]  \end{aligned}\]
The first term and the ones with an even power cancel. \[\begin{aligned}
   f'(a) = \lim_{h\to0} \text{ } \frac{1}{2h} [ 2f'(a) (h)+ \frac{2f'''(a)}{6}(h)^3+ \cdots) ] \\
    f'(a) = \lim_{h\to0} \text{ } f'(a) + \frac{1}{6} f'''(\xi)h^2\end{aligned}\]

This is second order, because the \(h\) is squared.
