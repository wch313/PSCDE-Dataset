import torch
from torch.nn import Module, Parameter, Softmax
torch_ver = torch.__version__[:3]

class BSRAw(Module):

    def __init__(self, in_dim):
        super(BSRAw, self).__init__()
        self.chanel_in = in_dim
        self.gamma = Parameter(torch.zeros(1))
        self.softmax  = Softmax(dim=-1)
    def forward(self,x):

        m_batchsize, C, height, width = x.size()
        x_perm1 = x.permute(0, 3, 2, 1).contiguous()
        x_out1 = torch.max(x_perm1, 1)[0].unsqueeze(1)+ torch.mean(x_perm1, 1).unsqueeze(1)
        proj_query = x_out1.view(m_batchsize, C, -1)
        proj_key   = x_out1.view(m_batchsize, C, -1).permute(0, 2, 1)
        energy = torch.bmm(proj_query, proj_key)
        energy = torch.max(energy, -1, keepdim=True)[0].expand_as(energy)-energy
        attention = self.softmax(energy)
        proj_value = x.view(m_batchsize, C, -1)

        out = torch.bmm(attention, proj_value)
        out = out.view(m_batchsize, C, height, width)

        out = self.gamma*out + x
        return out


class BSRAh(Module):
    def __init__(self, in_dim):
        super(BSRAh, self).__init__()
        self.chanel_in = in_dim

        self.gamma = Parameter(torch.zeros(1))
        self.softmax  = Softmax(dim=-1)
    def forward(self,x):
        m_batchsize, C, height, width = x.size()
        x_perm1 = x.permute(0, 2, 1, 3).contiguous()
        x_out1 = torch.max(x_perm1, 1)[0].unsqueeze(1)+ torch.mean(x_perm1, 1).unsqueeze(1)
        proj_query = x_out1.view(m_batchsize, C, -1)
        proj_key   = x_out1.view(m_batchsize, C, -1).permute(0, 2, 1)
        energy = torch.bmm(proj_query, proj_key)
        energy = torch.max(energy, -1, keepdim=True)[0].expand_as(energy)-energy
        attention = self.softmax(energy)
        proj_value = x.view(m_batchsize, C, -1)

        out = torch.bmm(attention, proj_value)
        out = out.view(m_batchsize, C, height, width)

        out = self.gamma*out + x
        return out


if __name__ == '__main__':
    model = BSRAh('cuda')
    a=torch.rand((2,3,512,256))
    print(model(a).shape)