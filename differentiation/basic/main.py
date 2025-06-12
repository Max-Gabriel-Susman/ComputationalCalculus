import torch 

# Create a scalar tensor and tell autograd to track it
x = torch.tensor(3.0, requires_grad=True)

# Define your function of x
y = x**2 + 2*x + 1

# Back-propagate a unit “seed” (∂y/∂y = 1)
y.backward()

print("dy/dx at x=3", x.grad.item())