# [Logistic Regression]
## Sigmoid Derivative
$s(z) = \frac{1}{1 + e^{-z}}$ 

$s'(z) = \frac{e^{-z}}{\left(1 + e^{-z}\right)} = s(z) (1 - s\left( z
    \right))$

## Softmax Derivative
$\sigma(\mathbf{z})_{j} = \frac{e^{\mathbf{z}_{j}}}{\sum_{k = 1}^{K}
e^{\mathbf{z}_{k}}}$ 

$\frac{\partial \sigma\left( \mathbf{z} \right)_{j} }{\partial \mathbf{z}_{j}}
= \frac{\left(\sum_{k=1}^{K} e^{\mathbf{z}_{k}}\right) e^{\mathbf{z}_{j}} -
e^{\mathbf{z}_{j}} e^{\mathbf{z}_{j}}}{\left( \sum_{k=1}^{K} e^{\mathbf{z}_{k}}
\right)^{2} } = \sigma\left( \mathbf{z} \right)_{j} \left( 1 - \sigma\left(
\mathbf{z} \right)_{j}  \right) $

## Multiclass LR Convex
$\nabla_{\mathbf{W}_{\ell}} L\left( \mathbf{W} \right) = - \sum_{i=1}^{n} \left(
\delta_{\ell, y_{i}} - P\left( \hat{Y}_{i} = \ell \right) \right) \mathbf{x}_{i}$

$\begin{align*}
\nabla^{2}_{\mathbf{W}_{\ell_{kl}}} L\left( \mathbf{W} \right) &= \frac{\partial^{2} L \left( \mathbf{W} \right) }{\partial \mathbf{W}_{\ell_{k}} \partial \mathbf{W}_{\ell_{l}}}
\\
&= \frac{\partial}{\partial \mathbf{W}_{\ell_{k}}} \left( - \sum_{i=1}^{n}
\left( \delta_{\ell, y_{i}} - P\left( \hat{Y}_{i} = \ell \right)  \right)
\mathbf{x}_{il}  \right) 
\\
&= \sum_{i = 1}^{n} \left(\frac{\partial}{\partial \mathbf{W}_{\ell_{k}}}
P\left( \hat{Y}_{i} = \ell \right) \mathbf{x}_{il} \right)
\\
&= \sum_{k=1}^{n} \left( P\left( \hat{Y}_{i} = \ell \right) \left( 1 - P\left(
\hat{Y}_{i} = \ell \right)  \right)\mathbf{x}_{ik} \mathbf{x}_{il} \right) 
\end{align*}$

$\nabla^{2}_{\mathbf{W}_{\ell_{kl}}} L\left( \mathbf{W} \right) =
\sum_{k=1}^{K} \left( P\left( \hat{Y}_{i} = \ell \right) \left( 1 - P\left(
\hat{Y}_{i} = \ell \right)  \right)\mathbf{x}_{i} \mathbf{x}_{i}^{\top} \right)
\succeq 0$
