# Scaling and dimensional analysis

We want to study a problem where a given function is epxressed in some **units of measures**. Let's say this function is

$$
\begin{equation}
    f(t) = I e^{-\alpha t},
\end{equation}
$$

where $I$ is a **distance** and $\alpha$ is an **inverse time**. This function describes the exponential decay of the position of an object as time passes by.
The **numerical values** of $f$ depends on the values the we insert into $I$ and $\alpha$.
Mathematically speaking, $f$ is a map between a time domain $T$ and a length domain $L$

$$
\begin{align}
    f : T &\rightarrow L \\
    t &\mapsto I e^{-\alpha t},
\end{align}
$$

where the actual numerical values in $T$ and $L$ depend on the **chosen units of measure**.

Let's define some units, also known as **a scale**:

$$
\begin{align}
    t &= t_c \, t^* \\
    f(t) &= f_c \, f^*(t^*),
\end{align}
$$

where $t_c$ and $f_c$ are some **refactoring numbers** that defines the scaling of the problem. The subscipt $c$ stands for *characteristic*, since these two factors are generally related to some physical property of the system.
The scaled function will be

$$
\begin{align}
    f(t) &= I e^{-\alpha t} \\
    f_c \, f^*(t^*) &= I e^{-\alpha \, t_c \, t^*} \\
    f^*(t^*) &= e^{-t^*}
\end{align}
$$

where in the last line **we defined the scaling factors** as $t_c=1/\alpha$ and $f_c=I$. The domain and codomain of $f^*$ has changed as well:

$$
\begin{align}
    f^* : T^* &\rightarrow L^* \\
    t^* &\mapsto e^{- t^*}.
\end{align}
$$

The **new scaled** function has some important properties:
- it is **dimensionless**.
- it lives in the $T^*$ and $L^*$ domains, which capture the characteristic length of the system and thus are well suited for numerical evaluation.
- in a software, $T^*$ and $L^*$ are generally represented with an array of values. If we want to change the units of $t^*$ and $f^*(t^*)$, we just need to strecth $T^*$ and $L^*$ with the desired factors.
- it is **general**, it can be computed once and for all, different systems can be computed with different choices of $I$ and $\alpha$.

To go back to the **dimensional function** and the original **dimensional domains**, we simply perform the substitution

$$
\begin{align}
    f(t) &= f_c \, f^*(t^*) =  f_c \, f^*(\frac{t}{t_c}) \\
    t &= t_c \, t^*
\end{align}
$$

Altough this is very trivial to understand and put into practice, it is important to be aware that errors in refactoring units in a software could lead to disastrous consequences.

## Refactoring a differential equation

The above example of rescaling a function is extremely simple. We identify the constants in a formula and the we factor them out to produce a dimensionless expression.

The situation is a bit more complicated for a differential equation. Suppose we have

$$
\begin{equation}
    \frac{df(t)}{dt} = -\alpha f(t), \quad f(0) = I
\end{equation}
$$

which is a simple ODE with initial conditions. The solution to this equation is (surprise!) our toy function of the previous section.

Let's perform the same substitution as before

$$
\begin{align}
    t &= t_c \, t^* \\
    f(t) &= f_c \, f^*(t^*).
\end{align}
$$

Step by step we have

$$
\begin{equation}
    \frac{df(t)}{dt} = \frac{df(t)}{dt^*} \frac{dt^*}{dt} = \frac{d}{dt^*}(f_c \, f^*(t^*)) \frac{dt^*}{dt} = \frac{f_c}{t_c} \frac{df^*(t^*)}{dt^*}
\end{equation}
$$

$$
\begin{equation}
    I = f(t=0) = f_c f^*(t^*(t=0)) = f_c \, f^*(t^* = 0)
\end{equation}
$$

We combine the above two and obtain

$$
\begin{equation}
\boxed{
    \frac{df^*(t^*)}{dt^*} = -\alpha \, t_c \, f^*(t^*), \quad f^*(0) = \frac{I}{f_c}}
\end{equation}
$$

And again **we choose** $t_c=1/\alpha$ and $f_c=I$. This produce the **general** equation

$$
\begin{equation}
\boxed{
    \frac{df^*(t^*)}{dt^*} = - f^*(t^*), \quad f^*(0) = 1}.
\end{equation}
$$

The new equation is written in a **dimensionless form** that captures the general properties of the system. The solution is the expression of $f^*(t^*) = e^{-t^*}$ of the previous section. The crucial thing to keep in mind is that we can **compute the dimensionless solution** with whatever numerical method we like. Once that solution is calculated, we can plug in the scaling factors as we did previously and get back the **dimensional function** and the original **dimensional domains**

$$
\begin{align}
    f(t) &= f_c \, f^*(t^*) =  f_c \, f^*(\frac{t}{t_c}) \\
    t &= t_c \, t^*
\end{align}
$$

**Note:** this example is trivial because we already know the analytical solution. But for more complicated differential equations, that requires intense numerical calculations, rescaling is a powerful technique that
- improves numerical efficiency: rescaled equations generally have values around unity (i.e. domains are in the $[0,1]$ intervals);
- and must be **computed only once** for all the different parameters of the model.