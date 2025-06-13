# To compute second-order derivatives, set create_graph=True in backward()
import torch

x = torch.tensor(2.0, requires_grad=True)
y = x**3 

y.backward(create_graph=True)
dy_dx = x.grad 

dy_dx.backward()
d2y_dx2 = x.grad 

print(f"First derivative dy/dx: {dy_dx.item()}")
print(f"d^2y/dx^2: {d2y_dx2.item()}")