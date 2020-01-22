==========================================          ==========================================
             TMUX COMMAND                                        WINDOW (TAB)
==========================================          ==========================================

List    tmux ls                                     List         ^b w
New          -s <session>                           Create       ^b c
Attach       att -t <session>                       Rename       ^b , <name>
Rename       rename-session -t <old> <new>          Last         ^b l               (lower-L)
Kill         kill-session -t <session>              Close        ^b &

==========================================          Goto #       ^b <0-9>
             CONTROLS                               Next         ^b n
==========================================          Previous     ^b p
                                                    Choose       ^b w <name>
Detach       ^b d
List         ^b =                                   ==========================================
Buffer       ^b <PgUpDn>                                         PANE (SPLIT WINDOW)
Command      ^b : <command>                         ==========================================

Copy         ^b [ ... <space> ... <enter>           Show #       ^b q
 Moving         vim/emacs key bindings              Split Horiz  ^b "                --------
 Start          <space>                             Split Vert   ^b %                   |
 Copy           <enter>                             Pane->Window ^b !
Paste        ^b ]                                   Kill         ^b x

==========================================          Reorganize   ^b <space>
             SESSION (Set of Windows)               Expand       ^b <alt><arrow>
==========================================          Resize       ^b ^<arrow>
                                                    Resize x n   ^b <n> <arrow>
New          ^b :new     ^b :new -s <name>
Rename       ^b $                                   Select       ^b <arrow>
List         ^b s                                   Previous     ^b {
Next         ^b (                                   Next         ^b }
Previous     ^b )                                   Switch       ^b o                  other
                                                    Swap         ^b ^o
                                                    Last         ^b ;


---

[A awesome tmux configuration](https://github.com/gpakosz/.tmux)
Bindings
--------

tmux may be controlled from an attached client by using a key combination of a
prefix key, followed by a command key. This configuration uses `C-a` as a
secondary prefix while keeping `C-b` as the default prefix. In the following
list of key bindings:
  - `<prefix>` means you have to either hit <kbd>Ctrl</kbd> + <kbd>a</kbd> or <kbd>Ctrl</kbd> + <kbd>b</kbd>
  - `<prefix> c` means you have to hit <kbd>Ctrl</kbd> + <kbd>a</kbd> or <kbd>Ctrl</kbd> + <kbd>b</kbd> followed by <kbd>c</kbd>
  - `<prefix> C-c` means you have to hit <kbd>Ctrl</kbd> + <kbd>a</kbd> or <kbd>Ctrl</kbd> + <kbd>b</kbd> followed by <kbd>Ctrl</kbd> + <kbd>c</kbd>

This configuration uses the following bindings:

 - `<prefix> e` opens `~/.tmux.conf.local` with the editor defined by the
   `$EDITOR` environment variable (defaults to `vim` when empty)
 - `<prefix> r` reloads the configuration
 - `C-l` clears both the screen and the tmux history

 - `<prefix> C-c` creates a new session
 - `<prefix> C-f` lets you switch to another session by name

 - `<prefix> C-h` and `<prefix> C-l` let you navigate windows (default
   `<prefix> n` and `<prefix> p` are unbound)
 - `<prefix> Tab` brings you to the last active window

 - `<prefix> -` splits the current pane vertically
 - `<prefix> _` splits the current pane horizontally
 - `<prefix> h`, `<prefix> j`, `<prefix> k` and `<prefix> l` let you navigate
   panes ala Vim
 - `<prefix> H`, `<prefix> J`, `<prefix> K`, `<prefix> L` let you resize panes
 - `<prefix> <` and `<prefix> >` let you swap panes
 - `<prefix> +` maximizes the current pane to a new window

 - `<prefix> m` toggles mouse mode on or off

 - `<prefix> U` launches Urlview (if available)
 - `<prefix> F` launches Facebook PathPicker (if available)

 - `<prefix> Enter` enters copy-mode
 - `<prefix> b` lists the paste-buffers
 - `<prefix> p` pastes from the top paste-buffer
 - `<prefix> P` lets you choose the paste-buffer to paste from

Additionally, `copy-mode-vi` matches [my own Vim configuration][]

[my own Vim configuration]: https://github.com/gpakosz/.vim.git

Bindings for `copy-mode-vi`:

- `v` begins selection / visual mode
- `C-v` toggles between blockwise visual mode and visual mode
- `H` jumps to the start of line
- `L` jumps to the end of line
- `y` copies the selection to the top paste-buffer
- `Escape` cancels the current operation
