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
    f: T \rightarrow L \\
    t \mapsto I e^{-\alpha t},
\end{align}
$$

where the actual numerical values in $T$ and $L$ depend on the **chosen units of measure**.

Let's define some units, also known as **a scale**:

