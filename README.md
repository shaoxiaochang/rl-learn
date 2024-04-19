# 強化學習

windows環境

## 測試安裝環境
- [x] Classic Control
- [x] Box2D
- [x] Toy Text
- [ ] MuJoCo
- [ ] Atari

## gymnasium install
```bash
pip install gymnasium
```

## Box2D install
```bash
pip install gymnasium[box2d]
```
錯誤處理:
```bash
pip install -U pip setuptools wheel
pip install swig
pip install pyproject
```
swig安裝: https://blog.csdn.net/m0_43605481/article/details/127128463

c++安裝: https://medium.com/@a37708867/using-gymnasium-in-windows-000613c628ab

## Lunar Lander DQN
參考 DQN-LunarLander-V2.ipynb

## FrozenLake Q Learning
參考 Qlearning-FrozenLake-v1.py