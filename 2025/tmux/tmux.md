[TOC]

# 1. 问题

用远程工具连接linux，每次重新连接，打开过的目录和界面都被关闭，每次都需要重新打开，比较麻烦
  
# 2. 解决方案

* 使用tmux，可以保留打开的窗口状态，并且可以比较好的分屏，一边运行代码，一边查看后台log

## 2.1. 安装配置

* 安装 `apt install tmux`

* 常见配置见 .tmux.conf

  ```sh
  set -sg repeat-time 300
  set -s focus-events on

  # -- prefix
  unbind C-b
  set -g prefix 'C-i'

  # reload configuration
  bind -n C-r source-file ~/.tmux.conf \; display '~/.tmux.conf sourced'

  # split window
  bind | split-window -h  # Bind 'Ctrl+b |' to horizontal split
  bind - split-window -v  # Bind 'Ctrl+b -' to vertical split
  # exit can close the window like unsplit window

  # pane navigation
  bind -n C-h select-pane -L
  bind -n C-j select-pane -D
  bind -n C-k select-pane -U
  bind -n C-l select-pane -R

  # resize
  bind -n C-f resize-pane -Z

  # copy C-i+[ 进入选择，hjkl移动光标，v开始选择，有结束选择，C-i+]黏贴
  setw -g mode-keys vi
  bind-key -T copy-mode-vi 'y' send -X copy-selection-and-cancel
  bind-key -T copy-mode-vi 'v' send -X begin-selection

  # unbind-key -n Tab
  # unbind Tab
  bind-key Tab send-keys Tab
  # unbind -n Tab

  set -g window-size latest
  set-window-option -g aggressive-resize on
  ```

## 2.2. 常见命令

* session管理
  * 创建 tmux new -s xiaobao
  * 查看 tmux ls
  * 删除 tmux kill-session -t xiaobao
  * attach： tmux a -t xiaobao
  * deattach：ctrl+i d

* 窗口管理
  * 竖向分割: ctrl+i, |
  * 横向分割：ctrl+i, -
  * 关闭分割：ctrl+d
  * 最大化窗口：ctrl+f

* 移动
  * 上下左右：ctrl+j,  ctrl+k, ctrl+l, ctrl+h

* 复制黏贴
  * 进入选择：ctrl+i, [
  * 开始选择：ctrl+v
  * 复制: y
  * 黏贴：ctrl+i, ]

# 3. 结论

# 4. 展望

# 5. 文献
