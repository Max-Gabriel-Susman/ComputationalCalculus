import torch 

# If a function has multiple inputs, Pytorch calculates the gradient for each variable
x = torch.tensor(2.0, requires_grad=True)
y = torch.tensor(3.0, requires_grad=True)

z = x**2 + y**3 
z.backward()

print(f"dz/dx: {x.grad.item()}")
print(f"dz/dy: {y.grad.item()}")