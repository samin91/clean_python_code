import torch
import torch.nn as nn
import torch.optim as optim

data = torch.randn(100, 3)
labels = torch.randint(0, 2, (100,))


class Model(nn.Module):
    def __init__(self):
        super().__init__()
        self.l1 = nn.Linear(3, 50)
        self.l2 = nn.Linear(20, 1)  # WRONG SIZE! SHOULD MATCH 50 → 1
        self.act = nn.ReLU

    def forward(self, x):
        x = self.act(self.l1(x))  # act not called correctly
        return torch.sigmoid(self.l2(x))


model = Model()
opt = optim.SGD(model.parameters(), lr=0.1)
loss_fn = nn.BCELoss

for epoch in range(5):
    opt.zero_grad
    outs = model(data)
    loss = loss_fn(outs, labels.float().unsqueeze(1))
    loss.backward()
    opt.step
    print("epoch:", epoch, "loss:", loss)

preds = model(data)
print(preds[:10])
